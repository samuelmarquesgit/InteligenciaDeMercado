# PRD — Product Requirements Document
## SalesInsight PY · Pipeline de Análise de Vendas

> Versão 1.1 · Última atualização: 01/06/2026

---

## 1. Visão do Produto

### 1.1 Sumário Executivo

O **SalesInsight PY** é um pipeline de análise de dados de vendas desenvolvido 100% em Python, criado como mini-projeto avaliativo do Módulo 01 do curso de IA para Análise Preditiva (SCTEC). O sistema transforma dados brutos de um CSV de vendas em insights acionáveis, segmentações de clientes e projeções de tendência, com exportação de relatórios e visualizações.

### 1.2 Problema

Empresas de varejo acumulam históricos de vendas em CSV mas carecem de ferramentas simples para transformar esses dados em decisões estratégicas. O time de negócios precisa responder rapidamente a perguntas como: *quais produtos lideram a receita? quais regiões performam melhor? há tendência de crescimento para o próximo trimestre?*

### 1.3 Solução

Um pipeline em Python que automatiza o ciclo completo: **ingestão → limpeza → transformação → análise → visualização → exportação**, tornando a análise reproduzível, auditável e portátil (local ou Google Colab).

### 1.4 Público-Alvo

- Analistas de Dados Júnior
- Times de negócio de varejo
- Avaliadores e professores do curso SCTEC

---

## 2. Objetivos e Métricas de Sucesso

| Objetivo | Métrica | Meta | Status |
|---|---|---|---|
| Cobrir todos os RFs do mini-projeto | Requisitos implementados | 14/14 | ✅ 14/14 |
| Código executável sem erros | `python salesinsight.py` roda do início ao fim | 100% | ✅ Validado |
| Gráficos exportados | Arquivos PNG gerados em `outputs/graficos/` | ≥ 3 | ✅ 3 PNG |
| Relatórios exportados | CSV e JSON em `outputs/` | ≥ 3 arquivos | ✅ 2 CSV + 1 JSON |
| Nota mínima no projeto | Pontuação | ≥ 7,5 / 10 | Pendente avaliação |
| Commits no GitHub | Histórico de commits | ≥ 5 commits | A verificar |
| Prazo de entrega | Submissão no AVA | até 08/06/2026 12h | Pendente |

---

## 3. Requisitos Funcionais

### RF01 — Criar ou Carregar Dataset de Vendas
**Status: ✅ Implementado**

Gerar sinteticamente um dataset de 200 registros com dados propositalmente sujos (nulos, datas inválidas, strings com espaços). Salvar em `vendas.csv`.

**Implementado em:** `gerar_dataset_vendas(n_registros=200, seed=42)`

---

### RF02 — Inspecionar e Descrever os Dados
**Status: ✅ Implementado**

Exibir no console: shape, colunas, tipos, valores nulos e contagem de duplicatas.

**Implementado em:** `inspecionar_dados(df)`

---

### RF03 — Limpar e Tratar os Dados
**Status: ✅ Implementado**

Tratar: nulos em `quantidade` e `preco_unitario`, datas inválidas (parse com `errors='coerce'`), espaços extras em strings (`.str.strip()`). Registrar contagem de registros removidos.

**Implementado em:** `limpar_dados(df)` → retorna `(df_limpo, relatorio)`

---

### RF04 — Criar Colunas Derivadas
**Status: ✅ Implementado**

Novas colunas: `receita_total`, `mes`, `mes_nome`, `trimestre`, `ano`, `faixa_receita_item` (via `np.select`).

**Implementado em:** `criar_colunas_derivadas(df)`

---

### RF05 — Métricas Agregadas (groupby)
**Status: ✅ Implementado**

Receita por mês, top 5 produtos, receita por categoria, receita e ticket médio por região.

**Implementado em:** `calcular_metricas(df)`

---

### RF06 — Segmentar Clientes
**Status: ✅ Implementado**

Agrupar por cliente, calcular total gasto, classificar em Bronze / Prata / Ouro com função lambda.

**Implementado em:** `segmentar_clientes(df)`

| Segmento | Critério |
|---|---|
| Bronze | total_gasto < R$ 5.000 |
| Prata | R$ 5.000 ≤ total_gasto ≤ R$ 15.000 |
| Ouro | total_gasto > R$ 15.000 |

---

### RF07 — Estatísticas com NumPy
**Status: ✅ Implementado**

Converter coluna para array NumPy; calcular `mean`, `median`, `std`, `sum`, `percentile`; demonstrar broadcasting (normalização min-max) e operação vetorizada.

