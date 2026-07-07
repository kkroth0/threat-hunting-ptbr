# GCP

## Objetivo
Plataforma em nuvem para projetos, IAM, contas de serviço, computação, armazenamento, BigQuery, Kubernetes e logs de auditoria.

## Tipo de plataforma
Plataforma em nuvem

## Como funciona
- A atividade GCP deve ser modelada em torno de organização, pasta, projeto, conta de serviço e recurso.
- Os logs de auditoria nativos ainda não estão mapeados diretamente nesta biblioteca, portanto a postura e o contexto da rede são os pontos de partida atuais.
- Chaves de conta de serviço, ligações IAM e logs de acesso a dados são as principais superfícies de busca, uma vez conectadas.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)

## O que revisar
- Novas chaves de conta de serviço, alterações de vinculação IAM, concessões do proprietário do projeto e alterações de identidade da carga de trabalho.
- Buckets públicos, exportações BigQuery, registro de alterações no coletor, alterações no firewall e novos IPs externos.
- Criação incomum de projetos, uso de região, alterações no Kubernetes e movimentação de dados para destinos externos.

## Coisas de segurança para observar
- As contas de serviço são caminhos comuns de persistência e privilégio em GCP.
- BigQuery e Cloud Storage precisam de registro de acesso a dados para buscas de exfiltração significativas.
- A exclusão ou o redirecionamento do coletor de registro pode indicar evasão de defesa.

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
