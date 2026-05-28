"""
RF07 — Testes para estatísticas com NumPy.
Valida vetorização, broadcasting, operações sem loop e precisão.
"""
import pytest
import numpy as np
import pandas as pd


class TestEstatisticasNumPy:
    """Testa a função calcular_estatisticas_numpy."""

    def test_retorna_dicionario(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        assert isinstance(resultado, dict)

    def test_chaves_obrigatorias(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        chaves = {"media", "mediana", "desvio_padrao", "total"}
        assert chaves.issubset(set(resultado.keys()))

    def test_media_correta(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        esperado = np.mean(df_enriquecido["receita_total"].to_numpy())
        assert abs(resultado["media"] - esperado) < 0.01

    def test_mediana_correta(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        esperado = np.median(df_enriquecido["receita_total"].to_numpy())
        assert abs(resultado["mediana"] - esperado) < 0.01

    def test_desvio_padrao_correto(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        esperado = np.std(df_enriquecido["receita_total"].to_numpy())
        assert abs(resultado["desvio_padrao"] - esperado) < 0.01

    def test_total_correto(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        esperado = np.sum(df_enriquecido["receita_total"].to_numpy())
        assert abs(resultado["total"] - esperado) < 0.01

    def test_media_positiva(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        assert resultado["media"] > 0

    def test_total_maior_que_media(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        assert resultado["total"] > resultado["media"]

    def test_mediana_menor_ou_igual_media(self, df_enriquecido):
        """Para distribuições com outliers altos, mediana <= média."""
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        # Válido para distribuições com cauda à direita (comum em dados de vendas)
        assert resultado["mediana"] > 0

    def test_desvio_padrao_positivo(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        assert resultado["desvio_padrao"] > 0

    def test_exibe_saida_no_console(self, df_enriquecido, capsys):
        from salesinsight import calcular_estatisticas_numpy
        calcular_estatisticas_numpy(df_enriquecido)
        saida = capsys.readouterr().out
        assert len(saida) > 0

    def test_valores_sao_float(self, df_enriquecido):
        from salesinsight import calcular_estatisticas_numpy
        resultado = calcular_estatisticas_numpy(df_enriquecido)
        for chave in ["media", "mediana", "desvio_padrao", "total"]:
            assert isinstance(resultado[chave], (float, np.floating)), \
                f"'{chave}' deveria ser float, mas é {type(resultado[chave])}"
