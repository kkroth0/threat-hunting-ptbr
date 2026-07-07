# Netskope

## Objetivo
SASE, CASB, gateway web seguro, DLP, aplicativo em nuvem, página, conexão, rede e telemetria de política.

## Categoria
SASE/CASB

## Como funciona
- Os eventos descrevem usuário, dispositivo, aplicativo, URL, categoria, ação, política, risco e contexto de conexão.
- A telemetria CASB/SWG conecta o comportamento de identidade ao uso de aplicativos em nuvem e saída da web.
- DLP e alertas de malware podem fornecer pivôs de alto contexto para movimentação de arquivos e atividades arriscadas de SaaS.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [NetskopeAlerts_CL](../../sentinel/tables/reference/NetskopeAlerts_CL.md)
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)
- [NetskopeEventsAudit_CL](../../sentinel/tables/reference/NetskopeEventsAudit_CL.md)
- [NetskopeEventsConnection_CL](../../sentinel/tables/reference/NetskopeEventsConnection_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)
- [NetskopeEventsPage_CL](../../sentinel/tables/reference/NetskopeEventsPage_CL.md)

## O que revisar
- Acesso não autorizado a aplicativos, categorias de aplicativos arriscadas, uploads para armazenamento pessoal e novos destinos na nuvem.
- Alertas DLP, desvios de política, eventos de malware, downloads anômalos e uso impossível ou raro de aplicativos.
- Sessões Web de dispositivos arriscados, locais não gerenciados, proxies, anonimizadores e domínios recentemente observados.

## Uso de caça
- Acesso não autorizado a aplicativos
- revisão do alerta DLP
- Acesso a destinos de alto risco
- Saída incomum e atividade do usuário na web

## Coisas de segurança para observar
- A exfiltração na nuvem geralmente aparece como tráfego normal do navegador, a menos que usuário, aplicativo, volume e contexto de arquivo sejam unidos.
- Os campos de ação da política devem ser interpretados com cuidado: permitir, bloquear, alertar, orientar e colocar em quarentena têm significados diferentes.
- Netskope pode ajudar a conectar identidade, endpoint, SaaS e buscas de rede quando os detalhes do endpoint são limitados.

## Perguntas úteis sobre caça
- Quais usuários enviaram volumes incomuns para armazenamento em nuvem não autorizado?
- Quais aplicativos arriscados aparecem pela primeira vez no ambiente?
- Quais eventos bloqueados ou treinados se repetem até que ocorra um evento permitido com sucesso?

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
