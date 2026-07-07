
Para um SOC focado em Threat Hunting, vale a pena estruturar isso como um framework reutilizável, não apenas um conjunto de queries. Isso reduz o tempo de investigação e garante consistência.

Eu dividiria em três pilares.

1. Biblioteca de Templates KQL

Crie pastas por categoria.

Identity

Logins anômalos

Impossible Travel

MFA Failure

Password Spray

Privilege Escalation

Criação de usuários

Alteração de grupos administrativos

Endpoint

PowerShell

CMD

WMI

PsExec

Scheduled Tasks

Serviços criados

Drivers carregados

Processos suspeitos

DLL Hijacking

LOLBins

Network

Conexões para países incomuns

Beaconing

DNS suspeito

HTTP User-Agent anômalo

Comunicação com IPs maliciosos

Port Scan

Email

Phishing

Attachment executável

Links externos

Display Name Spoofing

Cloud

Azure AD

Azure Activity

AWS CloudTrail

GCP Audit

Threat Intelligence

IOC IP

IOC Domain

IOC Hash

IOC URL

Persistence

Registry Run Keys

Startup Folder

Scheduled Tasks

Services

Lateral Movement

RDP

SMB

WinRM

Remote PowerShell

Exfiltration

Upload para serviços cloud

Grandes volumes de dados

Compressão seguida de upload

---

2. Template padrão para todas as queries

Cada query deveria conter:

Objetivo

MITRE ATT&CK

Fonte de logs

Hipótese

Query

Campos importantes

Como investigar

Possíveis falsos positivos

Próximos passos

Exemplo:

Nome:
PowerShell Encoded Commands

MITRE:
T1059.001

Objetivo:
Detectar uso de PowerShell codificado.

Logs:
DeviceProcessEvents

Hipótese:
Um atacante executou PowerShell utilizando Base64.

KQL:
...

Investigar:

- Quem executou
- Parent Process
- Device
- Horário
- Linha de comando

Falsos positivos:
Ferramentas administrativas.

Resposta:
Isolar endpoint.

---

3. Processo Diário

Todos os dias

Identity

Contas bloqueadas

MFA Failure

Password Spray

Novos administradores

Endpoint

PowerShell

CMD

LOLBins

PsExec

Rundll32

Regsvr32

Certutil

MSHTA

Network

DNS suspeito

Beaconing

Conexões para países incomuns

Alto volume de conexões

Cloud

Novos Tokens

Consentimentos OAuth

Criação de aplicações

Threat Intelligence

IOC Match

Hash Match

IP Match

Tempo estimado: 30–60 minutos.

---

Processo Semanal

Caçadas mais profundas.

Contas privilegiadas

Persistência

Scheduled Tasks

Serviços novos

DLL Side Loading

Living off the Land

Uso incomum de ferramentas administrativas

Kerberoasting

AS-REP Roasting

Lateral Movement

Tempo: 4–6 horas.

---

Processo Mensal

Threat Hunting estratégico.

Revisão dos últimos TTPs publicados

Atualização dos IOCs

Atualização das Queries

Gap Analysis

Cobertura MITRE

Métricas

Lições aprendidas

Novas hipóteses de caça

---

Estrutura da biblioteca

Threat Hunting

01_Identity

02_Endpoint

03_Network

04_Email

05_Cloud

06_Threat_Intelligence

07_Persistence

08_Lateral_Movement

09_Exfiltration

10_Ransomware

11_Insider_Threat

12_Custom_Hunts

Além disso, eu montaria uma biblioteca de aproximadamente 100 a 150 templates KQL, organizada por técnicas da matriz MITRE ATT&CK. Esse volume cobre a maior parte dos cenários encontrados em um SOC moderno utilizando Microsoft Sentinel e Microsoft Defender XDR, formando uma base sólida para investigações repetíveis e para evolução contínua do processo de Threat Hunting.
