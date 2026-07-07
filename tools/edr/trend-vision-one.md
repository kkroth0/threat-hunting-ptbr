# Trend Vision One

## Objetivo
Telemetria XDR/EDR para processo de endpoint, arquivo, registro, rede, técnicas de ataque observadas e alertas de ambiente de trabalho.

## Categoria
XDR/EDR

## Como funciona
- Os eventos de técnica de ataque observados mapeiam o comportamento do endpoint para táticas e técnicas no estilo MITRE.
- Os alertas do Workbench agrupam eventos relacionados e fornecem contexto de investigação.
- As tabelas de integridade ajudam a confirmar a cobertura do sensor de endpoint antes de confiar nos resultados da busca de endpoint.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)
- [TrendMicro_XDR_WORKBENCH_CL](../../sentinel/tables/reference/TrendMicro_XDR_WORKBENCH_CL.md)
- [TrendMicro_XDR_Health_Check_CL](../../sentinel/tables/reference/TrendMicro_XDR_Health_Check_CL.md)
- [TrendMicro_XDR_OAT_Health_Check_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_Health_Check_CL.md)

## O que revisar
- Execução de scripts suspeitos, linhagem de processos, persistência de registro, processos filhos incomuns e retornos de chamada de rede.
- Alertas de ambiente de trabalho com alta gravidade, hosts repetidos, técnicas MITRE recorrentes ou status não triado.
- Lacunas de integridade de endpoints, agentes obsoletos e tabelas que param de gerar relatórios para servidores críticos.

## Uso de caça
- Processo suspeito e execução de script
- Triagem de alertas do Workbench
- comportamento mapeado MITRE ATT&CK
- Integridade do conector de endpoint

## Coisas de segurança para observar
- As detecções de endpoint são mais fortes quando a linhagem do processo é preservada e unida ao contexto identity/network.
- Os adversários geralmente desabilitam ou evitam EDR antes de ransomware, exfiltração ou roubo de credenciais.
- O comportamento bruto do endpoint deve ser convertido em casos de uso estáveis somente após revisão falso-positiva.

## Perguntas úteis sobre caça
- Quais hosts mostram PowerShell, LOLBins, WMI suspeitos ou criação de serviço?
- Quais técnicas MITRE aparecem repetidamente sem escalonamento de incidentes?
- Quais endpoints pararam de relatar pouco antes de um evento de alto risco?

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
