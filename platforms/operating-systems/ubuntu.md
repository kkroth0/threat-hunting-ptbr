# Ubuntu

## Objetivo
Superfície de caça Linux específica para Ubuntu para apt, dpkg, snap, systemd, SSH, sudo e cargas de trabalho de servidor comuns.

## Tipo de plataforma
Sistema operacional

## Como funciona
- Ubuntu normalmente usa logs de autenticação, syslog, journald, logs apt/dpkg, cloud-init e unidades systemd.
- Mudanças em pacotes e serviços podem explicar novos processos, persistência ou ouvintes inesperados.
- As cargas de trabalho da nuvem Ubuntu devem ser correlacionadas com eventos do plano de controle da nuvem e descobertas de exposição.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [Syslog](../../sentinel/tables/reference/Syslog.md)
- [Heartbeat](../../sentinel/tables/reference/Heartbeat.md)

## O que revisar
- Instalações Apt/dpkg, novos repositórios, novos serviços, unidades systemd modificadas e pacotes snap suspeitos.
- alterações de chave SSH, anomalias sudo, tarefas cron, novos usuários e alterações de inicialização na nuvem.
- Exploração de carga de trabalho da Web, shells reversos, armazenamento temporário de arquivos e conexões de saída inesperadas.

## Coisas de segurança para observar
- A instalação de pacotes é normal em servidores, mas arriscada quando ocorre em usuários, caminhos ou horários incomuns.
- Cloud-init e systemd podem fornecer persistência que se parece com administração normal.
- A função do servidor Ubuntu é importante: web, banco de dados, CI e hosts bastion têm linhas de base diferentes.

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
