"""
RF01 — Testes para geração do dataset sintético.
Valida que gerar_dataset_vendas() produz dados com a estrutura e
os dados sujos esperados para o pipeline de limpeza.
"""
import pytest
import pandas as pd
import numpy as np
from tests.conftest import COLUNAS_BRUTO, PRODUTOS, REGIOES


class TestGeracaoDataset:
    """Testa a função gerar_dataset_vendas."""

    def test_retorna_dataframe(self, df_bruto):
        assert isinstance(df_bruto, pd.DataFrame)

    def test_quantidade_de_registros(self, df_bruto):
        assert len(df_bruto) == 200

    def test_quantidade_de_colunas(self, df_bruto):
        assert df_bruto.shape[1] == 8

    def test_nomes_das_colunas(self, df_bruto):
        assert list(df_bruto.columns) == COLUNAS_BRUTO

    def test_id_venda_sequencial(self, df_bruto):
        assert df_bruto["id_venda"].min() == 1
        assert df_bruto["id_venda"].max() == 200

    def test_produtos_validos(self, df_bruto):
        produtos_no_dataset = set(df_bruto["produto"].str.strip().unique())
        assert produtos_no_dataset.issubset(set(PRODUTOS))

    def test_regioes_validas(self, df_bruto):
        regioes_no_dataset = set(df_bruto["regiao"].unique())
        assert regioes_no_dataset.issubset(set(REGIOES))

    def test_presenca_de_nulos_em_quantidade(self, df_bruto):
        """Dataset deve ter dados sujos: nulos em quantidade."""
        assert df_bruto["quantidade"].isnull().sum() > 0

    def test_presenca_de_nulos_em_preco(self, df_bruto):
        """Dataset deve ter dados sujos: nulos em preco_unitario."""
        assert df_bruto["preco_unitario"].isnull().sum() > 0

    def test_presenca_de_datas_invalidas(self, df_bruto):
        """Dataset deve ter dados sujos: 'DATA INVÁLIDA'."""
        datas_invalidas = df_bruto["data_venda"].astype(str).str.contains("INVÁLIDA|INVALIDA", na=False)
        assert datas_invalidas.sum() > 0

    def test_reproducibilidade_com_seed(self):
        """Mesma seed deve gerar exatamente o mesmo dataset."""
        from salesinsight import gerar_dataset_vendas
        df1 = gerar_dataset_vendas(n_registros=100, seed=42)
        df2 = gerar_dataset_vendas(n_registros=100, seed=42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_seeds_diferentes_geram_datasets_diferentes(self):
        """Seeds diferentes devem gerar datasets diferentes."""
        from salesinsight import gerar_dataset_vendas
        df1 = gerar_dataset_vendas(n_registros=100, seed=42)
        df2 = gerar_dataset_vendas(n_registros=100, seed=99)
        assert not df1.equals(df2)

    def test_n_registros_parametrizavel(self):
        """n_registros deve controlar o tamanho do dataset."""
        from salesinsight import gerar_dataset_vendas
        df = gerar_dataset_vendas(n_registros=50, seed=42)
        assert len(df) == 50

    def test_clientes_no_formato_correto(self, df_bruto):
        """Clientes devem seguir o padrão Cliente_XXX."""
        import re
        padrao = re.compile(r"^Cliente_\d{3}$")
        clientes = df_bruto["cliente"].dropna().unique()
        for cliente in clientes:
            assert padrao.match(cliente.strip()), f"Cliente fora do padrão: {cliente}"

    def test_quantidade_maxima_por_linha(self, df_bruto):
        """Quantidade por venda deve ser no máximo 10."""
        max_qtd = df_bruto["quantidade"].dropna().max()
        assert max_qtd <= 10

    def test_quantidade_minima_por_linha(self, df_bruto):
        """Quantidade por venda deve ser no mínimo 1."""
        min_qtd = df_bruto["quantidade"].dropna().min()
        assert min_qtd >= 1
