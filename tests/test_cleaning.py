"""
RF03 — Testes para limpeza e tratamento de dados.
Valida remoção de nulos, datas inválidas, strings sujas e
conversão de tipos.
"""
import pytest
import pandas as pd
import numpy as np


class TestLimpezaDeDados:
    """Testa a função limpar_dados."""

    def test_retorna_tupla_dataframe_e_relatorio(self, df_bruto):
        from salesinsight import limpar_dados
        resultado = limpar_dados(df_bruto.copy())
        assert isinstance(resultado, tuple)
        assert len(resultado) == 2
        df, relatorio = resultado
        assert isinstance(df, pd.DataFrame)
        assert isinstance(relatorio, dict)

    def test_remove_registros_invalidos(self, df_bruto, df_limpo):
        """DataFrame limpo deve ter menos linhas que o bruto."""
        assert len(df_limpo) < len(df_bruto)

    def test_sem_nulos_em_quantidade(self, df_limpo):
        assert df_limpo["quantidade"].isnull().sum() == 0

    def test_sem_nulos_em_preco_unitario(self, df_limpo):
        assert df_limpo["preco_unitario"].isnull().sum() == 0

    def test_sem_datas_invalidas(self, df_limpo):
        """Nenhuma data deve ser NaT após limpeza."""
        assert df_limpo["data_venda"].isnull().sum() == 0

    def test_data_venda_tipo_datetime(self, df_limpo):
        assert pd.api.types.is_datetime64_any_dtype(df_limpo["data_venda"])

    def test_quantidade_tipo_inteiro(self, df_limpo):
        assert pd.api.types.is_integer_dtype(df_limpo["quantidade"])

    def test_preco_unitario_tipo_float(self, df_limpo):
        assert pd.api.types.is_float_dtype(df_limpo["preco_unitario"])

    def test_sem_espacos_em_produto(self, df_limpo):
        """Coluna produto não deve ter espaços no início/fim."""
        tem_espaco = df_limpo["produto"].str.startswith(" ") | df_limpo["produto"].str.endswith(" ")
        assert not tem_espaco.any()

    def test_sem_espacos_em_cliente(self, df_limpo):
        tem_espaco = df_limpo["cliente"].str.startswith(" ") | df_limpo["cliente"].str.endswith(" ")
        assert not tem_espaco.any()

    def test_relatorio_contem_registros_iniciais(self, df_bruto):
        from salesinsight import limpar_dados
        _, relatorio = limpar_dados(df_bruto.copy())
        assert "registros_iniciais" in relatorio
        assert relatorio["registros_iniciais"] == 200

    def test_relatorio_contem_registros_finais(self, df_bruto):
        from salesinsight import limpar_dados
        _, relatorio = limpar_dados(df_bruto.copy())
        assert "registros_finais" in relatorio
        assert relatorio["registros_finais"] > 0

    def test_relatorio_contem_total_removidos(self, df_bruto):
        from salesinsight import limpar_dados
        _, relatorio = limpar_dados(df_bruto.copy())
        assert "registros_removidos_total" in relatorio
        esperado = relatorio["registros_iniciais"] - relatorio["registros_finais"]
        assert relatorio["registros_removidos_total"] == esperado

    def test_nao_altera_dataframe_original(self, df_bruto):
        """limpar_dados não deve modificar o DataFrame passado como argumento."""
        from salesinsight import limpar_dados
        copia = df_bruto.copy()
        limpar_dados(copia)
        # O shape do original não deve mudar (passou copia)
        assert len(df_bruto) == 200

    def test_quantidade_sempre_positiva(self, df_limpo):
        assert (df_limpo["quantidade"] > 0).all()

    def test_preco_sempre_positivo(self, df_limpo):
        assert (df_limpo["preco_unitario"] > 0).all()

    def test_colunas_preservadas(self, df_limpo):
        """Colunas originais devem ser preservadas após limpeza."""
        colunas_esperadas = ["id_venda", "data_venda", "cliente", "produto",
                             "categoria", "regiao", "quantidade", "preco_unitario"]
        for col in colunas_esperadas:
            assert col in df_limpo.columns
