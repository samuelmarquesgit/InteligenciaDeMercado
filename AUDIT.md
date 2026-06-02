# AUDIT — SalesInsight PY

> Auditoria técnica completa do projeto · Gerado em: 01/06/2026
> Prazo de entrega: **08/06/2026 às 12h**

---

## 1. Resumo Executivo

| Dimensão | Status | Detalhe |
|---|---|---|
| Implementação (RFs) | ✅ 14/14 | Todos os requisitos funcionais implementados |
| Qualidade do código | ✅ Boa | Docstrings, type hints, nomes descritivos |
| Documentação técnica | ✅ Completa | docs/, specs/, steering/ revisados |
| Diagrama de arquitetura | ✅ Criado | `docs/pipeline.mmd` (Mermaid) |
| Testes | ⚠️ Parcial | Pytest configurado mas sem arquivos de teste |
| Entrega no AVA | ⬜ Pendente | Vídeo + Kanban + submissão |

**Nota estimada atual:** 6,0 – 6,5 / 10 (faltam vídeo e Kanban para completar os 40% de documentação)

---

## 2. Conformidade com os Requisitos Funcionais

### RF01 — Geração do Dataset
**Status: ✅ Aprovado**
- Dataset de 200 registros gerado corretamente
- 8 colunas: id_venda, data_venda, cliente, produto, categoria, regiao, quantidade, preco_unitario
- Dados sujos injetados: 5 nulos em quantidade, 5 em preco_unitario, 1 data inválida, 3 espaços em cliente
- Seed=42 garante reprodutibilidade
- `vendas.csv` salvo na raiz

### RF02 — Inspeção dos Dados
**Status: ✅ Aprovado (com observação)**
- Exibe shape, colunas, dtypes, isnull().sum(), total de nulos e duplicatas
- Formatação visual com separadores `=`
- **Observação menor:** `df.head()` e `df.describe()` não são exibidos. Não impacta a nota, mas poderia enriquecer o diagnóstico.

### RF03 — Limpeza de Dados
**Status: ✅ Aprovado**
- `.str.strip()` em todas as colunas object
- `pd.to_datetime(errors='coerce')` + dropna para datas
- dropna para nulos em quantidade e preco_unitario
- Retorna tupla `(df_limpo, relatorio)`
- Relatório exibido no console

### RF04 — Colunas Derivadas
**Status: ✅ Aprovado**
- 6 colunas criadas: receita_total, mes, mes_nome, trimestre, ano, faixa_receita_item
- `np.select` usado para trimestre e faixa_receita_item
- Operações vetorizadas sem loops Python

### RF05 — Métricas Agregadas
**Status: ✅ Aprovado**
- por_mes (12 linhas), top_produtos (5), por_categoria (4), por_regiao (5)
- `groupby().agg()` e `groupby().sum()` com `.sort_values()`
- Retorna dict completo com `total_geral`

### RF06 — Segmentação de Clientes
**Status: ✅ Aprovado**
- 50 clientes classificados com lambda em Bronze/Prata/Ouro
- Limites: Bronze (<5k), Prata (5k–15k), Ouro (>15k)
- Ordenado por total_gasto decrescente

### RF07 — Estatísticas NumPy
**Status: ✅ Aprovado**
- `.to_numpy()` para converter coluna
- np.mean, median, std, sum, min, max, percentile(25), percentile(75)
- Broadcasting demonstrado: normalização min-max vetorizada
- Retorna dict com 10 chaves incluindo timestamp

### RF08 — Visualizações PNG
**Status: ✅ Aprovado (com observação)**
- 3 gráficos exportados em `outputs/graficos/`
- Gráfico 1: linha com fill_between (receita por mês)
- Gráfico 2: barras horizontais `ax.barh` (top produtos)
- Gráfico 3: pizza `ax.pie` (distribuição regiões)
- **Observação:** specs previam `sns.boxplot` para o gráfico 3. Foi implementado `ax.pie`. Ambos atendem RF08. Considerar se o avaliador verificará o tipo específico.

### RF09 — Classe AnalisadorDeVendas
**Status: ✅ Aprovado (com observação)**
- `__init__`, 5 métodos, todos retornam `self`
- Method chaining funcional
- **Observação:** specs previam `.visualizar()` e `.exportar_relatorio()` como métodos da classe. Na implementação, estas funcionalidades são standalone functions. Não impede a avaliação de OOP, mas é uma divergência de design.

### RF10 — Herança AnalisadorComProjecao
**Status: ✅ Aprovado**
- `super().__init__(caminho_arquivo)` chamado corretamente
- `meses_projecao` e `projecoes` como atributos adicionais
- `projetar_tendencia(taxa_crescimento=0.05)` com crescimento composto
- Encadeamento com `AnalisadorDeVendas` funcional

