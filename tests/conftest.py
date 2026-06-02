"""
Fixtures compartilhadas entre todos os testes do SalesInsight PY.
"""
import pytest
import pandas as pd
import numpy as np
import sys
import os

# Garante que o módulo salesinsight seja encontrado
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session")
def df_bruto():
    """Retorna o DataFrame bruto gerado com seed=42 (200 linhas)."""
    from salesinsight import gerar_dataset_vendas
    return gerar_dataset_vendas(n_registros=200, seed=42)


@pytest.fixture(scope="session")
def df_limpo(df_bruto):
    """Retorna o DataFrame após limpeza."""
    from salesinsight import limpar_dados
    df, _ = limpar_dados(df_bruto.copy())
    return df


@pytest.fixture(scope="session")
def df_enriquecido(df_limpo):
    """Retorna o DataFrame com colunas derivadas."""
    from salesinsight import criar_colunas_derivadas
    return criar_colunas_derivadas(df_limpo.copy())


@pytest.fixture(scope="session")
def metricas(df_enriquecido):
    """Retorna o dicionário de métricas agregadas."""
    from salesinsight import calcular_metricas
    return calcular_metricas(df_enriquecido)


@pytest.fixture(scope="session")
def clientes(df_enriquecido):
    """Retorna o DataFrame de clientes segmentados."""
    from salesinsight import segmentar_clientes
    return segmentar_clientes(df_enriquecido)


@pytest.fixture(scope="session")
def projecoes(metricas):
    """Retorna lista de projeções de 3 meses."""
    ultimo_mes = int(metricas["por_mes"]["mes"].max())
    return [
        {"mes": ultimo_mes + i, "receita_projetada": round(metricas["total_geral"] / 12 * (1.05 ** i), 2)}
        for i in range(1, 4)
    ]


@pytest.fixture
def output_dir(tmp_path):
    """Retorna um diretório temporário para outputs de testes."""
    graficos = tmp_path / "graficos"
    graficos.mkdir(parents=True)
    return str(tmp_path)


COLUNAS_BRUTO = [
    "id_venda", "data_venda", "cliente", "produto",
    "categoria", "regiao", "quantidade", "preco_unitario"
]

COLUNAS_DERIVADAS = [
    "receita_total", "mes", "mes_nome", "trimestre", "ano", "faixa_receita_item"
]

PRODUTOS = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"]
REGIOES = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
SEGMENTOS = {"Bronze", "Prata", "Ouro"}
