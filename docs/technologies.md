# Tecnologias — SalesInsight PY

> Stack técnica completa do projeto

---

## Linguagem Principal

### Python 3.10+
- Linguagem única do projeto (100% Python)
- Compatível com Google Colab, VS Code e terminal
- Versão mínima: 3.10 (suporte moderno a type hints)

---

## Bibliotecas de Análise de Dados

### pandas 2.x

| Recurso | Uso no projeto |
|---|---|
| `pd.read_csv()` | Carregamento do dataset `vendas.csv` |
| `pd.to_datetime(errors='coerce')` | Conversão e validação de datas (inválidas → NaT) |
| `.str.strip()` | Remoção de espaços extras em strings |
| `.dropna(subset=[...])` | Remoção de linhas com nulos críticos |
| `.groupby().agg()` | Métricas por mês, produto, categoria, região |
| `.apply(lambda)` | Segmentação de clientes e transformações |
| `.to_csv(encoding="utf-8")` | Exportação de relatórios |
| `DataFrame`, `Series` | Estrutura principal de dados |
| `.reset_index(drop=True)` | Reinicialização de índice após filtros |
| `.select_dtypes()` | Seleção de colunas por tipo para limpeza |

### NumPy 1.x / 2.x

| Recurso | Uso no projeto |
|---|---|
| `np.random.default_rng(seed)` | Geração reprodutível do dataset sintético |
| `np.mean`, `np.median`, `np.std` | Estatísticas descritivas vetorizadas |
| `np.percentile(arr, 25/75)` | Cálculo de quartis (P25, P75) |
| `np.sum`, `np.min`, `np.max` | Agregações vetorizadas |
| `np.select(condições, escolhas)` | Classificação condicional sem loop Python |
| Broadcasting min-max | `(x - x.min()) / (x.max() - x.min())` |
| `np.integers`, `np.uniform` | Geração de dados sintéticos |
| `.to_numpy()` | Conversão de Series pandas para array NumPy |

---

## Visualização

### Matplotlib 3.x

| Recurso | Uso no projeto |
|---|---|
| `matplotlib.use("Agg")` | Backend sem display (compatível com Colab/servidor) |
| `plt.subplots()` | Criação de figuras com axes |
| `ax.plot()` com `fill_between` | Gráfico de linha (receita por mês) |
| `ax.barh()` | Barras horizontais (top produtos) |
| `ax.pie()` | Pizza (distribuição por região) |
| `ax.set_title/xlabel/ylabel` | Anotações e labels dos gráficos |
| `fig.savefig(dpi=100)` | Exportação de PNG com qualidade definida |
| `plt.close(fig)` | Liberação de memória após cada gráfico |

### Seaborn 0.13+

| Recurso | Uso no projeto |
|---|---|
| `sns.set_theme(style="whitegrid", palette="muted")` | Estilo global aplicado a todos os gráficos |

---

## Módulos da Stdlib Python

| Módulo | Uso no projeto |
|---|---|
| `os` | `os.makedirs(exist_ok=True)`, `os.path.join()` |
| `json` | `json.dump(indent=2, ensure_ascii=False)`, `json.load()` |
| `re` | `re.compile()`, `re.sub()` — limpeza e validação de strings |
| `datetime` | `datetime.datetime.now()` — timestamp nas estatísticas |
| `random` | `random.seed(seed)` — reprodutibilidade |
| `numpy.random` | `np.random.default_rng(seed)` — geração do dataset |

---

## Ferramentas de Desenvolvimento

### VS Code
- Extensão Python (Microsoft) + Pylance
- IntelliSense, linting e debug integrado
- Execução via terminal integrado (PowerShell/bash)

### Google Colab
- Ambiente principal recomendado pela disciplina
- Todas as libs pré-instaladas (pandas, numpy, matplotlib, seaborn)
- Suporte a `!python salesinsight.py` em células de código

### Git + GitHub
- Controle de versão com branches descritivas por funcionalidade
- Commits semânticos (Conventional Commits)
- Pull Requests com template padronizado

### GitHub Desktop
- Interface gráfica para commits, push e gerenciamento de branches

---

## Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\activate

# Ativar (Linux/macOS)
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Verificar instalação
pip show pandas numpy matplotlib seaborn
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

| Ambiente | Suporte | Observação |
|---|---|---|
| Google Colab | Nativo (sem instalação) | Recomendado pela disciplina |
| Windows 10/11 + Python 3.10+ | Via pip | Testado neste projeto |
| macOS + Python 3.10+ | Via pip | Compatível |
| Linux + Python 3.10+ | Via pip | Compatível |
| Jupyter Notebook local | Via pip | Funcional com `!python salesinsight.py` |

---

## Considerações de Performance

| Operação | Abordagem | Justificativa |
|---|---|---|
| Classificação condicional | `np.select` | Vetorizado; evita `apply` com loop Python |
| Estatísticas | Funções NumPy nativas | 10–100× mais rápido que loops Python |
| Geração do dataset | `np.random.default_rng` | API moderna do NumPy, thread-safe |
| Limpeza de strings | `.str.strip()` em Series | Operação vetorizada do pandas |
| Gráficos | `plt.close()` após cada PNG | Evita leak de memória com múltiplos gráficos |
