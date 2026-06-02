# Tasks — SalesInsight PY

> Tasks detalhadas para implementação do pipeline · Ordenadas por dependência
> Atualizado em: 01/06/2026

---

## T01 — Configurar Repositório e Ambiente ✅ Concluída

**Branch:** `chore/setup-repo` | **Issue:** #1

- [x] Criar repositório no GitHub (`InteligenciaDeMercado`)
- [x] Criar branches `main` e `develop`
- [x] Criar `requirements.txt` com pandas, numpy, matplotlib, seaborn
- [x] Criar `.gitignore` (.venv, __pycache__, outputs/graficos/*.png)
- [x] Criar `salesinsight.py` com header e estrutura base
- [x] Criar pasta `outputs/graficos/` com `.gitkeep`
- [x] Configurar venv: `python -m venv .venv`

---

## T02 — RF01: Gerar Dataset Sintético ✅ Concluída

**Branch:** `feat/dataset-generator` | **Issue:** #3 | **Depende de:** T01

- [x] Implementar `gerar_dataset_vendas(n_registros=200, seed=42)`
- [x] Usar `np.random.default_rng(seed)` para reprodutibilidade
- [x] Garantir exatamente 50 clientes únicos (Cliente_001 a Cliente_050)
- [x] Injetar dados sujos: 5 nulos em quantidade, 5 em preco, 1 data inválida, 3 espaços
- [x] Salvar com `df.to_csv("vendas.csv", index=False)`

---

## T03 — RF02: Inspecionar Dados ✅ Concluída

**Branch:** `feat/data-inspection` | **Issue:** #4 | **Depende de:** T02

- [x] Implementar `inspecionar_dados(df)` com docstring
- [x] Exibir: shape, colunas, dtypes, isnull().sum(), duplicatas
- [x] Formatar saída com separadores visuais

---

## T04 — RF03 + RF13: Limpar Dados e Regex ✅ Concluída

**Branch:** `feat/data-cleaning` | **Issue:** #5 | **Depende de:** T03

- [x] Implementar `limpar_dados(df)`:
  - `.str.strip()` em todas as colunas object
  - `pd.to_datetime(errors='coerce')` + dropna
  - `.dropna(subset=["quantidade", "preco_unitario"])`
  - Conversão de tipos (`int`, `float`)
  - Retorno: `(df_limpo, relatorio)`
- [x] Implementar `limpar_strings_com_regex(df)`:
  - `re.compile(r"[^a-zA-Z0-9_ ]")` + `re.sub()` para limpar
  - `re.compile(r"^Cliente_\d{3}$")` para validar
  - Criar colunas `cliente_limpo` e `cliente_valido`

---

## T05 — RF04: Colunas Derivadas ✅ Concluída

**Branch:** `feat/feature-engineering` | **Issue:** #6 | **Depende de:** T04

- [x] Implementar `criar_colunas_derivadas(df)`:
  - `receita_total = quantidade * preco_unitario` (`.round(2)`)
  - `mes`, `mes_nome` (mapeamento pt-BR), `trimestre` (Q1–Q4), `ano`
  - `faixa_receita_item` via `np.select` (Baixo/Médio/Alto Valor)

---

## T06 — RF05: Métricas com groupby ✅ Concluída

**Branch:** `feat/metrics-aggregation` | **Issue:** #7 | **Depende de:** T05

- [x] Implementar `calcular_metricas(df)`:
  - `por_mes`: groupby("mes") → receita_total
  - `top_produtos`: top 5 por receita
  - `por_categoria`: receita por categoria
  - `por_regiao`: receita_total + media_ticket por região
  - Retorna dict com todas as tabelas + `total_geral`

---

## T07 — RF06: Segmentação de Clientes com Lambda ✅ Concluída

**Branch:** `feat/customer-segmentation` | **Issue:** #8 | **Depende de:** T05

- [x] Implementar `segmentar_clientes(df)` com lambda para classificação
- [x] Verificar: 50 clientes, 3 segmentos (Bronze/Prata/Ouro)
- [x] Exibir distribuição de segmentos no console

---

## T08 — RF07: Estatísticas NumPy ✅ Concluída

**Branch:** `feat/numpy-statistics` | **Issue:** #9 | **Depende de:** T05

- [x] Implementar `calcular_estatisticas_numpy(df)`:
  - `.to_numpy()` para converter coluna
  - `np.mean`, `np.median`, `np.std`, `np.sum`, `np.min`, `np.max`
  - `np.percentile` para P25 e P75
  - Broadcasting: normalização min-max `(x - x.min()) / (x.max() - x.min())`
- [x] Retorna dict com todas as estatísticas + timestamp

---

## T09 — RF11: Lambda e Higher-Order Functions ✅ Concluída

**Branch:** `feat/lambda-hof` | **Issue:** #10 | **Depende de:** T05

- [x] Implementar `processar_coluna(df, coluna, func)`
- [x] Demonstrar chamada com lambda no `main()`
- [x] Garantir ≥ 4 usos de lambda no código total (RF06, RF13, RF11)

---

## T10 — RF08: Visualizações PNG ✅ Concluída

**Branch:** `feat/visualizations` | **Issue:** #11 | **Depende de:** T06

- [x] Implementar `gerar_visualizacoes(df, metricas, output_dir)`:
  - Gráfico 1: linha com área — receita por mês
  - Gráfico 2: barras horizontais — top 5 produtos
  - Gráfico 3: pizza — distribuição por região
- [x] Verificar: 3 PNG gerados em `outputs/graficos/`
- [x] `plt.close(fig)` após cada gráfico

---

## T11 — RF12: Exportação CSV e JSON ✅ Concluída

**Branch:** `feat/export-reports` | **Issue:** #12 | **Depende de:** T06, T07, T08

- [x] Implementar `exportar_resultados(metricas, clientes, stats)`
- [x] Exportar 2 CSV e 1 JSON
- [x] Ler o JSON exportado com `json.load()` e confirmar no console

---

## T12 — RF09: Classe AnalisadorDeVendas ✅ Concluída

**Branch:** `feat/analyzer-class` | **Issue:** #13 | **Depende de:** T04–T11

- [x] Implementar `AnalisadorDeVendas` com:
  - `__init__`, `carregar()`, `limpar()`, `transformar()`, `analisar()`, `resumo()`
  - Todos os métodos retornam `self`
- [x] Testar encadeamento: `.carregar().limpar().transformar().analisar().resumo()`

---

## T13 — RF10: Classe AnalisadorComProjecao ✅ Concluída

**Branch:** `feat/projection-class` | **Issue:** #14 | **Depende de:** T12

- [x] Implementar `AnalisadorComProjecao(AnalisadorDeVendas)` com `super()`
- [x] Atributos: `self.meses_projecao`, `self.projecoes`
- [x] Método `projetar_tendencia(taxa_crescimento=0.05)` com crescimento composto
- [x] Retorna `self` para encadeamento

---

## T14 — RF14: Pipeline Completo (main) ✅ Concluída

**Branch:** `feat/main-pipeline` | **Issue:** #15 | **Depende de:** T13

- [x] Implementar `main()` com pipeline completo via `AnalisadorComProjecao`
- [x] Adicionar `if __name__ == "__main__": main()`
- [x] `python salesinsight.py` executa do início ao fim sem erros
- [x] Verificar todos os outputs gerados

---

## T15 — Documentação Final ✅ Concluída

**Branch:** `docs/readme` | **Issue:** #17 | **Depende de:** T14

- [x] Atualizar README com todos os conceitos aplicados e status
- [x] Revisar e melhorar toda a documentação técnica (docs/, specs/, steering/)
- [x] Criar diagrama Mermaid do pipeline
- [ ] Inserir link do vídeo no README (pendente gravação)
- [ ] Inserir link do Kanban no README (pendente criação)

---

## T16 — Testes e Entrega ⬜ Pendente

**Issue:** #16, #18 | **Depende de:** T14, T15

- [ ] Testar no Google Colab (upload + execução)
- [ ] Gravar vídeo de até 5 minutos mostrando execução do pipeline
- [ ] Hospedar no Google Drive (link público) ou YouTube não listado
- [ ] Criar Quadro Kanban no GitHub Projects
- [ ] Fechar todas as issues no GitHub
- [ ] Tornar repositório público no GitHub
- [ ] Submeter links no AVA até 08/06/2026 às 12h