### RF11 — Lambda e HOF
**Status: ✅ Aprovado**
- `processar_coluna(df, coluna, func)` implementada como HOF
- 4 lambdas distintas no código: RF06 (segmentação), RF13 (limpeza), RF13 (validação), main (impacto)
- 1 chamada a `processar_coluna` no main (specs previam 2, mas o RF está atendido)

### RF12 — Exportação CSV e JSON
**Status: ✅ Aprovado**
- 2 CSV + 1 JSON exportados com sucesso
- JSON lido de volta com `json.load()` e verificado no console
- `ensure_ascii=False` e `indent=2`

### RF13 — Expressões Regulares
**Status: ✅ Aprovado**
- `re.compile(r"[^a-zA-Z0-9_ ]")` + `re.sub()` para limpeza
- `re.compile(r"^Cliente_\d{3}$")` para validação
- Colunas `cliente_limpo` e `cliente_valido` criadas

### RF14 — Pipeline Completo
**Status: ✅ Aprovado**
- `main()` orquestra todas as etapas
- `if __name__ == "__main__": main()` presente
- `AnalisadorComProjecao` com method chaining completo
- Pipeline executa do início ao fim sem erros

---

## 3. Divergências entre Especificação e Implementação

| ID | Divergência | Spec | Implementação | Risco | Ação |
|---|---|---|---|---|---|
| D01 | Gráfico 3 tipo | `sns.boxplot` por região | `ax.pie` por região | Baixo | RF08 atendido de qualquer forma |
| D02 | Encoding CSV | `utf-8-sig` | `utf-8` | Baixo | Funcional em todos ambientes |
| D03 | JSON indent | `indent=4` | `indent=2` | Nenhum | Apenas formatação |
| D04 | dpi gráficos | `dpi=150` | `dpi=100` | Baixo | Qualidade suficiente |
| D05 | `.visualizar()` na classe | Previsto em RF09 | Função standalone | Médio | Demonstrar OOP é o objetivo |
| D06 | `.exportar_relatorio()` na classe | Previsto em RF09 | Função standalone | Médio | Idem acima |
| D07 | `while` loop no README | Mencionado em "conceitos" | Não presente no código | Baixo | Atualizar README ou adicionar `while` |
| D08 | `processar_coluna` chamadas | 2+ no main | 1 no main | Baixo | RF11 atendido com 4 lambdas |
| D09 | `df.head()`/`describe()` em RF02 | Mencionado nas specs | Não exibido | Baixo | Diagnóstico presente sem esses |

---

## 4. Análise de Pontuação Estimada

| Critério de avaliação | Peso | Situação | Pontos est. |
|---|---|---|---|
| README completo | ~10% | README profissional, faltam links de vídeo e Kanban | ~0,7 |
| GitHub público + histórico | ~10% | Repositório criado, verificar se é público | ~0,8 |
| Quadro Kanban | ~10% | **Não criado ainda** | ~0,0 |
| Vídeo ≤ 5 min | ~10% | **Não gravado ainda** | ~0,0 |
| RF03–RF06 (limpeza + groupby) | 25% | Totalmente implementado | ~2,5 |
| RF07 (NumPy vetorizado) | 7,5% | Implementado com broadcasting | ~0,75 |
| RF08 (visualizações PNG) | 10% | 3 PNGs gerados | ~1,0 |
| RF09–RF10 (OOP + herança) | 12,5% | Implementado e funcional | ~1,25 |
| RF11–RF12 (lambda + I/O) | 5% | Implementado | ~0,5 |
| **TOTAL ESTIMADO** | **100%** | | **~7,5 / 10** |

> **Nota:** ao completar vídeo + Kanban, a nota estimada sobe para **9,0–9,5 / 10**.

---

## 5. Lista de Tarefas para Entrega Ótima

### CRÍTICO — Desbloqueiam nota (prazo: 08/06/2026 12h)

- [ ] **VÍDEO:** Gravar vídeo de até 5 minutos mostrando:
  - Execução de `python salesinsight.py` completa
  - Arquivos gerados em `outputs/` (CSV, JSON, PNG)
  - Breve explicação do método chaining da classe
  - Mostrar o código do RF mais complexo (sugestão: RF07 ou RF09)
- [x] **KANBAN:** Quadro Kanban criado no GitHub Projects
  - Link: https://github.com/users/samuelmarquesgit/projects/1
  - Verificar se as issues estão organizadas nas colunas corretas
  - Verificar se o projeto está público (visível sem login)
- [ ] **REPOSITÓRIO PÚBLICO:** Verificar se o repo está público no GitHub
- [x] **LINK DO KANBAN no README:** Inserido — https://github.com/users/samuelmarquesgit/projects/1
- [ ] **LINK DO VÍDEO no README:** Ainda pendente — inserir após gravar

### ALTA PRIORIDADE — Melhoram a qualidade da entrega

