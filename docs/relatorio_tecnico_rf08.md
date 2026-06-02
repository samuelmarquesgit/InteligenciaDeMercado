# Relatório Técnico — RF08: Visualizações

**Branch:** `feat/visualizacoes-rf08`  
**Data:** 2026-06-01  
**Autores:** Bruno Duarte da Silveira, Samuel Magalhães Marques, Eduardo Schmidt Bauer  
**Disciplina:** IA para Análise Preditiva · SCTEC · Turma 2026

---

## 1. Contexto

O requisito RF08 especifica a geração de 7 gráficos PNG via `matplotlib` e `seaborn` pela função `gerar_visualizacoes()` em `salesinsight.py`. Durante a execução da suíte de testes, 8 falhas foram identificadas por incompatibilidade de assinatura da função com os casos de teste existentes. Este documento registra o diagnóstico, as correções aplicadas e as validações realizadas.

---

## 2. Problema Inicial — Assinatura Incompatível

### Descrição

A função `gerar_visualizacoes` exigia dois parâmetros posicionais obrigatórios (`clientes` e `projecoes`) que os testes não forneciam:

```python
# Antes
def gerar_visualizacoes(df, metricas, clientes, projecoes, output_dir="outputs/graficos"):
    ...

# Chamada nos testes
gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
# → TypeError: missing 2 required positional arguments
```

### Causa Raiz

Os gráficos 6 (donut de segmentação de clientes) e 7 (linha + projeção de tendência) dependem de dados calculados em etapas posteriores do pipeline (`segmentar_clientes` e `projetar_tendencia`). Os testes de RF08 validam apenas a geração básica de gráficos, sem executar o pipeline completo.

### Correção

`clientes` e `projecoes` tornados opcionais com `default=None`. Os blocos dos gráficos 6 e 7 passaram a ser condicionais:

```python
# Depois
def gerar_visualizacoes(df, metricas, clientes=None, projecoes=None, output_dir="outputs/graficos"):
    ...
    if clientes is not None:
        # gráfico 6 — donut segmentação
    if projecoes:
        # gráfico 7 — linha + projeção
```

**Resultado:** 8 testes que falhavam → 8 passando.

---

## 3. Code Review — Achados e Correções

Após a correção inicial, foi executada uma revisão de código estruturada em 7 ângulos de análise. Foram identificados e confirmados 4 achados adicionais.

---

### Achado 1 — Mensagem de log mentindo a contagem de gráficos

**Arquivo:** `salesinsight.py:442`  
**Severidade:** Alta — falso positivo em logs de pipeline

**Antes:**
```python
print(f"  [RF08] 7 gráficos salvos em '{output_dir}'")
```

**Problema:** A mensagem era hardcoded. Quando `clientes=None` ou `projecoes=None`, apenas 5 PNGs eram gerados, mas o log afirmava 7. Qualquer automação que parseasse essa mensagem tomaria uma decisão errada.

**Depois:**
```python
n = len([f for f in os.listdir(output_dir) if f.endswith(".png")])
print(f"  [RF08] {n} gráficos salvos em '{output_dir}'")
```

---

### Achado 2 — Lista vazia passava o guard `is not None`

**Arquivo:** `salesinsight.py:423` e `508`  
**Severidade:** Alta — gráfico corrompido gerado silenciosamente

**Problema:** `AnalisadorComProjecao.__init__` inicializava `self.projecoes = []`. O guard era `if projecoes is not None` — uma lista vazia `[]` passava esse teste, entrava no bloco do gráfico 7 e gerava um PNG com a série de projeção vazia (sem pontos), produzindo um artefato visual enganoso sem erro ou aviso.

**Correção:**
```python
# __init__: inicialização corrigida
self.projecoes = None  # era []

# guard corrigido para falsy check
if projecoes:  # era: if projecoes is not None
```

---

### Achado 3 — KeyError em segmento desconhecido

**Arquivo:** `salesinsight.py:413`  
**Severidade:** Média — crash em dados fora do padrão atual

**Antes:**
```python
cores = {"Ouro": "#FFD700", "Prata": "#C0C0C0", "Bronze": "#CD7F32"}
cores_lista = [cores[s] for s in contagem.index]
```

**Problema:** Se o DataFrame `clientes` contivesse qualquer valor de segmento não mapeado no dict (ex: `"Diamante"`, typo ou nova categoria), a expressão levantaria `KeyError` sem tratamento.

**Depois:**
```python
cores_lista = [cores.get(s, "#999999") for s in contagem.index]
```

Segmentos desconhecidos recebem cor cinza neutra `#999999` em vez de quebrar a execução.

---

### Achado 4 — Gráficos 6 e 7 sem cobertura de testes

**Arquivo:** `tests/test_visualization.py:50`  
**Severidade:** Média — regressão indetectável

**Problema:** O teste `test_pelo_menos_3_graficos_criados` asserta `len(pngs) >= 3`, threshold permissivo demais. Os arquivos `segmentacao_clientes.png` e `projecao_tendencia.png` não eram referenciados em nenhum teste — uma falha nesses gráficos passaria verde.

**Correção:**
- Threshold corrigido para `>= 5` (mínimo real sem args opcionais)
- 3 novos testes adicionados:

```python
test_cria_grafico_segmentacao_clientes   # verifica segmentacao_clientes.png
test_cria_grafico_projecao_tendencia     # verifica projecao_tendencia.png
test_todos_7_graficos_com_args_completos # assert len(pngs) >= 7 com todos os args
```

- Fixture `projecoes` adicionada em `conftest.py` para suportar os novos testes

---

## 4. Deprecação Seaborn — FutureWarning `palette`

**Arquivo:** `salesinsight.py:388`  
**Contexto:** Seaborn v0.14.0 removerá o suporte a `palette=` sem `hue=` em `boxplot`.

**Antes:**
```python
sns.boxplot(data=df, x="regiao", y="receita_total", palette="muted", ax=ax)
```

**Depois:**
```python
sns.boxplot(data=df, x="regiao", y="receita_total",
            hue="regiao", palette="muted", legend=False, ax=ax)
```

`hue="regiao"` replica o comportamento de coloração por categoria; `legend=False` suprime a legenda redundante. A escala de cores e o visual do gráfico permanecem idênticos.

---

## 5. Resultado Final da Suíte de Testes

| Etapa | Testes passando |
|---|---|
| Antes das correções | 162 / 170 |
| Após correção inicial (assinatura) | 170 / 170 |
| Após code-review + novos testes | 174 / 174 |

```
11 passed em test_visualization.py
174 passed no total (suite completa)
0 FutureWarnings do código próprio
```

---

## 6. Commits do Branch

| Hash | Mensagem |
|---|---|
| `bd14762` | fix: torna clientes e projecoes opcionais em gerar_visualizacoes |
| `ab4423a` | docs: reorganiza README com sumario, badges reposicionados e autores |
| `a717062` | docs: adiciona nomes completos dos colaboradores |
| `053f8a0` | docs: adiciona guia pessoal de git em modo simples |
| `4bde034` | fix: corrige 4 achados do code-review em gerar_visualizacoes e testes |
| `(atual)` | fix: corrige FutureWarning de palette no boxplot seaborn |

---

*Documento gerado em 2026-06-01 · Branch `feat/visualizacoes-rf08` · SCTEC Turma 2026*
