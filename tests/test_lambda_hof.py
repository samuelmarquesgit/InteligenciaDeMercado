"""
RF11 — Testes para funções lambda e higher-order functions.
Valida processar_coluna() e uso de lambda em contextos distintos.
"""
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def df_simples(df_enriquecido):
    """DataFrame reduzido para testes rápidos."""
    return df_enriquecido.head(20).copy()


class TestProcessarColuna:
    """Testa a função processar_coluna (higher-order function)."""

    def test_cria_coluna_transformada(self, df_simples):
        from salesinsight import processar_coluna
        resultado = processar_coluna(df_simples.copy(), "receita_total", lambda x: round(x / 1000, 2))
        assert "receita_total_transformado" in resultado.columns

    def test_aplica_funcao_corretamente(self, df_simples):
        from salesinsight import processar_coluna
        df = df_simples.copy()
        resultado = processar_coluna(df, "receita_total", lambda x: x * 2)
        esperado = df["receita_total"] * 2
        pd.testing.assert_series_equal(
            resultado["receita_total_transformado"].reset_index(drop=True),
            esperado.reset_index(drop=True),
            check_names=False
        )

    def test_nao_modifica_coluna_original(self, df_simples):
        from salesinsight import processar_coluna
        df = df_simples.copy()
        original = df["receita_total"].copy()
        processar_coluna(df, "receita_total", lambda x: x + 1)
        pd.testing.assert_series_equal(df["receita_total"], original)

    def test_aceita_lambda_categorica(self, df_simples):
        from salesinsight import processar_coluna
        resultado = processar_coluna(
            df_simples.copy(), "quantidade", lambda x: "Alto" if x > 5 else "Baixo"
        )
        assert "quantidade_transformado" in resultado.columns
        assert set(resultado["quantidade_transformado"].unique()).issubset({"Alto", "Baixo"})

    def test_aceita_lambda_normalizacao(self, df_simples):
        from salesinsight import processar_coluna
        receitas = df_simples["receita_total"]
        min_r, max_r = receitas.min(), receitas.max()
        resultado = processar_coluna(
            df_simples.copy(), "receita_total",
            lambda x: round((x - min_r) / (max_r - min_r), 4)
        )
        vals = resultado["receita_total_transformado"]
        assert vals.min() >= 0
        assert vals.max() <= 1

    def test_retorna_dataframe(self, df_simples):
        from salesinsight import processar_coluna
        resultado = processar_coluna(df_simples.copy(), "receita_total", lambda x: x)
        assert isinstance(resultado, pd.DataFrame)

    def test_funciona_com_funcao_nomeada(self, df_simples):
        from salesinsight import processar_coluna

        def dobrar(x):
            return x * 2

        resultado = processar_coluna(df_simples.copy(), "receita_total", dobrar)
        assert "receita_total_transformado" in resultado.columns


class TestLambdaContextos:
    """Valida uso de lambda em contextos distintos no pipeline."""

    def test_lambda_em_segmentacao(self, df_enriquecido):
        """Lambda é usada na classificação Bronze/Prata/Ouro."""
        from salesinsight import segmentar_clientes
        clientes = segmentar_clientes(df_enriquecido)
        # Verifica que a lógica de lambda está correta
        bronze = clientes[clientes["segmento"] == "Bronze"]
        assert (bronze["total_gasto"] < 5000).all()

    def test_lambda_em_apply_desconto(self, df_enriquecido):
        """Lambda em apply para calcular desconto."""
        df = df_enriquecido.copy()
        df["desconto"] = df["receita_total"].apply(lambda x: 0.10 if x > 10000 else 0.05)
        assert set(df["desconto"].unique()).issubset({0.10, 0.05})

    def test_lambda_em_sorted(self, df_enriquecido):
        """Lambda como key em sorted."""
        produtos = df_enriquecido.groupby("produto")["receita_total"].sum().reset_index()
        lista = produtos.to_dict("records")
        ordenado = sorted(lista, key=lambda p: p["receita_total"], reverse=True)
        receitas = [p["receita_total"] for p in ordenado]
        assert receitas == sorted(receitas, reverse=True)
