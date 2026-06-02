# SalesInsight PY - Criacao de Issues e Populacao do Kanban
# Repositorio: samuelmarquesgit/InteligenciaDeMercado
# Kanban: projeto #1
#
# Pre-requisito: gh CLI autenticado  ->  gh auth login
# Execucao: .\scripts\create_issues_kanban.ps1

$REPO    = "samuelmarquesgit/InteligenciaDeMercado"
$OWNER   = "samuelmarquesgit"
$PROJECT = 1

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  SalesInsight PY - Issues + Kanban"            -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# ── Labels ────────────────────────────────────────────────
Write-Host "`n[Labels] Criando labels necessarios..." -ForegroundColor Yellow
$labelDefs = @(
    @{ name = "feat";  color = "0075ca"; desc = "Nova funcionalidade" },
    @{ name = "docs";  color = "0052cc"; desc = "Documentacao" },
    @{ name = "chore"; color = "e4e669"; desc = "Configuracao e entrega" },
    @{ name = "done";  color = "0e8a16"; desc = "Concluido" }
)
foreach ($lbl in $labelDefs) {
    $exists = gh label list --repo $REPO --json name 2>$null |
              ConvertFrom-Json | Where-Object { $_.name -eq $lbl.name }
    if (-not $exists) {
        gh label create $lbl.name --color $lbl.color --description $lbl.desc --repo $REPO | Out-Null
        Write-Host "  Criado: $($lbl.name)" -ForegroundColor Green
    } else {
        Write-Host "  Ja existe: $($lbl.name)" -ForegroundColor Gray
    }
}

# ── Funcao auxiliar (usa --body-file para evitar problemas de parsing) ────────
function New-KanbanIssue {
    param(
        [string]   $Title,
        [string]   $Body,
        [string[]] $Labels,
        [bool]     $Close = $false
    )

    Write-Host "`n  >> $Title" -ForegroundColor Yellow

    # Escreve o body em arquivo temporario
    $tmp = [System.IO.Path]::GetTempFileName()
    [System.IO.File]::WriteAllText($tmp, $Body, [System.Text.Encoding]::UTF8)

    $labelArg = $Labels -join ","
    $url = gh issue create `
        --repo       $REPO `
        --title      $Title `
        --body-file  $tmp `
        --label      $labelArg 2>&1

    Remove-Item $tmp -ErrorAction SilentlyContinue

    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ERRO: $url" -ForegroundColor Red
        return
    }

    $number = ($url -split "/")[-1]

    gh project item-add $PROJECT --owner $OWNER --url $url 2>$null | Out-Null

    if ($Close) {
        gh issue close $number --repo $REPO --comment "Implementado em salesinsight.py - concluido." 2>$null | Out-Null
        Write-Host "  OK (fechado): $url" -ForegroundColor Green
    } else {
        Write-Host "  OK (aberto):  $url" -ForegroundColor Cyan
    }

    Start-Sleep -Milliseconds 600
}

# ============================================================
# BLOCO 1 - CONFIGURACAO INICIAL
# ============================================================
Write-Host "`n[Bloco 1/3] Configuracao inicial..." -ForegroundColor Magenta

New-KanbanIssue `
    -Title  "chore: configurar repositorio, branches e ambiente virtual" `
    -Body   "## Configuracao Inicial`n`n- [x] Repositorio criado no GitHub`n- [x] Branches main e develop`n- [x] requirements.txt (pandas, numpy, matplotlib, seaborn)`n- [x] .gitignore (.venv, __pycache__, outputs/*.png)`n- [x] Ambiente virtual: python -m venv .venv`n- [x] Pastas: outputs/graficos/, docs/, specs/, steering/`n- [x] Templates de PR e Issues em .github/" `
    -Labels @("chore","done") -Close $true

# ============================================================
# BLOCO 2 - REQUISITOS FUNCIONAIS RF01 a RF14
# ============================================================
Write-Host "`n[Bloco 2/3] Requisitos funcionais RF01-RF14..." -ForegroundColor Magenta

