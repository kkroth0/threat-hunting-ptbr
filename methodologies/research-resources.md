# Recursos de pesquisa

Use esta página para transformar notícias, inteligência de fornecedores, relatórios de vulnerabilidade, observações internas e exploração de dados em ideias de busca.

O objetivo não é ler tudo todos os dias. O objetivo é rastrear fontes de sinal alto suficientes para que você possa decidir:

- Isso é relevante para o nosso meio ambiente?
- Quais tabelas Sentinel podem comprovar ou refutar a exposição?
- Isso deveria se tornar uma caça diária, semanal, Intel ou mensal?
- Isso deve se tornar uma detecção, uma lista de observação, uma pasta de trabalho, uma correção do analisador ou um item de lista de pendências?

## Cadência de rastreamento
| Cadência | Fontes | Saída |
| --- | --- | --- |
| Diariamente | CISA KEV, principais notícias, blogs de fornecedores de ferramentas que você possui, conversas de exploração ativa, incidentes Sentinel. | Buscas de informações no mesmo dia, verificações urgentes de exposição, varreduras IOC. |
| Semanalmente | Pesquisa de fornecedores, relatórios de ransomware, pesquisa cloud/SaaS/identity, detecção de conteúdo. | Novas hipóteses, buscas de base, candidatos à detecção. |
| Mensalmente | Relatórios de tendências, cobertura ATT&CK, cobertura de detecção, qualidade da tabela, custo e revisão de ingestão. | Atualizações de roteiros, lacunas de cobertura, novas caçadas recorrentes. |
| Orientado a eventos | Crítico CVE, exploração ativa, segmentação por setor, incidente, descoberta da equipe vermelha. | Busca prioritária de informações ou suporte de resposta a incidentes. |

## Tipos de Fonte
| Fonte | Usar para | Saída |
| --- | --- | --- |
| Notícias | Conscientização rápida de campanhas ativas, violações, ondas de exploração e vítimas de ransomware. | Notas de triagem e possíveis buscas de informações. |
| Avisos governamentais | Exploração confirmada, vulnerabilidades, mitigações, orientação a nível nacional. | Revisão de exposição e tarefas patch/hunt priorizadas. |
| Inteligência do fornecedor | TTPs, comportamento de malware, rastreamento de atores, lógica de detecção, IOCs. | Caça de hipóteses, informações e engenharia de detecção. |
| Inteligência de vulnerabilidade | CVEs, explorabilidade, exploração em estado selvagem, produtos afetados. | Exposição de ativos e caça a atividades de exploração. |
| Feeds de malware e phishing | Domínios, URLs, hashes, padrões de tráfego, comportamento de carga útil. | varreduras IOC e caçadas network/email. |
| Pesquisa em nuvem e SaaS | Abuso do plano de controle da nuvem, ataques de identidade, exposição de dados SaaS. | Caça à nuvem, identidade e SaaS. |
| Inteligência interna | Incidentes, ataques fracassados, red team, pentest, tickets SOC, lacunas de detecção. | Caças de alta confiança adaptadas ao seu ambiente. |
| Exploração de fontes de dados | Novas tabelas Sentinel, novas ferramentas, novos campos, novos analisadores. | Linhas de base baseadas em dados e melhorias de cobertura. |

## Notícias diárias e amplos relatórios de segurança
Acompanhe-os para obter uma consciência rápida, não como a verdade final. Converta itens relevantes em pesquisas de fonte primária antes de escrever detecções.

