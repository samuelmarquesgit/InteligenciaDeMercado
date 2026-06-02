# Steering — Estrutura

> Organização de pastas, arquivos e convenções do projeto
> Atualizado em: 01/06/2026

---

## Estrutura Completa do Repositório

```
InteligenciaDeMercado/
│
├── salesinsight.py              # Pipeline principal — ponto de entrada único
├── vendas.csv                   # Dataset gerado (200 linhas × 8 colunas)
├── requirements.txt             # Dependências Python
├── pytest.ini                   # Configuração de testes (pytest)
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Documentação principal do projeto
│
├── outputs/                     # Saídas geradas pelo pipeline
│   ├── .gitkeep                 # Mantém a pasta no Git
│   ├── metricas_por_mes.csv     # Gerado pelo pipeline (gitignored)
│   ├── segmentacao_clientes.csv # Gerado pelo pipeline (gitignored)
│   ├── estatisticas_gerais.json # Gerado pelo pipeline (gitignored)
│   └── graficos/
│       ├── .gitkeep
│       ├── vendas_por_mes.png   # Gerado (gitignored)
│       ├── top_produtos.png     # Gerado (gitignored)
│       └── distribuicao_regioes.png # Gerado (gitignored)
│
├── docs/                        # Documentação técnica e de processo
│   ├── PRD.md                   # Product Requirements Document
│   ├── BACKLOG.md               # Rastreamento de tarefas com status
│   ├── architeture.md           # Arquitetura, camadas e hierarquia de classes
│   ├── gitflow.md               # Convenções Git do projeto
│   ├── roadmap.md               # Linha do tempo e entregas
│   ├── technologies.md          # Stack técnica detalhada
│   ├── test_report.md           # Relatório de validação e divergências
│   └── prompts/                 # Rastreabilidade de uso de IA
│
├── specs/                       # Especificações técnicas
│   ├── requirements.md          # RFs e RNFs com critérios de aceite e status
│   ├── tasks.md                 # Tasks com passo-a-passo e status
│   └── design.md                # Decisões de design de código e console
│
├── steering/                    # Direcionamento estratégico
│   ├── product.md               # Visão, posicionamento e critérios de sucesso
│   ├── structure.md             # Este arquivo — organização do projeto
│   └── tech.md                  # Decisões técnicas, stack e checklist
│
└── .github/                     # Templates GitHub
    ├── pull_request_template.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

---

## Convenções de Nomenclatura

### Arquivos Python
- Snake case: `salesinsight.py`
- Arquivo único conforme requisito do mini-projeto

### Funções
- Snake case em português, verbo no infinitivo
- `gerar_`, `inspecionar_`, `limpar_`, `criar_`, `calcular_`, `segmentar_`, `processar_`, `exportar_`

### Classes
- PascalCase em português: `AnalisadorDeVendas`, `AnalisadorComProjecao`

### Variáveis
- Snake case em português: `df_bruto`, `df_limpo`, `por_mes`, `top_produtos`

### Constantes de Módulo
- UPPER_SNAKE_CASE: `PRODUTOS`, `REGIOES`, `CATEGORIAS`, `NOMES_MESES`

### Branches Git
- `tipo/descricao-em-kebab-case`: `feat/data-cleaning`, `docs/readme`, `chore/setup-repo`

### Commits
- Conventional Commits: `feat: implementa...`, `fix: corrige...`, `docs: atualiza...`

---

## O que vai para o Git e o que não vai

### Commitado
- `salesinsight.py`
- `vendas.csv` (dataset sintético pequeno — 200 linhas ~50KB)
- `requirements.txt`
- `pytest.ini`
- `.gitignore`
- `README.md`
- Toda a pasta `docs/`
- Toda a pasta `specs/`
- Toda a pasta `steering/`
- `.github/` templates
- `outputs/.gitkeep`, `outputs/graficos/.gitkeep`

### Ignorado (.gitignore)
- `.venv/` — ambiente virtual
- `__pycache__/`, `*.pyc`, `*.pyo`
- `outputs/metricas_por_mes.csv` — gerado pelo pipeline
- `outputs/segmentacao_clientes.csv`
- `outputs/estatisticas_gerais.json`
- `outputs/graficos/*.png`
- `.DS_Store` (macOS)
- `Thumbs.db` (Windows)

---

## Princípios de Organização

1. **Separação de responsabilidades:** código × documentação × specs × saídas
2. **Documentação vive no repositório:** tudo em Markdown, versionado com o código
3. **Rastreabilidade:** cada tarefa tem branch, issue e commit correspondente
4. **Reprodutibilidade:** `vendas.csv` + `requirements.txt` garantem execução idêntica em qualquer máquina
5. **Transparência:** status de cada RF documentado em `docs/BACKLOG.md` e `specs/requirements.md`
