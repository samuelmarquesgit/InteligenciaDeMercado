# Test Report — SalesInsight PY

> Relatório de validação do pipeline · Atualizado em: ___/___/2026

---

## Sumário de Testes

| RF | Funcionalidade | Status | Observações |
|---|---|---|---|
| RF01 | Geração do dataset | ⬜ Pendente | |
| RF02 | Inspeção dos dados | ⬜ Pendente | |
| RF03 | Limpeza de dados | ⬜ Pendente | |
| RF04 | Colunas derivadas | ⬜ Pendente | |
| RF05 | Métricas groupby | ⬜ Pendente | |
| RF06 | Segmentação de clientes | ⬜ Pendente | |
| RF07 | Estatísticas NumPy | ⬜ Pendente | |
| RF08 | Visualizações PNG | ⬜ Pendente | |
| RF09 | Classe AnalisadorDeVendas | ⬜ Pendente | |
| RF10 | Herança + Projeção | ⬜ Pendente | |
| RF11 | Lambda + HOF | ⬜ Pendente | |
| RF12 | Exportação CSV/JSON | ⬜ Pendente | |
| RF13 | Regex | ⬜ Pendente | |
| RF14 | Pipeline completo | ⬜ Pendente | |

**Legenda:** ✅ Passou · ❌ Falhou · ⬜ Pendente · ⚠️ Parcial

---

## Casos de Teste

### TC01 — Dataset Gerado Corretamente
```
Entrada: gerar_dataset_vendas(n_registros=200, seed=42)
Esperado:
  - DataFrame com 200 linhas e 8 colunas
  - Colunas: id_venda, data_venda, cliente, produto, categoria, regiao, quantidade, preco_unitario
  - Presença de ~5% nulos em quantidade, ~4% em preco_unitario
  - Presença de ~2% de "DATA INVÁLIDA"
  - Presença de ~3% de strings com espaço extra em produto
Resultado: [ ]
```

### TC02 — Inspeção Exibe Metadados Corretos
```
Entrada: inspecionar_dados(df_bruto)
Esperado:
  - Shape: (200, 8)
  - dtypes corretos (object para strings, int64 para id)
  - isnull().sum() mostra ~10 nulos em quantidade, ~8 em preco_unitario
Resultado: [ ]
```

### TC03 — Limpeza Remove Registros Inválidos
```
Entrada: limpar_dados(df_bruto)
Esperado:
  - Relatório de limpeza exibido
  - Registros finais < 200 (removidos nulos + datas inválidas)
  - Coluna data_venda do tipo datetime64
  - Nenhum espaço extra em colunas de texto
  - quantidade do tipo int, preco_unitario do tipo float
Resultado: [ ]
```

### TC04 — Colunas Derivadas Criadas
```
Entrada: criar_colunas_derivadas(df_limpo)
Esperado:
  - Colunas novas: receita_total, mes, mes_nome, trimestre, ano, faixa_receita_item
  - receita_total = quantidade * preco_unitario (sem nulos)
  - trimestre em formato "Q1", "Q2", "Q3", "Q4"
  - faixa_receita_item em {"Baixo Valor", "Médio Valor", "Alto Valor"}
Resultado: [ ]
```

### TC05 — Métricas Agregadas
```
Entrada: calcular_metricas(df_limpo)
Esperado:
  - dict com chaves: por_mes, top_produtos, por_categoria, por_regiao
  - por_mes: 12 linhas (uma por mês)
  - top_produtos: 5 linhas
  - por_regiao: 5 linhas (Sudeste, Sul, Nordeste, Centro-Oeste, Norte)
Resultado: [ ]
```

### TC06 — Segmentação de Clientes
```
Entrada: segmentar_clientes(df_limpo)
Esperado:
  - DataFrame com 50 clientes (Cliente_001 a Cliente_050)
  - Colunas: cliente, total_gasto, segmento
  - Segmentos: Bronze, Prata, Ouro
  - Ordenado por total_gasto decrescente
Resultado: [ ]
```

### TC07 — NumPy Vetorizado
```
Entrada: calcular_estatisticas_numpy(df_limpo)
Esperado:
  - Exibe: media, mediana, desvio_padrao, total, p25, p75
  - Receitas normalizadas entre 0 e 1
  - Count de vendas acima da média
  - Sem uso de loops Python para cálculos
Resultado: [ ]
```

### TC08 — Gráficos PNG Exportados
```
Entrada: gerar_visualizacoes(df_limpo, metricas)
Esperado:
  - 3 arquivos PNG em outputs/graficos/:
    * vendas_por_mes.png
    * top_produtos.png
    * distribuicao_regioes.png
  - Arquivos com tamanho > 0 bytes
Resultado: [ ]
```

### TC09 — Exportação CSV e JSON
```
Entrada: exportar_resultados(metricas, clientes, stats)
Esperado:
  - metricas_por_mes.csv em outputs/
  - segmentacao_clientes.csv em outputs/
  - estatisticas_gerais.json em outputs/
  - JSON relido e exibido no console com sucesso
Resultado: [ ]
```

### TC10 — Pipeline Completo (main)
```
Entrada: python salesinsight.py
Esperado:
  - Execução do início ao fim sem erros
  - Todos os outputs gerados
  - Resumo executivo exibido
  - Projeção de 3 meses exibida
  - Mensagem "[CONCLUÍDO] Pipeline finalizado com sucesso!"
Resultado: [ ]
```

---

## Ambiente de Teste

- Python: ___
- pandas: ___
- numpy: ___
- matplotlib: ___
- seaborn: ___
- SO: ___
- Data do teste: ___/___/2026

---

## Bugs Conhecidos

| ID | Descrição | Status | Branch de fix |
|---|---|---|---|
| — | Nenhum registrado | — | — |
