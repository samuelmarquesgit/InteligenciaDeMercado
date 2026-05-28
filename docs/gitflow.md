# GitFlow — SalesInsight PY

> Convenções de branches, commits e fluxo de trabalho do projeto

---

## Estratégia de Branches

```
main
│   └── Branch de produção. Apenas código testado e aprovado.
│       Recebe merges apenas via Pull Request aprovado.
│
develop
│   └── Branch de integração. Toda feature é mergeada aqui primeiro.
│       Base para criação de todas as branches de feature.
│
feat/<descrição>
│   └── Branches de funcionalidade. Criadas a partir de develop.
│       Exemplos: feat/dataset-generator, feat/data-cleaning
│
fix/<descrição>
│   └── Correção de bugs identificados em develop ou main.
│
docs/<descrição>
│   └── Atualizações de documentação sem mudança de código.
│
chore/<descrição>
│   └── Configuração, build, dependências (requirements.txt, .gitignore).
│
test/<descrição>
    └── Testes do pipeline completo.
```

---

## Branches do Projeto

| Branch | Base | Finalidade |
|---|---|---|
| `main` | — | Código final entregue no AVA |
| `develop` | `main` | Integração contínua de features |
| `chore/setup-repo` | `develop` | Configuração inicial (gitignore, requirements, .github) |
| `chore/project-structure` | `develop` | Estrutura de pastas e arquivos base |
| `feat/dataset-generator` | `develop` | RF01 — Geração do dataset sintético |
| `feat/data-inspection` | `develop` | RF02 — Inspeção dos dados |
| `feat/data-cleaning` | `develop` | RF03 + RF13 — Limpeza e regex |
| `feat/feature-engineering` | `develop` | RF04 — Colunas derivadas |
| `feat/metrics-aggregation` | `develop` | RF05 — groupby e métricas |
| `feat/customer-segmentation` | `develop` | RF06 — Segmentação com lambda |
| `feat/numpy-statistics` | `develop` | RF07 — NumPy vetorizado |
| `feat/lambda-hof` | `develop` | RF11 — Lambda e higher-order functions |
| `feat/visualizations` | `develop` | RF08 — Gráficos Matplotlib/Seaborn |
| `feat/export-reports` | `develop` | RF12 — Exportação CSV/JSON |
| `feat/analyzer-class` | `develop` | RF09 — Classe AnalisadorDeVendas |
| `feat/projection-class` | `develop` | RF10 — Herança AnalisadorComProjecao |
| `feat/main-pipeline` | `develop` | RF14 — main() e pipeline completo |
| `docs/readme` | `develop` | Documentação final do README |

---

## Fluxo de Trabalho

```
1. Criar branch a partir de develop
   git checkout develop
   git checkout -b feat/data-cleaning

2. Desenvolver e commitar com commits semânticos
   git add salesinsight.py
   git commit -m "feat: implementa limpeza de dados e tratamento de nulos"

3. Abrir Pull Request: feat/data-cleaning → develop
   - Preencher o template de PR
   - Verificar checklist

4. Após aprovação, fazer merge em develop
   (squash merge recomendado para histórico limpo)

5. Ao finalizar o projeto: PR de develop → main
```

---

## Convenção de Commits Semânticos

### Formato
```
<type>(<scope>): <descrição curta no imperativo>

[corpo opcional — explica o "porquê"]

[rodapé opcional — referência de issue]
```

### Tipos

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade (RF) |
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

feat: cria função gerar_dataset_vendas com dados sintéticos e seed fixo

feat: implementa inspecionar_dados com shape, dtypes e isnull

feat: adiciona limpeza de dados com tratamento de nulos e datas invalidas

feat: implementa limpeza de strings com re.sub e re.compile

feat: cria colunas derivadas receita_total trimestre e faixa_receita_item

feat: adiciona metricas agregadas por mes produto categoria e regiao

feat: implementa segmentacao de clientes por nivel de gasto com lambda

feat: adiciona calculos estatisticos com numpy vetorizado e broadcasting

feat: cria funcao processar_coluna como higher-order function

feat: gera visualizacoes linha barras e boxplot exportadas em PNG

feat: exporta relatorios em CSV e JSON com validacao de leitura

feat: cria classe AnalisadorDeVendas com construtor atributos e metodos

feat: adiciona AnalisadorComProjecao com heranca super e media movel

feat: implementa main e pipeline completo ponta a ponta

docs: atualiza README com instrucoes execucao e checklist de conceitos

fix: corrige conversao de datas invalidas no pipeline de limpeza
```

---

## Regras de Proteção de Branch

- `main`: requer Pull Request; sem push direto
- `develop`: requer Pull Request de branches `feat/*`, `fix/*`, `docs/*`, `chore/*`
- Branches de feature: descartadas após merge

---

## Checklist de PR

Antes de abrir qualquer PR, verificar:

- [ ] Branch criada a partir de `develop` (não de `main`)
- [ ] Commits semânticos
- [ ] `python salesinsight.py` roda sem erros
- [ ] Template de PR preenchido
- [ ] Issue referenciada no PR
