# Microsoft Entra ID

## Objetivo
Plano de identidade primário para usuário, dispositivo, aplicativo, entidade de serviço, acesso condicional, MFA e atividade de função.

## Categoria
Identity

## Como funciona
- Produz registros de entrada para padrões de acesso interativos, não interativos, de aplicativo e de entidade de serviço.
- Produz registros de auditoria para alterações de diretório, atribuições de funções, consentimento de aplicativos, registro de dispositivos e alterações de políticas.
- Adiciona contexto de identidade por meio de tabelas de enriquecimento, como detalhes de identidade, UEBA, análise de pares e análise de comportamento.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)
- [IdentityInfo](../../sentinel/tables/reference/IdentityInfo.md)
- [BehaviorAnalytics](../../sentinel/tables/reference/BehaviorAnalytics.md)
- [UserPeerAnalytics](../../sentinel/tables/reference/UserPeerAnalytics.md)

## O que revisar
- Logins malsucedidos seguidos de sucesso, novas geografias, dispositivos desconhecidos e aplicativos clientes incomuns.
- Atribuição de funções privilegiadas, ativação de funções elegíveis, alterações de credenciais principais de serviço e consentimento de candidatura.
- alterações no registro do método MFA, alterações na política de acesso condicional, fluxo de código do dispositivo e indicadores de reprodução de token.

## Uso de caça
- Spray de senha
- Login bem-sucedido suspeito
- Nova atribuição de função privilegiada
- Login arriscado e revisão de acesso condicional

## Coisas de segurança para observar
- O abuso de contas válidas costuma ser mais silencioso que o malware e deve ser baseado em usuário, aplicativo, país e dispositivo.
- As entidades de serviço e os aplicativos OAuth podem se tornar caminhos de acesso à nuvem persistentes se credenciais ou permissões forem adicionadas.
- As operações LATAM devem observar phishing regional, preenchimento de credenciais, representação de suporte técnico e iscas com tema de pagamento.

## Perguntas úteis sobre caça
- Quais usuários se autenticam em novos países ou ASNs e depois acessam aplicativos confidenciais?
- Quais aplicativos receberam novas permissões delegadas ou de aplicativo?
- Quais usuários privilegiados alteraram MFA, senha, dispositivo ou estado de função fora das janelas normais?

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
