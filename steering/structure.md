# Steering — Estrutura

> Organização de pastas, arquivos e convenções do projeto

---

## Estrutura Completa do Repositório

```
InteligenciaDeMercado/
│
├── salesinsight.py              # Pipeline principal — ponto de entrada único
├── vendas.csv                   # Dataset gerado (não commitar se for grande)
├── requirements.txt             # Dependências Python
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Documentação principal do projeto
│
├── outputs/                     # Saídas geradas pelo pipeline (gitignored parcialmente)
│   ├── .gitkeep                 # Mantém a pasta no Git
│   ├── context_pack.md          # Contexto rápido do projeto
│   ├── metricas_por_mes.csv     # Gerado pelo pipeline (gitignored)
│   ├── segmentacao_clientes.csv # Gerado pelo pipeline (gitignored)
│   ├── estatisticas_gerais.json # Gerado pelo pipeline (gitignored)
│   └── graficos/                # Gráficos PNG gerados (gitignored)
│       ├── .gitkeep
│       ├── vendas_por_mes.png
│       ├── top_produtos.png
│       └── distribuicao_regioes.png
│
├── docs/                        # Documentação técnica e de processo
│   ├── PRD.md                   # Product Requirements Document
│   ├── BACKLOG.md               # Todas as tarefas com status
│   ├── architeture.md           # Arquitetura e decisões de design
│   ├── gitflow.md               # Convenções Git do projeto
│   ├── roadmap.md               # Linha do tempo e entregas
│   ├── technologies.md          # Stack técnica detalhada
│   ├── automation_workflow.md   # Fluxo de execução e automações
│   ├── test_report.md           # Relatório de testes e validação
│   └── prompts/                 # Rastreabilidade de uso de IA
│       ├── ciclos-ia.md         # Log de interações com IA
│       ├── prompt-create-prd.md # Prompt usado para o PRD
│       └── prompt-advanced-visualization.md
│
├── specs/                       # Especificações técnicas
│   ├── requirements.md          # RFs e RNFs detalhados com critérios de aceite
│   ├── tasks.md                 # Tasks com passo-a-passo de implementação
│   └── design.md                # Decisões de design de código e console
│
├── steering/                    # Direcionamento estratégico
│   ├── product.md               # Visão, posicionamento e critérios de sucesso
│   ├── structure.md             # Este arquivo — organização do projeto
│   └── tech.md                  # Decisões técnicas e stack
│
└── .github/                     # Templates GitHub
    ├── pull_request_template.md # Template padrão de PR
    └── ISSUE_TEMPLATE/
        ├── bug_report.md        # Template de bug report
        └── feature_request.md  # Template de feature request
```

---

## Convenções de Nomenclatura

### Arquivos Python
- Snake case: `salesinsight.py`, `vendas.csv`
- Arquivo único conforme requisito do mini-projeto

### Funções
- Snake case em português: `gerar_dataset_vendas`, `limpar_dados`, `calcular_metricas`
- Verbos no infinitivo: `gerar_`, `limpar_`, `criar_`, `calcular_`, `segmentar_`, `exportar_`

### Classes
- PascalCase: `AnalisadorDeVendas`, `AnalisadorComProjecao`

### Variáveis
- Snake case em português: `df_bruto`, `df_limpo`, `por_mes`, `top_produtos`

### Branches Git
- `tipo/descricao-em-kebab-case`: `feat/data-cleaning`, `docs/readme`, `chore/setup-repo`

### Commits
- Conventional Commits: `feat: implementa...`, `fix: corrige...`, `docs: atualiza...`

---

## O que vai para o Git e o que não vai

### ✅ Commitado
- `salesinsight.py`
- `vendas.csv` (dataset sintético pequeno — 200 linhas ~50KB)
- `requirements.txt`
- `.gitignore`
- `README.md`
- Toda a pasta `docs/`
- Toda a pasta `specs/`
- Toda a pasta `steering/`
- `.github/` templates
- `outputs/context_pack.md`
- `outputs/.gitkeep`, `outputs/graficos/.gitkeep`

### ❌ Ignorado (.gitignore)
- `.venv/` (ambiente virtual)
- `__pycache__/`
- `*.pyc`, `*.pyo`
- `outputs/metricas_por_mes.csv` (gerado pelo pipeline)
- `outputs/segmentacao_clientes.csv`
- `outputs/estatisticas_gerais.json`
- `outputs/graficos/*.png`
- `.DS_Store` (macOS)
- `Thumbs.db` (Windows)

---

## Princípios de Organização

1. **Separação de responsabilidades:** código (`salesinsight.py`) × documentação (`docs/`) × specs (`specs/`) × saídas (`outputs/`)
2. **Documentação vive no repositório:** tudo em Markdown, versionado junto com o código
3. **Rastreabilidade:** cada task tem branch, issue e commit correspondente
4. **Reprodutibilidade:** `vendas.csv` e `requirements.txt` garantem execução idêntica em qualquer máquina
