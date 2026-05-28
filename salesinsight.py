"""
SalesInsight PY — Pipeline de Análise de Vendas
Módulo 1, Semana 08 — SCTEC

Executa o pipeline completo:
  RF01  gerar_dataset_vendas      → Dataset sintético com dados sujos
  RF02  inspecionar_dados         → Inspeção e diagnóstico
  RF03  limpar_dados              → Limpeza e normalização de tipos
  RF04  criar_colunas_derivadas   → Feature engineering com np.select
  RF05  calcular_metricas         → Agregações com groupby
  RF06  segmentar_clientes        → Classificação Bronze/Prata/Ouro
  RF07  calcular_estatisticas_numpy → Estatísticas vetorizadas
  RF08  gerar_visualizacoes       → Gráficos PNG (matplotlib/seaborn)
  RF09  AnalisadorDeVendas        → Classe com method chaining
  RF10  AnalisadorComProjecao     → Herança + super() + projeções
  RF11  processar_coluna          → Higher-order function + lambda
  RF12  exportar_resultados       → Exportação CSV e JSON
  RF13  limpar_strings_com_regex  → Limpeza com re.sub e re.compile
  RF14  main                      → Orquestra o pipeline completo
"""

import os
import re
import json
import random
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


# ─── Constantes do domínio ────────────────────────────────────────────────────

PRODUTOS = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"]

REGIOES = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]

CATEGORIAS = {
    "Notebook":    "Computadores",
    "Monitor":     "Computadores",
    "Smartphone":  "Mobile",
    "Tablet":      "Mobile",
    "Teclado":     "Periféricos",
    "Mouse":       "Periféricos",
    "Headset":     "Áudio",
}

NOMES_MESES = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março",    4: "Abril",
    5: "Maio",    6: "Junho",     7: "Julho",     8: "Agosto",
    9: "Setembro",10: "Outubro", 11: "Novembro", 12: "Dezembro",
}


# ─── RF01: Geração do Dataset Sintético ───────────────────────────────────────

def gerar_dataset_vendas(n_registros: int = 200, seed: int = 42) -> pd.DataFrame:
    """RF01 — Gera dataset sintético de vendas com dados sujos intencionais.

    Garante:
    - Exatamente 50 clientes únicos (Cliente_001 a Cliente_050)
    - Datas distribuídas ao longo de 2024
    - Dados sujos: nulos em quantidade/preco, data inválida, espaços em cliente
    - Quantidade entre 1 e 10 por linha
    - Reprodutibilidade total com seed
    """
    rng = np.random.default_rng(seed)
    random.seed(seed)
    np.random.seed(seed)

    clientes_unicos = [f"Cliente_{str(i).zfill(3)}" for i in range(1, 51)]

    # Garante todos os 50 clientes nos primeiros 50 registros
    base = list(clientes_unicos)
    extras = rng.choice(clientes_unicos, size=n_registros - 50, replace=True).tolist()
    todos_clientes = base + extras

    # Embaralha mantendo reprodutibilidade
    perm = rng.permutation(n_registros)
    clientes_col = [todos_clientes[i] for i in perm]

    # Datas distribuídas uniformemente por 2024
    datas_base = pd.date_range("2024-01-01", "2024-12-31", periods=n_registros)
    datas_col = [str(d.date()) for d in datas_base[perm]]

    produtos_col = rng.choice(PRODUTOS, size=n_registros, replace=True).tolist()
    regioes_col  = rng.choice(REGIOES,  size=n_registros, replace=True).tolist()
    qtd_col      = rng.integers(1, 11, size=n_registros).tolist()          # 1–10
    preco_col    = rng.uniform(50.0, 5000.0, size=n_registros).round(2).tolist()
    cat_col      = [CATEGORIAS[p] for p in produtos_col]

    df = pd.DataFrame({
        "id_venda":      range(1, n_registros + 1),
        "data_venda":    datas_col,
        "cliente":       clientes_col,
        "produto":       produtos_col,
        "categoria":     cat_col,
        "regiao":        regioes_col,
        "quantidade":    qtd_col,
        "preco_unitario": preco_col,
    })

    # ── Injeção de dados sujos ──
    dirty = np.random.default_rng(seed + 99)

    # Nulos em quantidade (5 linhas)
    idx_qtd = dirty.choice(n_registros, size=5, replace=False)
    df.loc[idx_qtd, "quantidade"] = np.nan

    # Nulos em preco_unitario (5 linhas diferentes)
    restantes = [i for i in range(n_registros) if i not in idx_qtd]
    idx_preco = dirty.choice(restantes, size=5, replace=False)
    df.loc[idx_preco, "preco_unitario"] = np.nan

    # Uma data inválida
    df.loc[0, "data_venda"] = "DATA INVÁLIDA"

    # Espaços extras em 3 clientes
    idx_espaco = dirty.choice(n_registros, size=3, replace=False)
    for i in idx_espaco:
        df.loc[i, "cliente"] = f"  {df.loc[i, 'cliente']}  "

    return df


