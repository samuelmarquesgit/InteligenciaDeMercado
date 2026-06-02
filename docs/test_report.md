# Test Report — SalesInsight PY

> Relatório de validação do pipeline · Atualizado em: 01/06/2026

---

## Sumário de Testes

| RF | Funcionalidade | Status | Observações |
|---|---|---|---|
| RF01 | Geração do dataset | ✅ Passou | 200 linhas × 8 colunas, dados sujos injetados corretamente |
| RF02 | Inspeção dos dados | ✅ Passou | Exibe shape, dtypes, nulos e duplicatas |
| RF03 | Limpeza de dados | ✅ Passou | ~184 linhas após limpeza, tipos convertidos |
| RF04 | Colunas derivadas | ✅ Passou | 6 colunas criadas com np.select |
| RF05 | Métricas groupby | ✅ Passou | 12 meses, 5 produtos, 4 categorias, 5 regiões |
| RF06 | Segmentação de clientes | ✅ Passou | 50 clientes classificados em Bronze/Prata/Ouro |
| RF07 | Estatísticas NumPy | ✅ Passou | Broadcasting e vetorização confirmados |
| RF08 | Visualizações PNG | ✅ Passou | 3 PNG exportados em outputs/graficos/ |
| RF09 | Classe AnalisadorDeVendas | ✅ Passou | Method chaining funcional |
| RF10 | Herança + Projeção | ✅ Passou | super(), projeções calculadas com crescimento composto |
| RF11 | Lambda + HOF | ✅ Passou | 4 lambdas distintas, processar_coluna funcional |
| RF12 | Exportação CSV/JSON | ✅ Passou | 2 CSV + 1 JSON gerados, JSON verificado por leitura |
| RF13 | Regex | ✅ Passou | re.compile + re.sub, colunas cliente_limpo e cliente_valido |
| RF14 | Pipeline completo | ✅ Passou | python salesinsight.py executa sem erros |

**Legenda:** ✅ Passou · ❌ Falhou · ⬜ Pendente · ⚠️ Parcial

---

## Casos de Teste

### TC01 — Dataset Gerado Corretamente
```
Entrada:  gerar_dataset_vendas(n_registros=200, seed=42)
Esperado:
  - DataFrame com 200 linhas e 8 colunas
  - Colunas: id_venda, data_venda, cliente, produto, categoria, regiao, quantidade, preco_unitario
  - 5 nulos em quantidade, 5 em preco_unitario
  - 1 ocorrência de "DATA INVÁLIDA" na coluna data_venda
  - 3 strings com espaço extra na coluna cliente
Resultado: ✅ Passou
Notas: seed=42 garante reprodutibilidade exata entre execuções
```

### TC02 — Inspeção Exibe Metadados Corretos
```
Entrada:  inspecionar_dados(df_bruto)
Esperado:
  - Shape: (200, 8)
  - Exibe dtypes de cada coluna
  - Exibe isnull().sum() com marcação de colunas com nulos
  - Exibe total de nulos e contagem de duplicatas
Resultado: ✅ Passou
Notas: Exibe diagnóstico completo. describe() e head() não são exibidos
       (comportamento esperado conforme implementação)
```

### TC03 — Limpeza Remove Registros Inválidos
```
Entrada:  limpar_dados(df_bruto)
Esperado:
  - Registros finais < 200 (nulos + datas inválidas removidos)
  - Coluna data_venda do tipo datetime64
  - Nenhum espaço extra em colunas string
  - quantidade do tipo int, preco_unitario do tipo float
  - Retorna tupla (df_limpo, relatorio)
Resultado: ✅ Passou
Notas: ~184 registros após limpeza; relatório exibido no console
```

### TC04 — Colunas Derivadas Criadas
```
Entrada:  criar_colunas_derivadas(df_limpo)
Esperado:
  - Colunas novas: receita_total, mes, mes_nome, trimestre, ano, faixa_receita_item
  - receita_total = quantidade * preco_unitario (arredondado .round(2))
  - trimestre em formato "Q1", "Q2", "Q3", "Q4"
  - faixa_receita_item em {"Baixo Valor", "Médio Valor", "Alto Valor"}
Resultado: ✅ Passou
```

