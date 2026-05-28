"""
RF08 — Testes para geração de visualizações.
Valida que os 3 gráficos PNG são criados corretamente.
"""
import pytest
import os


class TestVisualizacoes:
    """Testa a função gerar_visualizacoes."""

    def test_cria_pasta_de_saida(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        assert os.path.isdir(graficos_dir)

    def test_cria_grafico_vendas_por_mes(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        arquivo = os.path.join(graficos_dir, "vendas_por_mes.png")
        assert os.path.isfile(arquivo), "vendas_por_mes.png não foi criado"

    def test_cria_grafico_top_produtos(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        arquivo = os.path.join(graficos_dir, "top_produtos.png")
        assert os.path.isfile(arquivo), "top_produtos.png não foi criado"

    def test_cria_grafico_distribuicao_regioes(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        arquivo = os.path.join(graficos_dir, "distribuicao_regioes.png")
        assert os.path.isfile(arquivo), "distribuicao_regioes.png não foi criado"

    def test_graficos_nao_sao_vazios(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        for nome in ["vendas_por_mes.png", "top_produtos.png", "distribuicao_regioes.png"]:
            path = os.path.join(graficos_dir, nome)
            assert os.path.getsize(path) > 0, f"{nome} está vazio"

    def test_pelo_menos_3_graficos_criados(self, df_enriquecido, metricas, output_dir):
        from salesinsight import gerar_visualizacoes
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        pngs = [f for f in os.listdir(graficos_dir) if f.endswith(".png")]
        assert len(pngs) >= 3

    def test_nao_modifica_dataframe(self, df_enriquecido, metricas, output_dir):
        import pandas as pd
        from salesinsight import gerar_visualizacoes
        copia = df_enriquecido.copy()
        graficos_dir = os.path.join(output_dir, "graficos")
        gerar_visualizacoes(df_enriquecido, metricas, output_dir=graficos_dir)
        pd.testing.assert_frame_equal(df_enriquecido, copia)

    def test_usa_diretorio_padrao(self, df_enriquecido, metricas, tmp_path, monkeypatch):
        """Deve criar outputs/graficos por padrão."""
        import os
        from salesinsight import gerar_visualizacoes
        monkeypatch.chdir(tmp_path)
        gerar_visualizacoes(df_enriquecido, metricas)
        assert os.path.isdir(tmp_path / "outputs" / "graficos")
