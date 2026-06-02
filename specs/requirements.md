# Especificação de Requisitos — SalesInsight PY

> Detalhamento técnico de todos os requisitos funcionais e não funcionais
> Atualizado em: 01/06/2026

---

## Requisitos Funcionais

### RF01 — Geração/Carregamento do Dataset
**Prioridade:** Alta | **Status:** ✅ Implementado

**Descrição:** O projeto deve ter um dataset de vendas com dados propositalmente sujos para exercitar limpeza.

**Critérios de Aceite:**
- [x] Função `gerar_dataset_vendas(n_registros=200, seed=42)` implementada
- [x] Dataset salvo como `vendas.csv` na raiz do projeto
- [x] Dataset contém exatamente 8 colunas: `id_venda`, `data_venda`, `cliente`, `produto`, `categoria`, `regiao`, `quantidade`, `preco_unitario`
- [x] 5 nulos em `quantidade`, 5 em `preco_unitario`
- [x] 1 ocorrência de `"DATA INVÁLIDA"` na coluna `data_venda`
- [x] 3 strings com espaço extra na coluna `cliente`
- [x] `np.random.default_rng(seed)` garante reprodutibilidade

---

### RF02 — Inspeção dos Dados
**Prioridade:** Alta | **Status:** ✅ Implementado

**Descrição:** Exibir informações diagnósticas do dataset para o analista.

**Critérios de Aceite:**
- [x] Função `inspecionar_dados(df)` implementada com docstring
- [x] Exibe: `df.shape`, `df.columns`, `df.dtypes`, `df.isnull().sum()`
- [x] Exibe total de nulos e contagem de duplicatas
- [x] Saída formatada no console com separadores visuais
- [ ] Exibe `df.head()` e `df.describe()` _(não implementado — item opcional)_

---

### RF03 — Limpeza e Tratamento de Dados
**Prioridade:** Alta | **Status:** ✅ Implementado

**Descrição:** Tratar inconsistências para garantir qualidade dos dados de entrada no pipeline.

**Critérios de Aceite:**
- [x] Função `limpar_dados(df)` implementada com docstring
- [x] Remove espaços extras com `.str.strip()` em todas as colunas object
- [x] Converte `data_venda` para datetime com `pd.to_datetime(errors='coerce')`
- [x] Remove linhas com `data_venda` nula (datas inválidas)
- [x] Remove linhas com `quantidade` ou `preco_unitario` nulos
- [x] Converte `quantidade` para int e `preco_unitario` para float
- [x] Retorna tupla `(df_limpo, relatorio)` onde `relatorio` é dict com contagens
- [x] Exibe relatório de limpeza no console

---

### RF04 — Colunas Derivadas
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `criar_colunas_derivadas(df)` implementada
- [x] `receita_total = quantidade * preco_unitario` (arredondado `.round(2)`)
- [x] `mes` = número do mês (1–12)
- [x] `mes_nome` = nome do mês em português (via mapeamento dict)
- [x] `trimestre` = "Q1", "Q2", "Q3" ou "Q4" via `np.select`
- [x] `ano` = ano extraído de `data_venda`
- [x] `faixa_receita_item` via `np.select`: "Baixo Valor" (<500), "Médio Valor" (500–5000), "Alto Valor" (≥5000)

---

### RF05 — Métricas Agregadas
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `calcular_metricas(df)` implementada
- [x] `por_mes`: receita_total agrupada por mês (12 linhas)
- [x] `top_produtos`: top 5 por receita_total
- [x] `por_categoria`: receita_total por categoria
- [x] `por_regiao`: receita_total e media_ticket por região
- [x] Retorna dict com todas as tabelas + `total_geral`

---

### RF06 — Segmentação de Clientes
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `segmentar_clientes(df)` implementada
- [x] Agrupa por cliente, calcula `total_gasto`
- [x] Classifica com **função lambda**: Bronze (<5k), Prata (5k–15k), Ouro (>15k)
- [x] Ordena por `total_gasto` decrescente
- [x] Exibe distribuição de segmentos no console

---

### RF07 — Estatísticas NumPy
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `calcular_estatisticas_numpy(df)` implementada
- [x] Converte `receita_total` para array NumPy com `.to_numpy()`
- [x] Calcula: `np.mean`, `np.median`, `np.std`, `np.sum`, `np.min`, `np.max`
- [x] Calcula: `np.percentile(valores, 25)` e `np.percentile(valores, 75)`
- [x] Demonstra **broadcasting**: normalização min-max vetorizada
- [x] Retorna dict com as estatísticas + timestamp

