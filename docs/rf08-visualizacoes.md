# RF08 — Visualizações com Matplotlib e Seaborn

> Documentação das implementações gráficas · Atualizado em: 31/05/2026

---

## Visão Geral

O RF08 foi expandido de **3 gráficos obrigatórios** para **7 gráficos**, incorporando visualizações que cobrem sazonalidade, distribuição estatística, segmentação de clientes e projeção de tendência.

---

## Alterações na Assinatura da Função

A função `gerar_visualizacoes()` recebeu dois novos parâmetros para suportar os gráficos 6 e 7:

```python
# Antes
def gerar_visualizacoes(df, metricas, output_dir="outputs/graficos")

# Depois
def gerar_visualizacoes(df, metricas, clientes, projecoes, output_dir="outputs/graficos")
```

| Parâmetro | Tipo | Usado em |
|---|---|---|
| `df` | `pd.DataFrame` | Gráficos 1, 4, 5 |
| `metricas` | `dict` | Gráficos 1, 2, 3, 7 |
| `clientes` | `pd.DataFrame` | Gráfico 6 |
| `projecoes` | `list` | Gráfico 7 |

A chamada no `main()` também foi atualizada:

```python
gerar_visualizacoes(df, analisador.metricas, analisador.clientes, analisador.projecoes)
```

---

## Gráficos Implementados

### Gráfico 1 — Receita por Mês (Bar Chart)
- **Arquivo:** `vendas_por_mes.png`
- **Fonte de dados:** `metricas["por_mes"]`
- **O que mostra:** Receita total acumulada em cada mês de 2024
- **Conceito:** `ax.bar()` com rótulos de meses no eixo X

---

### Gráfico 2 — Top 5 Produtos por Receita (Bar Horizontal)
- **Arquivo:** `top_produtos.png`
- **Fonte de dados:** `metricas["top_produtos"]`
- **O que mostra:** Ranking dos 5 produtos que mais geraram receita
- **Conceito:** `ax.barh()` com `invert_yaxis()` para ordenar do maior para o menor

---

### Gráfico 3 — Distribuição de Receita por Região (Pie Chart)
- **Arquivo:** `distribuicao_regioes.png`
- **Fonte de dados:** `metricas["por_regiao"]`
- **O que mostra:** Participação percentual de cada região na receita total
- **Conceito:** `ax.pie()` com `autopct` para exibir percentuais

---

### Gráfico 4 — Dispersão de Receita por Região (Boxplot) ✅ exigido pelo PRD
- **Arquivo:** `boxplot_regioes.png`
- **Fonte de dados:** `df` (transações individuais)
- **O que mostra:** Distribuição estatística das transações por região — mediana, quartis e outliers
- **Conceito:** `sns.boxplot()` — lê o DataFrame diretamente, não um agregado
- **Por que é mais rico que o pie chart:** O boxplot revela a dispersão dos dados. Duas regiões podem ter receita total parecida mas distribuições completamente diferentes.

---

### Gráfico 5 — Receita por Categoria × Mês (Heatmap)
- **Arquivo:** `heatmap_categoria_mes.png`
- **Fonte de dados:** `df` via `pivot_table`
- **O que mostra:** Sazonalidade de cada categoria ao longo dos meses — células mais escuras = maior receita
- **Conceito:** `df.pivot_table()` para reestruturar os dados + `sns.heatmap()` para visualizar
- **Como funciona o pivot:**
  ```python
  pivot = df.pivot_table(
      values="receita_total",   # o que agregar
      index="categoria",        # linhas da tabela
      columns="mes",            # colunas da tabela
      aggfunc="sum"             # como agregar
  )
  ```

---

### Gráfico 6 — Segmentação de Clientes (Donut Chart)
- **Arquivo:** `segmentacao_clientes.png`
- **Fonte de dados:** `clientes["segmento"]` (vem do RF06)
- **O que mostra:** Proporção de clientes Bronze, Prata e Ouro
- **Conceito:** `ax.pie()` com `wedgeprops=dict(width=0.5)` — o parâmetro `width` menor que 1 cria o buraco central do donut
- **Cores usadas:**
  | Segmento | Hex |
  |---|---|
  | Ouro | `#FFD700` |
  | Prata | `#C0C0C0` |
  | Bronze | `#CD7F32` |

---

### Gráfico 7 — Receita Realizada + Projeção (Line Chart)
- **Arquivo:** `projecao_tendencia.png`
- **Fonte de dados:** `metricas["por_mes"]` + `projecoes` (vem do RF10)
- **O que mostra:** Série histórica de 2024 combinada com projeção dos próximos 3 meses
- **Conceito:** Dois `ax.plot()` no mesmo eixo — um para o realizado, outro tracejado para a projeção. `ax.axvline(x=12)` marca o ponto de corte entre histórico e projeção.
- **Integração com RF10:** `AnalisadorComProjecao.projetar_tendencia()` calcula a projeção com crescimento composto de 5% ao mês. Este gráfico é a representação visual desse cálculo.

---

## Outputs Gerados

Todos os arquivos são salvos em `outputs/graficos/` com extensão `.png`.

| Arquivo | Gráfico | dpi |
|---|---|---|
| `vendas_por_mes.png` | Receita por mês | 100 |
| `top_produtos.png` | Top 5 produtos | 100 |
| `distribuicao_regioes.png` | Pie por região | 100 |
| `boxplot_regioes.png` | Boxplot por região | 150 |
| `heatmap_categoria_mes.png` | Heatmap categoria × mês | 150 |
| `segmentacao_clientes.png` | Donut Bronze/Prata/Ouro | 150 |
| `projecao_tendencia.png` | Linha real + projeção | 150 |

---

## Conceitos Aplicados

| Conceito | Onde aparece |
|---|---|
| `matplotlib` — `bar`, `barh`, `pie`, `plot` | Gráficos 1, 2, 3, 7 |
| `seaborn` — `boxplot`, `heatmap` | Gráficos 4, 5 |
| `pivot_table` para reestruturar dados | Gráfico 5 |
| `wedgeprops` para donut chart | Gráfico 6 |
| `axvline` para linha de corte vertical | Gráfico 7 |
| `tight_layout` + `savefig` + `close` | Todos |
| Integração RF06 → RF08 (clientes) | Gráfico 6 |
| Integração RF10 → RF08 (projeções) | Gráfico 7 |
