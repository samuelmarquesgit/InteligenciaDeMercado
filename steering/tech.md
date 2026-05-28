# Steering — Tecnologia

> Decisões técnicas, stack e princípios de implementação

---

## Stack Definitiva

| Camada | Tecnologia | Versão mínima | Justificativa |
|---|---|---|---|
| Linguagem | Python | 3.10+ | Requisito do mini-projeto |
| Dados tabulares | pandas | 2.0 | API moderna, `pd.to_datetime(errors='coerce')` |
| Computação numérica | NumPy | 1.24 | `np.select`, broadcasting, vetorização |
| Visualização | Matplotlib | 3.7 | Base para `plt.savefig()` |
| Visualização | Seaborn | 0.13 | API de alto nível para `barplot`, `boxplot` |
| Stdlib | re, json, datetime, os, random | Built-in | Sem dependências extras |

---

## Decisões Técnicas

### Por que um arquivo único (`salesinsight.py`)?
O requisito do mini-projeto especifica `salesinsight.py` como arquivo principal. Para projetos reais, o pipeline seria modularizado em `src/pipeline/`, `src/models/`, etc.

### Por que `seed=42`?
Garante **reprodutibilidade total**: qualquer pessoa que execute `python salesinsight.py` obterá exatamente o mesmo dataset, mesmos resultados e mesmos gráficos. Essencial para avaliação.

### Por que `np.select` em vez de `df.apply(lambda)`?
`np.select` opera sobre arrays NumPy de forma **vetorizada**, sem loop Python. Para classificações condicionais em DataFrames grandes, é 10–100x mais rápido que `apply`.

### Por que `pd.to_datetime(errors='coerce')` em vez de tratamento manual?
É a abordagem idiomática do pandas para datas inválidas. Converte automaticamente para `NaT` (Not a Time), que pode ser tratado com `.dropna()`.

### Por que `encoding="utf-8-sig"` nos CSVs?
O BOM (Byte Order Mark) do `utf-8-sig` garante que o Excel no Windows abra o arquivo sem problemas de encoding com caracteres especiais (ã, ç, ê, etc.).

### Por que method chaining na classe?
Permite pipeline fluente e legível:
```python
analisador.carregar().limpar().transformar().analisar().projetar_tendencia().visualizar()
```
Em vez de:
```python
analisador.carregar()
analisador.limpar()
analisador.transformar()
# ...
```

### Por que herança em vez de composição para `AnalisadorComProjecao`?
Herança é um **requisito explícito** do RF10. Em termos de design puro, composição seria mais flexível, mas herança demonstra o conceito de POO exigido.

---

## Padrões de Código

### Docstrings
```python
def limpar_dados(df):
    """
    Limpa e trata o DataFrame de vendas.
    Retorna o DataFrame limpo e um relatório de limpeza.
    """
```

### Typing (opcional mas recomendado)
```python
import pandas as pd
from typing import dict, tuple

def limpar_dados(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
```

### f-strings para formatação
```python
print(f"  Receita total anual:    R$ {receita:,.2f}")
print(f"  Registros removidos:    {n_removidos}")
```

### `os.makedirs(exist_ok=True)` para criar pastas
```python
os.makedirs("outputs/graficos", exist_ok=True)
```

---

## Limites Técnicos (v1.0)

| Limite | Valor | Razão |
|---|---|---|
| Registros no dataset | 200 | Exercício didático |
| Meses de projeção | 3 | Configurável via parâmetro |
| Produtos distintos | 7 | Dataset sintético |
| Clientes | 50 | Dataset sintético |
| Gráficos mínimos | 3 | Requisito RF08 |
| Commits mínimos | 5 | Requisito da disciplina |

---

## Ambiente de Desenvolvimento Recomendado

```
VS Code
  ├── Extensão: Python (Microsoft)
  ├── Extensão: Pylance
  ├── Extensão: GitLens (opcional)
  └── Extensão: Python Indent (opcional)

Google Colab (alternativa)
  └── Todas as libs pré-instaladas
```

---

## Checklist de Qualidade de Código

- [ ] Todas as funções têm docstring
- [ ] Nomes de variáveis em português e descritivos
- [ ] `seed=42` presente em `random.seed` e `np.random.seed`
- [ ] `plt.close()` após cada `plt.savefig()`
- [ ] `os.makedirs(exist_ok=True)` antes de salvar arquivos
- [ ] Sem loops Python onde `np.select` ou vetorização são possíveis
- [ ] `encoding="utf-8-sig"` nos CSVs exportados
- [ ] `ensure_ascii=False` no `json.dump`
- [ ] Bloco `if __name__ == "__main__":` no final
