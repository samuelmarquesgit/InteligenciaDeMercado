# Tasks — SalesInsight PY

> Tasks detalhadas para implementação do pipeline · Ordenadas por dependência

---

## T01 — Configurar Repositório e Ambiente

**Branch:** `chore/setup-repo`
**Issue:** #1
**Prioridade:** 🔴 Alta (pré-requisito de tudo)

**O que fazer:**
- [ ] Clonar repositório: `git clone git@github.com:samuelmarquesgit/InteligenciaDeMercado.git`
- [ ] Criar branch `develop` a partir de `main`
- [ ] Criar `requirements.txt` com pandas, numpy, matplotlib, seaborn
- [ ] Criar `.gitignore` (venv, __pycache__, .DS_Store, *.pyc, outputs/graficos/*.png)
- [ ] Criar `salesinsight.py` vazio com header comentado
- [ ] Criar pasta `outputs/graficos/` com `.gitkeep`
- [ ] Criar `venv`: `python -m venv .venv`
- [ ] Commitar: `chore: configura repositorio gitignore requirements e venv`
- [ ] Push: `git push -u origin develop`

---

## T02 — RF01: Gerar Dataset Sintético

**Branch:** `feat/dataset-generator`
**Issue:** #3
**Depende de:** T01

**O que fazer:**
- [ ] Implementar `gerar_dataset_vendas(n_registros=200, seed=42)`
- [ ] Usar `random.seed` e `np.random.seed`
- [ ] Inserir dados sujos: ~5% nulos em quantidade, ~4% em preço, ~2% datas inválidas, ~3% strings com espaço
- [ ] Salvar com `df.to_csv("vendas.csv", index=False)`
- [ ] Testar: executar e verificar `vendas.csv` gerado com 200 linhas
- [ ] Commitar: `feat: cria funcao gerar_dataset_vendas com dados sinteticos e seed fixo`

---

## T03 — RF02: Inspecionar Dados

**Branch:** `feat/data-inspection`
**Issue:** #4
**Depende de:** T02

**O que fazer:**
- [ ] Implementar `inspecionar_dados(df)` com docstring
- [ ] Exibir: shape, colunas, dtypes, isnull().sum(), head(), describe()
- [ ] Testar: `inspecionar_dados(pd.read_csv("vendas.csv"))` no console
- [ ] Commitar: `feat: implementa inspecionar_dados com shape dtypes e isnull`

---

## T04 — RF03 + RF13: Limpar Dados e Regex

**Branch:** `feat/data-cleaning`
**Issue:** #5
**Depende de:** T03

**O que fazer:**
- [ ] Implementar `limpar_dados(df)`:
  - `.str.strip()` em todas as colunas object
  - `pd.to_datetime(errors='coerce')` + dropna
  - `.dropna(subset=["quantidade", "preco_unitario"])`
  - Conversão de tipos
  - Retorno: `(df_limpo, relatorio)`
- [ ] Implementar `limpar_strings_com_regex(df)`:
  - `re.sub()` para remover caracteres inválidos
  - `re.compile()` para validar padrão `Cliente_XXX`
  - Criar colunas `cliente_limpo` e `cliente_valido`
- [ ] Testar: verificar contagens no relatório de limpeza
- [ ] Commitar: `feat: adiciona limpeza de dados com tratamento de nulos e regex`

---

## T05 — RF04: Colunas Derivadas

**Branch:** `feat/feature-engineering`
**Issue:** #6
**Depende de:** T04

**O que fazer:**
- [ ] Implementar `criar_colunas_derivadas(df)`:
  - `receita_total = quantidade * preco_unitario`
  - `mes`, `mes_nome`, `trimestre` (Q1–Q4), `ano`
  - `faixa_receita_item` via `np.select`
- [ ] Testar: verificar novas colunas com `df.head()` e `df.dtypes`
- [ ] Commitar: `feat: cria colunas derivadas receita_total trimestre e faixa_receita_item`

---

## T06 — RF05: Métricas com groupby

**Branch:** `feat/metrics-aggregation`
**Issue:** #7
**Depende de:** T05

**O que fazer:**
- [ ] Implementar `calcular_metricas(df)`:
  - `por_mes`: groupby("mes").agg(receita, quantidade, n_vendas)
  - `top_produtos`: top 5 por receita
  - `por_categoria`: receita por categoria
  - `por_regiao`: receita e ticket médio por região
  - Retorna dict com todas as tabelas
- [ ] Testar: verificar 12 linhas em `por_mes`, 5 linhas em `top_produtos`
- [ ] Commitar: `feat: adiciona metricas agregadas por mes produto categoria e regiao`

---

## T07 — RF06: Segmentação de Clientes com Lambda

**Branch:** `feat/customer-segmentation`
**Issue:** #8
**Depende de:** T05

**O que fazer:**
- [ ] Implementar `segmentar_clientes(df)` com lambda para classificação
- [ ] Verificar: 50 clientes, 3 segmentos (Bronze/Prata/Ouro)
- [ ] Testar: exibir top 10 e distribuição de segmentos
- [ ] Commitar: `feat: implementa segmentacao de clientes por nivel de gasto com lambda`

---

## T08 — RF07: Estatísticas NumPy

**Branch:** `feat/numpy-statistics`
**Issue:** #9
**Depende de:** T05

**O que fazer:**
- [ ] Implementar `calcular_estatisticas_numpy(df)`:
  - `.to_numpy()` para converter coluna
  - `np.mean`, `np.median`, `np.std`, `np.sum`, `np.percentile`
  - Broadcasting: normalização min-max
  - Vetorização: `receitas[receitas > media]`
- [ ] Testar: verificar valores numéricos no console
- [ ] Commitar: `feat: adiciona calculos estatisticos com numpy vetorizado e broadcasting`

---

## T09 — RF11: Lambda e Higher-Order Functions

**Branch:** `feat/lambda-hof`
**Issue:** #10
**Depende de:** T05

**O que fazer:**
- [ ] Implementar `processar_coluna(df, coluna, funcao_transformacao)`
- [ ] Demonstrar 2+ chamadas com lambdas diferentes
- [ ] Garantir 2+ usos distintos de lambda no código total
- [ ] Commitar: `feat: cria processar_coluna como higher-order function e demonstra lambdas`

---

## T10 — RF08: Visualizações PNG

**Branch:** `feat/visualizations`
**Issue:** #11
**Depende de:** T06

**O que fazer:**
- [ ] Implementar `gerar_visualizacoes(df, metricas, output_dir="outputs/graficos")`:
  - Gráfico 1: linha — receita por mês com fill_between
  - Gráfico 2: barras — top 5 produtos (sns.barplot)
  - Gráfico 3: boxplot — distribuição por região (sns.boxplot)
- [ ] Verificar: 3 PNG gerados em `outputs/graficos/`
- [ ] Commitar: `feat: gera visualizacoes linha barras e boxplot exportadas em PNG`

---

## T11 — RF12: Exportação CSV e JSON

**Branch:** `feat/export-reports`
**Issue:** #12
**Depende de:** T06, T07, T08

**O que fazer:**
- [ ] Implementar `exportar_resultados(metricas, clientes, stats_numpy)`
- [ ] Exportar 2 CSV e 1 JSON
- [ ] Ler o JSON exportado e confirmar no console
- [ ] Commitar: `feat: exporta relatorios em CSV e JSON com validacao de leitura`

---

## T12 — RF09: Classe AnalisadorDeVendas

**Branch:** `feat/analyzer-class`
**Issue:** #13
**Depende de:** T04–T11

**O que fazer:**
- [ ] Implementar `AnalisadorDeVendas` com todos os métodos encadeáveis
- [ ] Testar encadeamento completo
- [ ] Commitar: `feat: cria classe AnalisadorDeVendas com construtor atributos e metodos`

---

## T13 — RF10: Classe AnalisadorComProjecao

**Branch:** `feat/projection-class`
**Issue:** #14
**Depende de:** T12

**O que fazer:**
- [ ] Implementar `AnalisadorComProjecao(AnalisadorDeVendas)` com `super()`
- [ ] Método `projetar_tendencia()` com média móvel dos últimos 3 meses
- [ ] Testar: verificar projeções para 3 meses futuros
- [ ] Commitar: `feat: adiciona AnalisadorComProjecao com heranca super e media movel`

---

## T14 — RF14: Pipeline Completo (main)

**Branch:** `feat/main-pipeline`
**Issue:** #15
**Depende de:** T13

**O que fazer:**
- [ ] Implementar `main()` com pipeline completo via `AnalisadorComProjecao`
- [ ] Adicionar `if __name__ == "__main__": main()`
- [ ] Testar: `python salesinsight.py` do início ao fim
- [ ] Verificar todos os outputs gerados
- [ ] Commitar: `feat: implementa main e pipeline completo ponta a ponta`

---

## T15 — Documentação Final

**Branch:** `docs/readme`
**Issue:** #17
**Depende de:** T14

**O que fazer:**
- [ ] Atualizar README com todos os conceitos aplicados
- [ ] Inserir link do vídeo
- [ ] Inserir link do Kanban
- [ ] Commitar: `docs: atualiza README com instrucoes execucao e checklist de conceitos`

---

## T16 — Testes e Entrega

**Issue:** #16, #18
**Depende de:** T14, T15

**O que fazer:**
- [ ] Testar no Google Colab (upload + execução)
- [ ] Gravar vídeo de até 5 minutos
- [ ] Hospedar no Google Drive (link público) ou YouTube não listado
- [ ] Fechar todas as issues no GitHub
- [ ] Submeter links no AVA até 08/06/2026 às 12h
