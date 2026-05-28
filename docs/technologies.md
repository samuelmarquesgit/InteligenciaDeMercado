# Tecnologias — SalesInsight PY

> Stack técnica completa do projeto

---

## Linguagem Principal

### Python 3.10+
- Linguagem única do projeto (100% Python)
- Compatível com Google Colab, VS Code e terminal
- Versão mínima recomendada: 3.10 (suporte ao `match/case`, `typing` moderno)

---

## Bibliotecas de Análise de Dados

### pandas 2.x
| Recurso | Uso no projeto |
|---|---|
| `pd.read_csv()` | Carregamento do dataset `vendas.csv` |
| `pd.to_datetime(errors='coerce')` | Conversão e validação de datas |
| `.str.strip()` | Remoção de espaços extras em strings |
| `.dropna(subset=[...])` | Remoção de linhas com nulos críticos |
| `.groupby().agg()` | Métricas por mês, produto, categoria, região |
| `.apply(lambda)` | Segmentação de clientes e transformações |
| `.to_csv()` | Exportação de relatórios |
| `DataFrame`, `Series` | Estrutura principal de dados |

### NumPy 1.x / 2.x
| Recurso | Uso no projeto |
|---|---|
| `np.random.seed(42)` | Reprodutibilidade do dataset sintético |
| `np.mean`, `np.median`, `np.std` | Estatísticas descritivas |
| `np.percentile` | Cálculo de quartis (Q1, Q3) |
| `np.sum` | Receita total vetorizada |
| `np.select(condições, valores)` | Classificação por faixa de receita |
| Broadcasting (`receitas > media`) | Filtro vetorizado sem loop |
| Normalização min-max | `(x - x.min()) / (x.max() - x.min())` |

---

## Visualização

### Matplotlib 3.x
| Recurso | Uso no projeto |
|---|---|
| `plt.subplots()` | Criação de figuras |
| `ax.plot()` com `fill_between` | Gráfico de linha (receita por mês) |
| `ax.set_title/xlabel/ylabel` | Anotações dos gráficos |
| `plt.savefig(dpi=150)` | Exportação de PNG |
| `plt.rcParams` | Configuração global de estilos |

### Seaborn 0.13+
| Recurso | Uso no projeto |
|---|---|
| `sns.set_theme()` | Estilo global (`whitegrid`, paleta `muted`) |
| `sns.barplot()` | Top 5 produtos por receita |
| `sns.boxplot()` | Distribuição de receita por região |

---

## Módulos da Stdlib Python

| Módulo | Uso |
|---|---|
| `os` | `os.makedirs(exist_ok=True)`, `os.path.exists()` |
| `json` | `json.dump()`, `json.load()` — exportação/leitura de relatórios |
| `re` | `re.sub()`, `re.compile()` — limpeza de strings com regex |
| `datetime`, `timedelta` | Geração de datas sintéticas, extração de componentes |
| `random` | Geração do dataset sintético (`random.seed(42)`) |

---

## Ferramentas de Desenvolvimento

### VS Code
- Extensão Python (Pylance, Pylint)
- IntelliSense e debug integrado
- Execução via terminal integrado

### Google Colab
- Ambiente recomendado para a disciplina
- Todas as libs pré-instaladas
- Suporte a notebooks `.ipynb`

### Git + GitHub
- Controle de versão
- Branches descritivas por funcionalidade
- Commits semânticos (Conventional Commits)

### GitHub Desktop
- Interface gráfica para commits e push
- Recomendado pela disciplina

---

## Ambiente Virtual

```bash
# Criar venv
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Verificar instalação
pip list
```

### requirements.txt
```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.13
```

---

## Compatibilidade

| Ambiente | Suporte |
|---|---|
| Google Colab | ✅ Nativo (sem instalação) |
| Windows 10/11 + Python 3.10+ | ✅ Via pip |
| macOS + Python 3.10+ | ✅ Via pip |
| Linux + Python 3.10+ | ✅ Via pip |
| Jupyter Notebook local | ✅ Via pip |
