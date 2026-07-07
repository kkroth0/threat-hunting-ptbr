# iOS

## Objetivo
Contexto de endpoint móvel e acesso a aplicativos para dispositivos iOS gerenciados, sessões SaaS e acesso móvel apoiado por identidade.

## Tipo de plataforma
Sistema operacional

## Como funciona
- Esta biblioteca atualmente espera visibilidade iOS por meio de telemetria de auditoria Netskope, MDM, identidade e SaaS.
- O contexto útil inclui conformidade do dispositivo, acesso ao aplicativo, identidade do usuário, IP, localização e ação política.
- A telemetria do processo iOS de baixo nível é incomum em fluxos de trabalho SIEM, portanto, concentre-se no acesso e no comportamento.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)

## O que revisar
- Acesso SaaS sensível de dispositivos não gerenciados, desbloqueados, não compatíveis ou registrados recentemente.
- Geografias incomuns, redes arriscadas, viagens impossíveis e novas sessões em dispositivos móveis.
- Downloads, uploads, compartilhamento, atividade de aplicativos OAuth e repetidos desafios políticos de usuários móveis.

## Coisas de segurança para observar
- A busca de segurança iOS geralmente envolve controle de acesso e risco de sessão, e não eventos file/process.
- Os tokens móveis podem permanecer úteis após a redefinição da senha se as sessões e as concessões de aplicativos não forem revogadas.
- A conformidade do dispositivo, o acesso condicional e a política SASE devem ser revistos em conjunto.

## Caçar ideias
- Autenticação ou atividade administrativa fora da linha de base normal.
- Exposição pública, configuração arriscada, registro desativado ou novos ativos de alto risco.
- Caminhos de rede suspeitos, tráfego de saída, tunelamento ou movimentação de dados.
- Novos locais de persistência, acesso privilegiado ou desvio de política.
- Eventos envolvendo sistemas críticos, cargas de trabalho de produção, infraestrutura de identidade ou dados confidenciais.

## Fluxo de trabalho de triagem
1. Identifique a entidade da plataforma: conta, usuário, host, dispositivo, carga de trabalho, projeto, assinatura, locação ou recurso.
2. Confirme se a atividade é esperada para essa entidade e janela de tempo.
3. Junte-se à identidade, ao endpoint, à rede, à postura da nuvem e ao contexto do incidente.
4. Decida se o resultado é benigno, suspeito, um incidente confirmado, um candidato à detecção ou uma lacuna de cobertura.
5. Documente a telemetria ausente e as oportunidades de casos de uso.

## Perguntas sobre cobertura
- Os ativos críticos desta plataforma são conhecidos e etiquetados?
- Os logs estão habilitados para autenticação, administração, rede e alterações relevantes de segurança?
- O Sentinel recebe diariamente as tabelas esperadas?
- A tabela pode identificar usuário, host, origem IP, destino, ação e recurso?
- Quais caçadas não podem ser realizadas porque falta a telemetria necessária?

## Páginas da biblioteca relacionadas
- [Catálogo de tabelas Sentinel](../../sentinel/tables/index.md)
- [Fontes de dados](../../data-sources/README.md)
- [Biblioteca KQL](../../sentinel/kql/README.md)
- [HEARTH KQL Iniciantes](../../sentinel/kql/hearth/README.md)
