# Pull Request

## Tipo de mudança

<!-- Marque com [x] o que se aplica -->

- [ ] `feat` — Nova funcionalidade
- [ ] `fix` — Correção de bug
- [ ] `refactor` — Refatoração sem mudança de comportamento
- [ ] `docs` — Atualização de documentação
- [ ] `test` — Adição ou ajuste de testes
- [ ] `chore` — Tarefas de build, CI ou manutenção
- [ ] `perf` — Melhoria de performance
- [ ] `style` — Formatação, espaçamento (sem mudança de lógica)

---

## Issue relacionada

> Fecha #<número-da-issue> | Referencia #<número-da-issue>

---

## O que foi feito

<!-- Descreva com clareza o que foi implementado, alterado ou corrigido.
     Seja específico: qual função, módulo ou comportamento mudou? -->

-
-
-

---

## Por que foi feito

<!-- Qual problema resolve ou qual requisito atende?
     Referencie o RF correspondente (ex: RF03 – Limpeza de Dados) -->

---

## Como testar

<!-- Passo a passo para validar a mudança localmente -->

```bash
# Exemplo:
python salesinsight.py
```

1.
2.
3.

---

## Capturas de tela / Saídas esperadas

<!-- Se aplicável: cole saídas de console, gráficos gerados, CSV/JSON exportados -->

<details>
<summary>Clique para expandir</summary>

```
# Cole aqui a saída do console ou path dos arquivos gerados
```

</details>

---

## Checklist antes de abrir o PR

- [ ] O código roda sem erros (`python salesinsight.py`)
- [ ] Não quebro nenhuma funcionalidade já existente
- [ ] Segui as convenções de nomes e estilo do projeto
- [ ] Adicionei ou atualizei docstrings nas funções/classes modificadas
- [ ] Os arquivos de saída (CSV, JSON, PNG) são gerados corretamente
- [ ] Commit(s) seguem o padrão de commits semânticos (`type: descrição`)
- [ ] A branch tem nome semântico (ex: `feat/limpeza-de-dados`)
- [ ] Documentação em `docs/` atualizada, se necessário
- [ ] `BACKLOG.md` atualizado com o status da tarefa

---

## Impacto no pipeline

<!-- Marque quais etapas do pipeline são afetadas -->

- [ ] RF01 — Geração / Carregamento do Dataset
- [ ] RF02 — Inspeção dos Dados
- [ ] RF03 — Limpeza e Tratamento
- [ ] RF04 — Colunas Derivadas
- [ ] RF05 — Métricas Agregadas (groupby)
- [ ] RF06 — Segmentação de Clientes
- [ ] RF07 — Estatísticas NumPy
- [ ] RF08 — Visualizações
- [ ] RF09 — Classe AnalisadorDeVendas
- [ ] RF10 — Herança AnalisadorComProjecao
- [ ] RF11 — Lambda e Funções de Ordem Superior
- [ ] RF12 — Exportação CSV / JSON
- [ ] RF13 — Limpeza com Regex
- [ ] RF14 — Pipeline Completo (main)

---

## Observações adicionais

<!-- Dívidas técnicas, limitações conhecidas, decisões de design, próximos passos -->
