"""
RF04 — Testes para criação de colunas derivadas.
Valida criação de receita_total, mes, trimestre, ano e faixa_receita_item.
"""
import pytest
import pandas as pd
import numpy as np
from tests.conftest import COLUNAS_DERIVADAS


class TestColunasDerivadas:
    """Testa a função criar_colunas_derivadas."""

    def test_colunas_derivadas_criadas(self, df_enriquecido):
        for col in COLUNAS_DERIVADAS:
            assert col in df_enriquecido.columns, f"Coluna '{col}' não encontrada"

    def test_receita_total_e_produto_quantidade_x_preco(self, df_enriquecido):
        calculado = df_enriquecido["quantidade"] * df_enriquecido["preco_unitario"]
        pd.testing.assert_series_equal(
            df_enriquecido["receita_total"].round(2),
            calculado.round(2),
            check_names=False
        )

    def test_receita_total_sempre_positiva(self, df_enriquecido):
        assert (df_enriquecido["receita_total"] > 0).all()

    def test_mes_entre_1_e_12(self, df_enriquecido):
        assert df_enriquecido["mes"].between(1, 12).all()

    def test_trimestre_valores_validos(self, df_enriquecido):
        valores_validos = {"Q1", "Q2", "Q3", "Q4"}
        assert set(df_enriquecido["trimestre"].unique()).issubset(valores_validos)

    def test_ano_igual_a_2024(self, df_enriquecido):
        """Dataset sintético usa datas de 2024."""
        assert (df_enriquecido["ano"] == 2024).all()

    def test_faixa_receita_item_valores_validos(self, df_enriquecido):
        valores_validos = {"Baixo Valor", "Médio Valor", "Alto Valor", "Não Classificado"}
        assert set(df_enriquecido["faixa_receita_item"].unique()).issubset(valores_validos)

    def test_faixa_baixo_valor_menor_que_500(self, df_enriquecido):
        baixo = df_enriquecido[df_enriquecido["faixa_receita_item"] == "Baixo Valor"]
        if len(baixo) > 0:
            assert (baixo["receita_total"] < 500).all()

    def test_faixa_alto_valor_maior_ou_igual_5000(self, df_enriquecido):
        alto = df_enriquecido[df_enriquecido["faixa_receita_item"] == "Alto Valor"]
        if len(alto) > 0:
            assert (alto["receita_total"] >= 5000).all()

    def test_sem_nulos_em_receita_total(self, df_enriquecido):
        assert df_enriquecido["receita_total"].isnull().sum() == 0

    def test_sem_nulos_em_mes(self, df_enriquecido):
        assert df_enriquecido["mes"].isnull().sum() == 0

    def test_mes_nome_e_string(self, df_enriquecido):
        assert pd.api.types.is_object_dtype(df_enriquecido["mes_nome"])

    def test_trimestre_e_consistente_com_mes(self, df_enriquecido):
        """Q1 deve conter apenas meses 1, 2, 3."""
        q1 = df_enriquecido[df_enriquecido["trimestre"] == "Q1"]
        if len(q1) > 0:
            assert q1["mes"].isin([1, 2, 3]).all()

    def test_q4_contem_meses_10_11_12(self, df_enriquecido):
        q4 = df_enriquecido[df_enriquecido["trimestre"] == "Q4"]
        if len(q4) > 0:
            assert q4["mes"].isin([10, 11, 12]).all()

    def test_dataframe_original_tem_mais_colunas(self, df_limpo, df_enriquecido):
        """df_enriquecido deve ter mais colunas que df_limpo."""
        assert df_enriquecido.shape[1] > df_limpo.shape[1]
