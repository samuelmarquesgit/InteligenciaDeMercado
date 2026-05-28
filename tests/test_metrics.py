"""
RF05 — Testes para cálculo de métricas agregadas.
Valida groupby por mês, top produtos, categoria e região.
"""
import pytest
import pandas as pd


class TestMetricasAgregadas:
    """Testa a função calcular_metricas."""

    def test_retorna_dicionario(self, metricas):
        assert isinstance(metricas, dict)

    def test_chaves_obrigatorias_presentes(self, metricas):
        chaves = {"por_mes", "top_produtos", "por_categoria", "por_regiao"}
        assert chaves.issubset(set(metricas.keys()))

    def test_por_mes_e_dataframe(self, metricas):
        assert isinstance(metricas["por_mes"], pd.DataFrame)

    def test_por_mes_tem_12_linhas(self, metricas):
        """Dataset de 2024 deve ter exatamente 12 meses."""
        assert len(metricas["por_mes"]) == 12

    def test_por_mes_contem_colunas_necessarias(self, metricas):
        assert "mes" in metricas["por_mes"].columns
        assert "receita_total" in metricas["por_mes"].columns

    def test_receita_mensal_sempre_positiva(self, metricas):
        assert (metricas["por_mes"]["receita_total"] > 0).all()

    def test_top_produtos_tem_5_linhas(self, metricas):
        assert len(metricas["top_produtos"]) == 5

    def test_top_produtos_ordenado_por_receita(self, metricas):
        receitas = metricas["top_produtos"]["receita_total"].tolist()
        assert receitas == sorted(receitas, reverse=True)

    def test_por_categoria_e_dataframe(self, metricas):
        assert isinstance(metricas["por_categoria"], pd.DataFrame)

    def test_por_categoria_contem_receita(self, metricas):
        assert "receita_total" in metricas["por_categoria"].columns

    def test_por_regiao_tem_5_linhas(self, metricas):
        """5 regiões no dataset."""
        assert len(metricas["por_regiao"]) == 5

    def test_por_regiao_contem_ticket_medio(self, metricas):
        assert "media_ticket" in metricas["por_regiao"].columns

    def test_soma_por_mes_igual_total_geral(self, metricas, df_enriquecido):
        """Soma das receitas mensais deve igualar receita total."""
        soma_mensal = metricas["por_mes"]["receita_total"].sum()
        total_geral = df_enriquecido["receita_total"].sum()
        assert abs(soma_mensal - total_geral) < 0.01

    def test_por_mes_meses_entre_1_e_12(self, metricas):
        assert metricas["por_mes"]["mes"].between(1, 12).all()

    def test_top_produtos_contem_coluna_produto(self, metricas):
        assert "produto" in metricas["top_produtos"].columns
