# Android

## Objetivo
Contexto de endpoint móvel e acesso a aplicativos para dispositivos Android gerenciados, acesso SaaS arriscado e comportamento de rede móvel.

## Tipo de plataforma
Sistema operacional

## Como funciona
- Esta biblioteca atualmente espera visibilidade Android principalmente por meio de Netskope, SASE, CASB, MDM ou telemetria de identidade.
- A postura do dispositivo, o usuário, o aplicativo, a rede e o contexto de localização são mais realistas do que a telemetria de processo OS de baixo nível.
- As buscas de acesso móvel devem combinar identidade, atividade SaaS, conformidade do dispositivo e caminhos de rede arriscados.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)

## O que revisar
- Dispositivos não gerenciados ou não compatíveis que acessam aplicativos SaaS confidenciais.
- Locais arriscados, uso incomum de aplicativos, registros de novos dispositivos e viagens impossíveis com sessões móveis.
- Downloads/uploads para aplicativos arriscados, alertas de malware de ferramentas de segurança móvel e desvios de políticas.

## Coisas de segurança para observar
- O comprometimento móvel geralmente aparece como abuso de token/session, em vez da telemetria tradicional do processo de endpoint.
- BYOD e dispositivos não gerenciados precisam de expectativas diferentes dos dispositivos gerenciados corporativamente.
- Iscas de phishing e mensagens móveis são relevantes para operações LATAM, especialmente iscas com tema WhatsApp.

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
