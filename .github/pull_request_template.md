## O que foi feito
<!-- Descreva objetivamente o que foi implementado, alterado ou corrigido.
     Seja específico: qual função, classe ou comportamento mudou? -->

## Tipo de mudança
- [ ] `feat`     — Nova funcionalidade (RF implementado)
- [ ] `fix`      — Correção de bug
- [ ] `refactor` — Refatoração sem mudança de comportamento externo
- [ ] `docs`     — Atualização de documentação apenas
- [ ] `test`     — Adição ou ajuste de testes
- [ ] `chore`    — Build, config, dependências, CI
- [ ] `perf`     — Melhoria de performance
- [ ] `style`    — Formatação, espaçamento (sem mudança de lógica)

## Checklist
### Código
- [ ] `python salesinsight.py` executa sem erros do início ao fim
- [ ] Nenhuma funcionalidade existente foi quebrada
- [ ] Funções e classes modificadas têm docstring atualizada
- [ ] Nomes de variáveis e funções seguem o padrão em português do projeto

### Git e documentação
- [ ] Título do PR segue Conventional Commits (`type(scope): descrição`)
- [ ] Branch criada a partir de `develop` com nome semântico
- [ ] Commits seguem o padrão semântico (`feat:`, `fix:`, `docs:`, etc.)
- [ ] `docs/BACKLOG.md` atualizado com o novo status da tarefa
- [ ] Documentação em `docs/` ou `specs/` atualizada se necessário

## Impacto no pipeline
- [ ] RF01 — Geração do Dataset
- [ ] RF02 — Inspeção dos Dados
- [ ] RF03 — Limpeza e Tratamento
- [ ] RF04 — Colunas Derivadas
- [ ] RF05 — Métricas Agregadas (groupby)
- [ ] RF06 — Segmentação de Clientes
- [ ] RF07 — Estatísticas NumPy
- [ ] RF08 — Visualizações PNG
- [ ] RF09 — Classe AnalisadorDeVendas
- [ ] RF10 — Herança AnalisadorComProjecao
- [ ] RF11 — Lambda e Higher-Order Functions
- [ ] RF12 — Exportação CSV / JSON
- [ ] RF13 — Limpeza com Regex
- [ ] RF14 — Pipeline Completo (main)