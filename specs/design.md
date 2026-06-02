# Design — SalesInsight PY

> Decisões de design de código, interface de console e visualizações

---

## Interface de Console

O SalesInsight PY é uma aplicação CLI. A "interface" é o output formatado no console durante a execução do pipeline.

### Padrão de Formatação

```python
# Cabeçalho principal
print("\n" + "=" * 55)
print("  SALESINSIGHT PY — Pipeline de Análise de Vendas")
print("=" * 55)

# Seções internas (prefixo com RF)
print(f"  [RF01] Dataset gerado: {n} registros | salvo em vendas.csv")
print(f"  [RF03] Limpeza: {inicial} → {final} registros ({removidos} removidos)")
print(f"  [RF07] NumPy stats → média: R$ {media:,.2f} | total: R$ {total:,.2f}")

# Separadores de seção
print("\n" + "=" * 55)
print("  INSPEÇÃO DOS DADOS")
print("=" * 55)

# Resumo executivo
print("\n" + "─" * 45)
print("  RESUMO EXECUTIVO")
print("─" * 45)
print(f"  Receita total  : R$ {total:>15,.2f}")
```

### Convenções de Output

| Tipo | Formato | Exemplo |
|---|---|---|
| Progresso de RF | `[RFxx] mensagem` | `[RF04] Colunas derivadas criadas: [...]` |
| Classe | `[NomeClasse] mensagem` | `[Analisador] Carregado: (200, 8)` |
| Aviso | `⚠` na linha | `quantidade  5 ⚠` |
| Números monetários | `R$ X.XXX,XX` | `R$ 12.345,67` |

---

## Design das Visualizações

### Configuração Global

```python
sns.set_theme(style="whitegrid", palette="muted")
matplotlib.use("Agg")  # Backend sem display
```

### Gráficos Implementados

| # | Título | Tipo | Cor Principal | Arquivo |
|---|---|---|---|---|
| 1 | Receita por Mês — 2024 | Linha + área | `#4C72B0` (azul) | `vendas_por_mes.png` |
| 2 | Top 5 Produtos por Receita | Barras horizontais | `#DD8452` (laranja) | `top_produtos.png` |
| 3 | Distribuição de Receita por Região | Pizza | Paleta padrão matplotlib | `distribuicao_regioes.png` |

### Padrão por Gráfico

```python
fig, ax = plt.subplots(figsize=(W, H))
# ... plot code ...
ax.set_title("Título Descritivo", fontsize=14, fontweight="bold")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
fig.savefig(caminho, dpi=100, bbox_inches="tight")
plt.close(fig)
```

### Parâmetros de Exportação

| Parâmetro | Valor | Motivo |
|---|---|---|
| `dpi` | 100 | Qualidade adequada para apresentação |
| `bbox_inches` | `"tight"` | Evita labels cortados nas bordas |
| `figsize` gráfico 1 | `(12, 5)` | Linha horizontal: largo e estreito |
| `figsize` gráfico 2 | `(10, 5)` | Barras: médio |
| `figsize` gráfico 3 | `(8, 8)` | Pizza: quadrado |

---

## Design das Classes

### Princípios Aplicados

1. **Single Responsibility:** cada método executa uma etapa do pipeline
2. **Method Chaining:** todos os métodos retornam `self`
3. **State Management:** estado armazenado nos atributos da instância
4. **Herança simples:** `AnalisadorComProjecao` estende sem quebrar a interface pai

### Diagrama de Estado

```
Estado inicial (após __init__)
│  self.df_bruto   = None
│  self.df_limpo   = None
│  self.metricas   = None
│  self.clientes   = None
│  self.stats      = None
│
▼ .carregar()
│  self.df_bruto = DataFrame(200 × 8)
│
▼ .limpar()
│  self.df_limpo = DataFrame(~184 × 8)  ← remove ~16 linhas
│
▼ .transformar()
│  self.df_limpo = DataFrame(~184 × 14) ← +6 colunas derivadas
│
▼ .analisar()
│  self.metricas = {por_mes (12), top_produtos (5), por_categoria (4), por_regiao (5)}
│  self.clientes = DataFrame(50 × 3)
│  self.stats    = {media, mediana, std, total, ...}
│
▼ .projetar_tendencia()  [AnalisadorComProjecao]
│  self.projecoes = [{mes: 13, receita_projetada: X}, ...]
│
▼ .resumo()
   Exibe: receita total, clientes únicos, média mensal
```

---

## Design do Dataset Sintético

### Distribuição de Valores

| Campo | Valores | Distribuição |
|---|---|---|
| `produto` | 7 produtos (Notebook, Smartphone, Tablet, Monitor, Teclado, Mouse, Headset) | Uniforme aleatória |
| `categoria` | 4 categorias (Computadores, Mobile, Periféricos, Áudio) | Mapeada ao produto |
| `regiao` | 5 regiões (Sudeste, Sul, Nordeste, Centro-Oeste, Norte) | Uniforme aleatória |
| `cliente` | 50 clientes (Cliente_001 a Cliente_050) | Todos presentes + repetidos |
| `quantidade` | 1–10 | `np.integers(1, 11)` |
| `preco_unitario` | R$ 50 – R$ 5.000 | `np.uniform(50.0, 5000.0)` |
| `data_venda` | 2024-01-01 a 2024-12-31 | `pd.date_range` uniformemente espaçadas |

### Dados Sujos Injetados

| Tipo de sujeira | Quantidade | Coluna afetada |
|---|---|---|
| Nulos | 5 | `quantidade` |
| Nulos | 5 | `preco_unitario` |
| Data inválida | 1 | `data_venda` (linha 0) |
| Espaços extras | 3 | `cliente` |

---

## Design das Exportações

### CSV

```python
df.to_csv(caminho, index=False, encoding="utf-8")
```

Encoding `utf-8` — compatível com Python, Colab e leitores modernos.

### JSON

```python
json.dump(stats, f, ensure_ascii=False, indent=2)
```

Estrutura do `estatisticas_gerais.json`:
```json
{
  "media": 1234.56,
  "mediana": 987.65,
  "desvio_padrao": 456.78,
  "total": 234567.89,
  "minimo": 50.0,
  "maximo": 49999.99,
  "percentil_25": 600.0,
  "percentil_75": 15000.0,
  "media_normalizada": 0.3142,
  "gerado_em": "2026-06-01 10:30:00"
}
```

---

## Decisões de Nomenclatura

| Elemento | Convenção | Exemplo |
|---|---|---|
| Funções | `snake_case` em português, verbo no infinitivo | `gerar_dataset_vendas` |
| Classes | `PascalCase` em português | `AnalisadorDeVendas` |
| Variáveis locais | `snake_case` em português | `df_limpo`, `por_mes` |
| Constantes de módulo | `UPPER_SNAKE_CASE` | `PRODUTOS`, `REGIOES` |
| Parâmetros de função | `snake_case` em português | `n_registros`, `output_dir` |
| Arquivos de saída | `snake_case` em português | `metricas_por_mes.csv` |
