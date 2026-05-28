# Prompt — Visualizações Avançadas

> Rastreabilidade dos prompts para geração de gráficos do projeto

---

## Contexto

Este prompt é destinado a auxiliar na implementação do RF08 (Visualizações com Matplotlib e Seaborn), indo além dos 3 gráficos obrigatórios para criar visualizações mais ricas e informativas.

---

## Prompt Base

```
Dado o DataFrame `df_limpo` do projeto SalesInsight PY com as colunas:
id_venda, data_venda, cliente, produto, categoria, regiao, quantidade,
preco_unitario, receita_total, mes, mes_nome, trimestre, ano, faixa_receita_item

Crie funções Python usando Matplotlib e Seaborn para gerar as seguintes
visualizações adicionais, exportando cada uma como PNG com dpi=150:

1. Heatmap de receita por mês x categoria
2. Gráfico de pizza com distribuição de segmentos de clientes (Bronze/Prata/Ouro)
3. Gráfico de barras agrupadas comparando receita por trimestre e região
4. Histograma da distribuição de receita_total com linha de média e mediana

Cada função deve:
- Ter docstring explicando o gráfico
- Usar sns.set_theme(style="whitegrid")
- Ter título, labels de eixo e legenda
- Salvar em outputs/graficos/ com nome descritivo
- Retornar o caminho do arquivo salvo
```

---

## Prompt para Gráfico de Tendência com Projeção

```
Crie uma função Python chamada `plotar_tendencia_com_projecao(df, projecoes, output_dir)`
que gere um único gráfico combinando:
- Linha azul: receita histórica real por mês (de df)
- Linha laranja tracejada: receita projetada (de projecoes)
- Área sombreada na projeção indicando incerteza (+/- 10%)
- Marcadores nos pontos de dados
- Anotação de texto no último ponto projetado com o valor
- Exportar como "tendencia_com_projecao.png" em output_dir

Use Matplotlib puro. A função deve aceitar:
- df: DataFrame com colunas mes e receita_total
- projecoes: lista de dicts com mes e receita_projetada
- output_dir: str com caminho de saída
```

---

## Modelo de IA Utilizado

- **Claude Sonnet 4.6** via Claude Code (Anthropic)
- A ser utilizado durante a fase de implementação

---

## Notas de Uso

- Adaptar os prompts ao código já implementado antes de usar
- Verificar que os nomes de colunas batem com o DataFrame real
- Testar cada gráfico individualmente antes de integrar ao pipeline
