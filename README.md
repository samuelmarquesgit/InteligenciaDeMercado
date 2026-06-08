# SalesInsight PY — Pipeline de Análise de Vendas

> Mini-Projeto Avaliativo · Módulo 01 · Semana 08 · Desenvolvedor(a) em IA para Análise Preditiva · SCTEC

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-76b9d8)](https://seaborn.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)](https://github.com/samuelmarquesgit/InteligenciaDeMercado)

---

## Sobre o Projeto

O **SalesInsight PY** é um pipeline completo de análise e visualização de dados de vendas, desenvolvido 100% em Python como mini-projeto avaliativo do Módulo 01 do curso de IA para Análise Preditiva (SCTEC).

O sistema executa o ciclo completo de dados: **ingestão → limpeza → transformação → análise → visualização → exportação**, produzindo métricas agregadas, segmentação de clientes Bronze/Prata/Ouro, estatísticas vetorizadas com NumPy e projeção de tendência de receita, com saídas em CSV, JSON e PNG.

> **Prazo de entrega:** 08/06/2026 às 22h · **Peso:** 25% da nota do Módulo 01


## O que o sistema analisa

- Receita total e volume de vendas por mês, trimestre e ano
- Top produtos e categorias líderes de receita
- Desempenho comercial por região geográfica
- Segmentação de clientes por nível de gasto (Bronze · Prata · Ouro)
- Estatísticas descritivas vetorizadas (média, mediana, desvio-padrão, percentis)
- Projeção de tendência de receita para os próximos 3 meses

---

## Arquitetura do Pipeline

```
vendas.csv (200 linhas)
    │
    ▼ RF01 — gerar_dataset_vendas()
DataFrame Bruto (200 × 8)
    │
    ├── RF02 — inspecionar_dados()           → diagnóstico no console
    │
    ▼ RF03 — limpar_dados()
    ▼ RF13 — limpar_strings_com_regex()
DataFrame Limpo (~184 × 10)
    │
    ▼ RF04 — criar_colunas_derivadas()
    ▼ RF11 — processar_coluna() [HOF]
DataFrame Enriquecido (~184 × 15)
    │
    ├── RF05 — calcular_metricas()           → dict {por_mes, top_produtos, por_regiao}
    ├── RF06 — segmentar_clientes()          → Bronze / Prata / Ouro
    └── RF07 — calcular_estatisticas_numpy() → stats vetorizadas
              │
              ├── RF08 — gerar_visualizacoes()   → 3× PNG em outputs/graficos/
              └── RF12 — exportar_resultados()   → CSV + JSON em outputs/

AnalisadorComProjecao (RF09 + RF10)
    └── .carregar().limpar().transformar().analisar().projetar_tendencia().resumo()
```

---

## Estrutura do Repositório

```
InteligenciaDeMercado/
│
├── salesinsight.py              # Pipeline principal — ponto de entrada único
├── vendas.csv                   # Dataset sintético gerado pelo código
├── requirements.txt             # Dependências Python
├── pytest.ini                   # Configuração de testes
├── README.md                    # Este arquivo
│
├── outputs/
│   ├── metricas_por_mes.csv     # Gerado pelo pipeline
│   ├── segmentacao_clientes.csv # Gerado pelo pipeline
│   ├── estatisticas_gerais.json # Gerado pelo pipeline
│   └── graficos/
│       ├── vendas_por_mes.png
│       ├── top_produtos.png
│       └── distribuicao_regioes.png
│
├── docs/                        # Documentação técnica
│   ├── PRD.md                   # Product Requirements Document
│   ├── BACKLOG.md               # Rastreamento de tarefas
│   ├── architeture.md           # Arquitetura e decisões de design
│   ├── roadmap.md               # Linha do tempo e entregas
│   ├── gitflow.md               # Convenções Git
│   ├── technologies.md          # Stack técnica detalhada
│   └── test_report.md           # Relatório de validação
│
├── specs/                       # Especificações técnicas
│   ├── requirements.md          # RFs e RNFs com critérios de aceite
│   ├── tasks.md                 # Tasks de implementação
│   └── design.md                # Design de código e console
│
└── steering/                    # Direcionamento estratégico
    ├── product.md               # Visão e critérios de sucesso
    ├── structure.md             # Organização e convenções
    └── tech.md                  # Decisões técnicas
```

---

## Como Executar

### Google Colab (recomendado para a disciplina)

```python
# 1. Faça upload do salesinsight.py no Colab
# 2. Execute a célula abaixo:
!python salesinsight.py
```

### VS Code / Local

```bash
# 1. Clone o repositório
git clone git@github.com:samuelmarquesgit/InteligenciaDeMercado.git
cd InteligenciaDeMercado

# 2. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o pipeline
python salesinsight.py
```

### Saída esperada

```
=======================================================
  SALESINSIGHT PY — Pipeline de Análise de Vendas
=======================================================
  [RF01] Dataset gerado: 200 registros | salvo em vendas.csv
  [RF03] Limpeza: 200 → 184 registros (16 removidos)
  [RF04] Colunas derivadas criadas: [receita_total, mes, ...]
  [RF06] Segmentos: {'Ouro': X, 'Prata': X, 'Bronze': X}
  [RF07] NumPy stats → média: R$ X.XXX,XX | total: R$ XXX.XXX,XX
  [RF08] 3 gráficos salvos em 'outputs/graficos'
  [RF12] Exportados: metricas_por_mes.csv | segmentacao_clientes.csv | ...
  Pipeline concluído com sucesso!
```

---

## Requisitos Funcionais Implementados

| RF | Funcionalidade | Implementação |
|---|---|---|
| RF01 | Geração de dataset sintético | `gerar_dataset_vendas(n=200, seed=42)` |
| RF02 | Inspeção e diagnóstico | `inspecionar_dados(df)` |
| RF03 | Limpeza e tratamento | `limpar_dados(df)` |
| RF04 | Feature engineering | `criar_colunas_derivadas(df)` com `np.select` |
| RF05 | Métricas agregadas | `calcular_metricas(df)` com `groupby` |
| RF06 | Segmentação de clientes | `segmentar_clientes(df)` com `lambda` |
| RF07 | Estatísticas NumPy | `calcular_estatisticas_numpy(df)` vetorizado |
| RF08 | Visualizações PNG | `gerar_visualizacoes(df, metricas)` — 3 gráficos |
| RF09 | Classe com method chaining | `AnalisadorDeVendas` |
| RF10 | Herança + projeção | `AnalisadorComProjecao(AnalisadorDeVendas)` |
| RF11 | Higher-order function + lambda | `processar_coluna(df, col, func)` |
| RF12 | Exportação CSV e JSON | `exportar_resultados(metricas, clientes, stats)` |
| RF13 | Expressões regulares | `limpar_strings_com_regex(df)` |
| RF14 | Pipeline completo | `main()` — orquestra tudo de ponta a ponta |

---

## Conceitos de Python Aplicados

| Conceito | Onde é aplicado |
|---|---|
| Variáveis e tipos (`int`, `float`, `str`, `bool`, `list`, `dict`) | Dataset, métricas, relatório de limpeza |
| `if / elif / else` | Classificação de segmentos e faixas de receita |
| `for` | Loops de exibição e iteração sobre colunas |
| Funções com parâmetros e retorno tipado | Todas as 11 funções do pipeline |
| Funções lambda | Segmentação (RF06), limpeza (RF13), HOF (RF11) |
| Higher-order function | `processar_coluna()` — recebe função como argumento |
| Leitura/escrita de CSV | `pd.read_csv()` / `.to_csv()` |
| Leitura/escrita de JSON | `json.dump()` / `json.load()` com verificação |
| Módulo `datetime` | Extração de mês, trimestre e ano |
| Expressões regulares (`re`) | `re.compile()` + `re.sub()` para validação e limpeza |
| Pandas — `DataFrame`, `groupby`, filtros, `apply` | Estrutura de dados e agregações |
| NumPy — arrays, `np.select`, broadcasting, vetorização | Estatísticas e classificações condicionais |
| Matplotlib + Seaborn — gráficos PNG | 3 gráficos exportados em `outputs/graficos/` |
| Classes, `__init__`, `self`, herança, `super()` | `AnalisadorDeVendas` → `AnalisadorComProjecao` |
| GitHub Flow, branches descritivas, commits semânticos | Versionamento completo do projeto |

---

## Dependências

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.13
```

> O Google Colab já possui todas as bibliotecas instaladas por padrão.

---

## Links do Projeto

| Recurso | Link |
|---|---|
| Repositório GitHub | [samuelmarquesgit/InteligenciaDeMercado](https://github.com/samuelmarquesgit/InteligenciaDeMercado) |
| Quadro Kanban | [SalesInsight PY — Kanban](https://github.com/users/samuelmarquesgit/projects/1) |
| Vídeo de Demonstração | _[Google Drive / YouTube — a gravar]_ |

---

## Critérios de Avaliação

| Critério | Peso | Status |
|---|---|---|
| README + Kanban + Vídeo + GitHub público | 40% (4 pts) | Parcial — vídeo pendente |
| Limpeza, transformação e groupby (RF03–RF06) | 25% (2,5 pts) | Implementado |
| NumPy vetorizado (RF07) | 7,5% (0,75 pt) | Implementado |
| Visualizações PNG (RF08) | 10% (1 pt) | Implementado |
| OOP com herança (RF09–RF10) | 12,5% (1,25 pts) | Implementado |
| Lambda + HOF + I/O (RF11–RF12) | 5% (0,5 pt) | Implementado |

---

## Arquitetura Cliente-Servidor (Contexto)

Neste projeto, os dados são lidos de um arquivo CSV local. Em um cenário de produção real, esses dados viriam de uma **API REST**: o cliente (script Python) faria uma requisição HTTP GET a um servidor que retornaria os dados em JSON. A biblioteca `requests` permite consumir essas APIs diretamente em Python, seguindo a arquitetura cliente-servidor típica de sistemas de análise de dados modernos.

---

## Autor

**Samuel Marques** — [@samuelmarquesgit](https://github.com/samuelmarquesgit)
**Bruno Duarte da Silveira** — [@bruno-d-silveira] (https://github.com/bruno-d-silveira)
**Eduardo Schmidt Bauer** — [@eduardobauer1981] (https://github.com/eduardobauer1981)

*Projeto desenvolvido para a disciplina de IA – Desenvolvimento de IA para Análise Preditiva · SCTEC · 2026*
