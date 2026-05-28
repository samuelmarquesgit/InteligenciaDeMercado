# Automation Workflow — SalesInsight PY

> Fluxo de execução, automações e processos do projeto

---

## Fluxo de Execução do Pipeline

```
python salesinsight.py
         │
         ▼
┌─────────────────────────────────────────────────────┐
│  main()                                             │
│                                                     │
│  1. Verifica se vendas.csv existe                   │
│     └─► Não existe: gerar_dataset_vendas()          │
│                                                     │
│  2. AnalisadorComProjecao("vendas.csv")             │
│     .carregar()       ← pd.read_csv()               │
│     .limpar()         ← RF03 + RF13                 │
│     .transformar()    ← RF04                        │
│     .analisar()       ← RF05 + RF06 + RF07          │
│     .projetar_tendencia() ← RF10                    │
│     .visualizar()     ← RF08 → PNG                  │
│     .exportar_relatorio() ← RF12 → CSV              │
│                                                     │
│  3. limpar_strings_com_regex()  ← RF13              │
│  4. calcular_estatisticas_numpy() ← RF07            │
│  5. exportar_resultados() ← RF12 → CSV + JSON       │
│  6. analisador.resumo()                             │
│  7. analisador.exibir_projecao_detalhada()          │
└─────────────────────────────────────────────────────┘
         │
         ▼
    outputs/
    ├── metricas_por_mes.csv
    ├── segmentacao_clientes.csv
    ├── estatisticas_gerais.json
    └── graficos/
        ├── vendas_por_mes.png
        ├── top_produtos.png
        └── distribuicao_regioes.png
```

---

## Automação de Setup Local

```bash
# Script de setup completo (executar uma vez)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate    # Linux/macOS
pip install -r requirements.txt
python salesinsight.py
```

---

## Saídas Geradas Automaticamente

| Arquivo | Gerado por | Conteúdo |
|---|---|---|
| `vendas.csv` | `gerar_dataset_vendas()` | 200 linhas, 8 colunas, dados sintéticos sujos |
| `outputs/metricas_por_mes.csv` | `exportar_relatorio()` | Receita e quantidade por mês |
| `outputs/segmentacao_clientes.csv` | `exportar_resultados()` | 50 clientes com total_gasto e segmento |
| `outputs/estatisticas_gerais.json` | `exportar_resultados()` | media, mediana, std, total |
| `outputs/graficos/vendas_por_mes.png` | `gerar_visualizacoes()` | Gráfico de linha — receita mensal |
| `outputs/graficos/top_produtos.png` | `gerar_visualizacoes()` | Barras horizontais — top 5 produtos |
| `outputs/graficos/distribuicao_regioes.png` | `gerar_visualizacoes()` | Boxplot — receita por região |

---

## Fluxo de Versionamento (GitFlow Simplificado)

```bash
# Para cada nova funcionalidade (RF):
git checkout develop
git checkout -b feat/<nome-da-feature>

# ... desenvolver ...

git add salesinsight.py
git commit -m "feat: <descrição da funcionalidade>"
git push origin feat/<nome-da-feature>

# Abrir PR no GitHub: feat/<nome> → develop
# Após merge, deletar branch de feature

# Ao finalizar tudo:
# PR: develop → main
```

---

## Checklist de Execução Completa

```
[ ] python salesinsight.py roda sem erros
[ ] vendas.csv gerado com 200 linhas
[ ] Relatório de limpeza exibido no console
[ ] Colunas derivadas criadas (receita_total, trimestre, etc.)
[ ] Métricas por mês, produto, categoria e região exibidas
[ ] Segmentação de clientes exibida (Bronze/Prata/Ouro)
[ ] Estatísticas NumPy exibidas
[ ] 3 gráficos PNG salvos em outputs/graficos/
[ ] metricas_por_mes.csv salvo em outputs/
[ ] segmentacao_clientes.csv salvo em outputs/
[ ] estatisticas_gerais.json salvo e relido com sucesso
[ ] Projeção de 3 meses exibida no console
[ ] Resumo executivo exibido ao final
```
