# Steering — Tecnologia

> Decisões técnicas, stack e princípios de implementação
> Atualizado em: 01/06/2026

---

## Stack Definitiva

| Camada | Tecnologia | Versão mínima | Justificativa |
|---|---|---|---|
| Linguagem | Python | 3.10+ | Requisito do mini-projeto |
| Dados tabulares | pandas | 2.0 | API moderna, `pd.to_datetime(errors='coerce')` |
| Computação numérica | NumPy | 1.24 | `np.select`, broadcasting, vetorização |
| Visualização | Matplotlib | 3.7 | `plt.savefig()`, backend Agg |
| Visualização | Seaborn | 0.13 | `sns.set_theme()`, paletas prontas |
| Stdlib | re, json, datetime, os, random | Built-in | Sem dependências extras |

---

## Decisões Técnicas

### Por que um arquivo único (`salesinsight.py`)?
Requisito explícito do mini-projeto. Em projetos reais, o pipeline seria modularizado em `src/pipeline/`, `src/models/`, etc. A estrutura de pastas `docs/`, `specs/` e `steering/` organiza a documentação sem fragmentar o código.

### Por que `seed=42`?
Garante **reprodutibilidade total**: qualquer pessoa que execute `python salesinsight.py` obterá exatamente o mesmo dataset, os mesmos resultados e os mesmos gráficos. Essencial para avaliação por terceiros.

### Por que `np.select` em vez de `df.apply(lambda)`?
`np.select` opera sobre arrays NumPy de forma **vetorizada**, sem loop Python. Para classificações condicionais em DataFrames, é 10–100× mais rápido. O código comunica claramente a intenção de vetorização.

### Por que `pd.to_datetime(errors='coerce')` em vez de tratamento manual?
É a abordagem idiomática do pandas para datas inválidas. Converte automaticamente para `NaT` (Not a Time), que pode ser tratado com `.dropna()`. Evita regex manual para parsing de datas.

### Por que `encoding="utf-8"` nos CSVs?
Compatibilidade universal com Python, Linux, Colab e Excel moderno. O `utf-8-sig` (BOM) foi considerado mas pode causar problemas em ambientes Linux/Colab. `utf-8` puro é mais portátil.

### Por que method chaining na classe?
Permite pipeline fluente e legível em um único bloco:
```python
analisador.carregar().limpar().transformar().analisar().projetar_tendencia().resumo()
```
Cada método retorna `self`, habilitando o encadeamento sem variáveis intermediárias.

### Por que herança em vez de composição para `AnalisadorComProjecao`?
Herança é um **requisito explícito** do RF10. Em termos de design puro, composição seria mais flexível, mas herança demonstra o conceito de OOP exigido e usa `super()` conforme especificado.

### Por que `matplotlib.use("Agg")`?
O backend `Agg` (Anti-Grain Geometry) renderiza gráficos para arquivo sem precisar de um display/janela. Garante compatibilidade com Google Colab, servidores e ambientes headless. Deve ser configurado **antes** do `import matplotlib.pyplot`.

---

## Padrões de Código

### Type hints nas funções
```python
def limpar_dados(df: pd.DataFrame) -> tuple:
def gerar_dataset_vendas(n_registros: int = 200, seed: int = 42) -> pd.DataFrame:
def calcular_metricas(df: pd.DataFrame) -> dict:
```

### f-strings para formatação monetária
```python
print(f"  Receita total  : R$ {total:>15,.2f}")
print(f"  [RF07] média: R$ {stats['media']:,.2f} | total: R$ {stats['total']:,.2f}")
```

### Criação segura de pastas
```python
os.makedirs("outputs/graficos", exist_ok=True)
```

### Fechamento de figuras
```python
fig.savefig(caminho, dpi=100, bbox_inches="tight")
plt.close(fig)  # Libera memória — crítico em loops de gráficos
```

---

## Limites Técnicos (v1.0)

| Limite | Valor | Configurável? |
|---|---|---|
| Registros no dataset | 200 | Sim — `n_registros` |
| Seed do dataset | 42 | Sim — `seed` |
| Meses de projeção | 3 | Sim — `meses_projecao` |
| Taxa de crescimento | 5% a.m. | Sim — `taxa_crescimento` |
| Produtos distintos | 7 | Não (constante `PRODUTOS`) |
| Clientes | 50 | Não (hardcoded na geração) |
| Gráficos gerados | 3 | Não sem alterar `gerar_visualizacoes` |

---

## Checklist de Qualidade de Código

- [x] Todas as funções têm docstring
- [x] Nomes de variáveis em português e descritivos
- [x] `seed=42` presente com `np.random.default_rng(seed)` e `random.seed(seed)`
- [x] `plt.close(fig)` após cada `fig.savefig()`
- [x] `os.makedirs(exist_ok=True)` antes de salvar arquivos
- [x] Sem loops Python onde `np.select` ou vetorização são possíveis
- [x] `ensure_ascii=False` no `json.dump`
- [x] Bloco `if __name__ == "__main__":` no final
- [x] `matplotlib.use("Agg")` antes de `import matplotlib.pyplot`
- [x] Type hints nas assinaturas das funções

---

## Ambiente de Desenvolvimento Recomendado

```
VS Code
  ├── Extensão: Python (Microsoft)
  ├── Extensão: Pylance
  ├── Extensão: GitLens (opcional)
  └── Terminal integrado (PowerShell / bash)

Google Colab (alternativa)
  └── Todas as libs pré-instaladas
  └── Suporte nativo a !python salesinsight.py
```
