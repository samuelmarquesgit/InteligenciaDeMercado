# Context Pack — SalesInsight PY

> Pacote de contexto para onboarding rápido no projeto

---

## Resumo em 3 linhas

**O que é:** Pipeline Python de análise de dados de vendas (varejo).
**O que faz:** Lê CSV → limpa → transforma → analisa → visualiza → exporta relatórios.
**Por que existe:** Mini-projeto avaliativo do Módulo 01 de IA para Análise Preditiva (SCTEC). Prazo: 08/06/2026.

---

## Contexto do Negócio

Uma empresa de varejo tem um histórico de vendas em CSV e precisa de relatório analítico para a reunião trimestral da diretoria. Perguntas do time de negócios:

1. Como as vendas se comportam ao longo do tempo (por mês, trimestre)?
2. Quais produtos e categorias geram mais receita?
3. Quais regiões têm melhor desempenho?
4. Quais clientes são mais valiosos (segmentação Bronze/Prata/Ouro)?
5. Qual a projeção de tendência para o próximo trimestre?

---

## Arquivos Críticos

| Arquivo | Papel |
|---|---|
| `salesinsight.py` | Ponto de entrada — todo o pipeline em um arquivo |
| `vendas.csv` | Dataset de 200 linhas gerado sinteticamente com `seed=42` |
| `docs/PRD.md` | Requisitos completos (RF01–RF14) |
| `docs/BACKLOG.md` | Todas as tarefas com status e branch |
| `docs/architeture.md` | Diagrama e decisões de design |
| `specs/tasks.md` | Tasks detalhadas com critérios de aceite |

---

## Decisões Importantes

| Decisão | Razão |
|---|---|
| `seed=42` fixo | Reprodutibilidade garantida |
| Pipeline em arquivo único (`salesinsight.py`) | Requisito do mini-projeto |
| Method chaining na classe | API fluente — todos os métodos retornam `self` |
| `np.select` para classificações | Vetorizado — sem loops Python |
| `utf-8-sig` nos CSVs | Compatibilidade com Excel no Windows |
| Subclasse para projeção | Requisito explícito de herança (RF10) |

---

## Dataset (vendas.csv)

```
Colunas: id_venda, data_venda, cliente, produto, categoria, regiao, quantidade, preco_unitario
Linhas: 200 (dataset bruto) → ~180 (após limpeza)
Produtos: Notebook, Smartphone, Tablet, Monitor, Teclado, Mouse, Headset
Categorias: Computadores, Celulares, Periféricos
Regiões: Sudeste, Sul, Nordeste, Centro-Oeste, Norte
Clientes: Cliente_001 a Cliente_050
Período: 2024-01-01 a 2024-12-31
Dados sujos: ~5% nulos em quantidade, ~4% em preço, ~2% datas inválidas, ~3% strings com espaço
```

---

## Outputs Esperados

```
outputs/
├── metricas_por_mes.csv         ← receita e quantidade por mês
├── segmentacao_clientes.csv     ← 50 clientes com segmento
├── estatisticas_gerais.json     ← media, mediana, std, total
└── graficos/
    ├── vendas_por_mes.png       ← linha: receita mensal
    ├── top_produtos.png         ← barras: top 5 produtos
    └── distribuicao_regioes.png ← boxplot: receita por região
```

---

## Para Começar a Desenvolver

```bash
git clone git@github.com:samuelmarquesgit/InteligenciaDeMercado.git
cd InteligenciaDeMercado
git checkout develop
git checkout -b feat/<sua-feature>
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
# ... implementar RF ...
python salesinsight.py  # testar
git add salesinsight.py
git commit -m "feat: <descrição>"
# Abrir PR: feat/<nome> → develop
```
