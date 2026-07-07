# Microsoft Sentinel

## Objetivo
Central SIEM e espaço de trabalho de busca para correlação, KQL, revisão de incidentes, listas de observação, regras de análise e integridade operacional.

## Categoria
SIEM

## Como funciona
- Ingere logs de nuvem, identidade, endpoint, rede, SaaS e personalizados em tabelas Log Analytics.
- Usa KQL para pesquisar tabelas, correlacionar entidades, criar regras analíticas e oferecer suporte a fluxos de trabalho de busca.
- Conecta alertas, incidentes, inteligência de ameaças, listas de observação, automação e visualizações de pastas de trabalho em uma superfície de investigação.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [SecurityIncident](../../sentinel/tables/reference/SecurityIncident.md)
- [SecurityAlert](../../sentinel/tables/reference/SecurityAlert.md)
- [SentinelAudit](../../sentinel/tables/reference/SentinelAudit.md)
- [SentinelHealth](../../sentinel/tables/reference/SentinelHealth.md)
- [Anomalies](../../sentinel/tables/reference/Anomalies.md)
- [ThreatIntelIndicators](../../sentinel/tables/reference/ThreatIntelIndicators.md)
- [Watchlist](../../sentinel/tables/reference/Watchlist.md)
- [LAQueryLogs](../../sentinel/tables/reference/LAQueryLogs.md)
- [Usage](../../sentinel/tables/reference/Usage.md)

## O que revisar
- Integridade do conector, atrasos na ingestão, volume da tabela e uso faturável.
- Regras de análise com altos falsos positivos, lógica obsoleta, regras desabilitadas ou mapeamento de entidade ausente.
- Incidentes encerrados sem classificação significativa, alertas repetidos e fontes de alerta que nunca se tornam incidentes.
- Listas de observação, feeds de inteligência sobre ameaças, regras de automação e manuais com amplas permissões.

## Uso de caça
- Revisão da fila de alertas e incidentes
- Revisão da qualidade da detecção
- Correspondência de inteligência de ameaças
- Revisão de integridade e ingestão da fonte de dados

## Coisas de segurança para observar
- Lacunas de cobertura: ferramentas importantes conectadas, mas que não produzem as tabelas esperadas.
- Desvio de detecção: as regras não correspondem mais porque os esquemas, os analisadores ou os campos do fornecedor foram alterados.
- Risco operacional: regras ruidosas causando fadiga de alerta ou automação suprimindo sinal útil.

## Perguntas úteis sobre caça
- Quais mesas de alto risco deixaram de ser ingeridas nas últimas 24 horas?
- Quais detecções geram incidentes repetidamente sem descobertas confirmadas?
- Quais indicadores de informações sobre ameaças correspondem à telemetria interna em dados de identidade, endpoint, rede e nuvem?

## Fluxo de trabalho do analista
1. Confirme se o conector está íntegro e se a tabela esperada está recebendo dados.
2. Revise os campos mais importantes: hora, usuário, host, origem IP, destino, ação, gravidade, política e evento bruto.
3. Crie uma linha de base para atividades normais por usuário, ativo, aplicativo, política e local.
4. Procure comportamentos raros, novos, de alto risco ou acorrentados.
5. Documente as descobertas e promova lógica estável em [Casos de uso](../../use-cases/README.md).

## Lista de verificação de maturidade
- O proprietário da fonte de dados é conhecido.
- As tabelas Sentinel e os campos-chave esperados estão documentados.
- As suposições do analisador e a normalização de campo são revisadas.
- Pelo menos uma busca diária ou semanal utiliza esta fonte de dados.
- Falsos positivos e notas de ajuste são capturados após cada caçada.

## Páginas da biblioteca relacionadas
- [Mapa da tabela de ferramentas](../../sentinel/tables/tool-table-map.md)
- [Normalização de campo](../../sentinel/tables/field-normalization.md)
- [Biblioteca KQL](../../sentinel/kql/README.md)
- [Biblioteca de caça](../../hunts/README.md)