# ─── RF02: Inspeção dos Dados ─────────────────────────────────────────────────

def inspecionar_dados(df: pd.DataFrame) -> None:
    """RF02 — Exibe diagnóstico do DataFrame sem modificá-lo."""
    print("\n" + "=" * 55)
    print("  INSPEÇÃO DOS DADOS")
    print("=" * 55)
    print(f"  Shape           : {df.shape[0]} linhas × {df.shape[1]} colunas")
    print(f"  Colunas         : {list(df.columns)}")
    print("\n  Tipos de dados:")
    for col, dtype in df.dtypes.items():
        print(f"    {col:<20} {dtype}")
    print("\n  Valores nulos por coluna:")
    nulos = df.isnull().sum()
    for col, n in nulos.items():
        marca = " ⚠" if n > 0 else ""
        print(f"    {col:<20} {n}{marca}")
    print(f"\n  Total de nulos  : {int(nulos.sum())}")
    print(f"  Duplicatas      : {df.duplicated().sum()}")
    print("=" * 55)


# ─── RF03: Limpeza e Tratamento de Dados ──────────────────────────────────────

def limpar_dados(df: pd.DataFrame) -> tuple:
    """RF03 — Limpa o DataFrame e retorna (df_limpo, relatorio).

    Operações:
    - Remove espaços extras em todas as colunas string
    - Converte data_venda para datetime (remove inválidas)
    - Remove linhas com nulos em quantidade e preco_unitario
    - Converte quantidade para int e preco_unitario para float
    """
    df = df.copy()
    registros_iniciais = len(df)

    # Remove espaços em colunas string
    for col in df.select_dtypes(include=["object", "str"]).columns:
        df[col] = df[col].str.strip()

    # Converte data_venda e remove inválidas
    df["data_venda"] = pd.to_datetime(df["data_venda"], format="mixed", errors="coerce")
    datas_invalidas = int(df["data_venda"].isnull().sum())
    df = df.dropna(subset=["data_venda"])

    # Remove nulos em campos numéricos críticos
    nulos_numericos = int(df[["quantidade", "preco_unitario"]].isnull().any(axis=1).sum())
    df = df.dropna(subset=["quantidade", "preco_unitario"])

    # Conversão de tipos
    df["quantidade"] = df["quantidade"].astype(int)
    df["preco_unitario"] = df["preco_unitario"].astype(float)

    df = df.reset_index(drop=True)

    registros_finais = len(df)
    relatorio = {
        "registros_iniciais":      registros_iniciais,
        "registros_finais":        registros_finais,
        "registros_removidos_total": registros_iniciais - registros_finais,
        "datas_invalidas":         datas_invalidas,
        "nulos_numericos":         nulos_numericos,
    }

    print(f"\n  [RF03] Limpeza: {registros_iniciais} → {registros_finais} registros "
          f"({registros_iniciais - registros_finais} removidos)")

    return df, relatorio


# ─── RF04: Colunas Derivadas com np.select ────────────────────────────────────

def criar_colunas_derivadas(df: pd.DataFrame) -> pd.DataFrame:
    """RF04 — Cria 6 colunas derivadas usando np.select e vetorização pandas."""
    df = df.copy()

    # receita_total
    df["receita_total"] = (df["quantidade"] * df["preco_unitario"]).round(2)

    # mes (int 1–12)
    df["mes"] = df["data_venda"].dt.month

    # mes_nome (string em português)
    df["mes_nome"] = df["mes"].map(NOMES_MESES).astype(object)

    # trimestre (string "Q1"–"Q4") via np.select
    cond_trim = [
        df["mes"].isin([1, 2, 3]),
        df["mes"].isin([4, 5, 6]),
        df["mes"].isin([7, 8, 9]),
        df["mes"].isin([10, 11, 12]),
    ]
    df["trimestre"] = np.select(cond_trim, ["Q1", "Q2", "Q3", "Q4"], default="Q1")

    # ano
    df["ano"] = df["data_venda"].dt.year

    # faixa_receita_item via np.select
    cond_faixa = [
        df["receita_total"] < 500,
        df["receita_total"] < 5000,
        df["receita_total"] >= 5000,
    ]
    escolhas_faixa = ["Baixo Valor", "Médio Valor", "Alto Valor"]
    df["faixa_receita_item"] = np.select(cond_faixa, escolhas_faixa, default="Não Classificado")

    print(f"  [RF04] Colunas derivadas criadas: {['receita_total','mes','mes_nome','trimestre','ano','faixa_receita_item']}")
    return df


