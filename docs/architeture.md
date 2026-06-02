# Arquitetura — SalesInsight PY

> Visão técnica do pipeline, hierarquia de classes e decisões de design

---

## Visão Geral

O SalesInsight PY adota uma arquitetura de **pipeline em camadas**, onde cada camada tem responsabilidade única e alimenta a seguinte. A orquestração é feita pela hierarquia de classes `AnalisadorDeVendas` → `AnalisadorComProjecao`.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          salesinsight.py                            │
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────────┐  │
│  │ Ingestão │──►│ Limpeza  │──►│Transform.│──►│    Análise      │  │
│  │ RF01–02  │   │ RF03, 13 │   │  RF04,11 │   │  RF05, 06, 07   │  │
│  └──────────┘   └──────────┘   └──────────┘   └────────┬────────┘  │
│                                                          │           │
│                 ┌────────────────────────────────────────┤           │
│                 │  Saídas                                │           │
│                 │  Visualização (RF08) → 3× PNG         │           │
│                 │  Exportação  (RF12) → CSV + JSON      │           │
│                 │  Projeção    (RF10) → tendência        │           │
│                 └────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Camadas do Pipeline

### Camada 1 — Ingestão (RF01, RF02)
- Gera `vendas.csv` com 200 registros sintéticos e dados intencionalmente sujos
- Exibe diagnóstico: shape, dtypes, nulos por coluna, duplicatas
- **Entrada:** nenhuma · **Saída:** `df_bruto` (200 × 8)

### Camada 2 — Limpeza (RF03, RF13)
- Remove espaços extras em strings (`.str.strip()`)
- Converte `data_venda` para datetime com `pd.to_datetime(errors='coerce')`
- Remove linhas com nulos em campos críticos
- Aplica regex para validação e limpeza da coluna `cliente`
- Registra relatório de limpeza (registros removidos, tipos de problema)
- **Entrada:** `df_bruto` · **Saída:** `df_limpo` (~184 × 10) + `relatorio`

### Camada 3 — Transformação (RF04, RF11)
- Cria 6 colunas derivadas: `receita_total`, `mes`, `mes_nome`, `trimestre`, `ano`, `faixa_receita_item`
- Usa `np.select` para transformações condicionais vetorizadas (sem loops Python)
- Aplica higher-order function `processar_coluna()` com lambda
- **Entrada:** `df_limpo` · **Saída:** `df_enriquecido` (~184 × 15)

### Camada 4 — Análise (RF05, RF06, RF07)
- Agregações com `groupby`: por mês, produto, categoria e região
- Segmentação de clientes com lambda (Bronze / Prata / Ouro)
- Estatísticas NumPy: mean, median, std, percentile, broadcasting
- **Entrada:** `df_enriquecido` · **Saída:** `metricas` (dict) + `clientes` (DataFrame) + `stats` (dict)

### Camada 5 — Saídas (RF08, RF10, RF12)
- 3 gráficos PNG exportados em `outputs/graficos/`
- Projeção de tendência para N meses futuros
- 2 CSV e 1 JSON exportados em `outputs/`
- **Entrada:** métricas + DataFrames · **Saída:** arquivos em disco

---

## Hierarquia de Classes

```
AnalisadorDeVendas
│   __init__(caminho_arquivo)
│   ├── self.caminho_arquivo
│   ├── self.df_bruto     = None
│   ├── self.df_limpo     = None
│   ├── self.metricas     = None
│   ├── self.clientes     = None
│   └── self.stats        = None
│
│   carregar()    → pd.read_csv() → self.df_bruto
│   limpar()      → limpar_dados() → self.df_limpo
│   transformar() → criar_colunas_derivadas() → self.df_limpo
│   analisar()    → calcular_metricas() + segmentar_clientes() + ...
│   resumo()      → exibe receita total, clientes e média mensal
│
└── AnalisadorComProjecao(AnalisadorDeVendas)
        __init__(caminho_arquivo, meses_projecao=3)
        ├── super().__init__(caminho_arquivo)
        ├── self.meses_projecao
        └── self.projecoes = []

        projetar_tendencia(taxa_crescimento=0.05)
            → crescimento composto sobre média mensal
            → self.projecoes = [{mes, receita_projetada}, ...]
```

**Padrão method chaining** — todos os métodos retornam `self`:
```python
analisador = AnalisadorComProjecao("vendas.csv", meses_projecao=3)
(
    analisador
    .carregar()
    .limpar()
    .transformar()
    .analisar()
    .projetar_tendencia()
    .resumo()
)
```

