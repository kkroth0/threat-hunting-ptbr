# Windows

## Objetivo
Endpoint primário e superfície do sistema operacional do servidor para autenticação, processo, PowerShell, serviço, registro e buscas de movimento lateral.

## Tipo de plataforma
Sistema operacional

## Como funciona
- A telemetria Windows entra em Sentinel por meio das fontes SecurityEvent, WindowsEvent, AMA, Sysmon e EDR/XDR.
- Os eventos de segurança mostram logons, alterações de contas, alterações de políticas, criação de processos quando ativados e atividades privilegiadas.
- A telemetria no estilo EDR e Sysmon adiciona linhagem de processo, arquivo, registro, rede e contexto de módulo.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [SecurityEvent](../../sentinel/tables/reference/SecurityEvent.md)
- [WindowsEvent](../../sentinel/tables/reference/WindowsEvent.md)
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)
- [Heartbeat](../../sentinel/tables/reference/Heartbeat.md)

## O que revisar
- Anomalias de tipo de logon, alterações de administrador local, criação de serviço, tarefas agendadas, PowerShell, WMI e execução remota.
- Persistência de registro, cargas de driver, acesso LSASS, comprometimento de ferramentas de segurança e precursores de ransomware.
- Hosts com falta de telemetria, problemas de integridade do agente ou volume de eventos incomumente silencioso.

## Coisas de segurança para observar
- O registro de linha de comando do processo e o registro de bloco de script PowerShell melhoram materialmente a qualidade da caça.
- Controladores de domínio, Entra Connect, PKI, servidores de salto e estações de trabalho administrativas precisam de linhas de base separadas.
- As buscas de endpoint devem preservar a linhagem do processo e os relacionamentos parent/child sempre que possível.

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
