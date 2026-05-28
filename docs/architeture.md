# Arquitetura — SalesInsight PY

> Visão técnica do pipeline e das decisões de design

---

## Visão Geral

O SalesInsight PY adota uma arquitetura de **pipeline em camadas**, onde cada camada tem responsabilidade única e alimenta a próxima. A orquestração é feita por uma hierarquia de classes.

```
┌─────────────────────────────────────────────────────────────┐
│                     salesinsight.py                         │
│                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐ │
│  │  Ingestão│ → │ Limpeza  │ → │Transform.│ → │Análise  │ │
│  │  RF01-02 │   │  RF03,13 │   │   RF04   │   │ RF05-07 │ │
│  └──────────┘   └──────────┘   └──────────┘   └────┬────┘ │
│                                                      │      │
│                 ┌──────────────────────────────┐     │      │
│                 │  Visualização (RF08)          │ ◄───┘      │
│                 │  Exportação (RF12)            │            │
│                 │  Projeção (RF10)              │            │
│                 └──────────────────────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

---

## Camadas do Pipeline

### Camada 1 — Ingestão (RF01, RF02)
- Gera ou lê `vendas.csv` com dados sintéticos
- Exibe metadados: shape, dtypes, nulos, estatísticas descritivas
- **Saída:** DataFrame bruto (`df_bruto`)

### Camada 2 — Limpeza (RF03, RF13)
- Remove nulos críticos, datas inválidas, strings sujas
- Aplica regex para validação/limpeza de strings
- Registra relatório de limpeza
- **Saída:** DataFrame limpo (`df_limpo`)

### Camada 3 — Transformação (RF04, RF11)
- Cria colunas derivadas: `receita_total`, `mes`, `trimestre`, `faixa_receita_item`
- Usa `np.select` para transformações condicionais vetorizadas
- Aplica lambdas e funções de ordem superior
- **Saída:** DataFrame enriquecido

### Camada 4 — Análise (RF05, RF06, RF07)
- Agregações com `groupby`: por mês, produto, categoria, região
- Segmentação de clientes com lambda
- Estatísticas NumPy: mean, median, std, percentile, broadcasting
- **Saída:** dicionário de métricas + DataFrame de clientes

### Camada 5 — Visualização e Exportação (RF08, RF12)
- 3+ gráficos exportados como PNG (linha, barras, boxplot)
- Exportação de CSV e JSON
- **Saída:** arquivos em `outputs/`

### Camada 6 — Projeção (RF10)
- Média móvel dos últimos 3 meses como base
- Projeção para N meses futuros
- **Saída:** lista de projeções

---

## Hierarquia de Classes

```
AnalisadorDeVendas
│   __init__(caminho_arquivo)
│   carregar()       → lê CSV
│   limpar()         → RF03 + RF13
│   transformar()    → RF04
│   analisar()       → RF05 + RF06 + RF07
│   visualizar()     → RF08
│   exportar_relatorio() → RF12
│   resumo()
│
└── AnalisadorComProjecao (herda de AnalisadorDeVendas)
        __init__(caminho_arquivo, meses_projecao=3)
        projetar_tendencia()    → RF10 (média móvel)
        exibir_projecao_detalhada()
```

O padrão **method chaining** (retorno de `self`) permite encadeamento fluente:
```python
analisador.carregar().limpar().transformar().analisar().projetar_tendencia().visualizar()
```

---

## Fluxo de Dados

```
vendas.csv (200 linhas, 8 colunas)
    │
    ▼ pd.read_csv()
DataFrame Bruto (200 × 8)
    │
    ▼ limpar_dados() + limpar_strings_com_regex()
DataFrame Limpo (~180 × 10)     ← remove ~20 linhas inválidas
    │
    ▼ criar_colunas_derivadas()
DataFrame Enriquecido (~180 × 15)  ← +6 colunas derivadas
    │
    ├─► calcular_metricas()       → dict{por_mes, top_produtos, ...}
    ├─► segmentar_clientes()      → DataFrame(50 clientes × 3 cols)
    ├─► calcular_estatisticas_numpy() → dict{media, mediana, std, total}
    ├─► gerar_visualizacoes()     → 3× PNG em outputs/graficos/
    └─► exportar_resultados()     → 2× CSV + 1× JSON em outputs/
```

---

## Decisões de Design

| Decisão | Alternativa Considerada | Motivo da Escolha |
|---|---|---|
| Seed fixo (42) | Seed dinâmica | Reprodutibilidade garantida entre execuções |
| `pd.to_datetime(errors='coerce')` | Regex manual para datas | API idiomática do pandas; eficiente |
| `np.select` para classificação | `df.apply(lambda)` | Vetorizado; sem loop Python |
| Method chaining na classe | Chamadas separadas | API fluente; pipeline mais legível |
| Subclasse para projeção | Composição | Requisito do RF10 (herança obrigatória) |
| `utf-8-sig` no CSV | `utf-8` | Compatibilidade com Excel no Windows |

---

## Diagrama de Módulos

```
salesinsight.py
│
├── import pandas as pd
├── import numpy as np
├── import matplotlib.pyplot as plt
├── import seaborn as sns
├── import os
├── import json
├── import re
├── from datetime import datetime, timedelta
├── import random
│
├── def gerar_dataset_vendas()
├── def inspecionar_dados()
├── def limpar_dados()
├── def limpar_strings_com_regex()
├── def criar_colunas_derivadas()
├── def calcular_metricas()
├── def segmentar_clientes()
├── def calcular_estatisticas_numpy()
├── def processar_coluna()
├── def gerar_visualizacoes()
├── def exportar_resultados()
│
├── class AnalisadorDeVendas
│   └── class AnalisadorComProjecao(AnalisadorDeVendas)
│
└── def main()
    └── if __name__ == "__main__"
```
