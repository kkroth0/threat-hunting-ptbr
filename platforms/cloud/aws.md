# AWS

## Objetivo
Plataforma em nuvem para contas, IAM, serviços de computação, armazenamento, rede, sem servidor, contêiner, banco de dados e registro.

## Tipo de plataforma
Plataforma em nuvem

## Como funciona
- A atividade do plano de controle normalmente é capturada por meio de CloudTrail e logs de serviço relacionados quando integrados.
- O risco da nuvem deve ser analisado por conta, região, identidade, exposição pública, criticidade dos ativos e sensibilidade dos dados.
- Nesta biblioteca, a postura AWS é representada principalmente por meio de tabelas Orca e network/SASE até que os logs nativos AWS sejam conectados.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)

## O que revisar
- Uso de conta raiz, alterações de política IAM, criação de chave de acesso, atividade incomum AssumeRole e caminhos de escalonamento de privilégios.
- Buckets S3 públicos, serviços expostos, alterações de grupos de segurança, compartilhamento de snapshots e desativação de registros.
- Novas regiões, nova computação, saída incomum, exposição de segredos e vulnerabilidades críticas em ativos voltados para a Internet.

## Coisas de segurança para observar
- IAM e as chaves de acesso costumam ser a camada de acesso durável após o comprometimento da nuvem.
- Armazenamento público, grupos de segurança permissivos e registro desativado são sinais de exposição de alta prioridade.
- As buscas na nuvem precisam de propriedade de ativos e contexto de negócios para evitar o afogamento na automação esperada.

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