# RF01 -------------------------------------------------------------------
$b = "## RF01 - Geracao do Dataset Sintetico`n`n"
$b += "### Funcao`n"
$b += "gerar_dataset_vendas(n_registros=200, seed=42) -> pd.DataFrame`n`n"
$b += "### O que faz`n"
$b += "Gera 200 registros sinteticos com seed=42 para reproducibilidade total.`n"
$b += "Garante 50 clientes unicos (Cliente_001 a Cliente_050).`n"
$b += "Datas distribuidas por 2024. Salva em vendas.csv.`n`n"
$b += "### Dados sujos injetados`n"
$b += "- 5 nulos em quantidade`n"
$b += "- 5 nulos em preco_unitario`n"
$b += "- 1 data invalida na linha 0`n"
$b += "- 3 strings com espacos extras na coluna cliente`n`n"
$b += "### Colunas (8)`n"
$b += "id_venda, data_venda, cliente, produto, categoria, regiao, quantidade, preco_unitario`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] DataFrame 200 x 8`n"
$b += "- [x] seed=42 garante reproducibilidade`n"
$b += "- [x] vendas.csv salvo na raiz`n"
New-KanbanIssue -Title "feat(RF01): gerar_dataset_vendas - dataset sintetico com dados sujos" `
                -Body $b -Labels @("feat","done") -Close $true

# RF02 -------------------------------------------------------------------
$b = "## RF02 - Inspecao dos Dados`n`n"
$b += "### Funcao`n"
$b += "inspecionar_dados(df: pd.DataFrame) -> None`n`n"
$b += "### Output no console`n"
$b += "- Shape (linhas x colunas)`n"
$b += "- Lista de colunas`n"
$b += "- Tipos de dados por coluna`n"
$b += "- Contagem de nulos por coluna`n"
$b += "- Total de nulos e duplicatas`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] Exibe shape, colunas, dtypes, isnull e duplicatas`n"
$b += "- [x] Formatacao visual com separadores`n"
$b += "- [x] Nao modifica o DataFrame`n"
New-KanbanIssue -Title "feat(RF02): inspecionar_dados - diagnostico e metadados do DataFrame" `
                -Body $b -Labels @("feat","done") -Close $true

# RF03 -------------------------------------------------------------------
$b = "## RF03 - Limpeza e Tratamento de Dados`n`n"
$b += "### Funcao`n"
$b += "limpar_dados(df: pd.DataFrame) -> tuple`n`n"
$b += "### Operacoes`n"
$b += "1. str.strip() em todas as colunas string`n"
$b += "2. pd.to_datetime com errors=coerce na data_venda`n"
$b += "3. dropna nas linhas com datas invalidas`n"
$b += "4. dropna nas linhas com nulos em quantidade ou preco_unitario`n"
$b += "5. Conversao: quantidade -> int, preco_unitario -> float`n`n"
$b += "### Retorno`n"
$b += "Tupla (df_limpo, relatorio) com contagens de registros removidos`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] Retorna (df_limpo, relatorio)`n"
$b += "- [x] Tipos corretos apos limpeza`n"
$b += "- [x] Relatorio exibido no console`n"
New-KanbanIssue -Title "feat(RF03): limpar_dados - limpeza e tratamento de dados sujos" `
                -Body $b -Labels @("feat","done") -Close $true

# RF04 -------------------------------------------------------------------
$b = "## RF04 - Criacao de Colunas Derivadas`n`n"
$b += "### Funcao`n"
$b += "criar_colunas_derivadas(df: pd.DataFrame) -> pd.DataFrame`n`n"
$b += "### 6 colunas criadas`n"
$b += "- receita_total      : quantidade * preco_unitario`n"
$b += "- mes                : numero do mes (1-12)`n"
$b += "- mes_nome           : nome em portugues via dict`n"
$b += "- trimestre          : Q1/Q2/Q3/Q4 via np.select`n"
$b += "- ano                : ano extraido da data`n"
$b += "- faixa_receita_item : Baixo/Medio/Alto Valor via np.select`n`n"
$b += "### Tecnica`n"
$b += "np.select() vetorizado - sem loops Python`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] 6 colunas criadas`n"
$b += "- [x] np.select em 2 classificacoes`n"
New-KanbanIssue -Title "feat(RF04): criar_colunas_derivadas - feature engineering com np.select" `
                -Body $b -Labels @("feat","done") -Close $true

# RF05 -------------------------------------------------------------------
$b = "## RF05 - Metricas Agregadas com groupby`n`n"
$b += "### Funcao`n"
$b += "calcular_metricas(df: pd.DataFrame) -> dict`n`n"
$b += "### Agregacoes`n"
$b += "- por_mes       : receita_total por mes (12 linhas)`n"
$b += "- top_produtos  : top 5 por receita (5 linhas)`n"
$b += "- por_categoria : receita por categoria (4 linhas)`n"
$b += "- por_regiao    : receita + ticket medio por regiao (5 linhas)`n"
$b += "- total_geral   : soma total (float)`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] groupby().agg() utilizado`n"
$b += "- [x] Dict retornado com todas as chaves`n"
New-KanbanIssue -Title "feat(RF05): calcular_metricas - agregacoes com groupby" `
                -Body $b -Labels @("feat","done") -Close $true

# RF06 -------------------------------------------------------------------
$b = "## RF06 - Segmentacao de Clientes`n`n"
$b += "### Funcao`n"
$b += "segmentar_clientes(df: pd.DataFrame) -> pd.DataFrame`n`n"
$b += "### Segmentos via lambda`n"
$b += "- Bronze : total_gasto menor que 5000`n"
$b += "- Prata  : total_gasto entre 5000 e 15000`n"
$b += "- Ouro   : total_gasto maior que 15000`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] 50 clientes classificados`n"
$b += "- [x] Lambda com .apply()`n"
$b += "- [x] Ordenado por total_gasto decrescente`n"
New-KanbanIssue -Title "feat(RF06): segmentar_clientes - Bronze Prata Ouro com lambda" `
                -Body $b -Labels @("feat","done") -Close $true

# RF07 -------------------------------------------------------------------
$b = "## RF07 - Estatisticas com NumPy Vetorizado`n`n"
$b += "### Funcao`n"
$b += "calcular_estatisticas_numpy(df: pd.DataFrame) -> dict`n`n"
$b += "### Estatisticas calculadas`n"
$b += "- np.mean, np.median, np.std, np.sum, np.min, np.max`n"
$b += "- np.percentile P25 e P75`n`n"
$b += "### Broadcasting`n"
$b += "Normalizacao min-max: valores_norm = (x - min) / (max - min)`n`n"
$b += "### Retorno`n"
$b += "Dict com 10 chaves incluindo timestamp`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] .to_numpy() utilizado`n"
$b += "- [x] Broadcasting sem loop Python`n"
New-KanbanIssue -Title "feat(RF07): calcular_estatisticas_numpy - estatisticas vetorizadas NumPy" `
                -Body $b -Labels @("feat","done") -Close $true

# RF08 -------------------------------------------------------------------
$b = "## RF08 - Visualizacoes com Matplotlib e Seaborn`n`n"
$b += "### Funcao`n"
$b += "gerar_visualizacoes(df, metricas, output_dir) -> None`n`n"
$b += "### 3 graficos gerados`n"
$b += "1. Linha com area  : Receita por Mes 2024 -> vendas_por_mes.png`n"
$b += "2. Barras horiz.   : Top 5 Produtos       -> top_produtos.png`n"
$b += "3. Pizza           : Receita por Regiao   -> distribuicao_regioes.png`n`n"
$b += "### Config`n"
$b += "- matplotlib.use(Agg) - compativel com Colab`n"
$b += "- dpi=100, bbox_inches=tight`n"
$b += "- plt.close(fig) apos cada grafico`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] 3 PNG em outputs/graficos/`n"
$b += "- [x] plt.close apos cada figura`n"
New-KanbanIssue -Title "feat(RF08): gerar_visualizacoes - 3 graficos PNG matplotlib seaborn" `
                -Body $b -Labels @("feat","done") -Close $true

# RF09 -------------------------------------------------------------------
$b = "## RF09 - Classe AnalisadorDeVendas`n`n"
$b += "### Classe`n"
$b += "class AnalisadorDeVendas`n`n"
$b += "### Atributos`n"
$b += "self.caminho_arquivo, self.df_bruto, self.df_limpo`n"
$b += "self.metricas, self.clientes, self.stats`n`n"
$b += "### Metodos (todos retornam self)`n"
$b += "- .carregar()    : le o CSV`n"
$b += "- .limpar()      : aplica limpeza`n"
$b += "- .transformar() : colunas derivadas`n"
$b += "- .analisar()    : metricas + segmentacao + stats`n"
$b += "- .resumo()      : exibe resultado no console`n`n"
$b += "### Method chaining`n"
$b += "analisador.carregar().limpar().transformar().analisar().resumo()`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] Todos os metodos retornam self`n"
$b += "- [x] Encadeamento funcional`n"
New-KanbanIssue -Title "feat(RF09): AnalisadorDeVendas - classe com method chaining" `
                -Body $b -Labels @("feat","done") -Close $true

# RF10 -------------------------------------------------------------------
$b = "## RF10 - Heranca com AnalisadorComProjecao`n`n"
$b += "### Classe`n"
$b += "class AnalisadorComProjecao(AnalisadorDeVendas)`n`n"
$b += "### Heranca`n"
$b += "super().__init__(caminho_arquivo) no __init__`n"
$b += "Atributos adicionais: self.meses_projecao, self.projecoes`n`n"
$b += "### Metodo`n"
$b += "projetar_tendencia(taxa_crescimento=0.05)`n"
$b += "Calcula crescimento composto sobre media mensal`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] super().__init__() chamado`n"
$b += "- [x] Projecoes para 3 meses calculadas`n"
$b += "- [x] Retorna self`n"
New-KanbanIssue -Title "feat(RF10): AnalisadorComProjecao - heranca e projecao de tendencia" `
                -Body $b -Labels @("feat","done") -Close $true

# RF11 -------------------------------------------------------------------
$b = "## RF11 - Lambda e Higher-Order Functions`n`n"
$b += "### Funcao`n"
$b += "processar_coluna(df, coluna, func) -> pd.DataFrame`n`n"
$b += "### O que faz`n"
$b += "HOF que recebe qualquer funcao como parametro e aplica com .apply()`n"
$b += "Cria coluna _transformado sem modificar a original`n`n"
$b += "### Uso no main`n"
$b += "df = processar_coluna(df, receita_total, lambda x: Alto Impacto se x maior 10000)`n`n"
$b += "### 4 lambdas distintas no projeto`n"
$b += "1. RF06: segmentacao de clientes`n"
$b += "2. RF13: limpeza de strings com re.sub`n"
$b += "3. RF13: validacao com re.match`n"
$b += "4. main: classificacao de impacto`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] HOF recebe funcao como parametro`n"
$b += "- [x] lambda em 4 contextos distintos`n"
New-KanbanIssue -Title "feat(RF11): processar_coluna - higher-order function com lambda" `
                -Body $b -Labels @("feat","done") -Close $true

# RF12 -------------------------------------------------------------------
$b = "## RF12 - Exportacao CSV e JSON`n`n"
$b += "### Funcao`n"
$b += "exportar_resultados(metricas, clientes, stats) -> None`n`n"
$b += "### Arquivos exportados`n"
$b += "- outputs/metricas_por_mes.csv     (utf-8)`n"
$b += "- outputs/segmentacao_clientes.csv (utf-8)`n"
$b += "- outputs/estatisticas_gerais.json (indent=2, ensure_ascii=False)`n`n"
$b += "### Verificacao`n"
$b += "JSON relido com json.load() e valores exibidos no console`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] 2 CSV + 1 JSON gerados`n"
$b += "- [x] JSON verificado por leitura`n"
New-KanbanIssue -Title "feat(RF12): exportar_resultados - CSV e JSON com verificacao de integridade" `
                -Body $b -Labels @("feat","done") -Close $true

# RF13 -------------------------------------------------------------------
$b = "## RF13 - Limpeza com Expressoes Regulares`n`n"
$b += "### Funcao`n"
$b += "limpar_strings_com_regex(df: pd.DataFrame) -> pd.DataFrame`n`n"
$b += "### Padroes utilizados`n"
$b += "- Padrao 1: remove caracteres especiais da coluna cliente (re.sub)`n"
$b += "- Padrao 2: valida formato Cliente_NNN (re.match)`n`n"
$b += "### Colunas criadas`n"
$b += "- cliente_limpo  : string sem caracteres invalidos`n"
$b += "- cliente_valido : bool True/False para validacao`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] re.compile e re.sub utilizados`n"
$b += "- [x] re.compile e re.match utilizados`n"
$b += "- [x] Colunas cliente_limpo e cliente_valido criadas`n"
New-KanbanIssue -Title "feat(RF13): limpar_strings_com_regex - re.compile e re.sub" `
                -Body $b -Labels @("feat","done") -Close $true

# RF14 -------------------------------------------------------------------
$b = "## RF14 - Pipeline Completo (main)`n`n"
$b += "### Implementacao`n"
$b += "def main() com if __name__ == '__main__': main()`n`n"
$b += "### Sequencia de execucao`n"
$b += "1. RF01 - gerar_dataset_vendas -> vendas.csv`n"
$b += "2. RF02 - inspecionar_dados`n"
$b += "3. RF03 - limpar_dados`n"
$b += "4. RF04 - criar_colunas_derivadas`n"
$b += "5. RF13 - limpar_strings_com_regex`n"
$b += "6. RF11 - processar_coluna com lambda`n"
$b += "7. RF09+RF10 - AnalisadorComProjecao method chaining completo`n"
$b += "8. RF08 - gerar_visualizacoes`n"
$b += "9. RF12 - exportar_resultados`n`n"
$b += "### Execucao`n"
$b += "python salesinsight.py`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] Pipeline executa sem erros`n"
$b += "- [x] 3 PNG + 2 CSV + 1 JSON gerados`n"
$b += "- [x] if __name__ == main presente`n"
New-KanbanIssue -Title "feat(RF14): main - pipeline completo de ponta a ponta" `
                -Body $b -Labels @("feat","done") -Close $true

# ============================================================
# BLOCO 3 - DOCUMENTACAO E ENTREGA
# ============================================================
Write-Host "`n[Bloco 3/3] Documentacao e entrega..." -ForegroundColor Magenta