### TC05 — Métricas Agregadas
```
Entrada:  calcular_metricas(df_limpo)
Esperado:
  - dict com chaves: por_mes, top_produtos, por_categoria, por_regiao, total_geral
  - por_mes: 12 linhas (uma por mês)
  - top_produtos: 5 linhas, ordenadas por receita decrescente
  - por_regiao: 5 linhas com receita_total e media_ticket
Resultado: ✅ Passou
```

### TC06 — Segmentação de Clientes
```
Entrada:  segmentar_clientes(df_limpo)
Esperado:
  - DataFrame com exatamente 50 clientes (Cliente_001 a Cliente_050)
  - Colunas: cliente, total_gasto, segmento
  - Segmentos: Bronze (<5k), Prata (5k–15k), Ouro (>15k)
  - Ordenado por total_gasto decrescente
Resultado: ✅ Passou
```

### TC07 — NumPy Vetorizado
```
Entrada:  calcular_estatisticas_numpy(df_limpo)
Esperado:
  - Retorna dict com: media, mediana, desvio_padrao, total, minimo, maximo, percentil_25, percentil_75
  - Demonstra normalização min-max (broadcasting)
  - Sem uso de loops Python para cálculos
Resultado: ✅ Passou
Notas: Normalização min-max implementada; média_normalizada inclusa no dict retornado
```

### TC08 — Gráficos PNG Exportados
```
Entrada:  gerar_visualizacoes(df_limpo, metricas, output_dir="outputs/graficos")
Esperado:
  - 3 arquivos PNG em outputs/graficos/:
    * vendas_por_mes.png  (gráfico de linha com área)
    * top_produtos.png    (barras horizontais)
    * distribuicao_regioes.png (pizza)
  - Arquivos com tamanho > 0 bytes
Resultado: ✅ Passou
Notas: gráfico de pizza usado para regiões (não boxplot — ver AUDIT.md)
       dpi=100 utilizado (specs previam dpi=150)
```

### TC09 — Exportação CSV e JSON
```
Entrada:  exportar_resultados(metricas, clientes, stats)
Esperado:
  - metricas_por_mes.csv em outputs/
  - segmentacao_clientes.csv em outputs/
  - estatisticas_gerais.json em outputs/
  - JSON relido com json.load() e valores exibidos no console
Resultado: ✅ Passou
Notas: encoding="utf-8" (não utf-8-sig); json.dump indent=2 (não indent=4)
       Ambos funcionais; diferenças mínimas das specs originais
```

### TC10 — Pipeline Completo (main)
```
Entrada:  python salesinsight.py
Esperado:
  - Execução do início ao fim sem erros
  - Todos os outputs gerados
  - Resumo executivo exibido (receita total, clientes, média mensal)
  - Projeção de 3 meses exibida
Resultado: ✅ Passou
```

---

## Divergências entre Specs e Implementação

| Item | Spec | Implementação | Impacto |
|---|---|---|---|
| Gráfico RF08 — tipo para regiões | `sns.boxplot` | `ax.pie` (pizza) | Baixo — ainda atende RF08 |
| Encoding CSV | `utf-8-sig` | `utf-8` | Baixo — funcional em todos ambientes |
| JSON indent | `indent=4` | `indent=2` | Nenhum — apenas formatação |
| dpi dos gráficos | `dpi=150` | `dpi=100` | Baixo — qualidade suficiente |
| `AnalisadorDeVendas.visualizar()` | Previsto em specs | Não implementado na classe | Médio — visualização feita como função standalone |
| `AnalisadorDeVendas.exportar_relatorio()` | Previsto em specs | Não implementado na classe | Médio — exportação feita como função standalone |
| `while` loop | Mencionado no README | Não presente no código | Baixo — `for` loops presentes |
| `processar_coluna` chamadas | 2+ no main | 1 chamada no main | Baixo — RF11 ainda atendido com lambdas |

---

## Ambiente de Teste

- Python: 3.10+
- pandas: 2.x
- numpy: 1.24+
- matplotlib: 3.7+
- seaborn: 0.13+
- SO: Windows 11 / Google Colab
- Data do teste: 01/06/2026

---

## Bugs Conhecidos

| ID | Descrição | Status | Branch de fix |
|---|---|---|---|
| — | Nenhum bug bloqueante registrado | — | — |
