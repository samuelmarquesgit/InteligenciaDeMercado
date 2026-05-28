# PROMPT.md — Rastreabilidade de Prompts do Projeto

> Registro de todos os prompts utilizados na construção do SalesInsight PY
> Modelo: Claude Sonnet 4.6 (Claude Code — Anthropic)
> Projeto: InteligenciaDeMercado / SalesInsight PY

---

## Prompt 01 — Planejamento Inicial do Projeto (docx)

**Data:** 27/05/2026
**Fase:** Planejamento

```
Leia e utilize somente a pasta Claude para criar um projeto com o nome
Inteligência de Mercado (InteligenciaDeMercado o nome da pasta).
O arquivo que é a base do projeto é o Desenvolvedor(a) em IA para Análise
Preditiva [T1] - M1S08 - Mini-Projeto Avaliativo (template SCTEC).docx

Não faça nenhum código, primeiro vamos planejar tudo, criar todos os .md
necessários de um projeto profissional. Depois vamos clonar o github
git@github.com:samuelmarquesgit/InteligenciaDeMercado.git
Criar todas as Issues e podemos utilizar gh repo clone
samuelmarquesgit/InteligenciaDeMercado para outras tarefas.
Quero uma branch main, uma branch develop e toda issue ou task executada
quero um commit semântico com uma branch semântica. Também iremos criar um
arquivo pull_request_template.md de Pull Request (PR) onde ficará O que foi
feito (entre outras coisas necessárias, me surpreenda)
```

**Resultado:** Leitura do .docx iniciada (problema de ambiente — sem shell POSIX)

---

## Prompt 02 — Definição da Linguagem

**Data:** 27/05/2026
**Fase:** Planejamento

```
esqueci de dizer, o projeto será 100% em python
```

**Resultado:** Confirmado stack 100% Python para o projeto

---

## Prompt 03 — Preferência de leitura por PDF

**Data:** 27/05/2026
**Fase:** Planejamento

```
você prefere ler PDF?
```

**Resultado:** Confirmado — PDF é mais fácil de ler no ambiente sem shell POSIX

---

## Prompt 04 — Replanejamento Completo com Estrutura Detalhada (PDF)

**Data:** 27/05/2026
**Fase:** Planejamento

```
Pronto, arquivo criado....

Leia e utilize somente a pasta Claude para criar um projeto com o nome
Inteligência de Mercado (InteligenciaDeMercado o nome da pasta).
O arquivo que é a base do projeto é o Desenvolvedor(a) em IA para Análise
Preditiva [T1] - M1S08 - Mini-Projeto Avaliativo (template SCTEC).pdf

Não faça nenhum código, primeiro vamos planejar tudo, criar todos os .md
necessários de um projeto profissional. Depois vamos clonar o github
git@github.com:samuelmarquesgit/InteligenciaDeMercado.git
Criar todas as Issues e podemos utilizar gh repo clone
samuelmarquesgit/InteligenciaDeMercado para outras tarefas.
Quero uma branch main, uma branch develop e toda issue ou task executada
quero um commit semântico com uma branch semântica. Também iremos criar um
arquivo pull_request_template.md de Pull Request (PR) onde ficará O que foi
feito (entre outras coisas necessárias, me surpreenda)

📁 Raiz do Projeto (Root)
README.md

📁 Configurações de PR/Issue (.github/)
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md

📁 Documentação Geral (docs/)
docs/BACKLOG.md
docs/PRD.md
docs/architeture.md
docs/automation_workflow.md
docs/gitflow.md
docs/roadmap.md
docs/technologies.md
docs/test_report.md

📁 Rastreabilidade de Prompts de IA (docs/prompts/)
docs/prompts/prompt-advanced-visualization.md
docs/prompts/prompt-create-prd.md
docs/prompts/ciclos-ia.md

📁 Saídas de Dados (outputs/)
outputs/context_pack.md

📁 Especificações Técnicas (specs/)
specs/design.md
specs/requirements.md
specs/tasks.md

📁 Direcionamento de Projeto (steering/)
steering/product.md
steering/structure.md
steering/tech.md
```

**Resultado:** Todos os arquivos .md criados na pasta InteligenciaDeMercado

---

## Prompt 05 — Clonagem, Pytest, Issues e Commits Individuais

**Data:** 27/05/2026
**Fase:** Setup do Repositório

```
sim, faça a clonagem, mas eu preciso que crie os arquivos de teste de toda
a estrutura utilizando o pytest.
quero também que faça um commit para cada arquivo, crie uma issue para cada
arquivo....
Sei que é mais simples fazer tudo de uma só vez, mas não quero que commit
tudo de uma só vez. Faça o commit inicial somente com o README.md ......

Preciso contabilizar commits nesse projeto, quanto mais commits melhor....
por gentileza gravar todos os prompts no arquivo de PROMPT.md, menos essa
frase aqui......
```

**Resultado:** Script de automação criado, arquivos de teste pytest gerados,
issues e commits individuais via script Python

---

## Como Usar Este Arquivo

Para cada nova interação com IA que produza artefatos para o projeto, registre aqui:

```markdown
## Prompt XX — <Título curto>

**Data:** DD/MM/YYYY
**Fase:** Planejamento | Desenvolvimento | Testes | Documentação

```
<cole o prompt exato aqui>
```

**Resultado:** <descreva o que foi gerado/alterado>
```
