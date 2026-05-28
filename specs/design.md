# Design — SalesInsight PY

> Decisões de design de código e interface de usuário (console)

---

## Interface de Console

O SalesInsight PY é uma aplicação CLI (Command Line Interface). A "interface" é o output formatado no console durante a execução do pipeline.

### Padrão de Formatação dos Títulos de Seção

```python
# Seções principais
print("\n" + "="*60)
print("   SALESINSIGHT PY – Pipeline de Análise de Dados de Vendas")
print("="*60)

# Subsections
print("\n=== INSPEÇÃO INICIAL DO DATASET ===")
print("\n=== RELATÓRIO DE LIMPEZA ===")
print("\n=== COLUNAS DERIVADAS CRIADAS ===")
print("\n=== RECEITA POR MÊS ===")
print("\n=== TOP 5 PRODUTOS POR RECEITA ===")
print("\n=== SEGMENTAÇÃO DE CLIENTES ===")
print("\n=== ESTATÍSTICAS COM NUMPY ===")
print("\n=== LIMPEZA COM REGEX ===")
print("\n=== PROJEÇÃO DE TENDÊNCIA (Média Móvel Simples) ===")
print("\n=== DETALHAMENTO DAS PROJEÇÕES ===")
print("\n=== VISUALIZAÇÕES GERADAS COM SUCESSO ===")
```

### Padrão de Mensagens de Status

```python
# Informações de carregamento (classe)
print(f"[AnalisadorDeVendas] Arquivo carregado: {self.caminho_arquivo}")
print(f"[AnalisadorDeVendas] Relatório exportado: {caminho}")

# Avisos
print("[AVISO] Rode .analisar() antes de projetar.")

# Info
print("\n[INFO] Gerando dataset sintético...")

# Conclusão
print("\n[CONCLUÍDO] Pipeline finalizado com sucesso!")
```

---

## Design das Visualizações

### Paleta de Cores

| Gráfico | Cor Principal | Lib |
|---|---|---|
| Linha receita/mês | `#2196F3` (azul) + fill alpha 0.15 | Matplotlib |
| Barras top produtos | `"Blues_d"` | Seaborn |
| Boxplot regiões | `"Set2"` | Seaborn |

### Configurações Globais

```python
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12
```

### Padrão por Gráfico

```python
fig, ax = plt.subplots()
# ... plot ...
ax.set_title("Título Descritivo (Ano)")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
plt.tight_layout()
plt.savefig(caminho, dpi=150)
plt.close()
print(f"  Gráfico exportado: {caminho}")
```

---

## Design das Classes

### Princípios Aplicados

1. **Single Responsibility:** cada método faz uma coisa
2. **Method Chaining:** todos os métodos retornam `self`
3. **State Management:** estado do pipeline armazenado nos atributos da instância
4. **Herança simples:** `AnalisadorComProjecao` estende sem quebrar a interface de `AnalisadorDeVendas`

### Diagrama de Estado da Classe

```
Estado inicial (após __init__)
│  self.df_bruto = None
│  self.df_limpo = None
│  self.metricas = {}
│  self.clientes = None
│  self.relatorio_limpeza = {}
│
▼ .carregar()
│  self.df_bruto = DataFrame(200 × 8)
│
▼ .limpar()
│  self.df_limpo = DataFrame(~180 × 8)
│  self.relatorio_limpeza = {registros_removidos: ...}
│
▼ .transformar()
│  self.df_limpo = DataFrame(~180 × 14)  ← +6 colunas
│
▼ .analisar()
│  self.metricas = {por_mes, top_produtos, por_categoria, por_regiao}
│  self.clientes = DataFrame(50 × 3)
│
▼ .visualizar()
│  3 PNG gerados em outputs/graficos/
│
▼ .exportar_relatorio()
   1 CSV gerado em outputs/
```

---

## Design do Dataset Sintético

### Regras de Geração de Dados Sujos

```python
# 5% de nulos em quantidade
if random.random() < 0.05:
    quantidade = None

# 4% de nulos em preco_unitario
if random.random() < 0.04:
    preco = None

# 3% de strings com espaço extra
if random.random() < 0.03:
    produto = "  " + produto

# 2% de datas inválidas
"DATA INVÁLIDA" if random.random() <= 0.02 else data.strftime("%Y-%m-%d")
```

### Distribuição de Valores

| Campo | Valores | Distribuição |
|---|---|---|
| produto | 7 produtos | Uniforme |
| categoria | 3 categorias | Mapeada ao produto |
| regiao | 5 regiões | Uniforme |
| cliente | 50 clientes | Uniforme |
| quantidade | 1–10 | randint uniforme |
| preco | base × [0.85, 1.15] | Uniforme contínua |
| data | 2024-01-01 a 2024-12-31 | Aleatória |

---

## Estrutura de Saídas

### CSV

Exportados com `encoding="utf-8-sig"` para compatibilidade com Excel no Windows.

### JSON

```json
{
    "media": 1234.56,
    "mediana": 987.65,
    "desvio_padrao": 456.78,
    "total": 234567.89
}
```

### PNG

- Resolução: `dpi=150` (qualidade adequada para apresentação)
- Formato: `figsize=(12, 6)` — paisagem
- `plt.tight_layout()` antes de salvar (evita labels cortados)
