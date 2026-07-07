# LATAM Inteligência de ameaças e caça regional

Use esta página quando uma caçada precisar de contexto regional para a América Latina, especialmente Brasil, México, Colômbia, Chile, Argentina, Peru e toda a região Caribbean/Central/South América.

A caça focada em LATAM é importante porque as ameaças regionais geralmente usam idioma local, marcas locais, sistemas de pagamento locais, temas do governo local e infraestrutura específica do país. Um feed global genérico pode perder o contexto que torna um evento suspeito no Brasil ou no México.

## Foco Regional
| Área de foco | Por que é importante |
| --- | --- |
| Brasil | Grande ecossistema bancário digital, fraude PIX/payment, forte phishing em língua portuguesa, segmentação governamental e empresarial. |
| México | Grande presença empresarial e industrial, relevância governamental e de telecomunicações, phishing em espanhol, ransomware e exposição a extorsão. |
| Colômbia | Campanhas governamentais, financeiras, de saúde e phishing/malware com atrações locais. |
| Chile | Serviços financeiros, mineração, telecomunicações, adoção de nuvem e inteligência regional CSIRT/MISP. |
| Argentina | Setor público, finanças, energia e engenharia social em língua espanhola. |
| Peru e LATAM mais amplo | Mineração, energia, logística, governo, varejo e exposição ransomware/extortion. |

## Temas de ameaças para rastrear
| Tema | Exemplos | Tabelas Sentinel |
| --- | --- | --- |
| Phishing regional e representação de marca | Tributário, bancário, portais governamentais, notas fiscais, notificações judiciais, delivery, folha de pagamento, links de pagamento. | `OfficeActivity`, `SigninLogs`, `NetskopeEventsApplication_CL`, `Cloudflare_CL`. |
| Trojans bancários e infostealers | Grandoreiro, Mekotio, BBTok, Casbaneiro/Metamorfo, Guildma, Ousaban, Lumma, RedLine, Vidar. | `TrendMicro_XDR_OAT_CL`, `TrendMicro_XDR_WORKBENCH_CL`, `SecurityEvent`, `WindowsEvent`, `NetskopeAlerts_CL`. |
| Fraude de pagamento | Abuso de PIX, fraude de boleto/invoice, portais de pagamento falsos, iscas com tema SPEI do México. | `SigninLogs`, `OfficeActivity`, `NetskopeEventsApplication_CL`, `Cloudflare_CL`, logs de aplicativos quando disponíveis. |
| Ransomware e extorsão | Setor público, saúde, educação, energia, manufatura, serviços profissionais, finanças. | `SecurityIncident`, `SecurityAlert`, `TrendMicro_XDR_*`, `CommonSecurityLog`, `Netskope*`, `OrcaAlerts_CL`. |
| Corretores de acesso inicial | Venda de credenciais, acesso à conta RDP/VPN/cloud, sessões vazadas, fadiga MFA. | `SigninLogs`, `AuditLogs`, `IdentityInfo`, `BehaviorAnalytics`, `CommonSecurityLog`. |
| Abuso de nuvem e SaaS | Abuso de consentimento do OAuth, viagens impossíveis, novos aplicativos arriscados, alterações administrativas, roubo de tokens. | `SigninLogs`, `AuditLogs`, `OfficeActivity`, `AzureActivity`, `NetskopeEventsApplication_CL`. |
| WAF, bot e preenchimento de credenciais | Abuso de login em portais públicos, raspagem de API, campanhas de bot, padrões maliciosos de ASN. | `Cloudflare_CL`, `CommonSecurityLog`, `NetskopeEventsConnection_CL`. |
| Hacktivismo e DDoS | Eventos políticos regionais, segmentação governamental, segmentação media/brand. | `Cloudflare_CL`, `CommonSecurityLog`, `SecurityAlert`. |
| OT e infraestrutura crítica | Energia, mineração, telecomunicações, logística, manufatura, serviços públicos. | `CommonSecurityLog`, `Syslog`, `AzureActivity`, `OrcaAlerts_CL`, logs OT personalizados quando integrados. |

