"""
RF12 — Testes para exportação de CSV e JSON.
Valida criação dos arquivos, encoding, integridade e leitura posterior.
"""
import pytest
import pandas as pd
import json
import os


@pytest.fixture
def stats_numpy(df_enriquecido):
    from salesinsight import calcular_estatisticas_numpy
    return calcular_estatisticas_numpy(df_enriquecido)


class TestExportacaoCSV:
    """Testa exportação de resultados em CSV."""

    def test_cria_metricas_por_mes_csv(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        assert os.path.isfile(tmp_path / "outputs" / "metricas_por_mes.csv")

    def test_cria_segmentacao_clientes_csv(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        assert os.path.isfile(tmp_path / "outputs" / "segmentacao_clientes.csv")

    def test_metricas_por_mes_legivel(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        df = pd.read_csv(tmp_path / "outputs" / "metricas_por_mes.csv")
        assert len(df) == 12

    def test_segmentacao_clientes_legivel(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        df = pd.read_csv(tmp_path / "outputs" / "segmentacao_clientes.csv")
        assert len(df) == 50

    def test_csv_nao_vazio(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        for nome in ["metricas_por_mes.csv", "segmentacao_clientes.csv"]:
            path = tmp_path / "outputs" / nome
            assert os.path.getsize(path) > 0


class TestExportacaoJSON:
    """Testa exportação de estatísticas em JSON."""

    def test_cria_estatisticas_json(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        assert os.path.isfile(tmp_path / "outputs" / "estatisticas_gerais.json")

    def test_json_valido(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        path = tmp_path / "outputs" / "estatisticas_gerais.json"
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        assert isinstance(dados, dict)

    def test_json_contem_chaves_corretas(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        path = tmp_path / "outputs" / "estatisticas_gerais.json"
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        chaves = {"media", "mediana", "desvio_padrao", "total"}
        assert chaves.issubset(set(dados.keys()))

    def test_json_valores_sao_numericos(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        path = tmp_path / "outputs" / "estatisticas_gerais.json"
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        for chave in ["media", "mediana", "desvio_padrao", "total"]:
            assert isinstance(dados[chave], (int, float))

    def test_json_media_positiva(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        path = tmp_path / "outputs" / "estatisticas_gerais.json"
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        assert dados["media"] > 0

    def test_json_nao_vazio(self, metricas, clientes, stats_numpy, tmp_path, monkeypatch):
        from salesinsight import exportar_resultados
        monkeypatch.chdir(tmp_path)
        exportar_resultados(metricas, clientes, stats_numpy)
        path = tmp_path / "outputs" / "estatisticas_gerais.json"
        assert os.path.getsize(path) > 0