# ─── RF05: Métricas Agregadas com groupby ────────────────────────────────────

def calcular_metricas(df: pd.DataFrame) -> dict:
    """RF05 — Calcula métricas de negócio com groupby pandas."""

    # Receita por mês (12 linhas, sempre positivas pois os dados cobrem 2024 inteiro)
    por_mes = (
        df.groupby("mes", as_index=False)["receita_total"]
        .sum()
        .rename(columns={"receita_total": "receita_total"})
        .sort_values("mes")
        .reset_index(drop=True)
    )

    # Top 5 produtos por receita
    top_produtos = (
        df.groupby("produto", as_index=False)["receita_total"]
        .sum()
        .sort_values("receita_total", ascending=False)
        .head(5)
        .reset_index(drop=True)
    )

    # Por categoria
    por_categoria = (
        df.groupby("categoria", as_index=False)["receita_total"]
        .sum()
        .sort_values("receita_total", ascending=False)
        .reset_index(drop=True)
    )

    # Por região com ticket médio
    por_regiao = (
        df.groupby("regiao", as_index=False)
        .agg(
            receita_total=("receita_total", "sum"),
            media_ticket=("receita_total", "mean"),
        )
        .round(2)
        .reset_index(drop=True)
    )

    print(f"  [RF05] Métricas: {len(por_mes)} meses | top 5 produtos | {len(por_regiao)} regiões")
    return {
        "por_mes":      por_mes,
        "top_produtos": top_produtos,
        "por_categoria": por_categoria,
        "por_regiao":   por_regiao,
        "total_geral":  float(df["receita_total"].sum()),
    }


# ─── RF06: Segmentação de Clientes ───────────────────────────────────────────

def segmentar_clientes(df: pd.DataFrame) -> pd.DataFrame:
    """RF06 — Segmenta os 50 clientes em Bronze, Prata e Ouro.

    Thresholds fixos (absolutos em R$):
    - Bronze : total_gasto < 5.000
    - Prata  : 5.000 ≤ total_gasto ≤ 15.000
    - Ouro   : total_gasto > 15.000
    """
    por_cliente = (
        df.groupby("cliente", as_index=False)["receita_total"]
        .sum()
        .rename(columns={"receita_total": "total_gasto"})
        .sort_values("total_gasto", ascending=False)
        .reset_index(drop=True)
    )

    # Classificação via lambda (RF11 + RF06)
    classificar = lambda gasto: (
        "Ouro"   if gasto > 15000 else
        "Prata"  if gasto >= 5000 else
        "Bronze"
    )
    por_cliente["segmento"] = por_cliente["total_gasto"].apply(classificar)

    contagem = por_cliente["segmento"].value_counts().to_dict()
    print(f"  [RF06] Segmentos: {contagem}")
    return por_cliente


# ─── RF07: Estatísticas com NumPy Vetorizado ─────────────────────────────────

def calcular_estatisticas_numpy(df: pd.DataFrame) -> dict:
    """RF07 — Calcula estatísticas descritivas usando funções NumPy."""
    valores = df["receita_total"].to_numpy()
    stats = {
        "media":         float(np.mean(valores)),
        "mediana":       float(np.median(valores)),
        "desvio_padrao": float(np.std(valores)),
        "total":         float(np.sum(valores)),
        "minimo":        float(np.min(valores)),
        "maximo":        float(np.max(valores)),
    }
    print(f"  [RF07] NumPy stats → média: R$ {stats['media']:,.2f} | total: R$ {stats['total']:,.2f}")
    return stats


# ─── RF08: Visualizações ─────────────────────────────────────────────────────