## LATAM Mapa de origem
| Fonte | Região | Usar para |
| --- | --- | --- |
| [CSIRTAmericas](https://csirtamericas.org/en) | Américas | Coordenação regional CSIRT, alertas e troca de informações sobre ameaças. |
| [OAS Programa de segurança cibernética](https://www.oas.org/ext/en/security/cybersecurity-technical-program) | Américas | Cooperação regional em cibersegurança e contexto de capacidade CSIRT. |
| [LACNIC CSIRT](https://csirt.lacnic.net/) | LATAM/Caribbean | Diretório regional CSIRT, projetos de segurança, contexto de honeynet e infraestrutura de internet. |
| [LACNIC CSIRTs da região](https://csirt.lacnic.net/csirts-de-la-region) | LATAM/Caribbean | Descoberta de país CSIRT e mapeamento de contatos regionais. |
| [CERT.br](https://cert.br/en/) | Brasil | Coordenação de incidentes no Brasil, consciência situacional, estatísticas e orientação de segurança. |
| [CERT.br Brasileiro CSIRTs](https://www.cert.br/csirts/brazil/) | Brasil | Ecossistema CSIRT brasileiro e descoberta de contato setorial. |
| [CTIR Gov-BR](https://www.gov.br/ctir) | Governo do Brasil | Resposta a incidentes do governo federal brasileiro e avisos oficiais. |
| [CAIS/RNP](https://www.rnp.br/sistema-rnp/cais) | Rede Brasil academic/research | Alertas, resposta e coordenação da rede acadêmica. |
| [CERT-MX](https://www.gob.mx/gncertmx) | México | Resposta nacional a incidentes no México e orientação oficial. |
| [FIRST CERT-MX Perfil](https://www.first.org/members/teams/cert-mx) | México | identidade CERT-MX, contato e referência de associação FIRST. |
| [ColCERT](https://www.colcert.gov.co/800/w3-channel.html) | Colômbia | Boletins cibernéticos, avisos e coordenação do setor public/private na Colômbia. |
| [ColCERT Boletins](https://www.colcert.gov.co/800/w3-propertyvalue-412601.html) | Colômbia | Alertas de vulnerabilidade e campanha, incluindo Azure AD e temas de malware. |
| [CC-CSIRT Polícia Colômbia](https://cc-csirt.policia.gov.co/) | Colômbia | Crimes cibernéticos, phishing, alertas de malware e publicações IOC. |
| [CSIRT Governo do Chile](https://www.csirt.gob.cl/) | Chile | Alertas CSIRT nacionais do Chile, avisos e recursos IOC/MISP-related. |
| [CERT.ar](https://www.argentina.gob.ar/jefatura/innovacion-publica/ssetic/direccion-nacional-ciberseguridad/cert-ar) | Argentina | Resposta a incidentes do setor público na Argentina e orientação oficial. |
| [CERTuy](https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/politicas-y-gestion/certuy) | Uruguai | Orientação CERT nacional do Uruguai e contexto de resposta a incidentes. |

## Fornecedores regionais e fontes de pesquisa
| Fonte | Usar para |
| --- | --- |
| [CrowdStrike LATAM Relatório de cenário de ameaças](https://www.crowdstrike.com/en-us/resources/reports/latam-threat-landscape-report/) | LATAM adversário, ransomware, eCrime, corretor de acesso e tendências de intrusão direcionada. |
| [Pesquisa futura registrada LATAM](https://www.recordedfuture.com/research/latin-america-and-the-caribbean-cybercrime-landscape) | LATAM ecossistema de crimes cibernéticos, fórum, telegrama, ransomware e contexto de fraude. |
| [Group-IB LATAM Insights de inteligência](https://www.group-ib.com/resources/research-hub/intelligence-insights-latam-april-2025-english-spanish/) | táticas cibercriminosas focadas em LATAM e relatórios de inteligência. |
| [ESET WeLiveSecurity](https://www.welivesecurity.com/en/) | pesquisa Spanish/Portuguese-accessible, trojans bancários LATAM, malware e relatórios APT. |
| [Kaspersky Securelist](https://securelist.com/) | LATAM malware bancário, crimes cibernéticos regionais e famílias de malware. |
| [Pesquisa da Trend Micro](https://www.trendmicro.com/en_us/research.html) | LATAM trojans bancários, nuvem, e-mail, endpoint e pesquisa de vulnerabilidades. |
| [Laboratórios FortiGuard](https://www.fortinet.com/blog/threat-research) | Tendências de ameaças de rede LATAM, pesquisa relevante para firewall, atividade IPS/vulnerability. |
| [Pesquisa de Check Point](https://research.checkpoint.com/) | tendências de ataque LATAM, relatórios de ransomware, nuvem e malware. |
| [NETSCOUT LATAM Relatório de ameaças](https://www.netscout.com/threatreport/region/latam/) | LATAM DDoS e contexto de tendência de ataque na Internet. |

## Notas sobre idioma e localização
Rastreie os termos em português e espanhol porque as campanhas de phishing e malware geralmente localizam as iscas.

| Tema | Termos em Português | Termos em espanhol |
| --- | --- | --- |
| Impostos e governo | `Receita Federal`, `CPF`, `CNPJ`, `DARF`, `Nota Fiscal`, `eSocial`, `Gov.br` | `SAT`, `RFC`, `factura`, `constancia fiscal`, `gobierno`, `tramite` |
| Pagamentos | `PIX`, `boleto`, `segunda via`, `comprovante`, `pagamento` | `SPEI`, `transferencia`, `comprobante`, `pago`, `factura` |
| Jurídico e HR | `intimacao`, `processo`, `audiencia`, `rescisao`, `holerite` | `citatorio`, `demanda`, `audiencia`, `nomina`, `finiquito` |
| Entrega e faturas | `pedido`, `rastreamento`, `correios`, `nota fiscal` | `paquete`, `rastreo`, `aduana`, `factura` |
| Bancário | `banco`, `token`, `senha`, `cartao`, `conta bloqueada` | `banco`, `token`, `contrasena`, `tarjeta`, `cuenta bloqueada` |

## Caçar ideias
| Ideia de caça | Método | Tabelas Sentinel |
| --- | --- | --- |
| Novas iscas de phishing Portuguese/Spanish que levam a downloads de arquivos executáveis ​​ou arquivados. | Intel ou baseado em hipóteses | `NetskopeEventsApplication_CL`, `OfficeActivity`, `TrendMicro_XDR_OAT_CL`. |
| PIX ou domínios com tema boleto acessados ​​por usuários corporativos. | Intel ou baseado em dados | `NetskopeEventsPage_CL`, `Cloudflare_CL`, `CommonSecurityLog`. |
| México SAT/SPEI-themed phishing e coleta de credenciais. | Orientado pela Intel | `NetskopeAlerts_CL`, `SigninLogs`, `OfficeActivity`. |
| Download do arquivo Grandoreiro/Mekotio-style seguido de script ou execução de processo suspeito. | Hipótese conduzida | `TrendMicro_XDR_OAT_CL`, `SecurityEvent`, `WindowsEvent`, `NetskopeEventsApplication_CL`. |
| Tentativas de login de países LATAM normalmente não usados ​​por um usuário ou entidade de serviço. | Dados ou modelo assistido | `SigninLogs`, `IdentityInfo`, `BehaviorAnalytics`. |
| Alteração da função de administrador após login bem-sucedido de um novo LATAM ASN ou país. | Hipótese conduzida | `SigninLogs`, `AuditLogs`, `AzureActivity`. |
| Aumento do endpoint de login voltado ao público durante campanha regional ou evento político. | Orientado por dados | `Cloudflare_CL`, `CommonSecurityLog`, `SecurityAlert`. |
| Atividade precursora de ransomware em unidades de negócios LATAM. | Hipótese conduzida | `TrendMicro_XDR_*`, `SecurityEvent`, `CommonSecurityLog`, `OrcaAlerts_CL`. |
| Exfiltração de dados para armazenamento em nuvem incomum ou aplicativos de compartilhamento de arquivos. | Dados ou modelo assistido | `NetskopeEventsApplication_CL`, `NetskopeAlerts_CL`, `CommonSecurityLog`. |

## Listas de observação regionais
Crie listas de observação Sentinel para contexto regional:

- `LATAM_Critical_Assets`: região, país, unidade de negócio, proprietário, ambiente, criticidade.
- `LATAM_Approved_Admin_IPs`: país, escritório, intervalo VPN, intervalo de bastiões, proprietário.
- `LATAM_High_Risk_Brands`: marcas e domínios locais comumente personificados.
- `LATAM_Allowed_SaaS`: aplicativos SaaS aprovados por país ou unidade de negócios.
- `LATAM_VIP_Users`: executivos, finanças, folha de pagamento, tesouraria, jurídico e usuários administradores locais.
- `LATAM_Payment_Systems`: PIX, boleto, SPEI, portais bancários, processadores de pagamento, aplicativos de tesouraria.
- `LATAM_Regional_IOCs`: IOCs regional com limite de tempo de CSIRTs, fornecedores ou resposta a incidentes.

## Mapeamento Sentinel
| Pergunta | Tabelas | Enriquecimento |
| --- | --- | --- |
| Um usuário foi autenticado em um novo país LATAM ou ASN? | `SigninLogs` | `IdentityInfo`, `BehaviorAnalytics`, listas de observação country/IP aprovadas. |
| Os usuários visitaram phishing ou malware regional URLs? | `NetskopeEventsPage_CL`, `NetskopeEventsApplication_CL`, `Cloudflare_CL` | Lista de observação regional IOC, domínio age/reputation, informações sobre ameaças. |
| A atividade do endpoint correspondeu ao comportamento do trojan bancário LATAM? | `TrendMicro_XDR_OAT_CL`, `WindowsEvent`, `SecurityEvent` | Reputação de hash de arquivo, padrões de processo parent/child, fonte de download. |
| Um aplicativo público recebeu tráfego regional suspeito? | `Cloudflare_CL`, `CommonSecurityLog` | JA3/JA4, ASN, país, ação WAF, pontuação do bot. |
| Um usuário privilegiado alterou o acesso após login suspeito? | `SigninLogs`, `AuditLogs`, `AzureActivity`, `CyberArk_AuditEvents_CL` | lista de observação VIP/admin, intervalos de administração IP conhecidos. |
| Os ativos LATAM estão expostos ou vulneráveis ​​à exploração de CVEs? | `OrcaAlerts_CL`, `AzureActivity`, `AzureDiagnostics` | Lista de observação de ativos críticos, CISA KEV, avisos de fornecedores. |

## Ritmo operacional
| Cadência | LATAM Tarefa |
| --- | --- |
| Diariamente | Revise CISA KEV, CERT.br, CTIR Gov, CERT-MX, CSIRTAmericas, postagens de principais fornecedores, notícias sobre ransomware. |
| Semanalmente | Revise a atividade da unidade de negócios LATAM: anomalias de identidade, bloqueios da web, alertas DLP, alertas de endpoint, picos WAF/bot. |
| Orientado pela Intel | Converta IOCs regional, iscas, nomes de malware, CVEs e relatórios de campanha em consultas Sentinel. |
| Mensalmente | Revise as lacunas de cobertura regional, listas de observação, mapeamento de ativos, termos linguísticos e qualidade da fonte. |

## Lista de verificação de admissão de caça
Para cada item de inteligência LATAM, capture:

- País ou região.
- Idioma: Português, Espanhol, Inglês ou misto.
- Fonte e data.
- Tipo de ameaça: fraude, phishing, malware, ransomware, hacktivismo, vulnerabilidade, abuso na nuvem.
- Unidades de negócios ou países afetados.
- IOCs e TTPs.
- Marcas locais relevantes, sistemas de pagamento ou iscas governamentais.
- Tabelas Sentinel obrigatórias.
- Entidades esperadas.
- Cadência recomendada.
- Data de expiração para IOCs.

## Referências
- [CSIRTAmericas](https://csirtamericas.org/en)
- [OAS Programa Técnico de Segurança Cibernética](https://www.oas.org/ext/en/security/cybersecurity-technical-program)
- [LACNIC CSIRT](https://csirt.lacnic.net/)
- [CERT.br](https://cert.br/en/)
- [CTIR Gov-BR](https://www.gov.br/ctir)
- [perfil FIRST CERT-MX](https://www.first.org/members/teams/cert-mx)
- [ColCERT](https://www.colcert.gov.co/800/w3-channel.html)
- [CrowdStrike LATAM Relatório de cenário de ameaças](https://www.crowdstrike.com/en-us/resources/reports/latam-threat-landscape-report/)
- [Futuro registrado LAC Cenário de crimes cibernéticos](https://www.recordedfuture.com/research/latin-america-and-the-caribbean-cybercrime-landscape)