---

## Fluxo de Dados

```
vendas.csv (200 linhas × 8 colunas)
    │
    ▼ pd.read_csv()
DataFrame Bruto (200 × 8)
    │   id_venda | data_venda | cliente | produto | categoria | regiao | quantidade | preco_unitario
    │   ~16 linhas com dados sujos (nulos, datas inválidas, espaços)
    │
    ▼ limpar_dados() + limpar_strings_com_regex()
DataFrame Limpo (~184 × 10)
    │   + cliente_limpo | cliente_valido
    │
    ▼ criar_colunas_derivadas() + processar_coluna()
DataFrame Enriquecido (~184 × 15)
    │   + receita_total | mes | mes_nome | trimestre | ano
    │   + faixa_receita_item | receita_total_transformado
    │
    ├──► calcular_metricas()          → {por_mes (12), top_produtos (5), por_categoria (4), por_regiao (5)}
    ├──► segmentar_clientes()         → DataFrame (50 × 3): cliente | total_gasto | segmento
    ├──► calcular_estatisticas_numpy() → {media, mediana, std, total, min, max, p25, p75}
    ├──► gerar_visualizacoes()         → vendas_por_mes.png, top_produtos.png, distribuicao_regioes.png
    └──► exportar_resultados()         → metricas_por_mes.csv, segmentacao_clientes.csv, estatisticas_gerais.json
```

---

## Decisões de Design

| Decisão | Alternativa Considerada | Motivo da Escolha |
|---|---|---|
| Seed fixo `42` | Seed dinâmica | Reprodutibilidade garantida entre execuções e avaliações |
| `pd.to_datetime(errors='coerce')` | Regex manual para datas | API idiomática do pandas; converte inválidas para `NaT` |
| `np.select` para classificação | `df.apply(lambda)` | Vetorizado; 10–100× mais rápido que loop Python |
| Method chaining na classe | Chamadas separadas | API fluente; pipeline legível em bloco único |
| Subclasse para projeção | Composição | RF10 exige herança explícita com `super()` |
| `matplotlib.use("Agg")` | Backend padrão | Compatibilidade com ambientes sem display (Colab, servidor) |
| `encoding="utf-8"` nos CSVs | `utf-8-sig` | Compatibilidade universal; evitar BOM em Linux/Colab |

---

## Diagrama de Módulos

```
salesinsight.py
│
├── Imports
│   ├── os, re, json, random, datetime
│   ├── numpy as np
│   ├── pandas as pd
│   ├── matplotlib (Agg backend)
│   └── seaborn as sns
│
├── Constantes do domínio
│   ├── PRODUTOS (7 itens)
│   ├── REGIOES (5 regiões)
│   ├── CATEGORIAS (dict produto→categoria)
│   └── NOMES_MESES (dict int→str pt-BR)
│
├── Funções do pipeline (RF01–RF08, RF11–RF13)
│   ├── gerar_dataset_vendas()          ← RF01
│   ├── inspecionar_dados()             ← RF02
│   ├── limpar_dados()                  ← RF03
│   ├── criar_colunas_derivadas()       ← RF04
│   ├── calcular_metricas()             ← RF05
│   ├── segmentar_clientes()            ← RF06
│   ├── calcular_estatisticas_numpy()   ← RF07
│   ├── gerar_visualizacoes()           ← RF08
│   ├── processar_coluna()              ← RF11
│   ├── exportar_resultados()           ← RF12
│   └── limpar_strings_com_regex()      ← RF13
│
├── Classes OOP
│   ├── AnalisadorDeVendas              ← RF09
│   └── AnalisadorComProjecao           ← RF10
│
└── Ponto de entrada
    ├── main()                          ← RF14
    └── if __name__ == "__main__"
```

---

## Características Técnicas

| Característica | Detalhe |
|---|---|
| Arquivo único | `salesinsight.py` (~600 linhas) |
| Dataset | 200 registros × 8 colunas, seed=42 |
| Dados sujos injetados | 5 nulos em `quantidade`, 5 em `preco_unitario`, 1 data inválida, 3 strings com espaço |
| Registros após limpeza | ~184 (remove ~16 problemáticos) |
| Gráficos gerados | 3 PNG (dpi=100) |
| Outputs exportados | 2 CSV + 1 JSON |
| Clientes únicos | 50 (Cliente_001 a Cliente_050) |
| Período dos dados | 2024-01-01 a 2024-12-31 |
