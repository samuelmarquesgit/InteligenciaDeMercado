# SalesInsight PY — Pipeline de Análise Preditiva de Vendas

> Mini-Projeto Avaliativo · Módulo 01 · Semana 08 · Desenvolvedor(a) em IA para Análise Preditiva [T1] · SCTEC

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-76b9d8)](https://seaborn.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Sobre o Projeto

O **SalesInsight PY** é um pipeline completo de análise e visualização de dados de vendas desenvolvido 100% em Python. O sistema lê, limpa, transforma, analisa e visualiza um dataset de vendas de varejo, gerando métricas agregadas, segmentação de clientes e uma projeção simples de tendência de receita.

O projeto é entregue como parte avaliativa do Módulo 01 do curso de IA para Análise Preditiva da SCTEC, com peso de **25% da nota do módulo** e prazo de entrega em **08/06/2026 às 12h**.

---

## O que o sistema analisa

- Receita total e volume de vendas por mês e trimestre
- Top produtos e categorias por receita
- Desempenho comercial por região
- Segmentação de clientes por nível de gasto (Bronze · Prata · Ouro)
- Projeção simples de tendência para os próximos 3 meses (média móvel)
- Exportação de relatórios em CSV, JSON e gráficos em PNG

---

## Estrutura do Projeto

```
InteligenciaDeMercado/
│
├── salesinsight.py              # Pipeline principal (ponto de entrada)
├── vendas.csv                   # Dataset gerado sinteticamente pelo código
├── README.md                    # Este arquivo
│
├── outputs/
│   ├── metricas_por_mes.csv
│   ├── segmentacao_clientes.csv
│   ├── estatisticas_gerais.json
│   └── graficos/
│       ├── vendas_por_mes.png
│       ├── top_produtos.png
│       └── distribuicao_regioes.png
│
├── docs/                        # Documentação técnica do projeto
├── specs/                       # Especificações e requisitos
├── steering/                    # Direcionamento de produto e arquitetura
└── .github/                     # Templates de PR e Issues
```

---

## Como Executar

### Google Colab (recomendado para a disciplina)

1. Faça upload do `salesinsight.py` para o Colab
2. Execute: `!python salesinsight.py`
3. Ou cole o conteúdo em células de um notebook `.ipynb`

### VS Code / Local

```bash
# 1. Clone o repositório
git clone git@github.com:samuelmarquesgit/InteligenciaDeMercado.git
cd InteligenciaDeMercado

# 2. Crie e ative o ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o pipeline
python salesinsight.py
```

### Terminal direto

```bash
pip install pandas numpy matplotlib seaborn
python salesinsight.py
```

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

## Conceitos de Python Aplicados

| Conceito | Onde é usado |
|---|---|
| Variáveis, tipos (`int`, `float`, `str`, `bool`, `list`, `dict`) | Dataset, métricas, relatório de limpeza |
| `if / elif / else` | Classificação de segmentos e faixas de receita |
| `for / while` | Loops de exibição e iteração sobre dados |
| Funções com parâmetros e retorno | Todas as funções do pipeline |
| Funções lambda | Segmentação de clientes, `apply`, `sorted` |
| Função que recebe função como argumento | `processar_coluna()` (higher-order function) |
| Leitura/escrita de CSV | `pd.read_csv()` / `.to_csv()` |
| Leitura/escrita de JSON | `json.dump()` / `json.load()` |
| Módulo `datetime` | Extração de mês, trimestre e ano |
| Expressões regulares (`re`) | Limpeza de strings com `re.sub()` / `re.compile()` |
| Pandas — DataFrames, `groupby`, filtros | Estrutura principal de dados e agregações |
| NumPy — arrays, vetorização, broadcasting | Estatísticas e `np.select` |
| Matplotlib + Seaborn — gráficos PNG | Receita por mês, top produtos, boxplot |
| Classes, `__init__`, `self`, herança, `super()` | `AnalisadorDeVendas` → `AnalisadorComProjecao` |
| GitHub Flow, branches, commits semânticos | Versionamento do projeto |
| Kanban | Organização das tarefas no GitHub Projects |

---

## Arquitetura Cliente-Servidor (Contexto)

Neste projeto, os dados são lidos de um arquivo local CSV. Em um cenário de produção real, esses dados poderiam vir de uma **API REST**: o cliente (script Python) faria uma requisição HTTP GET a um servidor que retornaria os dados em JSON. A biblioteca `requests` permite consumir essas APIs diretamente em Python, seguindo a arquitetura cliente-servidor típica de sistemas de dados modernos.

---

## Ferramentas Utilizadas

- **Python 3.10+** — linguagem principal
- **pandas** — manipulação e análise de dados tabulares
- **NumPy** — operações vetorizadas e estatísticas
- **Matplotlib / Seaborn** — visualizações e exportação de gráficos
- **re, json, datetime, os, random** — módulos padrão da stdlib
- **VS Code / Google Colab** — ambiente de desenvolvimento
- **GitHub + GitHub Desktop** — versionamento
- **GitHub Projects** — quadro Kanban

---

## Quadro Kanban

> Acesse o quadro no GitHub Projects: [link do projeto no GitHub Projects]

---

## Vídeo de Demonstração

> [Inserir link do Google Drive ou YouTube aqui]

---

## Autor

**Samuel Marques** — [@samuelmarquesgit](https://github.com/samuelmarquesgit)

---

*Projeto desenvolvido para a disciplina de IA – Desenvolvimento de IA para Análise Preditiva · SCTEC · 2026*
