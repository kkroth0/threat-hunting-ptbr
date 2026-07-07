# Casos de uso e desenvolvimento de detecção

Use esta seção depois que uma busca produz lógica que deve ser executada repetidamente como detecção, regra analítica, pasta de trabalho, processo de lista de observação ou controle operacional.

O objetivo é transformar o conhecimento de caça em um caso de uso de segurança confiável:

```text
Hunt finding -> detection hypothesis -> analytic logic -> testing -> tuning -> deployment -> lifecycle review
```

## O que é um caso de uso?
Um caso de uso é um cenário documentado de detecção ou monitoramento que explica:

- Qual comportamento deve ser detectado.
- Por que o comportamento é importante.
- Quais tabelas e campos Sentinel são obrigatórios.
- Quais ferramentas geram os dados.
- Qual lógica KQL identifica o comportamento.
- Como validar verdadeiros positivos.
- Quais falsos positivos são esperados.
- O que o SOC deve fazer ao disparar.
- Como a detecção será ajustada e revisada.

## Quando uma caça se torna um caso de uso
Promova uma caçada quando uma ou mais forem verdadeiras:

- O comportamento é de alto risco e repetível.
- A caça encontrou atividades maliciosas ou suspeitas confirmadas.
- O mesmo padrão aparece em diversas caçadas.
- A lógica é estável o suficiente para ser executada de acordo com um cronograma.
- Os falsos positivos são compreendidos e ajustáveis.
- A fonte de dados é confiável.
- A saída tem um proprietário de resposta claro.
- O caso de uso preenche uma importante lacuna de detecção.

Não promova uma caçada ainda quando:

- Os campos obrigatórios estão ausentes ou inconsistentes.
- A consulta só funciona com interpretação manual do analista.
- O volume do resultado é muito alto e não é explicável.
- O proprietário da empresa ou a ação de resposta não são claros.
- A fonte de telemetria não está estável.

## Ciclo de vida do caso de uso
| Fase | Meta | Saída |
| --- | --- | --- |
| Ingestão | Capture a ideia de detecção de uma caçada, incidente, item de informação ou lacuna. | Use o rascunho do caso. |
| Projeto | Defina escopo, entidades, tabelas, gravidade, lógica e resposta. | Projeto de detecção. |
| Construir | Converta Hunt KQL em lógica de detecção agendada. | regra analítica Sentinel ou consulta de pasta de trabalho. |
| Teste | Valide com base em dados históricos e exemplos benignos conhecidos. | Notas de teste e alterações de ajuste. |
| Sintonia | Reduza o ruído com limites, junções, listas de observação e exclusões. | Pronto para produção KQL. |
| Implantar | Crie a regra analítica Sentinel e as configurações de incidente. | Detecção ativa. |
| Operar | Monitore alertas, falsos positivos, qualidade de incidentes e feedback de analistas. | Atraso de ajuste. |
| Revisão | Reavalie a lógica, as tabelas, a relevância das ameaças e os manuais de resposta. | Caso de uso atualizado ou retirado. |

## Design de caso de uso Sentinel
| Componente | Orientação |
| --- | --- |
| Nome da regra | Use uma nomenclatura clara que prioriza o comportamento, como `Suspicious PowerShell Encoded Command`. |
| Descrição | Explique o comportamento do adversário, as evidências esperadas e por que a regra é importante. |
| Táticas e técnicas | Mapeie para MITRE ATT&CK sempre que possível. |
| Gravidade | Use impacto e confiança, não apenas o volume de resultados da consulta. |
| Frequência de consulta | Combine a velocidade de comportamento esperada e a latência de dados. |
| Período de consulta | Longo o suficiente para detectar comportamento, curto o suficiente para evitar ruído. |
| Entidades | Mapeie conta, host, IP, URL, hash de arquivo, recurso de nuvem e campos de incidente. |
| Detalhes personalizados | Adicione campos que ajudem na triagem sem reabrir a consulta. |
| Agrupamento | Agrupe eventos em incidentes quando eles pertencerem ao mesmo usuário, host, IP ou recurso. |
| Supressão | Use com cautela; prefira ajustar a lógica primeiro. |
| Listas de observação | Use para IPs de administrador aprovados, VIPs, ativos de alto risco, listas de permissões e contexto regional. |
| Automação | Adicione manuais somente depois que a detecção estiver estável. |

## Fluxo de trabalho de busca para detecção
1. Comece a partir de uma página de busca concluída.
2. Copie o KQL final em um rascunho de caso de uso.
3. Identifique o comportamento e as entidades sobre as quais a regra deve alertar.
4. Remova colunas de exploração somente para analistas.
5. Adicione resumo e limites apropriados para execução agendada.
6. Adicione junções de enriquecimento somente se elas melhorarem a triagem.
7. Adicione tratamento de falsos positivos usando listas de observação ou condições explícitas.
8. Teste por pelo menos 30 dias quando o volume de dados permitir.
9. Revise alertas de amostra com SOC/IR antes da produção.
10. Implante como uma regra analítica Sentinel.
11. Revise após a primeira semana, primeiro mês e depois trimestralmente.

