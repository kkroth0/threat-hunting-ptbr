# Linux

## Objetivo
Superfície do sistema operacional de servidor e carga de trabalho para autenticação, sudo, serviço, processo, shell, pacote, arquivo e buscas de rede.

## Tipo de plataforma
Sistema operacional

## Como funciona
- A telemetria Linux geralmente chega por meio de fontes Syslog, integridade do agente, auditd/Sysmon-for-Linux ou EDR.
- Logs de autenticação, logs sudo, logs cron/systemd, logs do gerenciador de pacotes e execução de shell são fontes principais.
- O syslog bruto precisa de uma análise cuidadosa porque distros e serviços gravam formatos diferentes.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [Syslog](../../sentinel/tables/reference/Syslog.md)
- [Heartbeat](../../sentinel/tables/reference/Heartbeat.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)

## O que revisar
- força bruta SSH, logins bem-sucedidos após falhas, uso de sudo, novos usuários, alterações de chave SSH e escalonamento de privilégios.
- persistência Cron/systemd, downloads suspeitos, chmod em caminhos temporários, shells reversos e teste de arquivo.
- Shells filho do servidor Web, exploração de aplicativos públicos e retornos de chamada de saída inesperados SSH/SCP ou HTTP.

## Coisas de segurança para observar
- As caçadas Linux são mais fortes quando existe telemetria de processo auditd ou EDR, não apenas syslog genérico.
- As contas de serviço e os usuários de serviços da Web precisam de linhas de base porque são contextos pós-exploração comuns.
- Caminhos temporários, memória compartilhada e locais de inicialização são áreas de preparação comuns.

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