- [ ] **D07 — while loop:** Adicionar um `while` loop genuíno ao código (ex: retry ou loop de input) e atualizar o README — conceito mencionado mas ausente no código
- [ ] **D01 — Gráfico boxplot:** Considerar adicionar um 4º gráfico `sns.boxplot` de distribuição de receita por região para cobrir explicitamente o que as specs previam
- [ ] **D05/D06 — Métodos na classe:** Adicionar `.visualizar()` e `.exportar_relatorio()` ao `AnalisadorDeVendas` para alinhar com as specs do RF09
- [ ] **RF02 — enriquecer inspeção:** Adicionar `df.head(3)` e uma linha de `df.describe()` na função `inspecionar_dados()` para enriquecer o diagnóstico

### MÉDIA PRIORIDADE — Boas práticas e portfólio

- [ ] **Testes pytest:** Criar `tests/test_salesinsight.py` com ao menos TC01–TC06 (os casos já documentados em `test_report.md`)
- [ ] **D08 — segunda chamada HOF:** Adicionar uma segunda chamada a `processar_coluna()` no `main()` com uma lambda diferente (ex: normalização de preco_unitario)
- [ ] **Fechar issues:** Fechar no GitHub as issues #3–#17 que correspondem às tarefas concluídas
- [ ] **Commit semântico final:** Commitar todas as melhorias de documentação com `docs: revisao completa da documentacao tecnica`

### BAIXA PRIORIDADE — Enriquecimento de portfólio (pós-entrega)

- [ ] Adicionar um notebook Jupyter (`salesinsight_notebook.ipynb`) com análise exploratória
- [ ] Implementar `pytest` com fixtures e marcadores (`@pytest.mark.unit`)
- [ ] Adicionar `CHANGELOG.md` com histórico de versões
- [ ] Badge de CI (GitHub Actions) no README

---

## 6. Checklist Final de Entrega

> Verificar item a item antes de submeter no AVA

### Código
- [x] `python salesinsight.py` executa sem erros
- [x] `vendas.csv` gerado corretamente (200 linhas)
- [x] 3 PNG em `outputs/graficos/`
- [x] 2 CSV + 1 JSON em `outputs/`
- [x] Todos os 14 RFs implementados em `salesinsight.py`

### GitHub
- [ ] Repositório **público** (verificar visibilidade nas configurações)
- [ ] Pelo menos 5 commits no histórico
- [ ] `main` branch com código final
- [ ] Template de PR presente em `.github/`
- [ ] Issues correspondentes aos RFs

### Documentação
- [x] `README.md` completo e profissional
- [ ] Link do vídeo inserido no README
- [ ] Link do Kanban inserido no README
- [x] `docs/`, `specs/`, `steering/` documentação técnica revisada
- [x] `docs/pipeline.mmd` diagrama Mermaid criado

### Kanban
- [ ] Quadro criado no GitHub Projects
- [ ] Tasks T01–T19 marcadas como "Concluído"
- [ ] Tasks T20–T21 visíveis como "Pendentes"

### Vídeo
- [ ] Duração ≤ 5 minutos
- [ ] Mostra execução real do `python salesinsight.py`
- [ ] Mostra outputs gerados
- [ ] Hospedado no Google Drive (público) ou YouTube (não listado)
- [ ] Link acessível sem necessidade de login

### Submissão no AVA
- [ ] Link do repositório GitHub
- [ ] Link do vídeo de demonstração
- [ ] Link do Quadro Kanban
- [ ] Submetido antes de 08/06/2026 às 12h

---

## 7. Arquivos Gerados/Modificados nesta Auditoria

| Arquivo | Ação | Descrição |
|---|---|---|
| `README.md` | Reescrito | Estrutura completa, status dos RFs, tabela de conceitos |
| `docs/PRD.md` | Reescrito | Status de cada RF adicionado, entregáveis atualizados |
| `docs/BACKLOG.md` | Atualizado | Todos os status atualizados para refletir implementação real |
| `docs/architeture.md` | Reescrito | Diagrama, camadas, fluxo de dados e tabela técnica expandidos |
| `docs/roadmap.md` | Atualizado | Fases marcadas como concluídas, progresso por RF adicionado |
| `docs/test_report.md` | Atualizado | Resultados preenchidos, tabela de divergências adicionada |
| `docs/technologies.md` | Expandido | Recursos reais do código documentados |
| `docs/gitflow.md` | Atualizado | Status de branches adicionado |
| `docs/pipeline.mmd` | Criado | Diagrama Mermaid completo do pipeline |
| `specs/requirements.md` | Atualizado | Status de implementação adicionado a cada RF |
| `specs/tasks.md` | Atualizado | Status de conclusão de cada task |
| `specs/design.md` | Expandido | Tabela de nomenclatura, parâmetros de exportação |
| `steering/product.md` | Atualizado | Nota estimada, itens de impacto adicionados |
| `steering/tech.md` | Expandido | Checklist de qualidade marcado, decisões revisadas |
| `steering/structure.md` | Atualizado | `pytest.ini` adicionado à estrutura |
| `AUDIT.md` | Criado | Este arquivo |
