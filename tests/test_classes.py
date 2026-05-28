"""
RF09 + RF10 — Testes para as classes AnalisadorDeVendas e AnalisadorComProjecao.
Valida construtor, atributos, métodos, herança e super().
"""
import pytest
import pandas as pd
import os


@pytest.fixture
def csv_path(tmp_path):
    """Gera vendas.csv em pasta temporária para os testes."""
    from salesinsight import gerar_dataset_vendas
    df = gerar_dataset_vendas(n_registros=200, seed=42)
    path = str(tmp_path / "vendas.csv")
    df.to_csv(path, index=False)
    return path


class TestAnalisadorDeVendas:
    """Testa a classe AnalisadorDeVendas."""

    def test_instanciacao(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path)
        assert analisador is not None

    def test_atributo_caminho_arquivo(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path)
        assert analisador.caminho_arquivo == csv_path

    def test_atributo_df_bruto_inicialmente_none(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path)
        assert analisador.df_bruto is None

    def test_atributo_df_limpo_inicialmente_none(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path)
        assert analisador.df_limpo is None

    def test_metodo_carregar_retorna_self(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path)
        resultado = analisador.carregar()
        assert resultado is analisador

    def test_carregar_popula_df_bruto(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path).carregar()
        assert isinstance(analisador.df_bruto, pd.DataFrame)
        assert len(analisador.df_bruto) == 200

    def test_metodo_limpar_retorna_self(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path).carregar()
        resultado = analisador.limpar()
        assert resultado is analisador

    def test_limpar_popula_df_limpo(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = AnalisadorDeVendas(csv_path).carregar().limpar()
        assert isinstance(analisador.df_limpo, pd.DataFrame)
        assert len(analisador.df_limpo) < 200

    def test_method_chaining_completo(self, csv_path, tmp_path):
        from salesinsight import AnalisadorDeVendas
        analisador = (
            AnalisadorDeVendas(csv_path)
            .carregar()
            .limpar()
            .transformar()
            .analisar()
        )
        assert analisador.metricas
        assert analisador.clientes is not None

    def test_resumo_nao_lanca_excecao(self, csv_path):
        from salesinsight import AnalisadorDeVendas
        analisador = (
            AnalisadorDeVendas(csv_path)
            .carregar().limpar().transformar().analisar()
        )
        try:
            analisador.resumo()
        except Exception as e:
            pytest.fail(f"resumo() lançou exceção: {e}")


class TestAnalisadorComProjecao:
    """Testa a classe AnalisadorComProjecao (herança de AnalisadorDeVendas)."""

    def test_e_subclasse_de_analisador(self, csv_path):
        from salesinsight import AnalisadorDeVendas, AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path)
        assert isinstance(analisador, AnalisadorDeVendas)

    def test_atributo_meses_projecao(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path, meses_projecao=3)
        assert analisador.meses_projecao == 3

    def test_meses_projecao_default_e_3(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path)
        assert analisador.meses_projecao == 3

    def test_atributo_projecoes_inicialmente_vazio(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path)
        assert analisador.projecoes == []

    def test_projetar_tendencia_retorna_self(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = (
            AnalisadorComProjecao(csv_path)
            .carregar().limpar().transformar().analisar()
        )
        resultado = analisador.projetar_tendencia()
        assert resultado is analisador

    def test_projecoes_geradas(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = (
            AnalisadorComProjecao(csv_path, meses_projecao=3)
            .carregar().limpar().transformar().analisar()
            .projetar_tendencia()
        )
        assert len(analisador.projecoes) == 3

    def test_projecoes_tem_mes_e_receita(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = (
            AnalisadorComProjecao(csv_path)
            .carregar().limpar().transformar().analisar()
            .projetar_tendencia()
        )
        for p in analisador.projecoes:
            assert "mes" in p
            assert "receita_projetada" in p

    def test_receita_projetada_positiva(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = (
            AnalisadorComProjecao(csv_path)
            .carregar().limpar().transformar().analisar()
            .projetar_tendencia()
        )
        for p in analisador.projecoes:
            assert p["receita_projetada"] > 0

    def test_herda_metodo_carregar(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path)
        assert hasattr(analisador, "carregar")
        assert callable(analisador.carregar)

    def test_herda_atributo_metricas(self, csv_path):
        from salesinsight import AnalisadorComProjecao
        analisador = AnalisadorComProjecao(csv_path)
        assert hasattr(analisador, "metricas")