## Lista de verificação de teste
| Teste | Pergunta |
| --- | --- |
| Disponibilidade de dados | Todas as tabelas obrigatórias estão preenchidas para o lookback? |
| Qualidade de campo | Os campos-chave são preenchidos de forma consistente? |
| Repetição histórica | Quantos alertas teriam sido disparados nos últimos 7, 14 ou 30 dias? |
| Revisão benigna conhecida | Os padrões esperados de administração, scanner, automação ou negócios são excluídos ou documentados? |
| Simulação verdadeiro-positiva | O Atomic Red Team, o Red Team, os dados de laboratório ou os dados de incidentes conhecidos podem acioná-lo? |
| Mapeamento de entidades | O Sentinel cria entidades úteis de conta, host, IP, URL, arquivo ou nuvem? |
| Agrupamento de incidentes | Um comportamento cria um incidente útil em vez de muitas duplicatas? |
| capacidade de ação SOC | Um analista pode decidir o que fazer com base nos detalhes do alerta? |
| Impacto nos custos | A consulta é eficiente o suficiente para ser executada dentro do cronograma? |

## Padrões de ajuste
| Problema | Opção de ajuste |
| --- | --- |
| Muitos acessos de administrador conhecidos | Junte-se a um administrador aprovado IP ou a uma lista de observação de usuários administradores. |
| Muitos acessos à conta de serviço | Exclua identidades gerenciadas ou marque entidades de serviço de alto risco separadamente. |
| Muitos acessos do scanner | Adicione IPs de scanner, agentes de usuário de scanner ou contas de gerenciamento de vulnerabilidades às listas de observação. |
| Muitos blocos de baixo valor | Alerte apenas sobre bloqueios repetidos, países de risco, aplicativos críticos ou atividades de acompanhamento bem-sucedidas. |
| Contexto ausente | Junte-se a `IdentityInfo`, `BehaviorAnalytics`, `Watchlist`, `SecurityIncident` ou contexto de ativo. |
| Tabela de alerta de fornecedor barulhenta | Filtre por gravidade, confiança, nível de risco, status ou capacidade de ação. |

## Categorias de casos de uso
| Categoria | Exemplos de casos de uso | Tabelas |
| --- | --- | --- |
| Identidade | Spray de senha seguido de sucesso, viagem impossível, MFA suspeito, nova atribuição administrativa. | `SigninLogs`, `AuditLogs`, `IdentityInfo`, `BehaviorAnalytics`. |
| Ponto final | Xqzph00000xqz codificado, cadeia de processo suspeita, comportamento de despejo de credenciais, precursor de ransomware. | `SecurityEvent`, `WindowsEvent`, `TrendMicro_XDR_OAT_CL`. |
| Rede | Pico de tráfego negado, correlação IP maliciosa, destino de saída raro, padrão DDoS/WAF. | `CommonSecurityLog`, `Cloudflare_CL`, `NetskopeEventsNetwork_CL`. |
| SaaS e DLP | Acesso não autorizado a aplicativos, downloads incomuns, compartilhamento externo, padrões de alerta DLP. | `NetskopeAlerts_CL`, `NetskopeEventsApplication_CL`, `OfficeActivity`. |
| Nuvem | Atribuição de função arriscada, abuso de comando de execução VM, exposição pública, descoberta de postura crítica. | `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL`. |
| Intel | correspondência IOC, varredura da campanha TTP, campanha regional LATAM, exposição CVE explorada. | `ThreatIntelIndicators`, `Watchlist`, tabelas específicas de origem. |
| operações Sentinel | Falha no conector, queda na ingestão, detecção de ruído, incidentes sem dono. | `SentinelHealth`, `Usage`, `SecurityIncident`, `SecurityAlert`. |

## Métricas de qualidade de detecção
Acompanhe-os após a implantação:

- Alertas por day/week.
- Incidentes criados.
- Verdadeiros positivos.
- Falsos positivos.
- Descobertas benignas, mas úteis.
- Tempo médio para triagem.
- Tempo médio para fechar.
- Principais entidades.
- Principais razões falso-positivas.
- Data da última revisão.
- Mudanças de ajuste necessárias.

## Revise a cadência
| Tempo | Revise o foco |
| --- | --- |
| Primeiros 7 dias | Volume de alertas, falsos positivos, falhas de consulta, feedback SOC. |
| Primeiros 30 dias | Valor de detecção, gravidade, agrupamento, listas de observação, propriedade. |
| Trimestralmente | Relevância da ameaça, mapeamento ATT&CK, qualidade dos dados, desempenho, decisão de aposentadoria. |
| Após incidente | Este caso de uso disparou? Deveria ter disparado antes? Que evidências estavam faltando? |

## Documentação necessária
Cada caso de uso deve ter:

- Proprietário do caso de uso.
- Página de caça vinculada.
- Arquivo KQL vinculado ou regra analítica ID.
- tabelas e ferramentas Sentinel.
- mapeamento MITRE ATT&CK.
- Fundamentação da severidade e da confiança.
- Notas falso-positivas.
- Etapas de triagem.
- Proprietário da resposta.
- Data da revisão.
- Alterar histórico.

## Modelo
Use [Modelo de caso de uso](../templates/use-case-template.md) para documentar novas detecções.

## Seções relacionadas
- [Biblioteca de caça](../hunts/README.md)
- [Biblioteca KQL](../sentinel/kql/README.md)
- [Catálogo de tabelas Sentinel](../sentinel/tables/index.md)
- [Normalização de campo](../sentinel/tables/field-normalization.md)
- [Modelo de caça](../templates/hunt-template.md)