---

### RF08 — Visualizações
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `gerar_visualizacoes(df, metricas, output_dir)` implementada
- [x] Cria `output_dir` com `os.makedirs(exist_ok=True)`
- [x] **Gráfico 1:** linha com área — receita por mês
- [x] **Gráfico 2:** barras horizontais — top 5 produtos
- [x] **Gráfico 3:** pizza — distribuição de receita por região
- [x] Todos com título, labels, `plt.close()` após salvar
- [x] Arquivos salvos: `vendas_por_mes.png`, `top_produtos.png`, `distribuicao_regioes.png`

> **Nota:** specs originais previam `sns.boxplot` para o gráfico 3. A implementação usa `ax.pie`. Ambos atendem RF08.

---

### RF09 — Classe AnalisadorDeVendas
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Classe `AnalisadorDeVendas` com `__init__(self, caminho_arquivo)` implementada
- [x] Atributos: `self.caminho_arquivo`, `self.df_bruto`, `self.df_limpo`, `self.metricas`, `self.clientes`, `self.stats`
- [x] Métodos: `.carregar()`, `.limpar()`, `.transformar()`, `.analisar()`, `.resumo()`
- [x] Todos os métodos retornam `self` (method chaining)
- [x] `self` usado dentro de todos os métodos

---

### RF10 — Herança
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Classe `AnalisadorComProjecao(AnalisadorDeVendas)` implementada
- [x] `__init__` chama `super().__init__(caminho_arquivo)`
- [x] Atributos adicionais: `self.meses_projecao`, `self.projecoes`
- [x] Método `projetar_tendencia(taxa_crescimento=0.05)` com crescimento composto
- [x] Retorna `self` para encadeamento

---

### RF11 — Lambda e HOF
**Prioridade:** Média | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Lambda usada em ≥ 4 contextos distintos no código
- [x] Função `processar_coluna(df, coluna, func)` implementada
- [x] `processar_coluna` aceita lambda como argumento e aplica com `.apply()`
- [x] Chamada de `processar_coluna` demonstrada no `main()`

---

### RF12 — Exportação CSV e JSON
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `exportar_resultados(metricas, clientes, stats)` implementada
- [x] Exporta `metricas_por_mes.csv` com `encoding="utf-8"`
- [x] Exporta `segmentacao_clientes.csv` com `encoding="utf-8"`
- [x] Exporta `estatisticas_gerais.json` com `indent=2`, `ensure_ascii=False`
- [x] **Lê** o JSON exportado com `json.load()` e exibe no console (confirma integridade)

---

### RF13 — Expressões Regulares
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `limpar_strings_com_regex(df)` implementada
- [x] Usa `re.compile(r"[^a-zA-Z0-9_ ]")` + `re.sub()` para limpar `cliente`
- [x] Usa `re.compile(r"^Cliente_\d{3}$")` para validar formato
- [x] Cria coluna `cliente_limpo` e `cliente_valido`
- [x] Exibe contagem de clientes válidos e inválidos no console

---

### RF14 — Pipeline Completo (main)
**Prioridade:** Alta | **Status:** ✅ Implementado

**Critérios de Aceite:**
- [x] Função `main()` implementada com pipeline completo
- [x] Bloco `if __name__ == "__main__": main()` presente
- [x] Usa `AnalisadorComProjecao` com method chaining
- [x] Integra todas as funções standalone + classe
- [x] Termina com `.resumo()` exibindo receita total, clientes e média mensal

---

## Requisitos Não Funcionais

| ID | Requisito | Critério de Aceite | Status |
|---|---|---|---|
| RNF01 | Portabilidade | `python salesinsight.py` roda no Google Colab e localmente | ✅ |
| RNF02 | Reprodutibilidade | Mesma saída a cada execução (seed=42) | ✅ |
| RNF03 | Legibilidade | Funções com docstrings; nomes de variáveis em português | ✅ |
| RNF04 | Modularidade | Cada RF em função separada com parâmetros e retorno | ✅ |
| RNF05 | Rastreabilidade | Commits semânticos mapeando cada RF | Parcial |
