# Roadmap — SalesInsight PY

> Linha do tempo e entregas planejadas · Prazo final: 08/06/2026

---

## Linha do Tempo

```
27/05 ──────── 30/05 ──────── 02/06 ──────── 05/06 ──────── 08/06
  │               │               │               │               │
Setup &         Core            Análise &       Finalização    ENTREGA
Config          Pipeline        Visualização    & Vídeo         AVA
```

---

## Fase 1 — Setup & Configuração (27/05 – 28/05)

**Objetivo:** Repositório pronto e estrutura definida

- [x] Criar repositório no GitHub (`InteligenciaDeMercado`)
- [x] Criar branches `main` e `develop`
- [x] Criar estrutura de pastas e arquivos `.md`
- [ ] Criar `.gitignore` e `requirements.txt`
- [ ] Configurar `venv`
- [ ] Criar templates de PR e Issues no GitHub
- [ ] Criar Issues para todos os RFs no GitHub

**Entrega:** Repositório configurado, issues criadas, kanban populado

---

## Fase 2 — Core do Pipeline (28/05 – 01/06)

**Objetivo:** Funções base do pipeline implementadas e testadas

| Branch | RF | Entrega |
|---|---|---|
| `feat/dataset-generator` | RF01 | `gerar_dataset_vendas()` gerando `vendas.csv` |
| `feat/data-inspection` | RF02 | `inspecionar_dados()` exibindo metadados |
| `feat/data-cleaning` | RF03, RF13 | `limpar_dados()` + `limpar_strings_com_regex()` |
| `feat/feature-engineering` | RF04 | `criar_colunas_derivadas()` com `np.select` |

**Entrega:** Pipeline de ingestão, limpeza e transformação funcionando

---

## Fase 3 — Análise & Visualização (01/06 – 04/06)

**Objetivo:** Métricas, segmentação, estatísticas e gráficos

| Branch | RF | Entrega |
|---|---|---|
| `feat/metrics-aggregation` | RF05 | `calcular_metricas()` com groupby |
| `feat/customer-segmentation` | RF06 | `segmentar_clientes()` Bronze/Prata/Ouro |
| `feat/numpy-statistics` | RF07 | `calcular_estatisticas_numpy()` vetorizado |
| `feat/lambda-hof` | RF11 | `processar_coluna()` e 2+ usos de lambda |
| `feat/visualizations` | RF08 | 3 gráficos PNG exportados |
| `feat/export-reports` | RF12 | CSV + JSON em `outputs/` |

**Entrega:** Análise completa com outputs gerados

---

## Fase 4 — Classes & Pipeline Completo (04/06 – 06/06)

**Objetivo:** OOP, herança, projeção e pipeline integrado

| Branch | RF | Entrega |
|---|---|---|
| `feat/analyzer-class` | RF09 | `AnalisadorDeVendas` com `__init__` e métodos |
| `feat/projection-class` | RF10 | `AnalisadorComProjecao` com `super()` e projeção |
| `feat/main-pipeline` | RF14 | `main()` executando tudo de ponta a ponta |

**Entrega:** `salesinsight.py` completo, testado e rodando

---

## Fase 5 — Finalização & Entrega (06/06 – 08/06)

**Objetivo:** Documentação, vídeo e submissão

- [ ] Atualizar README com todos os conceitos aplicados
- [ ] Gravar vídeo de demonstração (≤ 5 minutos)
- [ ] Hospedar vídeo no Google Drive ou YouTube não listado
- [ ] Atualizar links no README.md
- [ ] Fechar issues concluídas no GitHub
- [ ] Mover cards para "Concluído" no Kanban
- [ ] Submeter links no AVA antes das 12h de 08/06/2026

---

## Marcos (Milestones)

| Marco | Data | Critério |
|---|---|---|
| M1 — Repositório configurado | 28/05/2026 | Branches criadas, issues abertas, kanban populado |
| M2 — Pipeline base | 01/06/2026 | RF01–RF04 funcionando |
| M3 — Análise completa | 04/06/2026 | RF05–RF13 + outputs gerados |
| M4 — Pipeline completo | 06/06/2026 | RF14 + classes OOP testadas |
| M5 — Entrega final | 08/06/2026 | Links no AVA, vídeo acessível |

---

## v2.0 — Pós-entrega (fora de escopo para avaliação)

Melhorias futuras para o portfólio:

- Integração com API REST (requests + FastAPI)
- Dashboard interativo com Streamlit
- Modelos ML reais (sklearn — regressão linear, random forest)
- Testes automatizados com pytest
- CI/CD com GitHub Actions
- Containerização com Docker
