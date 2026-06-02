# Roadmap — SalesInsight PY

> Linha do tempo e entregas planejadas · Prazo final: 08/06/2026

---

## Linha do Tempo

```
27/05 ──────── 30/05 ──────── 02/06 ──────── 05/06 ──────── 08/06
  │               │               │               │               │
Setup &         Core            Análise &       Finalização    ENTREGA
Config          Pipeline        Visualização    & Vídeo         AVA
  ✅              ✅               ✅             🟡 Em curso      ⬜
```

---

## Fase 1 — Setup & Configuração (27/05 – 28/05) ✅ Concluída

**Objetivo:** Repositório pronto e estrutura definida

- [x] Criar repositório no GitHub (`InteligenciaDeMercado`)
- [x] Criar branches `main` e `develop`
- [x] Criar estrutura de pastas e arquivos `.md`
- [x] Criar `.gitignore` e `requirements.txt`
- [x] Configurar `.venv`
- [x] Criar templates de PR e Issues no GitHub
- [ ] Criar Issues para todos os RFs no GitHub (verificar se estão abertas)

**Entregável:** Repositório configurado, estrutura de pastas e documentação base

---

## Fase 2 — Core do Pipeline (28/05 – 01/06) ✅ Concluída

**Objetivo:** Funções base do pipeline implementadas e testadas

| Branch | RF | Status | Entregável |
|---|---|---|---|
| `feat/dataset-generator` | RF01 | ✅ | `gerar_dataset_vendas()` gerando `vendas.csv` |
| `feat/data-inspection` | RF02 | ✅ | `inspecionar_dados()` exibindo diagnóstico |
| `feat/data-cleaning` | RF03, RF13 | ✅ | `limpar_dados()` + `limpar_strings_com_regex()` |
| `feat/feature-engineering` | RF04 | ✅ | `criar_colunas_derivadas()` com `np.select` |

**Entregável:** Pipeline de ingestão, limpeza e transformação funcionando

---

## Fase 3 — Análise & Visualização (01/06 – 04/06) ✅ Concluída

**Objetivo:** Métricas, segmentação, estatísticas e gráficos

| Branch | RF | Status | Entregável |
|---|---|---|---|
| `feat/metrics-aggregation` | RF05 | ✅ | `calcular_metricas()` com groupby |
| `feat/customer-segmentation` | RF06 | ✅ | `segmentar_clientes()` Bronze/Prata/Ouro |
| `feat/numpy-statistics` | RF07 | ✅ | `calcular_estatisticas_numpy()` vetorizado |
| `feat/lambda-hof` | RF11 | ✅ | `processar_coluna()` e 4 usos de lambda |
| `feat/visualizations` | RF08 | ✅ | 3 gráficos PNG exportados |
| `feat/export-reports` | RF12 | ✅ | CSV + JSON em `outputs/` |

**Entregável:** Análise completa com outputs gerados

---

## Fase 4 — Classes & Pipeline Completo (04/06 – 06/06) ✅ Concluída

**Objetivo:** OOP, herança, projeção e pipeline integrado

| Branch | RF | Status | Entregável |
|---|---|---|---|
| `feat/analyzer-class` | RF09 | ✅ | `AnalisadorDeVendas` com method chaining |
| `feat/projection-class` | RF10 | ✅ | `AnalisadorComProjecao` com `super()` e projeção |
| `feat/main-pipeline` | RF14 | ✅ | `main()` executando de ponta a ponta |

**Entregável:** `salesinsight.py` completo, testado e executando

---

## Fase 5 — Finalização & Entrega (06/06 – 08/06) 🟡 Em Andamento

**Objetivo:** Documentação, vídeo e submissão

- [x] Atualizar README com todos os conceitos aplicados
- [x] Revisar e melhorar toda a documentação técnica
- [x] Criar diagrama Mermaid do pipeline
- [ ] Gravar vídeo de demonstração (≤ 5 minutos)
- [ ] Hospedar vídeo no Google Drive ou YouTube não listado
- [ ] Criar e popular Quadro Kanban no GitHub Projects
- [ ] Inserir links reais no `README.md` (vídeo + Kanban)
- [ ] Fechar issues concluídas no GitHub
- [ ] Tornar repositório público no GitHub
- [ ] Submeter links no AVA antes das 12h de 08/06/2026

---

## Marcos (Milestones)

| Marco | Data Planejada | Status | Critério |
|---|---|---|---|
| M1 — Repositório configurado | 28/05/2026 | ✅ | Branches criadas, estrutura definida |
| M2 — Pipeline base | 01/06/2026 | ✅ | RF01–RF04 funcionando |
| M3 — Análise completa | 04/06/2026 | ✅ | RF05–RF13 + outputs gerados |
| M4 — Pipeline completo | 06/06/2026 | ✅ | RF14 + classes OOP testadas |
| M5 — Entrega final | 08/06/2026 | ⬜ | Links no AVA, vídeo acessível |

---

## Progresso por RF

| RF | Descrição | Status |
|---|---|---|
| RF01 | Geração de dataset | ✅ |
| RF02 | Inspeção de dados | ✅ |
| RF03 | Limpeza e tratamento | ✅ |
| RF04 | Colunas derivadas | ✅ |
| RF05 | Métricas aggregadas | ✅ |
| RF06 | Segmentação de clientes | ✅ |
| RF07 | Estatísticas NumPy | ✅ |
| RF08 | Visualizações PNG | ✅ |
| RF09 | Classe AnalisadorDeVendas | ✅ |
| RF10 | Herança + Projeção | ✅ |
| RF11 | Lambda + HOF | ✅ |
| RF12 | Exportação CSV/JSON | ✅ |
| RF13 | Regex | ✅ |
| RF14 | Pipeline completo | ✅ |

**14/14 RFs implementados (100%)**

---

## v2.0 — Pós-entrega (fora de escopo para avaliação)

Melhorias futuras para portfólio:

- Integração com API REST (requests + FastAPI)
- Dashboard interativo com Streamlit
- Modelos ML reais (sklearn — regressão linear, random forest)
- Testes automatizados com pytest
- CI/CD com GitHub Actions
- Containerização com Docker
- Notebook Jupyter com análise exploratória
