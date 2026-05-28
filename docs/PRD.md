# PRD — Product Requirements Document
## SalesInsight PY · Pipeline de Análise Preditiva de Vendas

> Versão 1.0 · Última atualização: 27/05/2026

---

## 1. Visão do Produto

### 1.1 Sumário Executivo

O **SalesInsight PY** é um pipeline de análise de dados de vendas desenvolvido 100% em Python, criado como mini-projeto avaliativo do Módulo 01 do curso de IA para Análise Preditiva (SCTEC). O sistema transforma dados brutos de um CSV de vendas em insights acionáveis, segmentações de clientes e projeções de tendência, com exportação de relatórios e visualizações.

### 1.2 Problema

Empresas de varejo acumulam históricos de vendas em CSV mas carecem de ferramentas simples para transformar esses dados em decisões estratégicas. O time de negócios precisa responder rapidamente a perguntas como: *quais produtos lideram a receita? quais regiões performam melhor? há tendência de crescimento para o próximo trimestre?*

### 1.3 Solução

Um pipeline em Python que automatiza o ciclo completo: **ingestão → limpeza → transformação → análise → visualização → exportação**, tornando a análise reproduzível, auditável e portátil (local ou Google Colab).

### 1.4 Público-Alvo

- Analistas de Dados Júnior
- Times de negócio de varejo
- Avaliadores e professores do curso SCTEC

---

## 2. Objetivos e Métricas de Sucesso

| Objetivo | Métrica | Meta |
|---|---|---|
| Cobrir todos os RFs do mini-projeto | Requisitos implementados | 14/14 |
| Código executável sem erros | `python salesinsight.py` roda do início ao fim | 100% |
| Gráficos exportados | Arquivos PNG gerados em `outputs/graficos/` | ≥ 3 |
| Relatórios exportados | CSV e JSON em `outputs/` | ≥ 3 arquivos |
| Nota mínima no projeto | Pontuação | ≥ 7,5 / 10 |
| Commits no GitHub | Histórico de commits | ≥ 5 commits |
| Prazo de entrega | Submissão no AVA | até 08/06/2026 12h |

---

## 3. Requisitos Funcionais

### RF01 — Criar ou Carregar Dataset de Vendas
Gerar sinteticamente um dataset de 200 registros com dados propositalmente sujos (nulos, datas inválidas, strings com espaços). Salvar em `vendas.csv`.

### RF02 — Inspecionar e Descrever os Dados
Exibir no console: shape, colunas, tipos, valores nulos e estatísticas descritivas.

### RF03 — Limpar e Tratar os Dados
Tratar: nulos em `quantidade` e `preco_unitario`, datas inválidas (parse com `errors='coerce'`), espaços extras em strings (`.str.strip()`). Registrar contagem de registros removidos.

### RF04 — Criar Colunas Derivadas
Novas colunas: `receita_total`, `mes`, `mes_nome`, `trimestre`, `ano`, `faixa_receita_item` (via `np.select`).

### RF05 — Métricas Agregadas (groupby)
Receita por mês, top 5 produtos, receita por categoria, receita e ticket médio por região.

### RF06 — Segmentar Clientes
Agrupar por cliente, calcular total gasto, classificar em Bronze / Prata / Ouro com função lambda.

### RF07 — Estatísticas com NumPy
Converter coluna para array NumPy; calcular `mean`, `median`, `std`, `sum`, `percentile`; demonstrar broadcasting e operação vetorizada.

### RF08 — Visualizações com Matplotlib e Seaborn
≥ 3 gráficos: linha (receita/mês), barras (top produtos), boxplot (distribuição por região). Exportar como PNG com `dpi=150`.

### RF09 — Classe AnalisadorDeVendas
Classe com `__init__`, atributos de instância (`self.df_bruto`, `self.df_limpo`, `self.metricas`, etc.) e métodos encadeáveis (`.carregar()`, `.limpar()`, `.transformar()`, `.analisar()`, `.visualizar()`, `.exportar_relatorio()`).

### RF10 — Herança AnalisadorComProjecao
Subclasse de `AnalisadorDeVendas` com `super().__init__()`, novo atributo `meses_projecao` e método `.projetar_tendencia()` (média móvel simples dos últimos 3 meses).

### RF11 — Lambda e Funções de Ordem Superior
≥ 2 usos distintos de lambda; função `processar_coluna(df, coluna, func)` que recebe outra função como argumento.

### RF12 — Ler e Escrever CSV e JSON
Exportar `metricas_por_mes.csv`, `segmentacao_clientes.csv`, `estatisticas_gerais.json`; ler JSON exportado para confirmar integridade.

### RF13 — Expressões Regulares (re)
`re.sub()` para limpar strings de clientes; `re.compile()` com padrão para validar formato `Cliente_XXX`.

### RF14 — Pipeline Completo (main)
Bloco `if __name__ == "__main__":` com função `main()` que executa todo o pipeline de ponta a ponta via `AnalisadorComProjecao`.

---

## 4. Requisitos Não Funcionais

| ID | Requisito | Critério |
|---|---|---|
| RNF01 | Portabilidade | Executa em Google Colab e localmente no Windows/Linux |
| RNF02 | Reprodutibilidade | `random.seed(42)` e `np.random.seed(42)` garantem saídas consistentes |
| RNF03 | Legibilidade | Funções documentadas com docstrings; nomes em português |
| RNF04 | Modularidade | Cada RF em função separada; pipeline orquestrado pela classe |
| RNF05 | Rastreabilidade | Commits semânticos por funcionalidade; branches descritivas |

---

## 5. Fora de Escopo (v1.0)

- Machine Learning real (modelos sklearn, redes neurais)
- Interface gráfica ou dashboard interativo (Streamlit, Dash)
- Consumo de API REST externa
- Banco de dados (SQL/NoSQL)
- Testes automatizados (pytest)
- CI/CD pipeline

---

## 6. Dependências e Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Biblioteca não instalada localmente | Médio | Alto | `requirements.txt` + instruções no README |
| Dataset gerado com seed diferente | Baixo | Médio | `seed=42` hardcoded no código |
| Prazo apertado (08/06/2026) | Médio | Alto | Kanban com priorização por RF obrigatório |
| Gráficos não gerados no Colab | Baixo | Médio | Usar `%matplotlib inline` ou `plt.savefig()` |

---

## 7. Entregáveis Obrigatórios

- [ ] `salesinsight.py` — pipeline completo
- [ ] `vendas.csv` — dataset (gerado ou externo)
- [ ] `README.md` — documentação do projeto
- [ ] Repositório público no GitHub
- [ ] Quadro Kanban com tarefas
- [ ] Vídeo de até 5 minutos
- [ ] Links submetidos no AVA até 08/06/2026 às 12h
