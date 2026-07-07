# Oracle Cloud

## Objetivo
Plataforma de nuvem para locação OCI, identidade, computação, rede, armazenamento, bancos de dados e descobertas de postura de nuvem.

## Tipo de plataforma
Plataforma em nuvem

## Como funciona
- OCI deve ser modelado por locação, compartimento, identidade, recurso e região.
- Esta biblioteca atualmente espera descobertas de postura por meio do Orca até que os logs OCI nativos sejam conectados.
- Banco de dados, armazenamento, identidade e exposição na rede pública são áreas de revisão de alto valor.

## Como esta biblioteca a utiliza
- Vincula o comportamento da plataforma às tabelas Sentinel abaixo.
- Usa o contexto da plataforma para decidir quais caçadas pertencem à cadência diária, semanal, intel ou mensal.
- Ajuda os analistas a entender se um evento é administração normal, configuração incorreta, exposição ou comportamento suspeito.

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)

## O que revisar
- alterações de política IAM, criação de chave user/API, alterações de federação e concessões de privilégios em nível de compartimento.
- Buckets públicos, computação exposta, acesso ao banco de dados, alterações na lista de segurança e configuração de log.
- Descobertas de postura crítica, exposição de segredos e cargas de trabalho vulneráveis voltadas para a Internet.

## Coisas de segurança para observar
- O design do compartimento pode ocultar o acesso com permissão excessiva se não for revisado com a criticidade dos recursos.
- Os serviços de banco de dados e armazenamento OCI podem conter dados confidenciais e precisam de linhas de base de acesso separadas.
- A integração de log nativo deve ser um item de roteiro se OCI for crítico para os negócios.

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
