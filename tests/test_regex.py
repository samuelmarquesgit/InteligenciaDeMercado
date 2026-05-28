"""
RF13 — Testes para limpeza de dados com expressões regulares.
Valida re.sub(), re.compile() e criação de colunas de validação.
"""
import pytest
import pandas as pd
import re


class TestLimpezaComRegex:
    """Testa a função limpar_strings_com_regex."""

    def test_cria_coluna_cliente_limpo(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        assert "cliente_limpo" in resultado.columns

    def test_cria_coluna_cliente_valido(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        assert "cliente_valido" in resultado.columns

    def test_cliente_valido_e_booleano(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        assert resultado["cliente_valido"].dtype == bool

    def test_clientes_limpos_sem_caracteres_especiais(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        padrao_invalido = re.compile(r"[^a-zA-Z0-9_ ]")
        for cliente in resultado["cliente_limpo"].dropna():
            assert not padrao_invalido.search(str(cliente)), \
                f"Caractere inválido em: {cliente}"

    def test_cliente_xxx_formato_valido(self, df_limpo):
        """Clientes no formato 'Cliente_XXX' devem ser marcados como válidos."""
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        padrao = re.compile(r"^Cliente_\d{3}$")
        clientes_validos = resultado[resultado["cliente_valido"]]["cliente_limpo"]
        for cliente in clientes_validos:
            assert padrao.match(str(cliente)), f"Marcado como válido mas não bate: {cliente}"

    def test_nao_modifica_outras_colunas(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        df = df_limpo.copy()
        colunas_antes = set(df.columns)
        resultado = limpar_strings_com_regex(df)
        novas_colunas = set(resultado.columns) - colunas_antes
        assert novas_colunas.issubset({"cliente_limpo", "cliente_valido"})

    def test_exibe_contagem_no_console(self, df_limpo, capsys):
        from salesinsight import limpar_strings_com_regex
        limpar_strings_com_regex(df_limpo.copy())
        saida = capsys.readouterr().out
        assert len(saida) > 0

    def test_retorna_dataframe(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        assert isinstance(resultado, pd.DataFrame)

    def test_sem_nulos_em_cliente_limpo(self, df_limpo):
        from salesinsight import limpar_strings_com_regex
        resultado = limpar_strings_com_regex(df_limpo.copy())
        assert resultado["cliente_limpo"].isnull().sum() == 0
