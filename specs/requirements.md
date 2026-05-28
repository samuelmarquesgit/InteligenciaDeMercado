# Especificação de Requisitos — SalesInsight PY

> Detalhamento técnico de todos os requisitos funcionais e não funcionais

---

## Requisitos Funcionais

### RF01 — Geração/Carregamento do Dataset
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Descrição:** O projeto deve ter um dataset de vendas com dados propositalmente sujos para exercitar limpeza.

**Critérios de Aceite:**
- [ ] Função `gerar_dataset_vendas(n_registros=200, seed=42)` implementada
- [ ] Dataset salvo como `vendas.csv` na raiz do projeto
- [ ] Dataset contém exatamente 8 colunas: `id_venda`, `data_venda`, `cliente`, `produto`, `categoria`, `regiao`, `quantidade`, `preco_unitario`
- [ ] ~5% de nulos em `quantidade`, ~4% em `preco_unitario`
- [ ] ~2% de `"DATA INVÁLIDA"` na coluna `data_venda`
- [ ] ~3% de strings com espaço extra em `produto`
- [ ] `random.seed(42)` e `np.random.seed(42)` garantem reprodutibilidade

---

### RF02 — Inspeção dos Dados
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Descrição:** Exibir informações diagnósticas do dataset para o analista.

**Critérios de Aceite:**
- [ ] Função `inspecionar_dados(df)` implementada com docstring
- [ ] Exibe: `df.shape`, `df.columns`, `df.dtypes`, `df.isnull().sum()`, `df.head()`, `df.describe()`
- [ ] Saída no console formatada com título `=== INSPEÇÃO INICIAL DO DATASET ===`

---

### RF03 — Limpeza e Tratamento de Dados
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Descrição:** Tratar inconsistências para garantir qualidade dos dados de entrada no pipeline.

**Critérios de Aceite:**
- [ ] Função `limpar_dados(df)` implementada com docstring
- [ ] Remove espaços extras com `.str.strip()` em todas as colunas object
- [ ] Converte `data_venda` para datetime com `pd.to_datetime(errors='coerce')`
- [ ] Remove linhas com `data_venda` nula (datas inválidas)
- [ ] Remove linhas com `quantidade` ou `preco_unitario` nulos
- [ ] Converte `quantidade` para int e `preco_unitario` para float
- [ ] Retorna tupla `(df_limpo, relatorio)` onde `relatorio` é dict com contagens
- [ ] Exibe relatório de limpeza no console

---

### RF04 — Colunas Derivadas
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `criar_colunas_derivadas(df)` implementada
- [ ] `receita_total = quantidade * preco_unitario`
- [ ] `mes` = número do mês (1–12)
- [ ] `mes_nome` = nome do mês em português (via `strftime` ou mapeamento)
- [ ] `trimestre` = "Q1", "Q2", "Q3" ou "Q4"
- [ ] `ano` = ano extraído
- [ ] `faixa_receita_item` via `np.select`: "Baixo Valor" (<500), "Médio Valor" (500–5000), "Alto Valor" (≥5000)

---

### RF05 — Métricas Agregadas
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `calcular_metricas(df)` implementada
- [ ] `por_mes`: receita_total, quantidade, n_vendas agrupados por mês
- [ ] `top_produtos`: top 5 por receita_total
- [ ] `por_categoria`: receita_total por categoria
- [ ] `por_regiao`: receita_total e media_ticket por região
- [ ] Retorna dict com todas as tabelas
- [ ] Exibe todas as tabelas no console

---

### RF06 — Segmentação de Clientes
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `segmentar_clientes(df)` implementada
- [ ] Agrupa por cliente, calcula `total_gasto`
- [ ] Classifica com **função lambda**: Bronze (<5k), Prata (5k–15k), Ouro (>15k)
- [ ] Ordena por `total_gasto` decrescente
- [ ] Exibe top 10 e distribuição de segmentos

---

### RF07 — Estatísticas NumPy
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `calcular_estatisticas_numpy(df)` implementada
- [ ] Converte `receita_total` para array NumPy com `.to_numpy()`
- [ ] Calcula: `np.mean`, `np.median`, `np.std`, `np.sum`, `np.percentile(25)`, `np.percentile(75)`
- [ ] Demonstra **broadcasting**: normalização min-max vetorizada
- [ ] Demonstra **operação vetorizada**: `receitas[receitas > media]` (sem loop)
- [ ] Retorna dict com as estatísticas

---