**Implementado em:** `calcular_estatisticas_numpy(df)`

---

### RF08 — Visualizações com Matplotlib e Seaborn
**Status: ✅ Implementado**

3 gráficos exportados como PNG: linha (receita/mês), barras horizontais (top produtos), pizza (distribuição por região).

**Implementado em:** `gerar_visualizacoes(df, metricas, output_dir)`

| Gráfico | Tipo | Arquivo |
|---|---|---|
| Receita por Mês | Linha com área | `vendas_por_mes.png` |
| Top 5 Produtos | Barras horizontais | `top_produtos.png` |
| Distribuição por Região | Pizza | `distribuicao_regioes.png` |

---

### RF09 — Classe AnalisadorDeVendas
**Status: ✅ Implementado**

Classe com `__init__`, atributos de instância e métodos encadeáveis via method chaining.

**Implementado em:** `class AnalisadorDeVendas`

Métodos: `.carregar()` · `.limpar()` · `.transformar()` · `.analisar()` · `.resumo()`

---

### RF10 — Herança AnalisadorComProjecao
**Status: ✅ Implementado**

Subclasse de `AnalisadorDeVendas` com `super().__init__()`, atributo `meses_projecao` e método `.projetar_tendencia()` com crescimento composto.

**Implementado em:** `class AnalisadorComProjecao(AnalisadorDeVendas)`

---

### RF11 — Lambda e Funções de Ordem Superior
**Status: ✅ Implementado**

4 usos de lambda em contextos distintos; função `processar_coluna(df, coluna, func)` que recebe outra função como argumento.

**Implementado em:** `processar_coluna(df, coluna, func)` + lambdas em RF06, RF13

---

### RF12 — Ler e Escrever CSV e JSON
**Status: ✅ Implementado**

Exportar `metricas_por_mes.csv`, `segmentacao_clientes.csv`, `estatisticas_gerais.json`; ler JSON exportado para confirmar integridade.

**Implementado em:** `exportar_resultados(metricas, clientes, stats)`

---

### RF13 — Expressões Regulares (re)
**Status: ✅ Implementado**

`re.sub()` para limpar strings de clientes; `re.compile()` com padrão para validar formato `Cliente_NNN`.

**Implementado em:** `limpar_strings_com_regex(df)`

---

### RF14 — Pipeline Completo (main)
**Status: ✅ Implementado**

Bloco `if __name__ == "__main__":` com função `main()` que executa todo o pipeline de ponta a ponta via `AnalisadorComProjecao`.

**Implementado em:** `main()` + `if __name__ == "__main__": main()`

---

## 4. Requisitos Não Funcionais

| ID | Requisito | Critério | Status |
|---|---|---|---|
| RNF01 | Portabilidade | Executa em Google Colab e localmente no Windows/Linux | ✅ |
| RNF02 | Reprodutibilidade | `seed=42` garante saídas consistentes | ✅ |
| RNF03 | Legibilidade | Funções documentadas com docstrings; nomes em português | ✅ |
| RNF04 | Modularidade | Cada RF em função separada; pipeline orquestrado pela classe | ✅ |
| RNF05 | Rastreabilidade | Commits semânticos por funcionalidade; branches descritivas | Parcial |

---

## 5. Fora de Escopo (v1.0)

- Machine Learning real (modelos sklearn, redes neurais)
- Interface gráfica ou dashboard interativo (Streamlit, Dash)
- Consumo de API REST externa
- Banco de dados (SQL/NoSQL)
- Testes automatizados com pytest
- CI/CD pipeline

---

## 6. Dependências e Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Biblioteca não instalada localmente | Médio | Alto | `requirements.txt` + instruções no README |
| Dataset gerado com seed diferente | Baixo | Médio | `seed=42` hardcoded no código |
| Prazo apertado (08/06/2026) | Médio | Alto | 19/21 tarefas concluídas — apenas vídeo e AVA pendentes |
| Gráficos não gerados no Colab | Baixo | Médio | `matplotlib.use("Agg")` configurado + `plt.savefig()` |
| Repositório privado no prazo | Médio | Alto | Tornar público antes da submissão |

---

## 7. Entregáveis Obrigatórios

- [x] `salesinsight.py` — pipeline completo
- [x] `vendas.csv` — dataset gerado
- [x] `README.md` — documentação do projeto
- [x] Repositório no GitHub (verificar se está público)
- [ ] Quadro Kanban com tarefas (GitHub Projects)
- [ ] Vídeo de até 5 minutos
- [ ] Links submetidos no AVA até 08/06/2026 às 12h