def gerar_visualizacoes(df: pd.DataFrame, metricas: dict,
                        output_dir: str = "outputs/graficos") -> None:
    """RF08 — Gera 3 gráficos PNG com matplotlib e seaborn."""
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="muted")

    # 1. Vendas por mês
    fig, ax = plt.subplots(figsize=(12, 5))
    por_mes = metricas["por_mes"]
    ax.bar(por_mes["mes"], por_mes["receita_total"], color="#4C72B0", edgecolor="white")
    ax.set_title("Receita por Mês — 2024", fontsize=14, fontweight="bold")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Receita (R$)")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan","Fev","Mar","Abr","Mai","Jun",
                         "Jul","Ago","Set","Out","Nov","Dez"])
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "vendas_por_mes.png"), dpi=100)
    plt.close(fig)

    # 2. Top produtos
    fig, ax = plt.subplots(figsize=(10, 5))
    top = metricas["top_produtos"]
    ax.barh(top["produto"], top["receita_total"], color="#DD8452", edgecolor="white")
    ax.set_title("Top 5 Produtos por Receita", fontsize=14, fontweight="bold")
    ax.set_xlabel("Receita Total (R$)")
    ax.invert_yaxis()
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "top_produtos.png"), dpi=100)
    plt.close(fig)

    # 3. Distribuição por região
    fig, ax = plt.subplots(figsize=(8, 8))
    por_regiao = metricas["por_regiao"]
    ax.pie(
        por_regiao["receita_total"],
        labels=por_regiao["regiao"],
        autopct="%1.1f%%",
        startangle=140,
    )
    ax.set_title("Distribuição de Receita por Região", fontsize=14, fontweight="bold")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "distribuicao_regioes.png"), dpi=100)
    plt.close(fig)

    print(f"  [RF08] 3 gráficos salvos em '{output_dir}'")


# ─── RF09: Classe AnalisadorDeVendas com method chaining ─────────────────────

class AnalisadorDeVendas:
    """RF09 — Lê um CSV de vendas e executa o pipeline via method chaining."""

    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.df_bruto = None
        self.df_limpo = None
        self.metricas = None
        self.clientes = None
        self.stats = None

    def carregar(self):
        """Lê o CSV e armazena em df_bruto."""
        self.df_bruto = pd.read_csv(self.caminho_arquivo)
        print(f"  [Analisador] Carregado: {self.df_bruto.shape}")
        return self

    def limpar(self):
        """Aplica limpeza de dados."""
        self.df_limpo, _ = limpar_dados(self.df_bruto)
        return self

    def transformar(self):
        """Cria colunas derivadas."""
        self.df_limpo = criar_colunas_derivadas(self.df_limpo)
        return self

    def analisar(self):
        """Calcula métricas, segmentação e estatísticas."""
        self.metricas = calcular_metricas(self.df_limpo)
        self.clientes = segmentar_clientes(self.df_limpo)
        self.stats = calcular_estatisticas_numpy(self.df_limpo)
        return self

    def resumo(self):
        """Exibe resumo executivo do pipeline."""
        total = self.metricas["total_geral"]
        n_clientes = len(self.clientes) if self.clientes is not None else 0
        print("\n" + "─" * 45)
        print("  RESUMO EXECUTIVO")
        print("─" * 45)
        print(f"  Receita total  : R$ {total:>15,.2f}")
        print(f"  Clientes únicos: {n_clientes}")
        print(f"  Média mensal   : R$ {total / 12:>15,.2f}")
        print("─" * 45)
        return self


# ─── RF10: Herança com AnalisadorComProjecao ─────────────────────────────────

class AnalisadorComProjecao(AnalisadorDeVendas):
    """RF10 — Estende AnalisadorDeVendas com projeção de tendência futura.

    Usa super() para inicializar a classe pai e adiciona:
    - meses_projecao: número de meses a projetar
    - projecoes: lista de dicts {"mes": N, "receita_projetada": X}
    """

    def __init__(self, caminho_arquivo: str, meses_projecao: int = 3):
        super().__init__(caminho_arquivo)
        self.meses_projecao = meses_projecao
        self.projecoes = []

    def projetar_tendencia(self, taxa_crescimento: float = 0.05):
        """Projeta receita mensal com crescimento composto."""
        media_mensal = self.metricas["total_geral"] / 12
        ultimo_mes = int(self.metricas["por_mes"]["mes"].max())

        self.projecoes = [
            {
                "mes": ultimo_mes + i,
                "receita_projetada": round(media_mensal * ((1 + taxa_crescimento) ** i), 2),
            }
            for i in range(1, self.meses_projecao + 1)
        ]

        print(f"  [RF10] Projeção para {self.meses_projecao} meses: "
              f"{[p['receita_projetada'] for p in self.projecoes]}")
        return self


