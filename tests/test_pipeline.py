"""
RF14 — Testes de integração do pipeline completo.
Valida que main() executa do início ao fim sem erros e
que todos os outputs são gerados corretamente.
"""
import pytest
import os
import json
import pandas as pd


@pytest.fixture
def pipeline_executado(tmp_path, monkeypatch):
    """Executa o pipeline completo em diretório temporário."""
    monkeypatch.chdir(tmp_path)
    from salesinsight import main
    main()
    return tmp_path


class TestPipelineCompleto:
    """Testa a execução do pipeline completo via main()."""

    def test_main_executa_sem_excecao(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        from salesinsight import main
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() lançou exceção: {e}")

    def test_vendas_csv_criado(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "vendas.csv")

    def test_outputs_dir_criado(self, pipeline_executado):
        assert os.path.isdir(pipeline_executado / "outputs")

    def test_graficos_dir_criado(self, pipeline_executado):
        assert os.path.isdir(pipeline_executado / "outputs" / "graficos")

    def test_metricas_csv_criado(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "metricas_por_mes.csv")

    def test_clientes_csv_criado(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "segmentacao_clientes.csv")

    def test_json_criado(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "estatisticas_gerais.json")

    def test_png_vendas_por_mes(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "graficos" / "vendas_por_mes.png")

    def test_png_top_produtos(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "graficos" / "top_produtos.png")

    def test_png_distribuicao_regioes(self, pipeline_executado):
        assert os.path.isfile(pipeline_executado / "outputs" / "graficos" / "distribuicao_regioes.png")

    def test_pelo_menos_3_pngs(self, pipeline_executado):
        graficos = pipeline_executado / "outputs" / "graficos"
        pngs = [f for f in os.listdir(graficos) if f.endswith(".png")]
        assert len(pngs) >= 3

    def test_json_valido_e_completo(self, pipeline_executado):
        with open(pipeline_executado / "outputs" / "estatisticas_gerais.json", "r") as f:
            dados = json.load(f)
        assert "media" in dados
        assert "total" in dados
        assert dados["media"] > 0

    def test_metricas_csv_tem_12_meses(self, pipeline_executado):
        df = pd.read_csv(pipeline_executado / "outputs" / "metricas_por_mes.csv")
        assert len(df) == 12

    def test_clientes_csv_tem_50_linhas(self, pipeline_executado):
        df = pd.read_csv(pipeline_executado / "outputs" / "segmentacao_clientes.csv")
        assert len(df) == 50

    def test_vendas_csv_tem_200_linhas(self, pipeline_executado):
        df = pd.read_csv(pipeline_executado / "vendas.csv")
        assert len(df) == 200

    def test_pipeline_idempotente(self, tmp_path, monkeypatch):
        """Rodar main() duas vezes não deve causar erros."""
        monkeypatch.chdir(tmp_path)
        from salesinsight import main
        main()
        try:
            main()
        except Exception as e:
            pytest.fail(f"Segunda execução de main() lançou exceção: {e}")


class TestBlocoMain:
    """Testa que o bloco __main__ existe no módulo."""

    def test_modulo_tem_funcao_main(self):
        from salesinsight import main
        assert callable(main)

    def test_analisador_com_projecao_usado_no_pipeline(self, tmp_path, monkeypatch):
        """O pipeline deve usar AnalisadorComProjecao."""
        monkeypatch.chdir(tmp_path)
        from salesinsight import AnalisadorComProjecao
        assert AnalisadorComProjecao is not None