| Fonte | Usar para |
| --- | --- |
| [BleepingComputer](https://www.bleepingcomputer.com/) | Violações, ransomware, vulnerabilidades exploradas, campanhas de malware. |
| [O registro](https://therecord.media/) | Política cibernética, invasões, ransomware, relatórios de ameaças geopolíticas. |
| [SecurityWeek](https://www.securityweek.com/) | Vulnerabilidade, segurança empresarial e notícias sobre incidentes. |
| [Leitura Negra](https://www.darkreading.com/) | Relatórios e análises de segurança corporativa. |
| [CyberScoop](https://cyberscoop.com/) | Relatórios governamentais, políticos, de espionagem e de crimes cibernéticos. |
| [KrebsOnSecurity](https://krebsonsecurity.com/) | Investigações de fraude, crime cibernético, identidade e violação. |
| [Notícias sobre hackers](https://thehackernews.com/) | Notícias rápidas sobre segurança e resumos de pesquisas de fornecedores. |
| [Ajuda Segurança da Rede](https://www.helpnetsecurity.com/) | Notícias e resumos de pesquisas sobre segurança empresarial. |
| [Notícias de negócios arriscados](https://news.risky.biz/) | Resumo diário de notícias de segurança e acompanhamento de campanhas. |
| [SANS NewsBites](https://www.sans.org/newsletters/newsbites/) | Notícias selecionadas sobre segurança de alto sinal. |

## Avisos governamentais e oficiais
Use-os para priorização de alta confiança, especialmente para vulnerabilidades exploradas e avisos do setor.

| Fonte | Usar para |
| --- | --- |
| [CISA Avisos de segurança cibernética](https://www.cisa.gov/news-events/cybersecurity-advisories) | Exploração ativa, aconselhamento dos atores, mitigações. |
| [CISA Vulnerabilidades exploradas conhecidas](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Explorado priorizado CVEs. |
| [Alertas CISA](https://www.cisa.gov/news-events/alerts) | Alertas e orientações de segurança urgentes. |
| [StopRansomware](https://www.cisa.gov/stopransomware) | Avisos, guias e relatórios conjuntos sobre ransomware. |
| [NVD](https://nvd.nist.gov/) | enriquecimento CVE, CVSS, referências, produtos afetados. |
| [Programa CVE](https://www.cve.org/) | Registros CVE e referências CNA. |
| [notas de vulnerabilidade CERT/CC](https://kb.cert.org/vuls/) | Divulgação coordenada e notas de vulnerabilidade. |
| [UK NCSC Avisos](https://www.ncsc.gov.uk/section/keep-up-to-date/advisories) | UK avisos governamentais e orientações sobre ameaças. |
| [CERT-EU Publicações](https://cert.europa.eu/publications) | EU relatórios de ameaças e vulnerabilidades institucionais. |
| [Alertas do Centro de Segurança Cibernética Australiano](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories) | ACSC alertas, avisos e orientações de mitigação. |
| [JPCERT/CC](https://www.jpcert.or.jp/english/) | Alertas e análises de malware com foco no Japão. |
| [CERT.br](https://www.cert.br/) | Tratamento, estatísticas e orientações de incidentes com foco no Brasil. |

## Vulnerabilidade e Inteligência de Exploração
Use-os para decidir se um CVE deve acionar busca de exposição, validação de patch ou pesquisas de exploração.

| Fonte | Usar para |
| --- | --- |
| [FIRST EPSS](https://www.first.org/epss/) | Priorização de exploração baseada em probabilidade. |
| [Explorar-DB](https://www.exploit-db.com/) | Referências de código de exploração pública. |
| [Banco de dados de vulnerabilidades Rapid7](https://www.rapid7.com/db/) | Contexto de exploração e referências do módulo Metasploit. |
| [GitHub Comunicados de segurança](https://github.com/advisories) | Vulnerabilidades de pacotes de código aberto. |
| [Projeto Zero do Google](https://googleprojectzero.blogspot.com/) | Pesquisa profunda de vulnerabilidades e análise de exploração. |
| [VulnCheck](https://vulncheck.com/) | Inteligência de exploração e vulnerabilidade. |
| [GreyNoise](https://www.greynoise.io/) | Contexto da atividade de digitalização e exploração da Internet. |
| [Servidor de sombra](https://www.shadowserver.org/) | Exposição na Internet, digitalização e relatórios de sumidouros. |
| [Censys](https://search.censys.io/) | Pesquisa de exposição na Internet e descoberta de ativos. |
| [Shodan](https://www.shodan.io/) | Descoberta de serviços expostos à Internet. |

## Inteligência de ameaças de grandes fornecedores
Rastreie primeiro os fornecedores que você possui e, em seguida, adicione fontes de pesquisa mais amplas.

| Fonte | Usar para |
| --- | --- |
| [Blog de segurança da Microsoft](https://www.microsoft.com/en-us/security/blog/) | Inteligência de ameaças da Microsoft, identidade, nuvem e pesquisa relevante para Sentinel. |
| [Centro de Resposta de Segurança da Microsoft](https://msrc.microsoft.com/update-guide) | Microsoft CVEs e orientação de atualização de segurança. |
| [Microsoft Defender Inteligência de ameaças](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-threat-intelligence) | Contexto e pesquisa do produto Microsoft TI. |
| [Google Cloud Inteligência de ameaças](https://cloud.google.com/blog/topics/threat-intelligence) | Pesquisa de ameaças Mandiant/Google, relatórios de atores, análise de nuvem e malware. |
| [Grupo de análise de ameaças do Google](https://blog.google/threat-analysis-group/) | Pesquisa de estado-nação, spyware e abuso de plataforma. |
| [Unidade Palo Alto 42](https://unit42.paloaltonetworks.com/) | Pesquisa de atores de ameaças, malware, nuvem, vulnerabilidade e ransomware. |
| [Cisco Talos](https://blog.talosintelligence.com/) | Malware, vulnerabilidades, campanhas, pesquisa de defesa de rede. |
| [CrowdStrike Operações de contra-adversário](https://www.crowdstrike.com/en-us/blog/category.counter-adversary-operations/) | Rastreamento de adversários e técnicas de intrusão. |
| [Laboratórios SentinelOne](https://www.sentinelone.com/labs/) | Pesquisa de malware, endpoint, ator e vulnerabilidade. |
| [Laboratórios Elastic Security](https://www.elastic.co/security-labs) | Engenharia de detecção, malware, endpoint e pesquisa em nuvem. |
| [Sophos X-Ops](https://news.sophos.com/en-us/category/sophos-x-ops/) | Ransomware, malware, comportamento do invasor e aprendizados sobre incidentes. |
| [Pesquisa da Trend Micro](https://www.trendmicro.com/en_us/research.html) | Pesquisa de malware, vulnerabilidade, nuvem, e-mail e atores. |
| [Centro de Pesquisa Avançada Trellix](https://www.trellix.com/en-us/about/newsroom/stories/research.html) | Malware, vulnerabilidades, campanhas e relatórios de ameaças. |
| [Laboratórios FortiGuard](https://www.fortinet.com/blog/threat-research) | Ameaças de rede, malware, IPS e atividade de vulnerabilidade. |
| [Pesquisa de Check Point](https://research.checkpoint.com/) | Pesquisa de malware, vulnerabilidades, phishing, dispositivos móveis e atores. |
| [ESET WeLiveSecurity](https://www.welivesecurity.com/en/) | APT, malware, espionagem e pesquisa de ameaças regionais. |
| [Kaspersky Securelist](https://securelist.com/) | APT, malware, ICS, pesquisa móvel e de crimes cibernéticos. |
| [Insight sobre ameaças do Proofpoint](https://www.proofpoint.com/us/blog/threat-insight) | Ameaças por e-mail, phishing, BEC, roubo de credenciais e rastreamento de atores. |
| [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research) | Pesquisa de ameaças na Web, nuvem, malware, phishing e ameaças de rede. |
| [Netskope Laboratórios de ameaças](https://www.netskope.com/netskope-threat-labs) | SASE, SaaS, aplicativo em nuvem e pesquisa de movimentação de dados. |
| [Blog Cloudflare - Segurança](https://blog.cloudflare.com/tag/security/) | WAF, DDoS, bot, edge, internet e pesquisa de vulnerabilidades. |
| [Radar Cloudflare](https://radar.cloudflare.com/) | Tendências da Internet, interrupções, ataques, roteamento, domínio e observações de tráfego. |
| [Pesquisa de segurança da Akamai](https://www.akamai.com/blog/security-research) | Pesquisa de ataques em escala da Web, DDoS, bot, API e Internet. |
| [Grupo Insikt Futuro Gravado](https://www.recordedfuture.com/research) | Inteligência estratégica e operacional contra ameaças cibernéticas. |
| [Relatório de detecção de ameaças Red Canary](https://redcanary.com/threat-detection-report/) | Tendências de detecção, mapeamentos ATT&CK e comportamentos de endpoint. |
| [Blog da Caçadora](https://www.huntress.com/blog) | intrusões SMB, abuso de identidade, persistência e comércio de endpoint. |

## Nuvem, SaaS e pesquisa de identidade
Essas fontes são especialmente úteis para suas tabelas Sentinel, como `SigninLogs`, `AuditLogs`, `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL`, `Netskope*` e `Cloudflare_CL`.

| Fonte | Usar para |
| --- | --- |
| [Blog de segurança AWS](https://aws.amazon.com/blogs/security/) | orientação de segurança AWS, detecções de nuvem, GuardDuty, IAM e padrões de incidentes. |
| [AWS Boletins de segurança](https://aws.amazon.com/security/security-bulletins/) | boletins de segurança do serviço AWS. |
| [Blog de segurança Google Cloud](https://cloud.google.com/blog/products/identity-security) | Google Cloud segurança, identidade, detecção de ameaças na nuvem e SecOps. |
| [Blog de segurança Azure](https://techcommunity.microsoft.com/category/azure/blog/azuresecurity) | Azure orientações de segurança e atualizações de proteção na nuvem. |
| [Blog de entrada da Microsoft](https://techcommunity.microsoft.com/category/microsoft-entra/blog/microsoft-entra-blog) | Identidade, acesso condicional, Entra ID e gerenciamento de acesso. |
| [Blog de segurança Okta](https://sec.okta.com/articles/) | Ataques de identidade, detecções específicas do Okta e técnicas de adversários. |
| [Blog de Segurança Duo](https://duo.com/blog) | MFA, identidade, acesso, autenticação resistente a phishing. |
| [Laboratórios CyberArk](https://www.cyberark.com/resources/threat-research-blog) | Acesso privilegiado, roubo de credenciais, pesquisa de segurança de identidade. |
| [Blog SpecterOps](https://specterops.io/blog/) | Caminhos de ataque de identidade, pesquisa Active Directory, Entra ID, BloodHound. |
| [Blog Semperis](https://www.semperis.com/blog/) | Active Directory, Entra ID, recuperação de identidade e ataques de identidade híbrida. |
| [Pesquisa Wiz](https://www.wiz.io/blog/tag/research) | Vulnerabilidades na nuvem, caminhos de ataque, pesquisa de exposição na nuvem. |
| [Blog Orca Security](https://orca.security/resources/blog/) | Pesquisa de postura, exposição, identidade e vulnerabilidade da nuvem. |
| [Pesquisa de ameaças Sysdig](https://sysdig.com/blog/tag/threat-research/) | Container, Kubernetes, tempo de execução em nuvem e atividade de criptomineração. |
| [Aqua Nautilus](https://www.aquasec.com/blog/category/nautilus/) | Ameaças nativas da nuvem, contêineres, Kubernetes e cadeia de suprimentos. |
| [Blog de renda](https://www.lacework.com/blog) | Detecção de ameaças na nuvem, postura e pesquisa de carga de trabalho. |
| [Laboratórios de segurança Datadog](https://securitylabs.datadoghq.com/) | Pesquisa de nuvem, contêiner, aplicativo e identidade. |

## Cadeia de suprimentos e segurança de código aberto
Útil para ferramentas de desenvolvedor, abuso de pacotes, comprometimento CI/CD, risco de dependência e downloads suspeitos.

| Fonte | Usar para |
| --- | --- |
| [Laboratório de segurança GitHub](https://securitylab.github.com/) | Pesquisa de vulnerabilidade de código aberto e análise CodeQL. |
| [GitHub Comunicados de segurança](https://github.com/advisories) | Verificações de vulnerabilidade de pacote e exposição de dependência. |
| [Blog OpenSSF](https://openssf.org/blog/) | Orientações e incidentes de segurança da cadeia de suprimentos de código aberto. |
| [Pesquisa de segurança Snyk](https://snyk.io/blog/category/security-research/) | Vulnerabilidades de pacotes, contêineres, IaC e ecossistema de desenvolvedores. |
| [Blog Sonatype](https://www.sonatype.com/blog) | Malware em repositórios de pacotes e risco de dependência. |
| [Pesquisa de segurança JFrog](https://jfrog.com/blog/tag/security-research/) | Malware de pacotes, vulnerabilidades de código aberto e pesquisa da cadeia de suprimentos. |
| [Blog ReversingLabs](https://www.reversinglabs.com/blog) | Pesquisa de cadeia de suprimentos de software, malware e ecossistema de pacotes. |
| [Soquete Blog](https://socket.dev/blog) | npm, PyPI, comprometimento de dependência e abuso de conta do mantenedor. |

## OT, ICS e infraestrutura crítica
Útil quando o ambiente inclui manufatura, energia, operações de saúde, sistemas prediais ou redes industriais.

| Fonte | Usar para |
| --- | --- |
| [CISA ICS Avisos](https://www.cisa.gov/news-events/ics-advisories) | Vulnerabilidades e mitigações do sistema de controle industrial. |
| [Blog Dragos](https://www.dragos.com/blog/) | ICS inteligência de ameaças e análise de incidentes industriais. |
| [Equipe Claroty82](https://claroty.com/team82/research) | vulnerabilidades OT, IoT, XIoT e pesquisa de ameaças. |
| [Laboratórios de redes Nozomi](https://www.nozominetworks.com/blog/) | OT/IoT tendências de pesquisa, malware e segurança industrial. |
| [Notificações de segurança da Schneider Electric](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp) | Avisos de segurança de produtos Schneider. |
| [Siemens ProductCERT](https://new.siemens.com/global/en/products/services/cert.html) | Alertas de segurança de produtos da Siemens. |

## Pesquisa de dispositivos móveis, navegadores e spyware
Útil para proteção executiva, acesso móvel, abuso de extensões de navegador, roubo de tokens e investigações de phishing.

| Fonte | Usar para |
| --- | --- |
| [Grupo de análise de ameaças do Google](https://blog.google/threat-analysis-group/) | Spyware, explorações de navegadores, abuso de plataforma e campanhas estatais. |
| [Laboratório Cidadão](https://citizenlab.ca/) | Spyware, fornecedores de vigilância, segmentação móvel e ameaças à sociedade civil. |
| [Inteligência sobre ameaças do Lookout](https://www.lookout.com/threat-intelligence) | Relatórios de phishing, spyware e ameaças móveis. |
| [Blog de segurança da Mozilla](https://blog.mozilla.org/security/) | Risco de segurança do navegador, complementos, privacidade e plataforma web. |
| [Blog de segurança do Chrome](https://security.googleblog.com/) | Chrome, Android, segurança da plataforma Google e pesquisa de exploração. |

## E-mail, phishing e abuso de SaaS
Útil para dados `OfficeActivity`, `SigninLogs`, `AuditLogs`, `NetskopeAlerts_CL` e web/proxy.

| Fonte | Usar para |
| --- | --- |
| [Insight sobre ameaças do Proofpoint](https://www.proofpoint.com/us/blog/threat-insight) | Campanhas de e-mail, phishing, BEC, roubo de credenciais. |
| [Blog Cofense](https://cofense.com/blog/) | Tendências de phishing e análise de campanha. |
| [Blog de segurança anormal](https://abnormalsecurity.com/blog) | BEC, abuso de SaaS, comprometimento do fornecedor, ameaças por e-mail. |
| [Blog de Segurança Sublime](https://sublime.security/blog) | Lógica de detecção de e-mail e pesquisa de campanhas de phishing. |
| [Blog de segurança de materiais](https://material.security/blog) | Perspectivas de segurança de e-mail, identidade e segurança SaaS. |
| [Mandiant/Google Cloud Inteligência de ameaças](https://cloud.google.com/blog/topics/threat-intelligence) | Operações de intrusão de e-mail e análise de atores. |

## Malware, IOC e feeds de phishing
Use-os para varreduras IOC, buscas de tráfego de malware, investigações URL/domain e enriquecimento. Trate os feeds não verificados com cuidado e valide os acessos.

| Fonte | Usar para |
| --- | --- |
| [abuse.ch URLhaus](https://urlhaus.abuse.ch/) | Malware URLs e infraestrutura de entrega de carga útil. |
| [abuse.ch MalwareBazaar](https://bazaar.abuse.ch/) | Amostras de malware, hashes, famílias e tags. |
| [abuse.ch ThreatFox](https://threatfox.abuse.ch/) | Compartilhamento da comunidade IOC. |
| [Rastreador Feodo](https://feodotracker.abuse.ch/) | Rastreamento de botnet C2. |
| [OpenPhish](https://openphish.com/) | Phishing URLs. |
| [PhishTank](https://phishtank.org/) | Banco de dados de phishing comunitário URL. |
| [Spamhaus DROP e EDROP](https://www.spamhaus.org/drop/) | Intervalos de redes maliciosas conhecidos. |
| [Análise de tráfego de malware](https://www.malware-traffic-analysis.net/) | PCAPs e padrões de tráfego de malware para treinamento e detecções. |
| [ANY.RUN Inteligência contra ameaças cibernéticas](https://any.run/cybersecurity-blog/) | Análise de sandbox e relatórios de comportamento de malware. |
| [Análise Híbrida](https://www.hybrid-analysis.com/) | Análise de amostras de malware e enriquecimento de hash. |
| [VirusTotal](https://www.virustotal.com/) | Arquivo, URL, domínio e enriquecimento IP. |
| [VX-Subterrâneo](https://vx-underground.org/) | Amostras de malware e artigos para pesquisa. Manuseie com segurança. |
| [MALpedia](https://malpedia.caad.fkie.fraunhofer.de/) | Base de conhecimento da família de malware e referências YARA. |

## Rastreamento de ransomware e extorsão
Use-os para segmentação por setor, ransomware TTPs, análises de exposição e buscas de informações de emergência.

| Fonte | Usar para |
| --- | --- |
| [StopRansomware](https://www.cisa.gov/stopransomware) | Avisos e mitigações oficiais de ransomware. |
| [Ransomware.live](https://www.ransomware.live/) | Rastreamento de sites de vazamento de ransomware e atividade de grupo. |
| [Blog da Emsisoft](https://www.emsisoft.com/en/blog/) | Tendências de ransomware, decodificadores e relatórios de vitimologia. |
| [O Relatório DFIR](https://thedfirreport.com/) | Cronogramas de intrusão, precursores de ransomware, ferramentas e comandos. |
| [Sophos X-Ops](https://news.sophos.com/en-us/category/sophos-x-ops/) | Operações de ransomware e aprendizados de incidentes. |
| [Pesquisa de Ransomware da Unidade 42](https://unit42.paloaltonetworks.com/category/threat-research/ransomware/) | Tendências de ransomware, grupos e pesquisa de resposta. |

## Conteúdo de detecção e caça
Use-os para converter pesquisas em consultas, análises e testes repetíveis.

| Fonte | Usar para |
| --- | --- |
| [Manual do Caçador de Ameaças](https://threathunterplaybook.com/) | Metodologia de caça, fontes de dados, notebooks e análises. |
| [HEARTH](https://github.com/THORCollective/HEARTH) | Hipóteses de caça comunitária organizadas com categorias no estilo PEAK. |
| [Recursos HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Resources.md) | Procure recursos de ideias e refina o fluxo de trabalho. |
| [SigmaHQ](https://github.com/SigmaHQ/sigma) | Regras de detecção genéricas que podem inspirar KQL. |
| [Microsoft Sentinel GitHub](https://github.com/Azure/Azure-Sentinel) | análises Sentinel, consultas de busca, analisadores, pastas de trabalho e soluções. |
| [Conteúdo de segurança do Splunk](https://research.splunk.com/) | Lógica de detecção, mapeamentos ATT&CK e histórias analíticas. |
| [Regras de detecção elástica](https://github.com/elastic/detection-rules) | Lógica de detecção e ideias de caça. |
| [Equipe Vermelha Atômica Canário Vermelho](https://github.com/redcanaryco/atomic-red-team) | Testes atômicos para validação de detecções e caçadas. |
| [LOLBAS](https://lolbas-project.github.io/) | Windows binários e scripts que vivem fora da terra. |
| [GTFOBins](https://gtfobins.github.io/) | Binários Unix úteis para escalonamento de privilégios e buscas de evasão. |
| [WADComs](https://wadcoms.github.io/) | referências de comandos ofensivos Windows e Active Directory. |
| [Desproteger projeto](https://unprotect.it/) | Técnicas de evasão de malware e ideias de detecção. |

## Frameworks e bases de conhecimento
Use-os para rotular caçadas, explicar comportamento e construir mapas de cobertura.

| Fonte | Usar para |
| --- | --- |
| [MITRE ATT&CK](https://attack.mitre.org/) | Táticas, técnicas, procedimentos, grupos, software. |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Técnicas defensivas e mapeamento de contramedidas. |
| [MITRE CAPEC](https://capec.mitre.org/) | Padrões de ataque. |
| [CWE](https://cwe.mitre.org/) | Categorias de fraquezas de software. |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | Categorias de risco de aplicativos da Web. |
| [OWASP API 10 principais seguranças](https://owasp.org/www-project-api-security/) | Abuso de API e ideias de busca de aplicativos. |
| [Aliança de segurança em nuvem](https://cloudsecurityalliance.org/research) | Pesquisa e orientação sobre segurança na nuvem. |

## Fontes setoriais, regionais e comunitárias
Use fontes do setor quando elas corresponderem ao seu negócio. Use fontes regionais quando melhorarem o idioma, a geografia ou o contexto regulatório local.

Para o fluxo de trabalho regional, consulte [LATAM Inteligência de ameaças e caça regional](latam-threat-intelligence.md).

| Fonte | Usar para |
| --- | --- |
| [CSIRTAmericas](https://csirtamericas.org/en) | Alertas regionais CSIRT, compartilhamento de informações e assistência técnica nas Américas. |
| [LACNIC CSIRT](https://csirt.lacnic.net/) | Diretório LATAM/Caribbean CSIRT, projetos honeynet e contexto de segurança de infraestrutura da Internet. |
| [CERT.br](https://www.cert.br/) | Tratamento de incidentes no Brasil, estatísticas e orientações de segurança. |
| [CTIR Gov-BR](https://www.gov.br/ctir) | Resposta e avisos a incidentes do governo federal brasileiro. |
| [CAIS/RNP](https://www.rnp.br/sistema-rnp/cais) | Coordenação e alertas de segurança da rede acadêmica no Brasil. |
| [CERT-MX](https://www.gob.mx/gncertmx) | Resposta e orientação nacional a incidentes no México. |
| [ColCERT](https://www.colcert.gov.co/800/w3-channel.html) | Boletins cibernéticos, avisos e coordenação nacional da Colômbia. |
| [CSIRT Governo do Chile](https://www.csirt.gob.cl/) | Alertas CSIRT nacionais do Chile, avisos e recursos de inteligência de ameaças. |
| [MS-ISAC](https://www.cisecurity.org/ms-isac) | US avisos de segurança do governo estadual, local, tribal e territorial. |
| [FS-ISAC](https://www.fsisac.com/) | Inteligência e compartilhamento de ameaças ao setor financeiro. |
| [Saúde-ISAC](https://h-isac.org/) | Compartilhamento de ameaças cibernéticas no setor de saúde. |
| [Auto-ISAC](https://automotiveisac.com/) | Compartilhamento de segurança no setor automotivo. |
| [ENISA Cenário de ameaças](https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends) | EU cenário de ameaças, tendências do setor e relatórios estratégicos. |
| [Europol EC3](https://www.europol.europa.eu/about-europol/european-cybercrime-centre-ec3) | Relatórios de tendências do crime cibernético e contexto de aplicação da lei. |

## Boletins informativos e feeds selecionados
Use resumos selecionados para evitar a perda de itens importantes e, ao mesmo tempo, mantenha a revisão diária curta.

| Fonte | Usar para |
| --- | --- |
| [SANS Centro de tempestades na Internet](https://isc.sans.edu/) | Diário diário do manipulador, atividades de ataque e observações da comunidade. |
| [SANS NewsBites](https://www.sans.org/newsletters/newsbites/) | Notícias de segurança com curadoria duas vezes por semana. |
| [Notícias de negócios arriscados](https://news.risky.biz/) | Resumo diário de notícias de segurança e relatórios de ameaças. |
| [TLDR Segurança da Informação](https://tldrsec.com/) | Boletim informativo de segurança focado no profissional. |
| [CyberWire Diário](https://thecyberwire.com/podcasts/daily-podcast) | Podcast diário de notícias cibernéticas e resumos. |
| [Schneier sobre segurança](https://www.schneier.com/) | Análise de segurança, política e perspectiva de risco de longo prazo. |

## Watchlist específica da ferramenta
Acompanhe-os porque eles se alinham com as ferramentas já mapeadas nesta biblioteca.

| Área de Ferramentas | Fontes para priorizar | Tabelas Sentinel |
| --- | --- | --- |
| Microsoft Sentinel e Entra ID | Blog de segurança da Microsoft, MSRC, Blog Entra, Blog de segurança Azure. | `SigninLogs`, `AuditLogs`, `SecurityIncident`, `SecurityAlert`, `AzureActivity`. |
| Trend Vision One | Pesquisa Trend Micro. | `TrendMicro_XDR_OAT_CL`, `TrendMicro_XDR_WORKBENCH_CL`. |
| Netskope | Netskope Laboratórios de ameaças. | `NetskopeAlerts_CL`, `NetskopeEventsApplication_CL`, `NetskopeEventsNetwork_CL`, `NetskopeEventsPage_CL`. |
| Cloudflare | Blog de segurança Cloudflare, radar Cloudflare. | `Cloudflare_CL`. |
| Orca Security | Orca Blog, Wiz Research, Sysdig Threat Research, Aqua Nautilus. | `OrcaAlerts_CL`, `AzureActivity`, `AzureDiagnostics`. |
| Fortigate | Laboratórios FortiGuard, CISA KEV, Exploit-DB, GreyNoise. | `CommonSecurityLog`, `Syslog`. |
| CyberArk | CyberArk Laboratórios, SpecterOps, Semperis. | `CyberArk_AuditEvents_CL`, `SigninLogs`, `AuditLogs`. |
| Microsoft 365 | Proofpoint, Blog de segurança da Microsoft, Cofense, Segurança anormal. | `OfficeActivity`, `SigninLogs`, `AuditLogs`, `NetskopeAlerts_CL`. |

## Automação e pipeline de admissão
À medida que a lista cresce, evite o rastreamento manual sempre que possível.

| Componente | Usar |
| --- | --- |
| leitor RSS | Assine blogs de fornecedores, notícias, avisos e feeds de pesquisa. |
| MISP | Armazene, correlacione e compartilhe IOCs e contexto de evento. |
| OpenCTI | Rastreie atores, campanhas, malware, TTPs e relacionamentos. |
| STIX/TAXII | Incorpore inteligência estruturada sobre ameaças em ferramentas que a suportem. |
| Sentinel `ThreatIntelIndicators` | Armazene indicadores ativos para varreduras KQL. |
| Listas de observação Sentinel | Armazene ativos de alto risco, IPs de administrador permitidos, aplicativos SaaS aprovados, usuários VIP e fornecedores prioritários. |
| Pendências de caça | Rastreie ideias brutas até que se tornem buscas com escopo definido. |
| Revisão mensal | Retire feeds obsoletos, adicione novas fontes de alto valor e remova fontes barulhentas. |

## Convertendo pesquisas em caçadas
| Contribuição de pesquisa | Tipo de caça | Exemplo Sentinel Dados |
| --- | --- | --- |
| Ator usa comandos de administração de nuvem após comprometimento de identidade. | Hipótese ou baseada em inteligência. | `SigninLogs`, `AuditLogs`, `AzureActivity`. |
| Nova campanha de bypass ou bot Cloudflare WAF. | Intel ou baseado em dados. | `Cloudflare_CL`. |
| O ransomware usa PowerShell suspeito e exclusão de backup. | Baseado em hipóteses. | `SecurityEvent`, `WindowsEvent`, `TrendMicro_XDR_OAT_CL`. |
| O relatório inclui IPs, domínios, URLs e hashes. | Varredura Intel IOC. | `ThreatIntelIndicators`, `CommonSecurityLog`, `Netskope*`, `TrendMicro*`, `Cloudflare_CL`. |
| CISA adiciona um CVE explorado que afeta um aplicativo público. | Intel e caça à exposição. | `OrcaAlerts_CL`, `Cloudflare_CL`, `AzureActivity`, inventário de ativos. |
| O fornecedor relata roubo de token SaaS ou abuso de OAuth. | Hipótese ou baseada em inteligência. | `SigninLogs`, `AuditLogs`, `OfficeActivity`, `NetskopeEventsApplication_CL`. |
| A nova tabela Sentinel está integrada. | Orientado por dados. | Perfil específico de tabela e normalização de campo. |
| O volume de alertas mudou este mês. | Revisão mensal baseada em dados. | `SecurityAlert`, `SecurityIncident`, `SentinelHealth`, `Usage`. |

## Lista de verificação de admissão de ideias
Capture cada nova ideia com:

- Título.
- Link de origem ou ticket interno.
- Data revisada.
- Tipo de fonte: notícias, consultoria, informações do fornecedor, CVE, IOC, TTP, incidente interno, fonte de dados.
- Breve resumo.
- Plataformas ou ferramentas afetadas.
- Unidades de negócios ou ativos críticos afetados.
- IOCs, TTPs, CVEs, nomes de atores, famílias de malware ou grupos de ransomware.
- Tabelas Sentinel obrigatórias.
- Entidades esperadas: usuário, host, IP, URL, hash, recurso de nuvem, aplicativo, alerta, incidente.
- Cadência proposta.
- Prioridade.
- Proprietário.
- Data de expiração ou revisão.

## Perguntas de refinamento
Antes de criar uma página de busca, responda:

- A ideia é testável?
- Quais dados comprovam ou refutam isso?
- Temos os dados em Sentinel?
- Que retrospectiva faz sentido?
- Como seria um verdadeiro positivo?
- Que atividade benigna poderia ser semelhante?
- Isso é urgente o suficiente para uma caçada à Intel?
- Qual equipe possui acompanhamento?

## Fluxo de trabalho da biblioteca
1. Adicione ideias brutas a um backlog de busca ou rastreador de problemas.
2. Use esta página para refiná-los.
3. Escolha a metodologia.
4. Crie uma página de busca em [Modelo de busca](../templates/hunt-template.md).
5. Adicione ou vincule KQL em [Biblioteca KQL](../sentinel/kql/README.md).
6. Agende-o em [Hunt Calendar](../cadence/hunt-calendar.md).
7. Se a busca for repetida com sucesso, promova-a para uma regra analítica Sentinel, lista de observação, pasta de trabalho ou melhoria do analisador.