$b = "## Documentacao Tecnica Completa`n`n"
$b += "### Arquivos revisados e criados`n"
$b += "- docs/PRD.md, BACKLOG.md, architeture.md, roadmap.md`n"
$b += "- docs/gitflow.md, technologies.md, test_report.md`n"
$b += "- docs/pipeline.mmd - diagrama Mermaid do pipeline`n"
$b += "- specs/requirements.md, tasks.md, design.md`n"
$b += "- steering/product.md, tech.md, structure.md`n"
$b += "- AUDIT.md - auditoria completa`n`n"
$b += "### Criterio de aceite`n"
$b += "- [x] Documentacao revisada e atualizada`n"
$b += "- [x] Diagrama Mermaid criado`n"
$b += "- [x] AUDIT.md com conformidade e lista de tarefas`n"
New-KanbanIssue -Title "docs: documentacao tecnica completa - PRD, BACKLOG, arquitetura, Mermaid" `
                -Body $b -Labels @("docs","done") -Close $true

$b = "## Video de Demonstracao`n`n"
$b += "### Roteiro sugerido (5 min)`n"
$b += "1. Mostrar estrutura do repositorio no GitHub`n"
$b += "2. Executar: python salesinsight.py`n"
$b += "3. Mostrar console output completo`n"
$b += "4. Abrir outputs/ e exibir 3 PNG gerados`n"
$b += "5. Mostrar classe AnalisadorComProjecao no codigo`n"
$b += "6. Mostrar Kanban no GitHub Projects`n`n"
$b += "### Requisitos`n"
$b += "- Duracao ate 5 minutos`n"
$b += "- Google Drive publico ou YouTube nao listado`n`n"
$b += "### Criterio de aceite`n"
$b += "- [ ] Video gravado e hospedado`n"
$b += "- [ ] Link inserido no README.md`n"
New-KanbanIssue -Title "chore: gravar video de demonstracao do pipeline (ate 5 min)" `
                -Body $b -Labels @("chore") -Close $false

$b = "## Submissao Final no AVA`n`n"
$b += "### Links a submeter`n"
$b += "- [ ] Repositorio GitHub (verificar se esta publico)`n"
$b += "- [ ] Video de demonstracao`n"
$b += "- [ ] Kanban: https://github.com/users/samuelmarquesgit/projects/1`n`n"
$b += "### Prazo`n"
$b += "08/06/2026 as 12h`n`n"
$b += "### Checklist`n"
$b += "- [ ] python salesinsight.py roda sem erros`n"
$b += "- [ ] Repositorio publico no GitHub`n"
$b += "- [ ] README com todos os links`n"
$b += "- [ ] Video acessivel sem login`n"
New-KanbanIssue -Title "chore: submeter links no AVA - prazo 08/06/2026 12h" `
                -Body $b -Labels @("chore") -Close $false

# ============================================================
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Concluido!" -ForegroundColor Green
Write-Host "  Issues: https://github.com/$REPO/issues"       -ForegroundColor White
Write-Host "  Kanban : https://github.com/users/$OWNER/projects/$PROJECT" -ForegroundColor White
Write-Host "================================================" -ForegroundColor Cyan
