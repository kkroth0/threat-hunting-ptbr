# Orca Security

## Objetivo
Postura da nuvem, risco de carga de trabalho, vulnerabilidade, exposição, segredos, identidade e telemetria de contexto de ativos.

## Categoria
CSPM/CWPP

## Como funciona
- As descobertas resumem os riscos nos ativos da nuvem sem a necessidade de cada carga de trabalho enviar logs de eventos brutos.
- O contexto dos ativos ajuda a priorizar sistemas expostos, vulneráveis, privilegiados, voltados para a Internet ou confidenciais.
- As descobertas de postura devem ser correlacionadas com AzureActivity, diagnósticos de nuvem, logs de rede e incidentes.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)

## O que revisar
- descobertas Critical/high sobre ativos voltados para a Internet, ativos de identidade, cargas de trabalho de produção e armazenamentos de dados.
- Segredos em arquivos, pacotes vulneráveis, interfaces administrativas expostas, armazenamento público e caminhos IAM arriscados.
- Descobertas que permanecem abertas em vários ciclos de busca ou reaparecem após a correção.

## Uso de caça
- Exposição crítica à nuvem
- Bem público vulnerável
- Privilégio ou exposição secreta

## Coisas de segurança para observar
- Os alertas de postura nem sempre são um comprometimento ativo, mas definem onde o comprometimento tem maior probabilidade de causar impacto.
- A exposição de alto risco deve ser convertida em buscas de informações quando novos CVEs ou campanhas de exploração aparecerem.
- Propriedade, criticidade dos ativos e exposição à Internet são fundamentais para priorizar a resposta.

## Perguntas úteis sobre caça
- Quais ativos voltados para a Internet apresentam vulnerabilidades críticas ou exposição a segredos?
- Quais contas de nuvem repetiram descobertas arriscadas?
- Quais descobertas de postura se sobrepõem a anomalias de rede ou identidade ativas?

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
