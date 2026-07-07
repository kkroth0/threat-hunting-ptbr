# Azure

## Objetivo
Plano de controle de nuvem primário e plataforma adjacente de identidade para esta biblioteca.

## Tipo de plataforma
Plataforma em nuvem

## Como funciona
- AzureActivity registra operações do plano de gerenciamento, como gravações de recursos, exclusões, atribuições de funções e alterações de política.
- AzureDiagnostics fornece logs de nível de serviço onde o diagnóstico de recursos está habilitado.
- Os dados de login e auditoria Entra ID devem ser associados às operações Azure para conectar a identidade à ação na nuvem.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [AzureActivity](../../sentinel/tables/reference/AzureActivity.md)
- [AzureDiagnostics](../../sentinel/tables/reference/AzureDiagnostics.md)
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)

## O que revisar
- Alterações na atribuição de funções, concessões owner/contributor, credenciais principais de serviço e alterações de identidade privilegiadas.
- IPs públicos, armazenamento exposto, acesso ao Key Vault, alterações nas configurações de diagnóstico e exclusão de recursos.
- Novas assinaturas, grupos de recursos, contas de automação, máquinas virtuais e alterações em grupos de segurança de rede.

## Coisas de segurança para observar
- O comprometimento Azure geralmente passa por Entra ID, entidades de serviço e atribuições de função.
- As configurações de diagnóstico e os controles de registro são de alto valor porque os invasores podem reduzir a visibilidade.
- Os ativos do Key Vault, do armazenamento e da automação merecem uma revisão de base mais rigorosa.

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
