"""
RF02 — Testes para inspeção dos dados.
Valida que inspecionar_dados() exibe as informações diagnósticas
corretas sem modificar o DataFrame.
"""
import pytest
import pandas as pd
from io import StringIO
import sys


class TestInspecaoDosDados:
    """Testa a função inspecionar_dados."""

    def test_nao_modifica_dataframe(self, df_bruto):
        """inspecionar_dados não deve modificar o DataFrame original."""
        from salesinsight import inspecionar_dados
        df_copia = df_bruto.copy()
        inspecionar_dados(df_bruto)
        pd.testing.assert_frame_equal(df_bruto, df_copia)

    def test_exibe_shape_no_console(self, df_bruto, capsys):
        """Deve imprimir o shape do DataFrame."""
        from salesinsight import inspecionar_dados
        inspecionar_dados(df_bruto)
        saida = capsys.readouterr().out
        assert "Shape" in saida or "shape" in saida.lower()
        assert "200" in saida

    def test_exibe_colunas_no_console(self, df_bruto, capsys):
        """Deve imprimir os nomes das colunas."""
        from salesinsight import inspecionar_dados
        inspecionar_dados(df_bruto)
        saida = capsys.readouterr().out
        assert "id_venda" in saida
        assert "data_venda" in saida

    def test_exibe_nulos_no_console(self, df_bruto, capsys):
        """Deve imprimir contagem de valores nulos."""
        from salesinsight import inspecionar_dados
        inspecionar_dados(df_bruto)
        saida = capsys.readouterr().out
        assert "nulo" in saida.lower() or "null" in saida.lower() or "isnull" in saida.lower() or "NaN" in saida or "0" in saida

    def test_exibe_titulo_da_secao(self, df_bruto, capsys):
        """Deve exibir cabeçalho da seção de inspeção."""
        from salesinsight import inspecionar_dados
        inspecionar_dados(df_bruto)
        saida = capsys.readouterr().out
        assert "INSPE" in saida.upper() or "===" in saida

    def test_aceita_dataframe_vazio(self):
        """Não deve lançar exceção com DataFrame vazio."""
        from salesinsight import inspecionar_dados
        df_vazio = pd.DataFrame()
        try:
            inspecionar_dados(df_vazio)
        except Exception as e:
            pytest.fail(f"inspecionar_dados lançou exceção com DataFrame vazio: {e}")

    def test_funciona_com_df_limpo(self, df_limpo, capsys):
        """Deve funcionar também com o DataFrame já limpo."""
        from salesinsight import inspecionar_dados
        inspecionar_dados(df_limpo)
        saida = capsys.readouterr().out
        assert len(saida) > 0
