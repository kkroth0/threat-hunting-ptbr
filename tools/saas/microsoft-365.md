# Microsoft 365

## Objetivo
SaaS produtividade e telemetria de colaboração para Exchange, SharePoint, OneDrive, Teams e atividades de auditoria relacionadas.

## Categoria
SaaS

## Como funciona
- OfficeActivity registra operações de usuários e administradores em cargas de trabalho Microsoft 365.
- O contexto de identidade de Entra ID deve ser associado à caixa de correio, ao arquivo, ao Teams e à atividade SharePoint.
- Caças de alto valor geralmente combinam autenticação, ações mailbox/file e eventos de auditoria administrativa.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [OfficeActivity](../../sentinel/tables/reference/OfficeActivity.md)
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)

## O que revisar
- Regras de caixa de entrada, encaminhamento, alterações de permissão de caixa de correio, eDiscovery suspeito e acesso incomum a e-mails.
- Downloads em massa de arquivos, compartilhamento externo, links anônimos, atividades incomuns do Teams e atividades arriscadas de aplicativos OAuth.
- Ações administrativas relacionadas a retenção, transporte, auditoria, DLP, permissões de caixa de correio ou configuração de locatário.

## Uso de caça
- Abuso de regras de caixa de correio
- Compartilhamento de arquivos suspeito
- Novo uso do aplicativo OAuth

## Coisas de segurança para observar
- O comprometimento do e-mail comercial geralmente começa com um login válido e depois passa para regras de caixa de correio ou encaminhamento.
- A exfiltração de arquivos pode parecer um uso normal de SaaS, a menos que o volume, o tempo, a linha de base do usuário e o destino sejam revisados.
- O consentimento do OAuth pode ignorar a resposta de redefinição de senha, a menos que os tokens e as permissões do aplicativo sejam revogados.

## Perguntas úteis sobre caça
- Quais usuários criaram regras de encaminhamento ou de caixa de entrada logo após um login arriscado?
- Quais contas baixaram ou compartilharam volumes incomuns de arquivos?
- Quais aplicativos OAuth obtiveram acesso a e-mails, arquivos ou escopos do Graph?

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
