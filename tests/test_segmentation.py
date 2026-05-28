"""
RF06 — Testes para segmentação de clientes.
Valida classificação Bronze/Prata/Ouro usando lambda.
"""
import pytest
import pandas as pd
from conftest import SEGMENTOS


class TestSegmentacaoClientes:
    """Testa a função segmentar_clientes."""

    def test_retorna_dataframe(self, clientes):
        assert isinstance(clientes, pd.DataFrame)

    def test_colunas_obrigatorias(self, clientes):
        assert "cliente" in clientes.columns
        assert "total_gasto" in clientes.columns
        assert "segmento" in clientes.columns

    def test_50_clientes(self, clientes):
        """Dataset tem 50 clientes únicos."""
        assert len(clientes) == 50

    def test_segmentos_validos(self, clientes):
        segmentos_encontrados = set(clientes["segmento"].unique())
        assert segmentos_encontrados.issubset(SEGMENTOS)

    def test_bronze_gasto_abaixo_5000(self, clientes):
        bronze = clientes[clientes["segmento"] == "Bronze"]
        if len(bronze) > 0:
            assert (bronze["total_gasto"] < 5000).all()

    def test_prata_gasto_entre_5000_e_15000(self, clientes):
        prata = clientes[clientes["segmento"] == "Prata"]
        if len(prata) > 0:
            assert ((prata["total_gasto"] >= 5000) & (prata["total_gasto"] <= 15000)).all()

    def test_ouro_gasto_acima_15000(self, clientes):
        ouro = clientes[clientes["segmento"] == "Ouro"]
        if len(ouro) > 0:
            assert (ouro["total_gasto"] > 15000).all()

    def test_ordenado_por_gasto_decrescente(self, clientes):
        gastos = clientes["total_gasto"].tolist()
        assert gastos == sorted(gastos, reverse=True)

    def test_total_gasto_sempre_positivo(self, clientes):
        assert (clientes["total_gasto"] > 0).all()

    def test_sem_duplicatas_de_clientes(self, clientes):
        assert clientes["cliente"].duplicated().sum() == 0

    def test_todos_os_clientes_presentes(self, clientes, df_enriquecido):
        """Todos os clientes do dataset enriquecido devem aparecer."""
        clientes_dataset = set(df_enriquecido["cliente"].unique())
        clientes_segmentados = set(clientes["cliente"].unique())
        assert clientes_dataset == clientes_segmentados

    def test_soma_total_gasto_igual_receita_total(self, clientes, df_enriquecido):
        """Soma de total_gasto deve igualar receita total do dataset."""
        soma_clientes = clientes["total_gasto"].sum()
        soma_dataset = df_enriquecido["receita_total"].sum()
        assert abs(soma_clientes - soma_dataset) < 0.01
