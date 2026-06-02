# Backlog — SalesInsight PY

> Rastreamento de todas as tarefas do projeto · Atualizado em: 01/06/2026

---

## Status das Tarefas

| ID | Tarefa | RF | Prioridade | Status | Branch | Issue |
|---|---|---|---|---|---|---|
| T01 | Configurar repositório, branches e proteções | — | Alta | ✅ Concluído | `chore/setup-repo` | #1 |
| T02 | Criar estrutura de pastas e arquivos base | — | Alta | ✅ Concluído | `chore/project-structure` | #2 |
| T03 | Criar `requirements.txt` e `.gitignore` | — | Alta | ✅ Concluído | `chore/project-structure` | #2 |
| T04 | Criar função `gerar_dataset_vendas()` | RF01 | Alta | ✅ Concluído | `feat/dataset-generator` | #3 |
| T05 | Criar função `inspecionar_dados()` | RF02 | Alta | ✅ Concluído | `feat/data-inspection` | #4 |
| T06 | Criar função `limpar_dados()` | RF03 | Alta | ✅ Concluído | `feat/data-cleaning` | #5 |
| T07 | Criar função `limpar_strings_com_regex()` | RF13 | Alta | ✅ Concluído | `feat/data-cleaning` | #5 |
| T08 | Criar função `criar_colunas_derivadas()` | RF04 | Alta | ✅ Concluído | `feat/feature-engineering` | #6 |
| T09 | Criar função `calcular_metricas()` com groupby | RF05 | Alta | ✅ Concluído | `feat/metrics-aggregation` | #7 |
| T10 | Criar função `segmentar_clientes()` com lambda | RF06 | Alta | ✅ Concluído | `feat/customer-segmentation` | #8 |
| T11 | Criar função `calcular_estatisticas_numpy()` | RF07 | Alta | ✅ Concluído | `feat/numpy-statistics` | #9 |
| T12 | Criar função `processar_coluna()` (higher-order) | RF11 | Média | ✅ Concluído | `feat/lambda-hof` | #10 |
| T13 | Criar função `gerar_visualizacoes()` | RF08 | Alta | ✅ Concluído | `feat/visualizations` | #11 |
| T14 | Criar função `exportar_resultados()` (CSV + JSON) | RF12 | Alta | ✅ Concluído | `feat/export-reports` | #12 |
| T15 | Criar classe `AnalisadorDeVendas` | RF09 | Alta | ✅ Concluído | `feat/analyzer-class` | #13 |
| T16 | Criar classe `AnalisadorComProjecao` (herança) | RF10 | Alta | ✅ Concluído | `feat/projection-class` | #14 |
| T17 | Criar função `main()` e bloco `__main__` | RF14 | Alta | ✅ Concluído | `feat/main-pipeline` | #15 |
| T18 | Testar pipeline completo (Colab ou VS Code) | — | Alta | ✅ Concluído | `test/full-pipeline` | #16 |
| T19 | Atualizar README e documentação técnica | — | Média | ✅ Concluído | `docs/readme` | #17 |
| T20 | Gravar vídeo de demonstração (até 5 min) | — | Alta | ⬜ Pendente | — | #18 |
| T21 | Submeter links no AVA | — | Alta | ⬜ Pendente | — | — |

---

## Legenda de Status

| Símbolo | Status |
|---|---|
| ⬜ Pendente | Não iniciado |
| 🔵 A Fazer | Priorizado para próxima sprint |
| 🟡 Em Andamento | Em desenvolvimento |
| ✅ Concluído | Entregue e testado |
| ❌ Bloqueado | Impedido por dependência |

---

## Kanban

### ⬜ Pendente
- T20 — Gravar vídeo de demonstração
- T21 — Submeter links no AVA

### 🟡 Em Andamento
_vazio_

### ✅ Concluído
T01 · T02 · T03 · T04 · T05 · T06 · T07 · T08 · T09 · T10 · T11 · T12 · T13 · T14 · T15 · T16 · T17 · T18 · T19

---

## Progresso Geral

**19/21 tarefas concluídas (90%)**

| Categoria | Total | Concluídas |
|---|---|---|
| Configuração e infra | 3 | 3 |
| Implementação (RF01–RF14) | 14 | 14 |
| Testes | 1 | 1 |
| Documentação | 1 | 1 |
| Entrega final | 2 | 0 |

---

## Dependências entre Tarefas

```
T01, T02, T03
    └─► T04 (dataset)
            └─► T05 (inspeção)
                └─► T06, T07 (limpeza + regex)
                        └─► T08 (colunas derivadas)
                                └─► T09 (groupby)
                                └─► T10 (segmentação)
                                └─► T11 (numpy stats)
                                └─► T12 (HOF)
                                        └─► T13 (visualizações)
                                        └─► T14 (exportação)
                                                └─► T15, T16 (classes)
                                                        └─► T17 (main)
                                                                └─► T18 (testes)
                                                                └─► T19 (docs)
                                                                        └─► T20 (vídeo)
                                                                                └─► T21 (AVA)
```

---

## Itens Críticos para Entrega

> Prazo: **08/06/2026 às 12h**

- [ ] **T20** — Gravar vídeo de até 5 minutos demonstrando a execução do pipeline
- [ ] **T21** — Submeter no AVA: link do GitHub + link do vídeo + link do Kanban
- [ ] Tornar o repositório **público** no GitHub
- [ ] Criar e popular o **Quadro Kanban** no GitHub Projects
- [ ] Inserir links reais de vídeo e Kanban no `README.md`
