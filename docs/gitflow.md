# GitFlow — SalesInsight PY

> Convenções de branches, commits e fluxo de trabalho do projeto

---

## Estratégia de Branches

```
main
│   Branch de produção. Código final entregue no AVA.
│   Recebe merges apenas via Pull Request aprovado.
│   Nunca recebe push direto.
│
develop
│   Branch de integração. Toda feature é mergeada aqui primeiro.
│   Base para criação de todas as branches de feature.
│
feat/<descrição>
│   Branches de funcionalidade. Criadas a partir de develop.
│   Exemplos: feat/dataset-generator, feat/data-cleaning
│
fix/<descrição>
│   Correção de bugs identificados em develop ou main.
│
docs/<descrição>
│   Atualizações de documentação sem mudança de código.
│
chore/<descrição>
│   Configuração, build, dependências (requirements.txt, .gitignore).
│
test/<descrição>
    Testes do pipeline completo.
```

---

## Branches do Projeto

| Branch | Base | Finalidade | Status |
|---|---|---|---|
| `main` | — | Código final entregue no AVA | ✅ |
| `develop` | `main` | Integração contínua de features | ✅ |
| `chore/setup-repo` | `develop` | Configuração inicial | ✅ Mergeada |
| `chore/project-structure` | `develop` | Estrutura de pastas e arquivos | ✅ Mergeada |
| `feat/dataset-generator` | `develop` | RF01 — Geração do dataset sintético | ✅ Mergeada |
| `feat/data-inspection` | `develop` | RF02 — Inspeção dos dados | ✅ Mergeada |
| `feat/data-cleaning` | `develop` | RF03 + RF13 — Limpeza e regex | ✅ Mergeada |
| `feat/feature-engineering` | `develop` | RF04 — Colunas derivadas | ✅ Mergeada |
| `feat/metrics-aggregation` | `develop` | RF05 — groupby e métricas | ✅ Mergeada |
| `feat/customer-segmentation` | `develop` | RF06 — Segmentação com lambda | ✅ Mergeada |
| `feat/numpy-statistics` | `develop` | RF07 — NumPy vetorizado | ✅ Mergeada |
| `feat/lambda-hof` | `develop` | RF11 — Lambda e higher-order functions | ✅ Mergeada |
| `feat/visualizations` | `develop` | RF08 — Gráficos Matplotlib/Seaborn | ✅ Mergeada |
| `feat/export-reports` | `develop` | RF12 — Exportação CSV/JSON | ✅ Mergeada |
| `feat/analyzer-class` | `develop` | RF09 — Classe AnalisadorDeVendas | ✅ Mergeada |
| `feat/projection-class` | `develop` | RF10 — Herança AnalisadorComProjecao | ✅ Mergeada |
| `feat/main-pipeline` | `develop` | RF14 — main() e pipeline completo | ✅ Mergeada |
| `feature/add-salesinsight-notebook` | `develop` | Notebook de análise exploratória | 🟡 Em aberto |
| `docs/readme` | `develop` | Documentação final | ✅ Mergeada |

---

## Fluxo de Trabalho

```
1. Criar branch a partir de develop
   git checkout develop
   git pull origin develop
   git checkout -b feat/nome-da-feature

2. Desenvolver com commits semânticos
   git add salesinsight.py
   git commit -m "feat(rf03): implementa limpeza de dados e tratamento de nulos"

3. Abrir Pull Request: feat/nome → develop
   - Preencher o template de PR
   - Verificar checklist
   - Referenciar a issue correspondente

4. Após aprovação, fazer merge em develop
   (squash merge recomendado para histórico limpo)

5. Ao finalizar o projeto: PR de develop → main
   - PR final de entrega
   - Verificar que todos os outputs são gerados
```

---

## Convenção de Commits Semânticos

### Formato
```
<type>(<scope>): <descrição curta no imperativo>

[corpo opcional — explica o "porquê"]

[rodapé opcional — Closes #<issue>]
```

### Tipos

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade (RF implementado) |
| `fix` | Correção de bug |
| `docs` | Apenas documentação |
| `refactor` | Refatoração sem mudança de comportamento |
| `test` | Testes |
| `chore` | Build, config, dependências |
| `perf` | Otimização de performance |
| `style` | Formatação (sem mudança de lógica) |

### Exemplos do Projeto

```bash
chore: configura gitignore, requirements.txt e venv

feat: cria gerar_dataset_vendas com dados sintéticos e seed fixo

feat: implementa inspecionar_dados com shape, dtypes e isnull

feat: adiciona limpar_dados com tratamento de nulos e datas invalidas

feat: implementa limpar_strings com re.sub e re.compile

feat: cria colunas derivadas receita_total trimestre e faixa_receita_item

feat: adiciona metricas agregadas por mes produto categoria e regiao

feat: implementa segmentacao de clientes Bronze Prata Ouro com lambda

feat: adiciona estatisticas numpy vetorizadas com broadcasting

feat: cria processar_coluna como higher-order function

feat: gera visualizacoes linha barras e pizza exportadas em PNG

feat: exporta relatorios CSV e JSON com validacao de leitura

feat: cria AnalisadorDeVendas com construtor atributos e method chaining

feat: adiciona AnalisadorComProjecao com heranca super e projecao composta

feat: implementa main e pipeline completo ponta a ponta

docs: atualiza README revisao completa da documentacao tecnica
```

---

## Regras de Proteção de Branch

| Branch | Proteção |
|---|---|
| `main` | Requer Pull Request; sem push direto |
| `develop` | Requer Pull Request de branches `feat/*`, `fix/*`, `docs/*`, `chore/*` |
| `feat/*` | Descartadas após merge |

---

## Checklist de PR

Antes de abrir qualquer Pull Request:

- [ ] Branch criada a partir de `develop` (não de `main`)
- [ ] Commits seguem a convenção semântica
- [ ] `python salesinsight.py` roda sem erros
- [ ] Template de PR preenchido
- [ ] Issue referenciada no PR (`Closes #N`)
- [ ] `BACKLOG.md` atualizado com o status da tarefa
