# Git — Guia Pessoal (Modo Vovô)

> Tudo que você precisa saber pra nunca mais travar no terminal.

---

## 1. Antes de tudo — verifique onde você está

```bash
git status
```
Mostra o estado atual: branch, arquivos modificados, arquivos novos.
**Sempre rode isso antes de fazer qualquer coisa.**

---

## 2. Fluxo completo do zero ao push

```bash
# 1. Veja o que mudou
git status

# 2. Adicione os arquivos que quer commitar
git add nome_do_arquivo.py
# ou adicione tudo de uma vez (cuidado):
git add .

# 3. Faça o commit com mensagem descritiva
git commit -m "feat: adiciona grafico de vendas por mes"

# 4. Suba pro GitHub
git push origin nome-do-branch
```

---

## 3. Branches — crie sempre, nunca commite no main

```bash
# Criar um branch novo e já entrar nele
git checkout -b feat/nome-da-feature

# Ver em qual branch você está
git branch

# Trocar de branch (sem criar)
git checkout nome-do-branch
```

### Prefixos que fazem sentido

| Prefixo | Quando usar |
|---|---|
| `feat/` | nova funcionalidade |
| `fix/` | correção de bug |
| `docs/` | documentação |
| `refactor/` | refatoração sem mudar comportamento |
| `test/` | testes |

---

## 4. Mensagens de commit — o padrão semântico

```
tipo: descrição curta no presente
```

**Exemplos:**
```bash
git commit -m "feat: adiciona segmentacao de clientes"
git commit -m "fix: corrige calculo de receita nula"
git commit -m "docs: atualiza README com instrucoes de execucao"
git commit -m "refactor: simplifica funcao de limpeza"
```

---

## 5. Ver o histórico

```bash
# Histórico resumido (mais útil)
git log --oneline

# Histórico completo com datas e autores
git log

# Ver o que mudou em cada arquivo
git diff
```

---

## 6. Corrigir antes de commitar

```bash
# Tirar um arquivo do stage (desfaz o git add)
git restore --staged nome_do_arquivo.py

# Descartar mudanças no arquivo (CUIDADO — sem volta)
git restore nome_do_arquivo.py
```

---

## 7. Sincronizar com o repositório remoto

```bash
# Baixar as atualizações do GitHub sem sobrescrever o seu trabalho
git pull origin main

# Ver os branches remotos disponíveis
git branch -r
```

---

## 8. Pull Request — o fluxo completo

```bash
# 1. Crie o branch
git checkout -b feat/minha-feature

# 2. Faça suas alterações e commits normalmente

# 3. Suba o branch pro GitHub
git push origin feat/minha-feature

# 4. Acesse o link que aparece no terminal e abra o PR no GitHub
```

O GitHub vai mostrar um link assim:
```
remote: https://github.com/usuario/repo/pull/new/feat/minha-feature
```
Abra esse link no navegador → preenche título e descrição → **Create pull request**.

---

## 9. Situações que travam todo mundo

### "Esqueci em qual branch estou"
```bash
git branch
```
O branch com `*` é onde você está.

### "Fiz commit na branch errada"
Não entre em pânico. Fale com alguém antes de rodar qualquer coisa com `reset`.

### "Meu push foi negado (403)"
Você não tem permissão no repositório. Pede pro dono te adicionar como colaborador em:
`Settings → Collaborators → Add people`

### "Tem conflito no merge"
O GitHub vai te mostrar os arquivos em conflito. Abre cada um, resolve manualmente, salva, faz `git add` e `git commit`.

---

## 10. Cola rápida — o dia a dia

```bash
git status                          # onde estou?
git checkout -b feat/minha-feature  # novo branch
git add arquivo.py                  # preparar arquivo
git commit -m "feat: descricao"     # registrar
git push origin feat/minha-feature  # subir pro GitHub
git log --oneline                   # ver histórico
git pull origin main                # baixar atualizações
```

---

*Salva esse arquivo. Consulta antes de qualquer operação nova.*