# ─── RF11: Higher-Order Function + Lambda ────────────────────────────────────

def processar_coluna(df: pd.DataFrame, coluna: str, func) -> pd.DataFrame:
    """RF11 — HOF que aplica qualquer função (incluindo lambda) a uma coluna.

    Cria uma nova coluna '{coluna}_transformado' sem modificar a original.
    """
    df = df.copy()
    df[f"{coluna}_transformado"] = df[coluna].apply(func)
    return df


# ─── RF12: Exportação de Resultados ──────────────────────────────────────────

def exportar_resultados(metricas: dict, clientes: pd.DataFrame, stats: dict) -> None:
    """RF12 — Exporta métricas, segmentação e estatísticas em CSV e JSON."""
    os.makedirs("outputs", exist_ok=True)

    metricas["por_mes"].to_csv(
        "outputs/metricas_por_mes.csv", index=False, encoding="utf-8"
    )

    clientes.to_csv(
        "outputs/segmentacao_clientes.csv", index=False, encoding="utf-8"
    )

    with open("outputs/estatisticas_gerais.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print("  [RF12] Exportados: metricas_por_mes.csv | segmentacao_clientes.csv | estatisticas_gerais.json")


# ─── RF13: Limpeza de Strings com Regex ──────────────────────────────────────

def limpar_strings_com_regex(df: pd.DataFrame) -> pd.DataFrame:
    """RF13 — Usa re.compile e re.sub para limpar e validar a coluna 'cliente'.

    Cria:
    - cliente_limpo  : cliente sem caracteres especiais (apenas letras, dígitos, _ e espaço)
    - cliente_valido : bool — True se segue o padrão 'Cliente_NNN'
    """
    df = df.copy()

    padrao_limpeza = re.compile(r"[^a-zA-Z0-9_ ]")
    df["cliente_limpo"] = df["cliente"].apply(
        lambda x: padrao_limpeza.sub("", str(x)).strip()
    )

    padrao_valido = re.compile(r"^Cliente_\d{3}$")
    df["cliente_valido"] = df["cliente_limpo"].apply(
        lambda x: bool(padrao_valido.match(str(x)))
    ).astype(bool)

    validos   = int(df["cliente_valido"].sum())
    invalidos = int((~df["cliente_valido"]).sum())
    print(f"  [RF13] Regex → válidos: {validos} | inválidos: {invalidos}")
    return df


# ─── RF14: Pipeline Principal ─────────────────────────────────────────────────

def main() -> None:
    """RF14 — Executa o pipeline completo de análise de vendas."""
    print("\n" + "=" * 55)
    print("  SALESINSIGHT PY — Pipeline de Análise de Vendas")
    print("=" * 55)

    # RF01 — Geração
    df_bruto = gerar_dataset_vendas(n_registros=200, seed=42)
    df_bruto.to_csv("vendas.csv", index=False, encoding="utf-8")
    print(f"  [RF01] Dataset gerado: {df_bruto.shape[0]} registros | salvo em vendas.csv")

    # RF02 — Inspeção
    inspecionar_dados(df_bruto)

    # RF03 — Limpeza
    df_limpo, relatorio = limpar_dados(df_bruto)

    # RF04 — Feature engineering
    df = criar_colunas_derivadas(df_limpo)

    # RF13 — Limpeza com regex
    df = limpar_strings_com_regex(df)

    # RF11 — HOF + lambda: marca vendas acima de R$ 10.000
    df = processar_coluna(
        df, "receita_total",
        lambda x: "Alto Impacto" if x > 10_000 else "Padrão"
    )

    # RF05–RF07 via AnalisadorComProjecao (RF09 + RF10)
    analisador = AnalisadorComProjecao("vendas.csv", meses_projecao=3)
    (
        analisador
        .carregar()
        .limpar()
        .transformar()
        .analisar()
        .projetar_tendencia()
        .resumo()
    )

    # RF08 — Visualizações
    gerar_visualizacoes(df, analisador.metricas)

    # RF12 — Exportação
    exportar_resultados(analisador.metricas, analisador.clientes, analisador.stats)

    print("\n" + "=" * 55)
    print("  Pipeline concluído com sucesso!")
    print("=" * 55)


if __name__ == "__main__":
    main()