### RF08 — Visualizações
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `gerar_visualizacoes(df, metricas, output_dir)` implementada
- [ ] Cria `output_dir` com `os.makedirs(exist_ok=True)`
- [ ] **Gráfico 1** (obrigatório): linha — receita por mês com `fill_between`
- [ ] **Gráfico 2** (obrigatório): barras horizontais — top 5 produtos com `sns.barplot`
- [ ] **Gráfico 3** (obrigatório): boxplot — distribuição de receita por região com `sns.boxplot`
- [ ] Todos com título, labels de eixo, `plt.tight_layout()`, `plt.savefig(dpi=150)`, `plt.close()`
- [ ] Arquivos salvos: `vendas_por_mes.png`, `top_produtos.png`, `distribuicao_regioes.png`

---

### RF09 — Classe AnalisadorDeVendas
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Classe `AnalisadorDeVendas` com `__init__(self, caminho_arquivo)` implementada
- [ ] Atributos: `self.caminho_arquivo`, `self.df_bruto`, `self.df_limpo`, `self.metricas`, `self.clientes`, `self.relatorio_limpeza`
- [ ] Métodos: `.carregar()`, `.limpar()`, `.transformar()`, `.analisar()`, `.visualizar()`, `.exportar_relatorio()`, `.resumo()`
- [ ] Todos os métodos retornam `self` (method chaining)
- [ ] `self` usado dentro de todos os métodos

---

### RF10 — Herança
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Classe `AnalisadorComProjecao(AnalisadorDeVendas)` implementada
- [ ] `__init__` chama `super().__init__(caminho_arquivo)`
- [ ] Atributos adicionais: `self.meses_projecao`, `self.projecoes`
- [ ] Método `projetar_tendencia()`: média móvel dos últimos 3 meses + fator de tendência
- [ ] Método `exibir_projecao_detalhada()`
- [ ] Retorna `self` para encadeamento

---

### RF11 — Lambda e HOF
**Prioridade:** Média | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Lambda usada em **≥ 2 contextos distintos** (ex: `apply`, `sorted`, `filter`)
- [ ] Função `processar_coluna(df, coluna, funcao_transformacao)` implementada
- [ ] `processar_coluna` aceita lambda como argumento e aplica com `.apply()`
- [ ] Demonstrar ao menos 2 chamadas de `processar_coluna` com lambdas diferentes

---

### RF12 — Exportação CSV e JSON
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `exportar_resultados(metricas, clientes, stats_numpy)` implementada
- [ ] Exporta `metricas_por_mes.csv` com `encoding="utf-8-sig"`
- [ ] Exporta `segmentacao_clientes.csv` com `encoding="utf-8-sig"`
- [ ] Exporta `estatisticas_gerais.json` com `indent=4`, `ensure_ascii=False`
- [ ] **Lê** o JSON exportado e exibe no console (confirma integridade)

---

### RF13 — Expressões Regulares
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `limpar_strings_com_regex(df)` implementada
- [ ] Usa `re.sub(r"[^a-zA-Z0-9_ ]", "", str(s))` para limpar cliente
- [ ] Usa `re.compile(r"^Cliente_\d{3}$")` para validar formato
- [ ] Cria coluna `cliente_limpo` e `cliente_valido`
- [ ] Exibe contagem de clientes com formato inválido

---

### RF14 — Pipeline Completo (main)
**Prioridade:** Alta | **Status:** ⬜ Pendente

**Critérios de Aceite:**
- [ ] Função `main()` implementada
- [ ] Bloco `if __name__ == "__main__": main()` presente
- [ ] Usa `AnalisadorComProjecao` para executar todo o pipeline
- [ ] Method chaining completo
- [ ] Calls extras: `limpar_strings_com_regex`, `calcular_estatisticas_numpy`, `exportar_resultados`
- [ ] Termina com `analisador.resumo()` e `analisador.exibir_projecao_detalhada()`
- [ ] Mensagem final: `"[CONCLUÍDO] Pipeline finalizado com sucesso!"`

---

## Requisitos Não Funcionais

| ID | Requisito | Critério de Aceite |
|---|---|---|
| RNF01 | Portabilidade | `python salesinsight.py` roda no Google Colab e localmente |
| RNF02 | Reprodutibilidade | Mesma saída a cada execução (seed=42) |
| RNF03 | Legibilidade | Funções com docstrings; nomes de variáveis em português |
| RNF04 | Modularidade | Cada RF em função separada com parâmetros e retorno |
| RNF05 | Rastreabilidade | Commits semânticos mapeando cada RF |
