#!/usr/bin/env python3
"""Generate the Markdown structure for the threat hunting library.

The source schema is the Microsoft Sentinel/Log Analytics table inventory pasted
into Codex. The generated output keeps Sentinel as the data catalog and maps
tables to tools, hunt scenarios, and recurring hunt cadences.
"""

from __future__ import annotations

import re
import shutil
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REFERENCE = ROOT / "references" / "sentinel" / "logmanagement-schema.txt"
ATTACHMENT_SCHEMA = Path(
    "/home/mandrade/.codex/attachments/ea46d974-fb2e-433f-9830-361c01fe2e95/pasted-text.txt"
)


TABLE_HEADER_RE = re.compile(r"^ ([A-Za-z][A-Za-z0-9_]*)$")
FIELD_RE = re.compile(r"^ ([A-Za-z0-9_]+) \(([^)]+)\)$")


FOLDER_MOVES = {
    "CTH.md": "methodologies/threat-hunting-overview.md",
    "Netskope.md": "tools/sase/netskope.md",
    "Orca Security.md": "tools/cspm/orca-security.md",
    "Tables.md": "sentinel/tables/index.md",
    "Tables_Data.md": "sentinel/tables/field-normalization.md",
    "Enviroments/Cloud/AWS.md": "platforms/cloud/aws.md",
    "Enviroments/Cloud/Azure.md": "platforms/cloud/azure.md",
    "Enviroments/Cloud/GCP.md": "platforms/cloud/gcp.md",
    "Enviroments/Cloud/Oracle.md": "platforms/cloud/oracle-cloud.md",
    "Operation Systems/Android.md": "platforms/operating-systems/android.md",
    "Operation Systems/IOS.md": "platforms/operating-systems/ios.md",
    "Operation Systems/Linux.md": "platforms/operating-systems/linux.md",
    "Operation Systems/Ubuntu.md": "platforms/operating-systems/ubuntu.md",
    "Operation Systems/Windows.md": "platforms/operating-systems/windows.md",
    "Threat Hunting /Data Driven.md": "methodologies/data-driven.md",
    "Threat Hunting /Hyphotesis Driven.md": "methodologies/hypothesis-driven.md",
    "Threat Hunting /Intel Driven.md": "methodologies/intel-driven.md",
    "Threat Hunting /PEAK Framework.md": "methodologies/peak-framework.md",
    "Scripts/Bash.md": "scripts/bash.md",
    "Scripts/C#.md": "scripts/csharp.md",
    "Scripts/GO.md": "scripts/go.md",
    "Scripts/Java.md": "scripts/java.md",
    "Scripts/Powershell.md": "scripts/powershell.md",
    "Scripts/Python.md": "scripts/python.md",
    "Tools/EDR/Karspersky Security Center.md": "tools/edr/kaspersky-security-center.md",
    "Tools/EDR/TrendAI Vision One.md": "tools/edr/trend-vision-one.md",
    "Tools/Firewall/Fortigate.md": "tools/firewall/fortigate.md",
    "Tools/SIEM/Elastic Security.md": "tools/siem/elastic-security.md",
    "Tools/SIEM/Microsoft Sentinel.md": "tools/siem/microsoft-sentinel.md",
    "Tools/WAF/Cloudflare.md": "tools/waf/cloudflare.md",
    "Tools/ZTNA/Guardicore.md": "tools/ztna/guardicore.md",
}


TABLE_GROUPS = OrderedDict(
    [
        (
            "identity-access",
            {
                "title": "Identity and Access",
                "description": "Authentication, Entra ID audit activity, UEBA, peer analytics, privileged access, and M365 user activity.",
                "tables": [
                    "SigninLogs",
                    "AuditLogs",
                    "IdentityInfo",
                    "BehaviorAnalytics",
                    "UserPeerAnalytics",
                    "OfficeActivity",
                    "CyberArk_AuditEvents_CL",
                ],
            },
        ),
        (
            "endpoint-os",
            {
                "title": "Endpoint and Operating Systems",
                "description": "Windows, Linux, agent health, process, logon, service, script, and host telemetry.",
                "tables": [
                    "SecurityEvent",
                    "WindowsEvent",
                    "Syslog",
                    "Heartbeat",
                    "AMAAgentHealth_CL",
                    "TrendMicro_XDR_OAT_CL",
                    "TrendMicro_XDR_WORKBENCH_CL",
                    "TrendMicro_XDR_Health_Check_CL",
                    "TrendMicro_XDR_OAT_Health_Check_CL",
                ],
            },
        ),
        (
            "network-edge",
            {
                "title": "Network, Edge, and SASE",
                "description": "Firewall, proxy, WAF, DNS, web, SASE, and edge telemetry normalized for network hunts.",
                "tables": [
                    "CommonSecurityLog",
                    "Cloudflare_CL",
                    "NetskopeAlerts_CL",
                    "NetskopeEventsApplication_CL",
                    "NetskopeEventsAudit_CL",
                    "NetskopeEventsConnection_CL",
                    "NetskopeEventsNetwork_CL",
                    "NetskopeEventsPage_CL",
                ],
            },
        ),
        (
            "cloud-posture",
            {
                "title": "Cloud and Posture",
                "description": "Azure control plane, cloud diagnostics, cloud security posture, workload risk, and exposure telemetry.",
                "tables": [
                    "AzureActivity",
                    "AzureDiagnostics",
                    "OrcaAlerts_CL",
                    "SAP_CL",
                ],
            },
        ),
        (
            "detections-cases-intel",
            {
                "title": "Detections, Cases, and Intel",
                "description": "Sentinel detections, incidents, anomalies, watchlists, health, audit, and threat intelligence.",
                "tables": [
                    "SecurityAlert",
                    "SecurityIncident",
                    "Anomalies",
                    "SentinelAudit",
                    "SentinelHealth",
                    "ThreatIntelIndicators",
                    "Watchlist",
                ],
            },
        ),
        (
            "application-monitoring",
            {
                "title": "Application and Platform Monitoring",
                "description": "Application Insights, Function Apps, Log Analytics query audit, ingestion usage, and application telemetry.",
                "tables": [
                    "AppDependencies",
                    "AppExceptions",
                    "AppMetrics",
                    "AppPerformanceCounters",
                    "AppRequests",
                    "AppSystemEvents",
                    "AppTraces",
                    "FunctionAppLogs",
                    "LAQueryLogs",
                    "Usage",
                ],
            },
        ),
    ]
)


TOOL_MAPPINGS = OrderedDict(
    [
        (
            "Microsoft Sentinel",
            {
                "path": "tools/siem/microsoft-sentinel.md",
                "category": "SIEM",
                "tables": [
                    "SecurityIncident",
                    "SecurityAlert",
                    "SentinelAudit",
                    "SentinelHealth",
                    "Anomalies",
                    "ThreatIntelIndicators",
                    "Watchlist",
                    "LAQueryLogs",
                    "Usage",
                ],
                "hunts": [
                    "Alert and incident queue review",
                    "Detection quality review",
                    "Threat intelligence matching",
                    "Data source health and ingestion review",
                ],
            },
        ),
        (
            "Microsoft Entra ID",
            {
                "path": "tools/identity/microsoft-entra-id.md",
                "category": "Identity",
                "tables": [
                    "SigninLogs",
                    "AuditLogs",
                    "IdentityInfo",
                    "BehaviorAnalytics",
                    "UserPeerAnalytics",
                ],
                "hunts": [
                    "Password spray",
                    "Suspicious successful sign-in",
                    "New privileged role assignment",
                    "Risky sign-in and Conditional Access review",
                ],
            },
        ),
        (
            "Microsoft 365",
            {
                "path": "tools/saas/microsoft-365.md",
                "category": "SaaS",
                "tables": ["OfficeActivity", "AuditLogs", "SigninLogs"],
                "hunts": [
                    "Mailbox rule abuse",
                    "Suspicious file sharing",
                    "New OAuth app usage",
                ],
            },
        ),
        (
            "Fortigate",
            {
                "path": "tools/firewall/fortigate.md",
                "category": "Firewall",
                "tables": ["CommonSecurityLog", "Syslog"],
                "hunts": [
                    "Denied traffic spike",
                    "Outbound connection anomaly",
                    "Malicious IP correlation",
                ],
            },
        ),
        (
            "Cloudflare",
            {
                "path": "tools/waf/cloudflare.md",
                "category": "WAF",
                "tables": ["Cloudflare_CL"],
                "hunts": [
                    "WAF attack spike",
                    "Bot score anomaly",
                    "Credential stuffing against public apps",
                ],
            },
        ),
        (
            "Netskope",
            {
                "path": "tools/sase/netskope.md",
                "category": "SASE/CASB",
                "tables": [
                    "NetskopeAlerts_CL",
                    "NetskopeEventsApplication_CL",
                    "NetskopeEventsAudit_CL",
                    "NetskopeEventsConnection_CL",
                    "NetskopeEventsNetwork_CL",
                    "NetskopeEventsPage_CL",
                ],
                "hunts": [
                    "Unsanctioned app access",
                    "DLP alert review",
                    "High-risk destination access",
                    "Unusual egress and user web activity",
                ],
            },
        ),
        (
            "Orca Security",
            {
                "path": "tools/cspm/orca-security.md",
                "category": "CSPM/CWPP",
                "tables": ["OrcaAlerts_CL"],
                "hunts": [
                    "Critical cloud exposure",
                    "Vulnerable public asset",
                    "Privilege or secret exposure",
                ],
            },
        ),
        (
            "Trend Vision One",
            {
                "path": "tools/edr/trend-vision-one.md",
                "category": "XDR/EDR",
                "tables": [
                    "TrendMicro_XDR_OAT_CL",
                    "TrendMicro_XDR_WORKBENCH_CL",
                    "TrendMicro_XDR_Health_Check_CL",
                    "TrendMicro_XDR_OAT_Health_Check_CL",
                ],
                "hunts": [
                    "Suspicious process and script execution",
                    "Workbench alert triage",
                    "MITRE ATT&CK mapped behavior",
                    "Endpoint connector health",
                ],
            },
        ),
        (
            "CyberArk",
            {
                "path": "tools/pam/cyberark.md",
                "category": "PAM",
                "tables": ["CyberArk_AuditEvents_CL"],
                "hunts": [
                    "Privileged session review",
                    "Safe or account policy change",
                    "Unusual credential retrieval",
                ],
            },
        ),
        (
            "Kaspersky Security Center",
            {
                "path": "tools/edr/kaspersky-security-center.md",
                "category": "EDR",
                "tables": [],
                "hunts": [
                    "Add Sentinel table mapping when connector or syslog path is confirmed",
                ],
            },
        ),
        (
            "Elastic Security",
            {
                "path": "tools/siem/elastic-security.md",
                "category": "SIEM",
                "tables": [],
                "hunts": [
                    "Use as external SIEM reference if Elastic detections are exported to Sentinel",
                ],
            },
        ),
        (
            "Guardicore",
            {
                "path": "tools/ztna/guardicore.md",
                "category": "ZTNA/Segmentation",
                "tables": [],
                "hunts": [
                    "Add Sentinel table mapping when connector or syslog path is confirmed",
                ],
            },
        ),
    ]
)


PLATFORMS = OrderedDict(
    [
        (
            "platforms/cloud/aws.md",
            {
                "title": "AWS",
                "tables": ["OrcaAlerts_CL", "NetskopeEventsNetwork_CL", "CommonSecurityLog"],
                "notes": "Use this page for AWS-specific hunts once CloudTrail, VPC Flow Logs, GuardDuty, or posture findings are mapped into Sentinel.",
            },
        ),
        (
            "platforms/cloud/azure.md",
            {
                "title": "Azure",
                "tables": ["AzureActivity", "AzureDiagnostics", "SigninLogs", "AuditLogs", "OrcaAlerts_CL"],
                "notes": "Primary cloud control-plane hunting source for this library.",
            },
        ),
        (
            "platforms/cloud/gcp.md",
            {
                "title": "GCP",
                "tables": ["OrcaAlerts_CL", "NetskopeEventsNetwork_CL"],
                "notes": "Use this page for GCP-specific activity and posture hunts after GCP audit logs are connected or normalized.",
            },
        ),
        (
            "platforms/cloud/oracle-cloud.md",
            {
                "title": "Oracle Cloud",
                "tables": ["OrcaAlerts_CL"],
                "notes": "Use this page for Oracle Cloud posture and activity hunts after OCI logs are connected or normalized.",
            },
        ),
        (
            "platforms/operating-systems/windows.md",
            {
                "title": "Windows",
                "tables": ["SecurityEvent", "WindowsEvent", "TrendMicro_XDR_OAT_CL", "Heartbeat"],
                "notes": "Primary operating-system source for endpoint authentication, process, service, PowerShell, and security event hunts.",
            },
        ),
        (
            "platforms/operating-systems/linux.md",
            {
                "title": "Linux",
                "tables": ["Syslog", "Heartbeat", "NetskopeEventsNetwork_CL"],
                "notes": "Use for daemon, authentication, command, network, and host health hunts when Linux logs are collected.",
            },
        ),
        (
            "platforms/operating-systems/ubuntu.md",
            {
                "title": "Ubuntu",
                "tables": ["Syslog", "Heartbeat"],
                "notes": "Ubuntu-specific hunting notes can live here when package, auth, sudo, or service logs are mapped.",
            },
        ),
        (
            "platforms/operating-systems/android.md",
            {
                "title": "Android",
                "tables": ["NetskopeEventsApplication_CL", "NetskopeEventsNetwork_CL"],
                "notes": "Use when mobile telemetry is routed through Netskope, MDM, or another connector.",
            },
        ),
        (
            "platforms/operating-systems/ios.md",
            {
                "title": "iOS",
                "tables": ["NetskopeEventsApplication_CL", "NetskopeEventsNetwork_CL"],
                "notes": "Use for mobile access hunts when iOS telemetry is routed through Netskope, MDM, or another connector.",
            },
        ),
    ]
)


TOOL_GUIDES = {
    "Microsoft Sentinel": {
        "purpose": "Central SIEM and hunting workspace for correlation, KQL, incident review, watchlists, analytics rules, and operational health.",
        "how_it_works": [
            "Ingests cloud, identity, endpoint, network, SaaS, and custom logs into Log Analytics tables.",
            "Uses KQL to search tables, correlate entities, build analytics rules, and support hunting workflows.",
            "Connects alerts, incidents, threat intelligence, watchlists, automation, and workbook views into one investigation surface.",
        ],
        "what_to_review": [
            "Connector health, ingestion delays, table volume, and billable usage.",
            "Analytics rules with high false positives, stale logic, disabled rules, or missing entity mapping.",
            "Incidents closed without meaningful classification, repeated alerts, and alert sources that never become incidents.",
            "Watchlists, threat intelligence feeds, automation rules, and playbooks with broad permissions.",
        ],
        "security_focus": [
            "Coverage gaps: important tools connected but not producing the expected tables.",
            "Detection drift: rules no longer matching because schemas, parsers, or vendor fields changed.",
            "Operational risk: noisy rules causing alert fatigue or automation suppressing useful signal.",
        ],
        "hunt_questions": [
            "Which high-risk tables stopped ingesting during the last 24 hours?",
            "Which detections repeatedly generate incidents without confirmed findings?",
            "Which threat intel indicators match internal telemetry across identity, endpoint, network, and cloud data?",
        ],
    },
    "Microsoft Entra ID": {
        "purpose": "Primary identity plane for user, device, application, service principal, Conditional Access, MFA, and role activity.",
        "how_it_works": [
            "Produces sign-in records for interactive, non-interactive, application, and service principal access patterns.",
            "Produces audit records for directory changes, role assignments, application consent, device registration, and policy changes.",
            "Adds identity context through enrichment tables such as identity details, UEBA, peer analytics, and behavior analytics.",
        ],
        "what_to_review": [
            "Failed sign-ins followed by success, new geographies, unfamiliar devices, and unusual client applications.",
            "Privileged role assignment, eligible role activation, service principal credential changes, and application consent.",
            "MFA method registration changes, Conditional Access policy changes, device code flow, and token replay indicators.",
        ],
        "security_focus": [
            "Valid-account abuse is often quieter than malware and should be baselined by user, app, country, and device.",
            "Service principals and OAuth apps can become persistent cloud access paths if credentials or permissions are added.",
            "LATAM operations should watch regional phishing, credential stuffing, helpdesk impersonation, and payment-themed lures.",
        ],
        "hunt_questions": [
            "Which users authenticate from new countries or ASNs and then access sensitive applications?",
            "Which applications received new delegated or application permissions?",
            "Which privileged users changed MFA, password, device, or role state outside normal windows?",
        ],
    },
    "Microsoft 365": {
        "purpose": "SaaS productivity and collaboration telemetry for Exchange, SharePoint, OneDrive, Teams, and related audit activity.",
        "how_it_works": [
            "OfficeActivity records user and admin operations across Microsoft 365 workloads.",
            "Identity context from Entra ID should be joined to mailbox, file, Teams, and SharePoint activity.",
            "High-value hunts usually combine authentication, mailbox/file actions, and administrative audit events.",
        ],
        "what_to_review": [
            "Inbox rules, forwarding, mailbox permission changes, suspicious eDiscovery, and unusual mail access.",
            "Mass file downloads, external sharing, anonymous links, unusual Teams activity, and risky OAuth app activity.",
            "Admin actions touching retention, transport, audit, DLP, mailbox permissions, or tenant configuration.",
        ],
        "security_focus": [
            "Business email compromise often starts with a valid sign-in and then moves into mailbox rules or forwarding.",
            "File exfiltration can look like normal SaaS usage unless volume, timing, user baseline, and destination are reviewed.",
            "OAuth consent can bypass password reset response unless tokens and app permissions are revoked.",
        ],
        "hunt_questions": [
            "Which users created forwarding or inbox rules shortly after a risky sign-in?",
            "Which accounts downloaded or shared unusual volumes of files?",
            "Which OAuth apps gained access to mail, files, or Graph scopes?",
        ],
    },
    "Fortigate": {
        "purpose": "Network firewall and VPN telemetry for perimeter access, policy enforcement, UTM events, and traffic visibility.",
        "how_it_works": [
            "Firewall events usually arrive in CommonSecurityLog or Syslog, depending on the connector path.",
            "Policy, action, source, destination, port, NAT, VPN, and URL fields are key for hunting.",
            "Firewall data becomes much stronger when joined with identity, endpoint, Cloudflare, Netskope, and threat intel.",
        ],
        "what_to_review": [
            "VPN login failures, successful logins after failures, new countries, and admin portal activity.",
            "Denied traffic spikes, repeated internal scanning, uncommon outbound ports, and policy shadowing.",
            "Traffic to known malicious IPs/domains, newly observed destinations, and command-and-control patterns.",
        ],
        "security_focus": [
            "VPN and firewall administration are common initial-access targets.",
            "Outbound allow rules can hide exfiltration or tunneling if only inbound traffic is reviewed.",
            "Parser quality matters: source user, source IP, destination, action, and policy fields must be reliable.",
        ],
        "hunt_questions": [
            "Which VPN users failed repeatedly and then succeeded?",
            "Which internal hosts talk to rare external ports or countries?",
            "Which deny events indicate scanning, exploit attempts, or misconfigured exposure?",
        ],
    },
    "Cloudflare": {
        "purpose": "Edge, CDN, DNS, bot, WAF, and public application telemetry for internet-facing services.",
        "how_it_works": [
            "Cloudflare events show requests before they reach origin infrastructure.",
            "WAF action, rule ID, URI, host, user-agent, source IP, country, bot score, and origin status help explain attack traffic.",
            "Cloudflare is strongest when correlated with application logs, identity access, firewall logs, and incident timelines.",
        ],
        "what_to_review": [
            "WAF blocks, managed challenges, bot scores, attack score shifts, and source ASN/country anomalies.",
            "Credential stuffing, path traversal, SSRF, RCE probes, webshell access, and repeated login endpoint hits.",
            "Public applications with high attack volume, origin errors, bypass attempts, or unprotected hostnames.",
        ],
        "security_focus": [
            "Blocked traffic is useful, but successful or challenged traffic can show probing that later bypasses controls.",
            "Public app hunts should compare edge telemetry with origin/app logs to detect exploitation after WAF visibility.",
            "Allow rules, page rules, worker logic, and DNS changes can create exposure if not governed.",
        ],
        "hunt_questions": [
            "Which URIs receive repeated exploit patterns from distributed sources?",
            "Which source ASNs or countries are new for an application?",
            "Which WAF rules are noisy, bypassed, or protecting critical endpoints?",
        ],
    },
    "Netskope": {
        "purpose": "SASE, CASB, secure web gateway, DLP, cloud app, page, connection, network, and policy telemetry.",
        "how_it_works": [
            "Events describe user, device, application, URL, category, action, policy, risk, and connection context.",
            "CASB/SWG telemetry connects identity behavior with cloud app usage and web egress.",
            "DLP and malware alerts can provide high-context pivots into file movement and risky SaaS activity.",
        ],
        "what_to_review": [
            "Unsanctioned app access, risky app categories, uploads to personal storage, and new cloud destinations.",
            "DLP alerts, policy bypasses, malware events, anomalous downloads, and impossible or rare app usage.",
            "Web sessions from risky devices, unmanaged locations, proxies, anonymizers, and newly observed domains.",
        ],
        "security_focus": [
            "Cloud exfiltration often appears as normal browser traffic unless user, app, volume, and file context are joined.",
            "Policy action fields must be interpreted carefully: allow, block, alert, coach, and quarantine have different meanings.",
            "Netskope can help bridge identity, endpoint, SaaS, and network hunts when endpoint detail is limited.",
        ],
        "hunt_questions": [
            "Which users uploaded unusual volumes to unsanctioned cloud storage?",
            "Which risky apps appear for the first time in the environment?",
            "Which blocked or coached events repeat until a successful allowed event occurs?",
        ],
    },
    "Orca Security": {
        "purpose": "Cloud posture, workload risk, vulnerability, exposure, secrets, identity, and asset-context telemetry.",
        "how_it_works": [
            "Findings summarize risk across cloud assets without needing every workload to send raw event logs.",
            "Asset context helps prioritize exposed, vulnerable, privileged, internet-facing, or sensitive systems.",
            "Posture findings should be correlated with AzureActivity, cloud diagnostics, network logs, and incidents.",
        ],
        "what_to_review": [
            "Critical/high findings on internet-facing assets, identity assets, production workloads, and data stores.",
            "Secrets in files, vulnerable packages, exposed admin interfaces, public storage, and risky IAM paths.",
            "Findings that remain open across multiple hunt cycles or reappear after remediation.",
        ],
        "security_focus": [
            "Posture alerts are not always active compromise, but they define where compromise is most likely to be impactful.",
            "High-risk exposure should be converted into intel hunts when new CVEs or exploit campaigns appear.",
            "Ownership, asset criticality, and internet exposure are key to prioritizing response.",
        ],
        "hunt_questions": [
            "Which internet-facing assets have critical vulnerabilities or secrets exposure?",
            "Which cloud accounts have repeated risky findings?",
            "Which posture findings overlap with active network or identity anomalies?",
        ],
    },
    "Trend Vision One": {
        "purpose": "XDR/EDR telemetry for endpoint process, file, registry, network, observed attack techniques, and workbench alerts.",
        "how_it_works": [
            "Observed Attack Technique events map endpoint behavior to MITRE-style tactics and techniques.",
            "Workbench alerts group related events and provide investigation context.",
            "Health tables help confirm endpoint sensor coverage before trusting endpoint hunt results.",
        ],
        "what_to_review": [
            "Suspicious script execution, process lineage, registry persistence, unusual child processes, and network callbacks.",
            "Workbench alerts with high severity, repeated hosts, recurring MITRE techniques, or untriaged status.",
            "Endpoint health gaps, stale agents, and tables that stop reporting for critical servers.",
        ],
        "security_focus": [
            "Endpoint detections are strongest when process lineage is preserved and joined with identity/network context.",
            "Adversaries often disable or evade EDR before ransomware, exfiltration, or credential theft.",
            "Raw endpoint behavior should be converted into stable use cases only after false-positive review.",
        ],
        "hunt_questions": [
            "Which hosts show suspicious PowerShell, LOLBins, WMI, or service creation?",
            "Which MITRE techniques appear repeatedly without incident escalation?",
            "Which endpoints stopped reporting shortly before a high-risk event?",
        ],
    },
    "CyberArk": {
        "purpose": "Privileged access, vault, safe, account, credential retrieval, and privileged session audit telemetry.",
        "how_it_works": [
            "Audit events record privileged account access, safe changes, session activity, policy changes, and credential operations.",
            "PAM telemetry should be joined with identity, endpoint, and incident data for privilege-abuse hunts.",
            "CyberArk context helps distinguish authorized privileged activity from unusual credential use.",
        ],
        "what_to_review": [
            "Credential retrieval outside normal hours, unusual safes, repeated failures, and new privileged account access.",
            "Safe membership changes, policy changes, password checkout/checkin anomalies, and session recording gaps.",
            "Privileged activity followed by endpoint, cloud, or identity changes.",
        ],
        "security_focus": [
            "Privileged credentials are high-impact even when the originating identity looks legitimate.",
            "Break-glass and service accounts need separate baselines from normal admin users.",
            "PAM events are most valuable when correlated with the actions performed after credential retrieval.",
        ],
        "hunt_questions": [
            "Which privileged accounts were accessed by new users or from new locations?",
            "Which safes had membership or policy changes?",
            "Which credential checkouts are followed by unusual endpoint or cloud administration?",
        ],
    },
    "Kaspersky Security Center": {
        "purpose": "Endpoint protection management and antivirus/EDR administration context. Sentinel mapping is pending in this library.",
        "how_it_works": [
            "Typically manages endpoint policy, malware events, updates, quarantine, and endpoint protection status.",
            "Telemetry may reach Sentinel through syslog, API export, custom connector, or another SIEM forwarding path.",
            "Until the connector is confirmed, treat this page as the mapping checklist for endpoint protection data.",
        ],
        "what_to_review": [
            "Malware detections, blocked executions, quarantine events, policy changes, and protection-disabled events.",
            "Outdated agents, signature/update failures, disabled modules, and unmanaged endpoints.",
            "Admin console changes, exclusions, tamper protection changes, and mass policy edits.",
        ],
        "security_focus": [
            "Protection gaps can explain why endpoint hunts miss activity.",
            "New exclusions or disabled protection may be a precursor to malware execution or ransomware.",
            "Mapping this tool into Sentinel should prioritize host identity, detection name, action, user, and file hash.",
        ],
        "hunt_questions": [
            "Which hosts repeatedly detect malware but never create Sentinel incidents?",
            "Which endpoints disabled protection or failed updates?",
            "Which exclusions were added shortly before suspicious endpoint activity?",
        ],
    },
    "Elastic Security": {
        "purpose": "External SIEM/EDR reference and detection source that can enrich Sentinel hunts when alerts or data are exported.",
        "how_it_works": [
            "Elastic can collect endpoint, network, cloud, and detection data outside Sentinel.",
            "This library should track which Elastic detections, alerts, or cases are forwarded into Sentinel.",
            "Use Elastic as a content reference only when the equivalent Sentinel tables and fields are mapped.",
        ],
        "what_to_review": [
            "Detection logic that can be translated into KQL or mapped to existing Sentinel tables.",
            "Alert forwarding quality, field normalization, entity mapping, and duplicate alert handling.",
            "Coverage differences between Elastic and Sentinel for endpoint, network, or cloud sources.",
        ],
        "security_focus": [
            "Parallel SIEMs can create blind spots if alerts stay in one platform and incidents in another.",
            "Translated detections need validation because EQL/Sigma/Elastic fields may not match Sentinel schemas.",
            "Duplicate detections should be tuned to avoid alert fatigue.",
        ],
        "hunt_questions": [
            "Which Elastic detections have no equivalent Sentinel use case?",
            "Which alerts are forwarded without useful entities?",
            "Which Elastic-only data sources should be onboarded or normalized in Sentinel?",
        ],
    },
    "Guardicore": {
        "purpose": "Segmentation and lateral movement context for east-west traffic, application dependencies, and policy enforcement. Sentinel mapping is pending.",
        "how_it_works": [
            "Segmentation tools observe flows between workloads and enforce communication policy.",
            "Telemetry can reveal unexpected internal paths that perimeter tools never see.",
            "Use this page to define the connector path, flow schema, policy events, and Sentinel tables once available.",
        ],
        "what_to_review": [
            "New workload-to-workload communication, denied east-west flows, and policy violations.",
            "RDP, SMB, WinRM, SSH, database, and admin protocol movement between unusual segments.",
            "Segmentation policy changes, enforcement mode changes, and critical asset exposure.",
        ],
        "security_focus": [
            "Lateral movement often hides inside internal traffic if east-west telemetry is missing.",
            "Segmentation alerts are best correlated with identity and endpoint process context.",
            "Unmapped connector data should be treated as a roadmap item for better lateral movement hunts.",
        ],
        "hunt_questions": [
            "Which hosts initiated new SMB/RDP/SSH paths across segments?",
            "Which denied flows suggest scanning or attempted lateral movement?",
            "Which critical servers have broader allowed paths than expected?",
        ],
    },
}


PLATFORM_GUIDES = {
    "AWS": {
        "purpose": "Cloud platform for accounts, IAM, compute, storage, network, serverless, container, database, and logging services.",
        "how_it_works": [
            "Control-plane activity is normally captured through CloudTrail and related service logs when integrated.",
            "Cloud risk should be reviewed by account, region, identity, public exposure, asset criticality, and data sensitivity.",
            "In this library, AWS posture is mostly represented through Orca and network/SASE tables until native AWS logs are connected.",
        ],
        "what_to_review": [
            "Root account use, IAM policy changes, access key creation, unusual AssumeRole activity, and privilege escalation paths.",
            "Public S3 buckets, exposed services, security group changes, snapshot sharing, and logging disablement.",
            "New regions, new compute, unusual egress, secrets exposure, and critical vulnerabilities on internet-facing assets.",
        ],
        "security_focus": [
            "IAM and access keys are often the durable access layer after cloud compromise.",
            "Public storage, permissive security groups, and disabled logging are high-priority exposure signals.",
            "Cloud hunts need asset ownership and business context to avoid drowning in expected automation.",
        ],
    },
    "Azure": {
        "purpose": "Primary cloud control-plane and identity-adjacent platform for this library.",
        "how_it_works": [
            "AzureActivity records management-plane operations such as resource writes, deletes, role assignments, and policy changes.",
            "AzureDiagnostics provides service-level logs where resource diagnostics are enabled.",
            "Entra ID sign-in and audit data should be joined to Azure operations to connect identity to cloud action.",
        ],
        "what_to_review": [
            "Role assignment changes, owner/contributor grants, service principal credentials, and privileged identity changes.",
            "Public IPs, exposed storage, Key Vault access, diagnostic setting changes, and resource deletion.",
            "New subscriptions, resource groups, automation accounts, virtual machines, and network security group changes.",
        ],
        "security_focus": [
            "Azure compromise often moves through Entra ID, service principals, and role assignments.",
            "Diagnostic settings and logging controls are high-value because attackers may reduce visibility.",
            "Key Vault, storage, and automation assets deserve tighter baseline review.",
        ],
    },
    "GCP": {
        "purpose": "Cloud platform for projects, IAM, service accounts, compute, storage, BigQuery, Kubernetes, and audit logs.",
        "how_it_works": [
            "GCP activity should be modeled around organization, folder, project, service account, and resource.",
            "Native audit logs are not yet directly mapped in this library, so posture and network context are the current starting points.",
            "Service account keys, IAM bindings, and data access logs are the core hunt surfaces once connected.",
        ],
        "what_to_review": [
            "New service account keys, IAM binding changes, project owner grants, and workload identity changes.",
            "Public buckets, BigQuery exports, logging sink changes, firewall changes, and new external IPs.",
            "Unusual project creation, region usage, Kubernetes changes, and data movement to external destinations.",
        ],
        "security_focus": [
            "Service accounts are common persistence and privilege paths in GCP.",
            "BigQuery and Cloud Storage need data-access logging for meaningful exfiltration hunts.",
            "Logging sink deletion or redirection can indicate defense evasion.",
        ],
    },
    "Oracle Cloud": {
        "purpose": "Cloud platform for OCI tenancy, identity, compute, networking, storage, databases, and cloud posture findings.",
        "how_it_works": [
            "OCI should be modeled by tenancy, compartment, identity, resource, and region.",
            "This library currently expects posture findings through Orca until native OCI logs are connected.",
            "Database, storage, identity, and public network exposure are high-value review areas.",
        ],
        "what_to_review": [
            "IAM policy changes, user/API key creation, federation changes, and compartment-level privilege grants.",
            "Public buckets, exposed compute, database access, security list changes, and logging configuration.",
            "Critical posture findings, secrets exposure, and vulnerable internet-facing workloads.",
        ],
        "security_focus": [
            "Compartment design can hide over-permissioned access if not reviewed with resource criticality.",
            "OCI database and storage services can hold sensitive data and need separate access baselines.",
            "Native log onboarding should be a roadmap item if OCI is business critical.",
        ],
    },
    "Windows": {
        "purpose": "Primary endpoint and server operating system surface for authentication, process, PowerShell, service, registry, and lateral movement hunts.",
        "how_it_works": [
            "Windows telemetry enters Sentinel through SecurityEvent, WindowsEvent, AMA, Sysmon, and EDR/XDR sources.",
            "Security events show logons, account changes, policy changes, process creation when enabled, and privileged activity.",
            "EDR and Sysmon-style telemetry add process lineage, file, registry, network, and module context.",
        ],
        "what_to_review": [
            "Logon type anomalies, local admin changes, service creation, scheduled tasks, PowerShell, WMI, and remote execution.",
            "Registry persistence, driver loads, LSASS access, security tool impairment, and ransomware precursors.",
            "Hosts with missing telemetry, agent health issues, or unusually quiet event volume.",
        ],
        "security_focus": [
            "Process command line logging and PowerShell script block logging materially improve hunt quality.",
            "Domain controllers, Entra Connect, PKI, jump servers, and admin workstations need separate baselines.",
            "Endpoint hunts should preserve process lineage and parent/child relationships where possible.",
        ],
    },
    "Linux": {
        "purpose": "Server and workload operating system surface for authentication, sudo, service, process, shell, package, file, and network hunts.",
        "how_it_works": [
            "Linux telemetry usually arrives through Syslog, agent health, auditd/Sysmon-for-Linux, or EDR sources.",
            "Auth logs, sudo logs, cron/systemd logs, package manager logs, and shell execution are key sources.",
            "Raw syslog needs careful parsing because distros and services write different formats.",
        ],
        "what_to_review": [
            "SSH brute force, successful logins after failures, sudo use, new users, SSH key changes, and privilege escalation.",
            "Cron/systemd persistence, suspicious downloads, chmod in temp paths, reverse shells, and archive staging.",
            "Web server child shells, public-facing app exploitation, and unexpected outbound SSH/SCP or HTTP callbacks.",
        ],
        "security_focus": [
            "Linux hunts are strongest when auditd or EDR process telemetry exists, not only generic syslog.",
            "Service accounts and web-service users need baselines because they are common post-exploit contexts.",
            "Temporary paths, shared memory, and startup locations are common staging areas.",
        ],
    },
    "Ubuntu": {
        "purpose": "Ubuntu-specific Linux hunting surface for apt, dpkg, snap, systemd, SSH, sudo, and common server workloads.",
        "how_it_works": [
            "Ubuntu commonly uses auth logs, syslog, journald, apt/dpkg logs, cloud-init, and systemd units.",
            "Package and service changes can explain new processes, persistence, or unexpected listeners.",
            "Cloud Ubuntu workloads should be correlated with cloud control-plane events and exposure findings.",
        ],
        "what_to_review": [
            "Apt/dpkg installs, new repositories, new services, modified systemd units, and suspicious snap packages.",
            "SSH key changes, sudo anomalies, cron jobs, new users, and cloud-init changes.",
            "Web workload exploitation, reverse shells, archive staging, and unexpected outbound connections.",
        ],
        "security_focus": [
            "Package installation is normal on servers but risky when it happens from unusual users, paths, or times.",
            "Cloud-init and systemd can provide persistence that looks like normal administration.",
            "Ubuntu server role matters: web, database, CI, and bastion hosts have different baselines.",
        ],
    },
    "Android": {
        "purpose": "Mobile endpoint and app-access context for managed Android devices, risky SaaS access, and mobile network behavior.",
        "how_it_works": [
            "This library currently expects Android visibility mainly through Netskope, SASE, CASB, MDM, or identity telemetry.",
            "Device posture, user, app, network, and location context are more realistic than low-level OS process telemetry.",
            "Mobile access hunts should combine identity, SaaS activity, device compliance, and risky network paths.",
        ],
        "what_to_review": [
            "Unmanaged or non-compliant devices accessing sensitive SaaS applications.",
            "Risky locations, unusual app usage, new device registrations, and impossible travel with mobile sessions.",
            "Downloads/uploads to risky apps, malware alerts from mobile security tooling, and policy bypasses.",
        ],
        "security_focus": [
            "Mobile compromise often appears as token/session abuse rather than traditional endpoint process telemetry.",
            "BYOD and unmanaged devices need different expectations from corporate-managed devices.",
            "Mobile phishing and messaging lures are relevant for LATAM operations, especially WhatsApp-themed lures.",
        ],
    },
    "iOS": {
        "purpose": "Mobile endpoint and app-access context for managed iOS devices, SaaS sessions, and identity-backed mobile access.",
        "how_it_works": [
            "This library currently expects iOS visibility through Netskope, MDM, identity, and SaaS audit telemetry.",
            "Useful context includes device compliance, app access, user identity, IP, location, and policy action.",
            "Low-level iOS process telemetry is uncommon in SIEM workflows, so focus on access and behavior.",
        ],
        "what_to_review": [
            "Sensitive SaaS access from unmanaged, jailbroken, non-compliant, or newly registered devices.",
            "Unusual geographies, risky networks, impossible travel, and new mobile device sessions.",
            "Downloads, uploads, sharing, OAuth app activity, and repeated policy challenges from mobile users.",
        ],
        "security_focus": [
            "iOS security hunting is often about access control and session risk rather than file/process events.",
            "Mobile tokens can remain useful after password reset if sessions and app grants are not revoked.",
            "Device compliance, Conditional Access, and SASE policy should be reviewed together.",
        ],
    },
}


QUERIES = OrderedDict(
    [
        (
            "daily/identity-failures-followed-by-success.kql",
            {
                "title": "Identity Failures Followed by Success",
                "cadence": "Daily Hunt",
                "tables": ["SigninLogs"],
                "tools": ["Microsoft Entra ID", "Microsoft Sentinel"],
                "objective": "Find users with repeated failed sign-ins followed by a successful sign-in from the same daily window.",
                "query": r"""let lookback = 1d;
let failureThreshold = 5;
let failures =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType != "0"
    | summarize
        FailedAttempts = count(),
        FailureIPs = make_set(IPAddress, 20),
        FailureApps = make_set(AppDisplayName, 20),
        FirstFailure = min(TimeGenerated),
        LastFailure = max(TimeGenerated)
        by UserPrincipalName;
let successes =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType == "0"
    | summarize
        Successes = count(),
        SuccessIPs = make_set(IPAddress, 20),
        SuccessApps = make_set(AppDisplayName, 20),
        FirstSuccess = min(TimeGenerated),
        LastSuccess = max(TimeGenerated)
        by UserPrincipalName;
failures
| where FailedAttempts >= failureThreshold
| join kind=inner successes on UserPrincipalName
| where LastFailure <= LastSuccess
| project
    UserPrincipalName,
    FailedAttempts,
    Successes,
    FailureIPs,
    SuccessIPs,
    FailureApps,
    SuccessApps,
    FirstFailure,
    LastFailure,
    FirstSuccess,
    LastSuccess
| order by FailedAttempts desc""",
            },
        ),
        (
            "daily/high-severity-alerts-and-incidents.kql",
            {
                "title": "High Severity Alerts and Incidents",
                "cadence": "Daily Hunt",
                "tables": [
                    "SecurityIncident",
                    "SecurityAlert",
                    "TrendMicro_XDR_WORKBENCH_CL",
                    "OrcaAlerts_CL",
                    "NetskopeAlerts_CL",
                ],
                "tools": [
                    "Microsoft Sentinel",
                    "Trend Vision One",
                    "Orca Security",
                    "Netskope",
                ],
                "objective": "Review high-priority detections and vendor alerts that may not yet be fully investigated.",
                "query": r"""let lookback = 1d;
union isfuzzy=true
(
    SecurityIncident
    | where TimeGenerated >= ago(lookback)
    | where Severity in ("High", "Medium") or Status !in ("Closed")
    | project TimeGenerated, Source = "Sentinel Incident", Severity, Status, Title, Entity = IncidentName, Url = IncidentUrl
),
(
    SecurityAlert
    | where TimeGenerated >= ago(lookback)
    | where AlertSeverity in ("High", "Medium")
    | project TimeGenerated, Source = "Sentinel Alert", Severity = AlertSeverity, Status, Title = AlertName, Entity = CompromisedEntity, Url = AlertLink
),
(
    TrendMicro_XDR_WORKBENCH_CL
    | where TimeGenerated >= ago(lookback)
    | where severity_s in~ ("critical", "high", "medium")
    | project TimeGenerated, Source = "Trend Vision One", Severity = severity_s, Status = investigationStatus_s, Title = workbenchName_s, Entity = HostHostName_s, Url = workbenchLink_s
),
(
    OrcaAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where risk_level_s in~ ("critical", "high", "medium")
    | project TimeGenerated, Source = "Orca Security", Severity = risk_level_s, Status = status_s, Title = alert_category_s, Entity = asset_name_s, Url = alert_ui_link_s
),
(
    NetskopeAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where severity in~ ("critical", "high", "medium") or severity_level in~ ("critical", "high", "medium")
    | project TimeGenerated, Source = "Netskope", Severity = coalesce(severity, severity_level), Status = acked, Title = alert_name, Entity = user, Url = url
)
| order by TimeGenerated desc""",
            },
        ),
        (
            "daily/endpoint-suspicious-powershell.kql",
            {
                "title": "Endpoint Suspicious PowerShell",
                "cadence": "Daily Hunt",
                "tables": ["SecurityEvent", "WindowsEvent", "TrendMicro_XDR_OAT_CL"],
                "tools": ["Microsoft Sentinel", "Trend Vision One"],
                "objective": "Find suspicious PowerShell and script execution from Windows and XDR telemetry.",
                "query": r"""let lookback = 1d;
let suspiciousTerms = dynamic(["-enc", "-encodedcommand", "frombase64string", "downloadstring", "invoke-expression", "iex ", "bypass", "hidden", "reflection.assembly"]);
union isfuzzy=true
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4688, 4103, 4104)
    | extend Command = tostring(coalesce(CommandLine, EventData))
    | project TimeGenerated, Source = "SecurityEvent", Computer, Account = coalesce(Account, SubjectUserName, TargetUserName), Command, ProcessName, ParentProcessName, EventID
),
(
    WindowsEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4688, 4103, 4104)
    | extend Command = tostring(EventData)
    | project TimeGenerated, Source = "WindowsEvent", Computer, Account = tostring(EventData.SubjectUserName), Command, ProcessName = tostring(EventData.NewProcessName), ParentProcessName = tostring(EventData.ParentProcessName), EventID
),
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | extend Command = tostring(coalesce(detail_processCmd_s, detail_objectCmd_s, detail_parentCmd_s, detail_eventDataScriptBlockText_s))
    | project TimeGenerated, Source = "Trend Vision One", Computer = detail_endpointHostName_s, Account = detail_processUser_s, Command, ProcessName = detail_processName_s, ParentProcessName = detail_parentName_s, EventID = toint(detail_eventId_d)
)
| where Command has_any (suspiciousTerms)
| order by TimeGenerated desc""",
            },
        ),
        (
            "daily/network-waf-and-firewall-blocks.kql",
            {
                "title": "Network WAF and Firewall Blocks",
                "cadence": "Daily Hunt",
                "tables": ["CommonSecurityLog", "Cloudflare_CL", "NetskopeEventsNetwork_CL"],
                "tools": ["Fortigate", "Cloudflare", "Netskope"],
                "objective": "Review blocked or high-risk network activity across firewall, WAF, and SASE telemetry.",
                "query": r"""let lookback = 1d;
union isfuzzy=true
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | where DeviceAction has_any ("deny", "drop", "block", "blocked") or SimplifiedDeviceAction has_any ("deny", "drop", "block")
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), Action = coalesce(DeviceAction, SimplifiedDeviceAction), SrcIp = SourceIP, DstIp = DestinationIP, DstPort = tostring(DestinationPort), Url = RequestURL, User = SourceUserName, Reason
),
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | where SecurityAction_s has_any ("block", "challenge", "jschallenge", "managed_challenge") or WAFAttackScore_d < 40
    | project TimeGenerated, Source = "Cloudflare", Action = SecurityAction_s, SrcIp = ClientIP_s, DstIp = OriginIP_s, DstPort = "", Url = ClientRequestURI_s, User = RequestHeaders_cf_access_user_s, Reason = SecurityRuleDescription_s
),
(
    NetskopeEventsNetwork_CL
    | where TimeGenerated >= ago(lookback)
    | where action has_any ("block", "deny") or ccl in~ ("poor", "low")
    | project TimeGenerated, Source = "Netskope Network", Action = action, SrcIp = srcip, DstIp = dstip, DstPort = tostring(dstport), Url = ur_normalized, User = user, Reason = policy
)
| summarize Events = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Reasons = make_set(Reason, 10), Users = make_set(User, 20) by Source, Action, SrcIp, DstIp, DstPort, Url
| order by Events desc""",
            },
        ),
        (
            "daily/data-source-health.kql",
            {
                "title": "Data Source Health",
                "cadence": "Daily Hunt",
                "tables": [
                    "Heartbeat",
                    "SentinelHealth",
                    "AMAAgentHealth_CL",
                    "TrendMicro_XDR_Health_Check_CL",
                    "TrendMicro_XDR_OAT_Health_Check_CL",
                ],
                "tools": ["Microsoft Sentinel", "Trend Vision One"],
                "objective": "Find collection gaps and connector health issues before hunting results are trusted.",
                "query": r"""let lookback = 1d;
union isfuzzy=true
(
    Heartbeat
    | where TimeGenerated >= ago(lookback)
    | summarize LastSeen = max(TimeGenerated), Events = count() by Source = "Heartbeat", Entity = Computer, Status = OSType
),
(
    SentinelHealth
    | where TimeGenerated >= ago(lookback)
    | summarize LastSeen = max(TimeGenerated), Events = count() by Source = "SentinelHealth", Entity = SentinelResourceName, Status = Status
),
(
    AMAAgentHealth_CL
    | where TimeGenerated >= ago(lookback)
    | summarize LastSeen = max(TimeGenerated), Events = count() by Source = "AMAAgentHealth", Entity = Type, Status = "Reported"
),
(
    TrendMicro_XDR_Health_Check_CL
    | where TimeGenerated >= ago(lookback)
    | summarize LastSeen = max(TimeGenerated), Events = count() by Source = "Trend XDR Health", Entity = tostring(clpId_g), Status = coalesce(error_s, "OK")
),
(
    TrendMicro_XDR_OAT_Health_Check_CL
    | where TimeGenerated >= ago(lookback)
    | summarize LastSeen = max(TimeGenerated), Events = count() by Source = "Trend OAT Health", Entity = tostring(clpId_g), Status = coalesce(error_s, "OK")
)
| extend AgeHours = datetime_diff("hour", now(), LastSeen)
| order by AgeHours desc""",
            },
        ),
        (
            "weekly/new-admin-or-role-changes.kql",
            {
                "title": "New Admin or Role Changes",
                "cadence": "Weekly Hunt",
                "tables": ["AuditLogs", "AzureActivity", "CyberArk_AuditEvents_CL"],
                "tools": ["Microsoft Entra ID", "Microsoft Sentinel", "CyberArk"],
                "objective": "Review privileged role, policy, password, and credential access changes.",
                "query": r"""let lookback = 7d;
let adminTerms = dynamic(["admin", "administrator", "role", "privileged", "owner", "password", "credential", "secret", "policy"]);
union isfuzzy=true
(
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | where ActivityDisplayName has_any (adminTerms) or OperationName has_any (adminTerms)
    | project TimeGenerated, Source = "AuditLogs", Actor = tostring(InitiatedBy), Operation = coalesce(ActivityDisplayName, OperationName), Target = tostring(TargetResources), Result, Details = tostring(AdditionalDetails)
),
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any (adminTerms) or ActivityStatusValue !in~ ("Succeeded", "Success")
    | project TimeGenerated, Source = "AzureActivity", Actor = Caller, Operation = OperationNameValue, Target = ResourceId, Result = ActivityStatusValue, Details = Properties
),
(
    CyberArk_AuditEvents_CL
    | where TimeGenerated >= ago(lookback)
    | where action has_any (adminTerms) or command has_any (adminTerms) or safe has_any (adminTerms)
    | project TimeGenerated, Source = "CyberArk", Actor = username, Operation = action, Target = coalesce(targetAccount, target, safe), Result = actionType, Details = message
)
| order by TimeGenerated desc""",
            },
        ),
        (
            "weekly/cloud-risk-posture.kql",
            {
                "title": "Cloud Risk Posture",
                "cadence": "Weekly Hunt",
                "tables": ["OrcaAlerts_CL", "AzureActivity", "AzureDiagnostics"],
                "tools": ["Orca Security", "Microsoft Sentinel"],
                "objective": "Review high-risk cloud posture findings and suspicious control-plane activity.",
                "query": r"""let lookback = 7d;
union isfuzzy=true
(
    OrcaAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where risk_level_s in~ ("critical", "high")
    | project TimeGenerated, Source = "Orca", Severity = risk_level_s, Asset = asset_name_s, Account = account_name_s, Region = asset_regions_s, Finding = alert_category_s, Recommendation = recommendation_s, Url = alert_ui_link_s
),
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where ActivityStatusValue !in~ ("Succeeded", "Success") or OperationNameValue has_any ("delete", "write", "roleAssignments", "policyAssignments")
    | project TimeGenerated, Source = "AzureActivity", Severity = ActivityStatusValue, Asset = Resource, Account = Caller, Region = ResourceGroup, Finding = OperationNameValue, Recommendation = ResultDescription, Url = ResourceId
),
(
    AzureDiagnostics
    | where TimeGenerated >= ago(lookback)
    | where ResultType !in~ ("Success", "Succeeded", "OK") or Level in~ ("Error", "Warning")
    | project TimeGenerated, Source = "AzureDiagnostics", Severity = coalesce(Level, ResultType), Asset = Resource, Account = "", Region = ResourceGroup, Finding = OperationName, Recommendation = ResultDescription, Url = ResourceId
)
| order by TimeGenerated desc""",
            },
        ),
        (
            "weekly/rare-app-and-user-agent-access.kql",
            {
                "title": "Rare App and User Agent Access",
                "cadence": "Weekly Hunt",
                "tables": ["SigninLogs", "OfficeActivity", "NetskopeEventsApplication_CL"],
                "tools": ["Microsoft Entra ID", "Microsoft 365", "Netskope"],
                "objective": "Find new or rare app/user-agent combinations for users over the last week.",
                "query": r"""let baselineStart = ago(30d);
let baselineEnd = ago(7d);
let huntWindow = 7d;
let signinBaseline =
    SigninLogs
    | where TimeGenerated between (baselineStart .. baselineEnd)
    | summarize by UserPrincipalName, AppDisplayName, ClientAppUsed, UserAgent;
let signinCurrent =
    SigninLogs
    | where TimeGenerated >= ago(huntWindow)
    | project TimeGenerated, Source = "SigninLogs", User = UserPrincipalName, App = AppDisplayName, Client = ClientAppUsed, UserAgent, IPAddress, ResultType;
let rareSignin =
    signinCurrent
    | join kind=leftanti signinBaseline on $left.User == $right.UserPrincipalName, $left.App == $right.AppDisplayName, $left.Client == $right.ClientAppUsed, UserAgent;
let netskope =
    NetskopeEventsApplication_CL
    | where TimeGenerated >= ago(huntWindow)
    | where ccl in~ ("poor", "low") or sanctioned_instance in~ ("false", "no")
    | project TimeGenerated, Source = "NetskopeApplication", User = userPrincipalName, App = app, Client = browser, UserAgent = useragent, IPAddress = srcip, ResultType = action;
let office =
    OfficeActivity
    | where TimeGenerated >= ago(huntWindow)
    | project TimeGenerated, Source = "OfficeActivity", User = UserId, App = OfficeWorkload, Client = ClientIP, UserAgent = UserAgent, IPAddress = ClientIP, ResultType = Operation;
union rareSignin, netskope, office
| summarize Events = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), IPs = make_set(IPAddress, 20), Results = make_set(ResultType, 20) by Source, User, App, Client, UserAgent
| order by Events desc""",
            },
        ),
        (
            "weekly/top-egress-and-denied-traffic.kql",
            {
                "title": "Top Egress and Denied Traffic",
                "cadence": "Weekly Hunt",
                "tables": ["CommonSecurityLog", "NetskopeEventsNetwork_CL", "Cloudflare_CL"],
                "tools": ["Fortigate", "Netskope", "Cloudflare"],
                "objective": "Baseline outbound volume, destinations, users, and blocked network activity.",
                "query": r"""let lookback = 7d;
union isfuzzy=true
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), User = SourceUserName, SrcIp = SourceIP, DstIp = DestinationIP, Destination = coalesce(DestinationHostName, DestinationDnsDomain, DestinationIP), Action = coalesce(DeviceAction, SimplifiedDeviceAction), Bytes = tolong(ReceivedBytes) + tolong(SentBytes)
),
(
    NetskopeEventsNetwork_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Netskope Network", User = userPrincipalName, SrcIp = srcip, DstIp = dstip, Destination = coalesce(dsthost, domain, ur_normalized), Action = action, Bytes = tolong(client_bytes) + tolong(server_bytes)
),
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Cloudflare", User = RequestHeaders_cf_access_user_s, SrcIp = ClientIP_s, DstIp = OriginIP_s, Destination = ClientRequestHost_s, Action = coalesce(SecurityAction_s, tostring(EdgeResponseStatus_d)), Bytes = tolong(ClientRequestBytes_d) + tolong(EdgeResponseBytes_d)
)
| summarize Events = count(), TotalBytes = sum(Bytes), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Actions = make_set(Action, 20) by Source, User, SrcIp, DstIp, Destination
| order by TotalBytes desc, Events desc""",
            },
        ),
        (
            "intel/ioc-ip-domain-url-hash-sweep.kql",
            {
                "title": "IOC IP Domain URL Hash Sweep",
                "cadence": "Intel Hunt",
                "tables": [
                    "ThreatIntelIndicators",
                    "CommonSecurityLog",
                    "Cloudflare_CL",
                    "NetskopeAlerts_CL",
                    "NetskopeEventsApplication_CL",
                    "NetskopeEventsNetwork_CL",
                    "TrendMicro_XDR_OAT_CL",
                    "TrendMicro_XDR_WORKBENCH_CL",
                    "OrcaAlerts_CL",
                ],
                "tools": [
                    "Microsoft Sentinel",
                    "Fortigate",
                    "Cloudflare",
                    "Netskope",
                    "Trend Vision One",
                    "Orca Security",
                ],
                "objective": "Match active threat intelligence observables against network, endpoint, cloud, and vendor telemetry.",
                "query": r"""let telemetryLookback = 7d;
let intelLookback = 30d;
let indicators =
    ThreatIntelIndicators
    | where TimeGenerated >= ago(intelLookback)
    | where IsActive == true and IsDeleted != true and Revoked != true
    | where isnotempty(ObservableValue)
    | project Indicator = tostring(ObservableValue), ObservableKey, Confidence, Tags, ValidUntil;
let telemetry =
    union isfuzzy=true
    (
        CommonSecurityLog
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "CommonSecurityLog", Entity = coalesce(SourceUserName, Computer), Observable = coalesce(DestinationIP, SourceIP, RequestURL, FileHash, DestinationHostName), Context = strcat(DeviceVendor, " ", DeviceProduct, " ", DeviceAction)
    ),
    (
        Cloudflare_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Cloudflare", Entity = RequestHeaders_cf_access_user_s, Observable = coalesce(ClientIP_s, OriginIP_s, ClientRequestURI_s, ClientRequestHost_s, JA3Hash_s), Context = strcat(SecurityAction_s, " ", SecurityRuleDescription_s)
    ),
    (
        NetskopeAlerts_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Netskope Alerts", Entity = userPrincipalName, Observable = coalesce(srcip, dstip, url, domain, sha256, md5), Context = strcat(alert_name, " ", action)
    ),
    (
        NetskopeEventsApplication_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Netskope Application", Entity = userPrincipalName, Observable = coalesce(srcip, dstip, url, domain, sha256, md5), Context = strcat(app, " ", action)
    ),
    (
        NetskopeEventsNetwork_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Netskope Network", Entity = userPrincipalName, Observable = coalesce(srcip, dstip, dsthost, domain, ur_normalized), Context = strcat(action, " ", policy)
    ),
    (
        TrendMicro_XDR_OAT_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Trend OAT", Entity = detail_endpointHostName_s, Observable = coalesce(detail_dst_s, detail_src_s, detail_domainName_s, detail_urlCat_s, detail_fileHashSha256_s, detail_objectFileHashSha256_s), Context = strcat(detail_detectionName_s, " ", detail_processName_s)
    ),
    (
        TrendMicro_XDR_WORKBENCH_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Trend Workbench", Entity = HostHostName_s, Observable = coalesce(IPAddress, URL_s, DomainName_s, FileHashValue_s), Context = strcat(severity_s, " ", workbenchName_s)
    ),
    (
        OrcaAlerts_CL
        | where TimeGenerated >= ago(telemetryLookback)
        | project TimeGenerated, Source = "Orca", Entity = asset_name_s, Observable = coalesce(asset_hostname_s, findings_PublicUrl_s, findings_PrimaryEndpoints_s, findings_Sha256_s, findings_Sha1_s), Context = strcat(risk_level_s, " ", alert_category_s)
    );
telemetry
| where isnotempty(Observable)
| join kind=inner indicators on $left.Observable == $right.Indicator
| project TimeGenerated, Source, Entity, Observable, ObservableKey, Confidence, Tags, ValidUntil, Context
| order by TimeGenerated desc""",
            },
        ),
        (
            "intel/trend-mitre-mapping-hunt.kql",
            {
                "title": "Trend MITRE Mapping Hunt",
                "cadence": "Intel Hunt",
                "tables": ["TrendMicro_XDR_OAT_CL", "SecurityAlert"],
                "tools": ["Trend Vision One", "Microsoft Sentinel"],
                "objective": "Pivot from ATT&CK tactic or technique mappings in Trend and Sentinel alerts.",
                "query": r"""let lookback = 14d;
let attackFilter = dynamic(["T1059", "T1078", "T1021", "T1110", "T1566", "T1486"]);
union isfuzzy=true
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | where detail_mitreMapping_s has_any (attackFilter) or detail_tacticId_s has_any (attackFilter)
    | project TimeGenerated, Source = "Trend OAT", Entity = detail_endpointHostName_s, User = detail_processUser_s, Tactics = detail_tacticId_s, Techniques = detail_mitreMapping_s, Detection = detail_detectionName_s, Process = detail_processName_s, Command = detail_processCmd_s
),
(
    SecurityAlert
    | where TimeGenerated >= ago(lookback)
    | where Techniques has_any (attackFilter) or SubTechniques has_any (attackFilter)
    | project TimeGenerated, Source = "Sentinel Alert", Entity = CompromisedEntity, User = "", Tactics, Techniques = strcat(Techniques, " ", SubTechniques), Detection = AlertName, Process = ProductName, Command = Description
)
| summarize Events = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Detections = make_set(Detection, 20), Commands = make_set(Command, 20) by Source, Entity, User, Tactics, Techniques, Process
| order by Events desc""",
            },
        ),
        (
            "intel/high-risk-cloud-exposure-sweep.kql",
            {
                "title": "High Risk Cloud Exposure Sweep",
                "cadence": "Intel Hunt",
                "tables": ["OrcaAlerts_CL", "AzureActivity", "Cloudflare_CL"],
                "tools": ["Orca Security", "Microsoft Sentinel", "Cloudflare"],
                "objective": "Hunt for exposed cloud assets, risky posture, and external access activity related to public services.",
                "query": r"""let lookback = 14d;
let riskyTerms = dynamic(["public", "internet", "exposed", "anonymous", "open", "0.0.0.0", "critical", "high"]);
union isfuzzy=true
(
    OrcaAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where risk_level_s in~ ("critical", "high") or RawData has_any (riskyTerms)
    | project TimeGenerated, Source = "Orca", Asset = asset_name_s, Account = account_name_s, Risk = risk_level_s, Finding = alert_category_s, Context = RawData, Url = alert_ui_link_s
),
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any ("networkSecurityGroups", "publicIPAddresses", "roleAssignments", "storageAccounts") or Properties has_any (riskyTerms)
    | project TimeGenerated, Source = "AzureActivity", Asset = Resource, Account = Caller, Risk = ActivityStatusValue, Finding = OperationNameValue, Context = Properties, Url = ResourceId
),
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | where EdgeResponseStatus_d >= 500 or SecurityAction_s has_any ("block", "challenge") or ClientRequestURI_s has_any ("/admin", "/login", "/wp-admin")
    | project TimeGenerated, Source = "Cloudflare", Asset = ClientRequestHost_s, Account = RequestHeaders_cf_access_user_s, Risk = tostring(EdgeResponseStatus_d), Finding = SecurityRuleDescription_s, Context = strcat(ClientIP_s, " ", ClientRequestURI_s), Url = ClientRequestURI_s
)
| order by TimeGenerated desc""",
            },
        ),
        (
            "monthly/coverage-and-ingestion-review.kql",
            {
                "title": "Coverage and Ingestion Review",
                "cadence": "Monthly Hunt",
                "tables": ["Usage", "Heartbeat", "SentinelHealth"],
                "tools": ["Microsoft Sentinel"],
                "objective": "Review whether expected data sources are still sending logs and whether ingestion changed materially.",
                "query": r"""let lookback = 30d;
let ingestion =
    Usage
    | where TimeGenerated >= ago(lookback)
    | summarize UsageEvents = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated) by DataType;
let hosts =
    Heartbeat
    | where TimeGenerated >= ago(lookback)
    | summarize HeartbeatEvents = count(), HostLastSeen = max(TimeGenerated), Hosts = dcount(Computer) by OSType;
let sentinelHealth =
    SentinelHealth
    | where TimeGenerated >= ago(lookback)
    | summarize HealthEvents = count(), HealthLastSeen = max(TimeGenerated) by SentinelResourceName, Status;
ingestion
| order by DataType asc
| project DataType, UsageEvents, FirstSeen, LastSeen
| union (
    hosts
    | project DataType = strcat("Heartbeat/", OSType), UsageEvents = HeartbeatEvents, FirstSeen = datetime(null), LastSeen = HostLastSeen
)
| union (
    sentinelHealth
    | project DataType = strcat("SentinelHealth/", SentinelResourceName, "/", Status), UsageEvents = HealthEvents, FirstSeen = datetime(null), LastSeen = HealthLastSeen
)""",
            },
        ),
        (
            "monthly/analytics-rule-and-incident-quality.kql",
            {
                "title": "Analytics Rule and Incident Quality",
                "cadence": "Monthly Hunt",
                "tables": ["SecurityIncident", "SecurityAlert", "SentinelAudit"],
                "tools": ["Microsoft Sentinel"],
                "objective": "Review noisy detections, incident lifecycle, ownership, and closure quality.",
                "query": r"""let lookback = 30d;
let incidents =
    SecurityIncident
    | where TimeGenerated >= ago(lookback)
    | summarize
        Incidents = dcount(IncidentNumber),
        OpenIncidents = dcountif(IncidentNumber, Status !in ("Closed")),
        ClosedIncidents = dcountif(IncidentNumber, Status == "Closed"),
        Owners = make_set(tostring(Owner), 20),
        Classifications = make_set(Classification, 20)
        by Severity, Title;
let alerts =
    SecurityAlert
    | where TimeGenerated >= ago(lookback)
    | summarize Alerts = count(), AlertEntities = dcount(CompromisedEntity), Tactics = make_set(Tactics, 20), Techniques = make_set(Techniques, 20) by AlertSeverity, AlertName, ProductName;
incidents
| project Type = "Incident", Severity, Name = Title, Count = Incidents, OpenCount = OpenIncidents, ClosedCount = ClosedIncidents, Details = strcat("Owners=", tostring(Owners), " Classifications=", tostring(Classifications))
| union (
    alerts
    | project Type = "Alert", Severity = AlertSeverity, Name = AlertName, Count = Alerts, OpenCount = long(null), ClosedCount = long(null), Details = strcat("Product=", ProductName, " Entities=", AlertEntities, " Tactics=", tostring(Tactics), " Techniques=", tostring(Techniques))
)
| order by Count desc""",
            },
        ),
        (
            "monthly/identity-baseline-review.kql",
            {
                "title": "Identity Baseline Review",
                "cadence": "Monthly Hunt",
                "tables": ["IdentityInfo", "SigninLogs", "AuditLogs"],
                "tools": ["Microsoft Entra ID", "Microsoft Sentinel"],
                "objective": "Review identity posture, inactive accounts, privileged changes, and high-volume sign-in patterns.",
                "query": r"""let lookback = 30d;
let signinSummary =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | summarize SignIns = count(), FailedSignIns = countif(ResultType != "0"), IPs = dcount(IPAddress), Apps = dcount(AppDisplayName), LastSignIn = max(TimeGenerated) by UserPrincipalName;
let auditSummary =
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | summarize AuditEvents = count(), Operations = make_set(ActivityDisplayName, 20), LastAudit = max(TimeGenerated) by Identity;
IdentityInfo
| summarize arg_max(TimeGenerated, *) by AccountUPN
| join kind=fullouter signinSummary on $left.AccountUPN == $right.UserPrincipalName
| join kind=leftouter auditSummary on $left.AccountUPN == $right.Identity
| project
    Account = coalesce(AccountUPN, UserPrincipalName, Identity),
    AccountDisplayName,
    AccountObjectId,
    SignIns,
    FailedSignIns,
    IPs,
    Apps,
    LastSignIn,
    AuditEvents,
    Operations,
    LastAudit,
    Tags,
    AssignedRoles
| order by FailedSignIns desc, SignIns desc""",
            },
        ),
        (
            "monthly/log-cost-and-billable-volume.kql",
            {
                "title": "Log Cost and Billable Volume",
                "cadence": "Monthly Hunt",
                "tables": [
                    "SigninLogs",
                    "AuditLogs",
                    "SecurityEvent",
                    "WindowsEvent",
                    "CommonSecurityLog",
                    "Cloudflare_CL",
                    "NetskopeAlerts_CL",
                    "NetskopeEventsApplication_CL",
                    "NetskopeEventsConnection_CL",
                    "NetskopeEventsNetwork_CL",
                    "NetskopeEventsPage_CL",
                    "OrcaAlerts_CL",
                    "TrendMicro_XDR_OAT_CL",
                    "TrendMicro_XDR_WORKBENCH_CL",
                ],
                "tools": ["Microsoft Sentinel"],
                "objective": "Rank table volume and billable size to guide retention, parsing, and cost tuning.",
                "query": r"""let lookback = 30d;
union withsource=TableName isfuzzy=true
    SigninLogs,
    AuditLogs,
    SecurityEvent,
    WindowsEvent,
    CommonSecurityLog,
    Cloudflare_CL,
    NetskopeAlerts_CL,
    NetskopeEventsApplication_CL,
    NetskopeEventsConnection_CL,
    NetskopeEventsNetwork_CL,
    NetskopeEventsPage_CL,
    OrcaAlerts_CL,
    TrendMicro_XDR_OAT_CL,
    TrendMicro_XDR_WORKBENCH_CL
| where TimeGenerated >= ago(lookback)
| summarize
    Events = count(),
    BillableMB = round(sum(_BilledSize) / 1024.0 / 1024.0, 2),
    FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated)
    by TableName, IsBillable = tostring(_IsBillable)
| order by BillableMB desc, Events desc""",
            },
        ),
    ]
)


METHODOLOGIES = {
    "methodologies/threat-hunting-overview.md": (
        "Threat Hunting Overview",
        "The library is organized around the hunting process: start with a question, confirm data coverage, run the query, validate results, document outcomes, and decide whether to create detection logic, a watchlist, or an investigation task.",
    ),
    "methodologies/hypothesis-driven.md": (
        "Hypothesis Driven Hunting",
        "Use when you can express a testable adversary or abuse hypothesis, such as 'an attacker with valid credentials is accessing a cloud admin portal from a new geography.'",
    ),
    "methodologies/data-driven.md": (
        "Data Driven Hunting",
        "Use when the hunt starts from available telemetry, baselines, outliers, and recurring review of Sentinel tables.",
    ),
    "methodologies/intel-driven.md": (
        "Intel Driven Hunting",
        "Use when new indicators, TTPs, campaigns, CVEs, or vendor intelligence need to be translated into searches against your Sentinel tables.",
    ),
    "methodologies/latam-threat-intelligence.md": (
        "LATAM Threat Intelligence and Regional Hunting",
        "Use when regional context for Brazil, Mexico, Colombia, Chile, Argentina, or wider LATAM operations should shape hunt ideas and Sentinel table mapping.",
    ),
    "methodologies/peak-framework.md": (
        "PEAK Framework",
        "Use PEAK-style thinking to keep hunts tied to purpose, execution, analysis, and knowledge capture. Each hunt page should preserve why it exists, how it runs, what was learned, and what should change.",
    ),
    "methodologies/model-assisted.md": (
        "Model Assisted Hunting",
        "Use when rarity, clustering, scoring, time-series, or machine learning can surface suspicious behavior that static KQL alone may miss.",
    ),
    "methodologies/research-resources.md": (
        "Research Resources",
        "Use when developing hunt ideas from threat intelligence, internal incidents, detection gaps, new data sources, or public research.",
    ),
}


SCRIPT_PAGES = {
    "scripts/powershell.md": ("PowerShell", "Windows endpoint collection, enrichment, triage, and response helper scripts."),
    "scripts/python.md": ("Python", "Parsing, enrichment, IOC transformation, API collection, and notebook-style analysis."),
    "scripts/bash.md": ("Bash", "Linux collection, text processing, and small automation around exported hunt results."),
    "scripts/go.md": ("Go", "Compiled utilities for high-volume parsing, collectors, or repeatable enrichment tools."),
    "scripts/java.md": ("Java", "Application or platform integrations that produce huntable telemetry."),
    "scripts/csharp.md": ("C#", "Windows, .NET, and Azure-oriented utilities or proof-of-concept parsers."),
}


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write(path: str | Path, content: str) -> None:
    target = ROOT / path if isinstance(path, str) else path
    ensure_parent(target)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_if_missing(path: str | Path, content: str) -> None:
    target = ROOT / path if isinstance(path, str) else path
    if target.exists():
        return
    write(target, content)


def read_schema() -> str:
    if not SCHEMA_REFERENCE.exists():
        ensure_parent(SCHEMA_REFERENCE)
        if not ATTACHMENT_SCHEMA.exists():
            raise FileNotFoundError(
                f"Schema source not found: {ATTACHMENT_SCHEMA} or {SCHEMA_REFERENCE}"
            )
        shutil.copyfile(ATTACHMENT_SCHEMA, SCHEMA_REFERENCE)
    return SCHEMA_REFERENCE.read_text(encoding="utf-8")


def migrate_placeholders() -> None:
    for src_name, dst_name in FOLDER_MOVES.items():
        src = ROOT / src_name
        dst = ROOT / dst_name
        if src.exists() and not dst.exists():
            ensure_parent(dst)
            src.replace(dst)


def parse_schema(text: str) -> tuple[OrderedDict[str, list[tuple[str, str]]], int, list[str]]:
    tables: OrderedDict[str, list[tuple[str, str]]] = OrderedDict()
    raw_table_count = 0
    duplicates: list[str] = []
    current: str | None = None

    for line in text.splitlines():
        header = TABLE_HEADER_RE.match(line)
        field = FIELD_RE.match(line)
        if header:
            current = header.group(1)
            raw_table_count += 1
            if current in tables:
                duplicates.append(current)
            else:
                tables[current] = []
            continue
        if field and current:
            item = (field.group(1), field.group(2))
            if item not in tables[current]:
                tables[current].append(item)

    tables = OrderedDict((name, fields) for name, fields in tables.items() if fields)
    return tables, raw_table_count, sorted(set(duplicates))


def table_link(table: str) -> str:
    return f"[{table}](reference/{table}.md)"


def root_table_link(table: str) -> str:
    return f"[{table}](../sentinel/tables/reference/{table}.md)"


def kql_link(path: str) -> str:
    return f"[`{path}`](../../sentinel/kql/{path})"


def bullet(items: list[str]) -> str:
    if not items:
        return "- TBD\n"
    return "\n".join(f"- {item}" for item in items) + "\n"


def table_bullet_links(tables: list[str], prefix: str = "../tables/reference") -> str:
    if not tables:
        return "- TBD\n"
    return "\n".join(f"- [{table}]({prefix}/{table}.md)" for table in tables) + "\n"


def describe_table(name: str) -> str:
    descriptions = {
        "SigninLogs": "Microsoft Entra ID sign-in telemetry for authentication, Conditional Access, risk, device, IP, and application access hunts.",
        "AuditLogs": "Microsoft Entra ID audit activity for directory, role, application, policy, and administrative changes.",
        "AzureActivity": "Azure control-plane operations for resource changes, failures, role assignments, and subscription activity.",
        "AzureDiagnostics": "Azure resource diagnostics and service logs for platform and resource-level hunting.",
        "CommonSecurityLog": "CEF-style security telemetry commonly used for firewalls, network security devices, and proxy logs.",
        "SecurityEvent": "Windows Security Event logs collected into Sentinel, useful for logon, process, account, service, and policy hunts.",
        "WindowsEvent": "Windows Event logs collected with AMA, useful for provider-specific endpoint and PowerShell hunts.",
        "OfficeActivity": "Microsoft 365 audit activity for Exchange, SharePoint, Teams, and other workloads.",
        "SecurityAlert": "Alert records produced by Microsoft and connected security products.",
        "SecurityIncident": "Microsoft Sentinel incident records for case management, triage quality, and incident lifecycle review.",
        "ThreatIntelIndicators": "Threat intelligence indicators stored in Sentinel for IOC matching and intel-driven hunts.",
        "IdentityInfo": "UEBA identity enrichment that helps join account details, tags, roles, and identity context to hunt results.",
        "BehaviorAnalytics": "UEBA behavior output used for entity risk, anomaly, and peer-based investigation.",
        "UserPeerAnalytics": "User peer group analytics for identity anomaly and outlier analysis.",
        "Heartbeat": "Agent heartbeat records used to verify coverage and collection health.",
        "LAQueryLogs": "Log Analytics query audit data for query review, expensive queries, and hunting activity governance.",
        "Usage": "Workspace usage records for ingestion, billable data, and data source coverage review.",
        "SentinelAudit": "Sentinel audit records for changes to Sentinel resources and operations.",
        "SentinelHealth": "Sentinel health records for connectors, analytics, automation, and operational monitoring.",
        "Watchlist": "Sentinel watchlist records for allowlists, business context, IOC lists, and enrichment.",
        "Anomalies": "Sentinel anomaly records for behavior and detection review.",
        "Cloudflare_CL": "Cloudflare custom log table for WAF, edge, bot, request, origin, and security action hunts.",
        "CyberArk_AuditEvents_CL": "CyberArk audit events for privileged access, safe, account, and session activity hunts.",
        "OrcaAlerts_CL": "Orca Security alerts and posture findings for cloud asset exposure, vulnerabilities, secrets, and configuration risk.",
        "TrendMicro_XDR_OAT_CL": "Trend Vision One observed attack technique telemetry for process, file, network, mail, registry, and MITRE-mapped endpoint hunts.",
        "TrendMicro_XDR_WORKBENCH_CL": "Trend Vision One workbench alerts for XDR triage and endpoint investigation.",
        "NetskopeAlerts_CL": "Netskope alert records for SASE, CASB, DLP, malware, and policy event review.",
        "NetskopeEventsApplication_CL": "Netskope application activity records for SaaS access, file, app, DLP, user, and device hunts.",
        "NetskopeEventsAudit_CL": "Netskope audit records for configuration and administrative activity.",
        "NetskopeEventsConnection_CL": "Netskope connection telemetry for web, proxy, and session-level network hunts.",
        "NetskopeEventsNetwork_CL": "Netskope network events for egress, tunnel, source, destination, protocol, and policy hunts.",
        "NetskopeEventsPage_CL": "Netskope page events for web access, URL, category, and policy review.",
    }
    if name.startswith("App"):
        return "Application Insights telemetry for application behavior, dependencies, exceptions, requests, traces, metrics, and performance hunting."
    if name.startswith("TrendMicro_XDR"):
        return "Trend Vision One custom table used for endpoint/XDR health, detection, or workbench hunting."
    if name.startswith("Netskope"):
        return "Netskope custom table used for SASE, CASB, web, DLP, application, and network hunting."
    return descriptions.get(name, "Sentinel/Log Analytics table available for hunting and correlation.")


def high_value_fields(fields: list[tuple[str, str]]) -> list[tuple[str, str]]:
    patterns = [
        "TimeGenerated",
        "UserPrincipalName",
        "User",
        "Account",
        "Identity",
        "IPAddress",
        "ClientIP",
        "SourceIP",
        "DestinationIP",
        "srcip",
        "dstip",
        "Computer",
        "Host",
        "Device",
        "EventID",
        "Operation",
        "Activity",
        "Action",
        "Severity",
        "Risk",
        "Status",
        "Command",
        "Process",
        "File",
        "Hash",
        "URL",
        "Url",
        "Domain",
        "Location",
        "Resource",
        "Incident",
        "Alert",
        "Tactic",
        "Technique",
        "mitre",
    ]
    selected: list[tuple[str, str]] = []
    for field in fields:
        name = field[0]
        if any(pattern.lower() in name.lower() for pattern in patterns):
            selected.append(field)
    if not selected:
        selected = fields[:12]
    return selected[:30]


def field_rows(fields: list[tuple[str, str]]) -> str:
    return "\n".join(f"| `{name}` | `{type_}` |" for name, type_ in fields)


def generate_table_reference(tables: OrderedDict[str, list[tuple[str, str]]]) -> None:
    for name, fields in tables.items():
        starter_projection = ", ".join(name for name, _ in high_value_fields(fields)[:8])
        content = f"""# {name}

## Hunting Purpose
{describe_table(name)}

## Key Hunting Fields
| Field | Type |
| --- | --- |
{field_rows(high_value_fields(fields))}

## Starter Query
```kql
{name}
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Quick Projection
```kql
{name}
| where TimeGenerated >= ago(24h)
| project {starter_projection}
| take 100
```

## Full Schema
| Field | Type |
| --- | --- |
{field_rows(fields)}
"""
        write(f"sentinel/tables/reference/{name}.md", content)


def generate_table_index(
    tables: OrderedDict[str, list[tuple[str, str]]], raw_count: int, duplicates: list[str]
) -> None:
    rows = []
    for name, fields in tables.items():
        group_names = [
            group["title"]
            for group in TABLE_GROUPS.values()
            if name in group["tables"]
        ]
        group = ", ".join(group_names) if group_names else "Unmapped"
        rows.append(f"| {table_link(name)} | {group} | {len(fields)} |")

    group_links = "\n".join(
        f"- [{group['title']}](by-domain/{slug}.md): {group['description']}"
        for slug, group in TABLE_GROUPS.items()
    )
    duplicate_note = ", ".join(duplicates) if duplicates else "None"
    content = f"""# Sentinel Table Catalog

This catalog was generated from the Microsoft Sentinel/Log Analytics schema exported into `references/sentinel/logmanagement-schema.txt`.

The source contained {raw_count} table entries. Duplicate sections were collapsed for: {duplicate_note}.

## Domain Views
{group_links}

## Tool to Table Map
- [Tool Table Map](tool-table-map.md)
- [Field Normalization](field-normalization.md)

## Table Reference
| Table | Domain | Fields |
| --- | --- | ---: |
{chr(10).join(rows)}
"""
    write("sentinel/tables/index.md", content)


def generate_group_pages(tables: OrderedDict[str, list[tuple[str, str]]]) -> None:
    for slug, group in TABLE_GROUPS.items():
        rows = []
        for table in group["tables"]:
            if table in tables:
                rows.append(
                    f"| [{table}](../reference/{table}.md) | {len(tables[table])} | {describe_table(table)} |"
                )
            else:
                rows.append(f"| `{table}` | Not in current schema | Map when data lands in Sentinel. |")
        content = f"""# {group['title']}

{group['description']}

## Tables
| Table | Fields | Hunting Purpose |
| --- | ---: | --- |
{chr(10).join(rows)}

## Perguntas comuns
- What security question can this table answer?
- Which entity can it identify: user, host, IP, URL, hash, cloud resource, or incident?
- Which other table should it join to for context?
- Which hunt cadence uses it: Daily, Weekly, Intel, or Monthly?
"""
        write(f"sentinel/tables/by-domain/{slug}.md", content)


def generate_tool_table_map() -> None:
    rows = []
    for tool, details in TOOL_MAPPINGS.items():
        tables = ", ".join(f"[{table}](reference/{table}.md)" for table in details["tables"]) or "TBD"
        hunts = "<br>".join(details["hunts"])
        rows.append(f"| [{tool}](../../{details['path']}) | {details['category']} | {tables} | {hunts} |")
    content = f"""# Tool Table Map

Use this map to move from a tool to the Sentinel tables it feeds, then from the tables to hunts and KQL.

| Tool | Category | Sentinel Tables | Hunt Usage |
| --- | --- | --- | --- |
{chr(10).join(rows)}
"""
    write("sentinel/tables/tool-table-map.md", content)


def generate_field_normalization() -> None:
    content = """# Field Normalization

Different tools use different field names for the same hunting entity. Normalize fields inside KQL before joining or summarizing.

## Mapeamento de entidade
| Entity | Common Fields |
| --- | --- |
| User | `UserPrincipalName`, `userPrincipalName`, `UserId`, `user`, `Account`, `AccountName`, `SubjectUserName`, `TargetUserName`, `username`, `UserAccountName_s` |
| Host | `Computer`, `HostHostName_s`, `hostname`, `asset_hostname_s`, `detail_endpointHostName_s`, `DeviceName`, `SourceHostName`, `DestinationHostName` |
| Source IP | `IPAddress`, `ClientIP_s`, `SourceIP`, `srcip`, `userip`, `ClientIP`, `IpAddress`, `detail_src_s` |
| Destination IP | `DestinationIP`, `dstip`, `OriginIP_s`, `detail_dst_s`, `IPAddress` |
| URL or Host | `RequestURL`, `ClientRequestURI_s`, `url`, `ur_normalized`, `URL_s`, `findings_PublicUrl_s`, `ClientRequestHost_s`, `domain`, `dsthost` |
| File Hash | `FileHash`, `sha256`, `md5`, `FileHashValue_s`, `detail_fileHashSha256_s`, `detail_objectFileHashSha256_s`, `findings_Sha256_s` |
| Action | `DeviceAction`, `SimplifiedDeviceAction`, `SecurityAction_s`, `action`, `detail_act_s`, `Activity`, `OperationName` |
| Severity | `Severity`, `AlertSeverity`, `severity`, `severity_s`, `risk_level_s`, `LogSeverity`, `ThreatSeverity` |

## Padrão KQL
```kql
<TableName>
| extend
    NormalizedUser = coalesce(UserPrincipalName, userPrincipalName, UserId, user, Account),
    NormalizedHost = coalesce(Computer, HostHostName_s, hostname),
    NormalizedSourceIp = coalesce(IPAddress, ClientIP_s, SourceIP, srcip, userip),
    NormalizedDestinationIp = coalesce(DestinationIP, dstip, OriginIP_s),
    NormalizedAction = coalesce(DeviceAction, SecurityAction_s, action, Activity),
    NormalizedSeverity = coalesce(Severity, AlertSeverity, severity, severity_s, risk_level_s)
```

## Notas
- Normalize only the fields needed for the hunt.
- Keep raw fields in the final projection so an analyst can pivot back to the original vendor event.
- Prefer `column_ifexists()` when writing shared parsers across optional custom tables.
"""
    write("sentinel/tables/field-normalization.md", content)


def generate_sentinel_readme(tables: OrderedDict[str, list[tuple[str, str]]]) -> None:
    custom_tables = [name for name in tables if name.endswith("_CL")]
    content = f"""# Microsoft Sentinel

Sentinel is the central data and hunting layer for this library.

The expected flow is:

```text
Tool or platform -> Sentinel table -> normalized entities -> hunt scenario -> KQL -> finding or detection
```

## Seções principais
- [Table Catalog](tables/index.md)
- [Tool Table Map](tables/tool-table-map.md)
- [Field Normalization](tables/field-normalization.md)
- [KQL Library](kql/README.md)

## Catálogo Atual
- Total unique tables with schema: {len(tables)}
- Custom connector tables: {len(custom_tables)}
- Source schema: `references/sentinel/logmanagement-schema.txt`

## Regra de caça
Before trusting a hunt result, confirm data coverage with [Data Source Health](../sentinel/kql/daily/data-source-health.kql).
"""
    write("sentinel/README.md", content)


def generate_kql_library() -> None:
    cadence_rows = []
    for path, details in QUERIES.items():
        write(f"sentinel/kql/{path}", details["query"])
        cadence, filename = path.split("/", 1)
        cadence_rows.append(
            f"| [{details['title']}]({path}) | {details['cadence']} | {', '.join(details['tables'])} |"
        )

    content = f"""# KQL Library

This folder stores reusable KQL for the hunting process. Each query maps to a hunt page and to one recurring cadence.

## HEARTH Iniciantes
- [HEARTH KQL Starters](hearth/README.md): one generated starter KQL candidate per HEARTH Flame, mapped to the Sentinel tables available in this library.

## Consultas
| Query | Cadence | Main Tables |
| --- | --- | --- |
{chr(10).join(cadence_rows)}

## Padrão de Trabalho
1. Confirm the table exists and is receiving data.
2. Run the query with the default lookback.
3. Tune thresholds for your baseline.
4. Save confirmed findings in the matching hunt page.
5. Promote repeated high-value logic into an analytic rule or workbook.
"""
    write("sentinel/kql/README.md", content)


def generate_hunt_pages() -> None:
    index_rows = []
    cadence_map = {
        "daily": "Daily Hunt",
        "weekly": "Weekly Hunt",
        "intel": "Intel Hunt",
        "monthly": "Monthly Hunt",
    }
    for path, details in QUERIES.items():
        cadence_slug, filename = path.split("/", 1)
        page_name = filename.replace(".kql", ".md")
        page_path = f"hunts/{cadence_slug}/{page_name}"
        table_links = "\n".join(
            f"- [{table}](../../sentinel/tables/reference/{table}.md)" for table in details["tables"]
        )
        tool_links = []
        for tool in details["tools"]:
            mapping = TOOL_MAPPINGS.get(tool)
            if mapping:
                tool_links.append(f"- [{tool}](../../{mapping['path']})")
            else:
                tool_links.append(f"- {tool}")
        content = f"""# {details['title']}

## Objetivo
{details['objective']}

## Cadência
{details['cadence']}

## Tabelas Sentinel
{table_links}

## Ferramentas
{chr(10).join(tool_links)}

## KQL
{kql_link(path)}

## Fluxo de trabalho do analista
1. Confirm data source health for the tables above.
2. Run the KQL with the default lookback.
3. Review top entities, outliers, and repeated patterns.
4. Enrich suspicious users, hosts, IPs, URLs, hashes, or cloud resources.
5. Record the decision: benign, suspicious, incident, detection candidate, or tuning item.

## Resultado Esperado
- Confirmed findings or documented false positives.
- Tuning notes for thresholds, allowlists, watchlists, or parser improvements.
- Detection or incident follow-up when the behavior repeats or shows impact.
"""
        write(page_path, content)
        index_rows.append(
            f"| [{details['title']}]({cadence_slug}/{page_name}) | {details['cadence']} | {', '.join(details['tables'])} |"
        )

    for slug, title in cadence_map.items():
        rows = [
            f"- [{details['title']}]({path.split('/', 1)[1].replace('.kql', '.md')})"
            for path, details in QUERIES.items()
            if path.startswith(slug + "/")
        ]
        content = f"""# {title}

Use this folder for hunts that run on the {title.lower()} cadence.

## Caçadas
{chr(10).join(rows)}
"""
        write(f"hunts/{slug}/README.md", content)

    content = f"""# Hunt Library

The hunt pages are the main product of this repository. Each page connects a scenario to Sentinel tables, tools, KQL, analyst workflow, and expected output.

## Índice de caça
| Hunt | Cadence | Main Tables |
| --- | --- | --- |
{chr(10).join(index_rows)}

## Cadências
- [Daily Hunt](daily/README.md)
- [Weekly Hunt](weekly/README.md)
- [Intel Hunt](intel/README.md)
- [Monthly Hunt](monthly/README.md)
"""
    write("hunts/README.md", content)


def generate_cadence() -> None:
    write(
        "cadence/README.md",
        """# Hunting Cadence

This section defines the operating rhythm for the threat hunting process.

## Cadências
- [Daily Hunt](daily-hunt.md): short, repeatable review for active risk and data health.
- [Weekly Hunt](weekly-hunt.md): deeper pattern review and baseline hunting.
- [Intel Hunt](intel-hunt.md): event-driven hunts from IOCs, TTPs, CVEs, or vendor intelligence.
- [Monthly Hunt](monthly-hunt.md): coverage, detection quality, cost, and strategic hunt review.
- [Hunt Calendar](hunt-calendar.md): recurring calendar for planning and rotation.
""",
    )
    write(
        "cadence/daily-hunt.md",
        """# Daily Hunt

## Objetivo
Catch active risk early and verify that the data needed for hunting is still healthy.

## Caixa de tempo sugerida
30 to 60 minutes.

## Runbook
1. Review high and medium incidents or alerts.
2. Check identity failures followed by success.
3. Review suspicious endpoint script activity.
4. Review WAF, firewall, and SASE blocks.
5. Confirm connector and agent health.

## Consultas
- [`identity-failures-followed-by-success.kql`](../sentinel/kql/daily/identity-failures-followed-by-success.kql)
- [`high-severity-alerts-and-incidents.kql`](../sentinel/kql/daily/high-severity-alerts-and-incidents.kql)
- [`endpoint-suspicious-powershell.kql`](../sentinel/kql/daily/endpoint-suspicious-powershell.kql)
- [`network-waf-and-firewall-blocks.kql`](../sentinel/kql/daily/network-waf-and-firewall-blocks.kql)
- [`data-source-health.kql`](../sentinel/kql/daily/data-source-health.kql)
""",
    )
    write(
        "cadence/weekly-hunt.md",
        """# Weekly Hunt

## Objetivo
Find behavior that needs a larger baseline than the daily hunt can provide.

## Caixa de tempo sugerida
2 to 4 hours.

## Runbook
1. Review privileged role, policy, and credential changes.
2. Review cloud posture and risky control-plane activity.
3. Hunt rare application and user-agent access.
4. Review top egress, denied traffic, and unusual destinations.
5. Convert repeated findings into watchlists, tuning, or detection candidates.

## Consultas
- [`new-admin-or-role-changes.kql`](../sentinel/kql/weekly/new-admin-or-role-changes.kql)
- [`cloud-risk-posture.kql`](../sentinel/kql/weekly/cloud-risk-posture.kql)
- [`rare-app-and-user-agent-access.kql`](../sentinel/kql/weekly/rare-app-and-user-agent-access.kql)
- [`top-egress-and-denied-traffic.kql`](../sentinel/kql/weekly/top-egress-and-denied-traffic.kql)
""",
    )
    write(
        "cadence/intel-hunt.md",
        """# Intel Hunt

## Objetivo
Rapidly translate new intelligence into searches across Sentinel tables.

## Gatilhos
- New IOCs from threat intelligence.
- New CVE relevant to exposed assets.
- Vendor alert or report with TTPs.
- New campaign targeting your sector.
- Internal incident or suspicious pattern requiring historical search.

## Runbook
1. Normalize IOCs into `ThreatIntelIndicators` or a watchlist.
2. Sweep across network, endpoint, cloud, identity, and vendor tables.
3. Pivot from any hit into entities and related events.
4. Record whether the intel is relevant, noisy, or actionable.
5. Promote stable logic into an analytic rule or recurring hunt.

## Consultas
- [`ioc-ip-domain-url-hash-sweep.kql`](../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql)
- [`trend-mitre-mapping-hunt.kql`](../sentinel/kql/intel/trend-mitre-mapping-hunt.kql)
- [`high-risk-cloud-exposure-sweep.kql`](../sentinel/kql/intel/high-risk-cloud-exposure-sweep.kql)
""",
    )
    write(
        "cadence/monthly-hunt.md",
        """# Monthly Hunt

## Objetivo
Improve the hunting program itself: coverage, cost, detection quality, and baselines.

## Caixa de tempo sugerida
Half day to one day.

## Runbook
1. Review ingestion, connector health, and coverage gaps.
2. Review alert and incident quality.
3. Review identity baseline and privileged activity trends.
4. Review billable volume and noisy tables.
5. Update the hunt roadmap and backlog.

## Consultas
- [`coverage-and-ingestion-review.kql`](../sentinel/kql/monthly/coverage-and-ingestion-review.kql)
- [`analytics-rule-and-incident-quality.kql`](../sentinel/kql/monthly/analytics-rule-and-incident-quality.kql)
- [`identity-baseline-review.kql`](../sentinel/kql/monthly/identity-baseline-review.kql)
- [`log-cost-and-billable-volume.kql`](../sentinel/kql/monthly/log-cost-and-billable-volume.kql)
""",
    )
    write(
        "cadence/hunt-calendar.md",
        """# Hunt Calendar

Use this as the recurring calendar for the threat hunting program.

## Rotação Semanal
| Day | Primary Hunt | Secondary Review | Output |
| --- | --- | --- | --- |
| Monday | Daily identity and incident review | Data source health | Findings, tickets, data gaps |
| Tuesday | Endpoint and script execution | Trend Vision One workbench | Suspicious hosts, detection candidates |
| Wednesday | Network, SASE, WAF, and firewall | Cloudflare and Netskope focus | Block review, egress anomalies |
| Thursday | Cloud and posture | Orca and AzureActivity focus | Exposed assets, owner follow-up |
| Friday | Weekly baseline hunt | Backlog and tuning review | Hunt notes, watchlists, rule tuning |

## Rotação Mensal
| Week | Theme | Suggested Hunts |
| --- | --- | --- |
| Week 1 | Identity and access | Failed-to-success, admin changes, rare apps |
| Week 2 | Endpoint and malware behavior | PowerShell, Trend MITRE mapping, workbench review |
| Week 3 | Network, SASE, and edge | Firewall blocks, Cloudflare WAF, Netskope egress |
| Week 4 | Cloud, coverage, and detection quality | Orca posture, ingestion review, incident quality |

## Intel Hunt SLA
| Intel Type | Start Target | Lookback |
| --- | --- | --- |
| Critical active exploitation | Same day | 30 to 90 days |
| High-confidence IOCs | 24 hours | 14 to 30 days |
| New TTP or campaign report | 2 to 5 business days | 30 to 180 days |
| Sector trend or research | Next weekly hunt | 30 to 180 days |

## Notas de calendário
- Keep daily hunts short and repeatable.
- Use weekly hunts for depth and baselines.
- Run intel hunts whenever new intelligence arrives.
- Use monthly hunts to improve coverage, cost, detection quality, and the roadmap.
""",
    )


def guide_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- TBD"


def linked_tables(tables: list[str], prefix: str = "../../sentinel/tables/reference") -> str:
    if not tables:
        return "- No Sentinel table confirmed yet."
    return "\n".join(f"- [{table}]({prefix}/{table}.md)" for table in tables)


def render_tool_page(tool: str, details: dict[str, object]) -> str:
    guide = TOOL_GUIDES.get(tool, {})
    tables = linked_tables(details["tables"])
    hunts = guide_bullets(details["hunts"])
    purpose = guide.get(
        "purpose",
        "Tool used as part of the hunting ecosystem. Confirm connector details, table mapping, and available fields before building detections.",
    )
    how_it_works = guide_bullets(
        guide.get(
            "how_it_works",
            [
                "Produces telemetry that can support detection, triage, enrichment, or investigation.",
                "Needs clear field mapping before it can be used safely in shared KQL.",
                "Works best when joined with identity, endpoint, network, cloud, or case-management context.",
            ],
        )
    )
    what_to_review = guide_bullets(
        guide.get(
            "what_to_review",
            [
                "Connector health, ingestion delay, schema changes, and missing fields.",
                "High-severity alerts, risky configuration changes, and recurring false positives.",
                "Events involving critical users, hosts, cloud assets, external destinations, or privileged actions.",
            ],
        )
    )
    security_focus = guide_bullets(
        guide.get(
            "security_focus",
            [
                "Understand what the tool can see and what it cannot see.",
                "Treat missing or stale telemetry as a coverage risk.",
                "Validate false positives before converting hunt logic into analytic rules.",
            ],
        )
    )
    hunt_questions = guide_bullets(
        guide.get(
            "hunt_questions",
            [
                "What changed recently?",
                "Which entities are rare for this environment?",
                "Which alerts or events repeat without a clear owner or response decision?",
            ],
        )
    )

    return f"""# {tool}

## Objetivo
{purpose}

## Categoria
{details['category']}

## Como funciona
{how_it_works}

## Como esta biblioteca a utiliza
- Maps this tool to the Sentinel tables below.
- Uses the mapped tables to build daily, weekly, intel, and monthly hunts.
- Converts repeated high-value findings into use cases and detection candidates.

## Tabelas Sentinel
{tables}

## O que revisar
{what_to_review}

## Uso de caça
{hunts}

## Coisas de segurança para observar
{security_focus}

## Perguntas úteis sobre caça
{hunt_questions}

## Fluxo de trabalho do analista
1. Confirm the connector is healthy and the expected table is receiving data.
2. Review the most important fields: time, user, host, source IP, destination, action, severity, policy, and raw event.
3. Build a baseline for normal activity by user, asset, app, policy, and location.
4. Hunt for rare, new, high-risk, or chained behavior.
5. Document findings and promote stable logic into [Use Cases](../../use-cases/README.md).

## Lista de verificação de maturidade
- Data source owner is known.
- Expected Sentinel tables and key fields are documented.
- Parser assumptions and field normalization are reviewed.
- At least one daily or weekly hunt uses this data source.
- False positives and tuning notes are captured after each hunt.

## Páginas da Biblioteca Relacionadas
- [Tool Table Map](../../sentinel/tables/tool-table-map.md)
- [Field Normalization](../../sentinel/tables/field-normalization.md)
- [KQL Library](../../sentinel/kql/README.md)
- [Hunt Library](../../hunts/README.md)
"""


def render_platform_page(path: str, details: dict[str, object]) -> str:
    title = details["title"]
    guide = PLATFORM_GUIDES.get(title, {})
    tables = linked_tables(details["tables"])
    purpose = guide.get("purpose", details["notes"])
    how_it_works = guide_bullets(
        guide.get(
            "how_it_works",
            [
                "Provides a runtime or cloud surface where identities, workloads, data, and network paths generate telemetry.",
                "Needs asset ownership and business criticality to make hunt prioritization meaningful.",
                "Should be correlated with identity, endpoint, network, and tool-specific detections.",
            ],
        )
    )
    what_to_review = guide_bullets(
        guide.get(
            "what_to_review",
            [
                "Authentication, administration, configuration, exposure, network paths, and data movement.",
                "New assets, risky permissions, public access, disabled logging, and unusual egress.",
                "Coverage gaps where the platform exists but Sentinel telemetry is incomplete.",
            ],
        )
    )
    security_focus = guide_bullets(
        guide.get(
            "security_focus",
            [
                "Know what telemetry exists, what is missing, and what cannot be inferred from the current tables.",
                "Prioritize critical assets, privileged identities, public exposure, and sensitive data paths.",
                "Document false positives caused by automation, deployments, patching, and administrator workflows.",
            ],
        )
    )
    platform_type = "Operating System" if "operating-systems" in path else "Cloud Platform"

    return f"""# {title}

## Objetivo
{purpose}

## Tipo de plataforma
{platform_type}

## Como funciona
{how_it_works}

## Como esta biblioteca a utiliza
- Links platform behavior to the Sentinel tables below.
- Uses platform context to decide which hunts belong in daily, weekly, intel, or monthly cadence.
- Helps analysts understand whether an event is normal administration, misconfiguration, exposure, or suspicious behavior.

## Tabelas Sentinel
{tables}

## O que revisar
{what_to_review}

## Coisas de segurança para observar
{security_focus}

## Caçar ideias
- Authentication or administrative activity outside the normal baseline.
- Public exposure, risky configuration, disabled logging, or new high-risk assets.
- Suspicious network paths, outbound traffic, tunneling, or data movement.
- New persistence locations, privileged access, or policy drift.
- Events involving critical systems, production workloads, identity infrastructure, or sensitive data.

## Fluxo de trabalho de triagem
1. Identify the platform entity: account, user, host, device, workload, project, subscription, tenancy, or resource.
2. Confirm whether the activity is expected for that entity and time window.
3. Join with identity, endpoint, network, cloud posture, and incident context.
4. Decide whether the result is benign, suspicious, a confirmed incident, a detection candidate, or a coverage gap.
5. Document missing telemetry and use-case opportunities.

## Perguntas de cobertura
- Are the critical assets for this platform known and tagged?
- Are logs enabled for authentication, administration, network, and security-relevant changes?
- Does Sentinel receive the expected tables daily?
- Can the table identify user, host, source IP, destination, action, and resource?
- Which hunts cannot be run because the required telemetry is missing?

## Páginas da Biblioteca Relacionadas
- [Sentinel Table Catalog](../../sentinel/tables/index.md)
- [Data Sources](../../data-sources/README.md)
- [KQL Library](../../sentinel/kql/README.md)
- [HEARTH KQL Starters](../../sentinel/kql/hearth/README.md)
"""


def generate_methods_scripts_platforms() -> None:
    for path, (title, body) in METHODOLOGIES.items():
        write_if_missing(
            path,
            f"""# {title}

{body}

## Como isso se adapta à biblioteca
- Start from a scenario in [Hunts](../hunts/README.md).
- Confirm coverage in [Sentinel Tables](../sentinel/tables/index.md).
- Run or tune the matching [KQL](../sentinel/kql/README.md).
- Document results using the [Hunt Template](../templates/hunt-template.md).
""",
        )

    write_if_missing(
        "methodologies/README.md",
        """# Methodologies

Use these pages to keep the library aligned to a repeatable hunting process instead of a loose query dump.

## páginas
- [Threat Hunting Overview](threat-hunting-overview.md)
- [Hypothesis Driven Hunting](hypothesis-driven.md)
- [Data Driven Hunting](data-driven.md)
- [Intel Driven Hunting](intel-driven.md)
- [LATAM Threat Intelligence](latam-threat-intelligence.md)
- [PEAK Framework](peak-framework.md)
- [Model Assisted Hunting](model-assisted.md)
- [Research Resources](research-resources.md)
""",
    )

    for path, (title, body) in SCRIPT_PAGES.items():
        write(
            path,
            f"""# {title}

{body}

## Uso da biblioteca
- Store reusable helpers, collectors, parsers, or enrichment workflows here.
- Link scripts back to the hunt page that uses them.
- Prefer Sentinel/KQL for repeatable hunting logic and scripts for enrichment or collection gaps.
""",
        )

    write(
        "scripts/README.md",
        """# Scripts

Scripts support the hunting process when KQL alone is not enough.

## Idiomas
- [PowerShell](powershell.md)
- [Python](python.md)
- [Bash](bash.md)
- [Go](go.md)
- [Java](java.md)
- [C#](csharp.md)
""",
    )

    for path, details in PLATFORMS.items():
        write(path, render_platform_page(path, details))

    write(
        "platforms/README.md",
        """# Platforms

Use platform pages to understand where telemetry originates before it lands in Sentinel.

## Sequência de conclusão
1. Read operating system pages to understand endpoint and device behavior.
2. Read cloud platform pages to understand control-plane, posture, identity, and resource behavior.
3. Map each platform to the Sentinel tables and hunts that depend on it.
4. Record coverage gaps where a platform exists but Sentinel does not yet receive the right telemetry.

## Como usar essas páginas
- Learn how the platform works at a hunting level.
- Review what security activity matters for the platform.
- Confirm which Sentinel tables represent the platform.
- Identify hunt ideas, use-case candidates, and missing telemetry.

## Nuvem
- [AWS](cloud/aws.md)
- [Azure](cloud/azure.md)
- [GCP](cloud/gcp.md)
- [Oracle Cloud](cloud/oracle-cloud.md)

## Sistemas Operacionais
- [Windows](operating-systems/windows.md)
- [Linux](operating-systems/linux.md)
- [Ubuntu](operating-systems/ubuntu.md)
- [Android](operating-systems/android.md)
- [iOS](operating-systems/ios.md)
""",
    )


def generate_tools() -> None:
    for tool, details in TOOL_MAPPINGS.items():
        write(details["path"], render_tool_page(tool, details))

    category_sections: OrderedDict[str, list[str]] = OrderedDict()
    for tool, details in TOOL_MAPPINGS.items():
        category_sections.setdefault(details["category"], []).append(
            f"- [{tool}]({Path(details['path']).relative_to('tools')})"
        )
    section_text = "\n\n".join(
        f"## {category}\n" + "\n".join(items) for category, items in category_sections.items()
    )
    write(
        "tools/README.md",
        f"""# Tools

Tools are documented by the Sentinel tables they feed, the hunts they support, and the security questions they help answer.

## Sequência de conclusão
1. Start with the tools that already feed Sentinel tables.
2. Learn how each tool works and what security activity it can see.
3. Review the mapped Sentinel tables and key hunt usage.
4. Convert repeated useful hunts into use cases or detection candidates.
5. Track tools with no confirmed Sentinel table as onboarding or normalization gaps.

## Como usar essas páginas
- Use the purpose and workflow sections to understand the tool.
- Use the review sections to know what to inspect during daily, weekly, intel, and monthly hunts.
- Use the Sentinel table list to find the data that backs each hunt.
- Use the maturity checklist to improve coverage over time.

{section_text}
""",
    )


def generate_data_sources() -> None:
    pages = {
        "data-sources/identity.md": (
            "Identity Data Sources",
            ["SigninLogs", "AuditLogs", "IdentityInfo", "BehaviorAnalytics", "UserPeerAnalytics", "CyberArk_AuditEvents_CL"],
            "Identity hunts focus on users, service principals, roles, authentication, privilege, and risky access.",
        ),
        "data-sources/endpoint.md": (
            "Endpoint Data Sources",
            ["SecurityEvent", "WindowsEvent", "Syslog", "TrendMicro_XDR_OAT_CL", "TrendMicro_XDR_WORKBENCH_CL", "Heartbeat"],
            "Endpoint hunts focus on process execution, PowerShell, logons, malware behavior, and host coverage.",
        ),
        "data-sources/network.md": (
            "Network Data Sources",
            ["CommonSecurityLog", "Cloudflare_CL", "NetskopeEventsNetwork_CL", "NetskopeEventsConnection_CL", "NetskopeEventsPage_CL", "Syslog"],
            "Network hunts focus on firewall, WAF, proxy, SASE, egress, destination, and connection behavior.",
        ),
        "data-sources/cloud.md": (
            "Cloud Data Sources",
            ["AzureActivity", "AzureDiagnostics", "OrcaAlerts_CL"],
            "Cloud hunts focus on control-plane changes, exposed assets, risky configuration, and posture drift.",
        ),
        "data-sources/saas.md": (
            "SaaS Data Sources",
            ["OfficeActivity", "NetskopeEventsApplication_CL", "NetskopeAlerts_CL", "SigninLogs"],
            "SaaS hunts focus on user application access, file activity, DLP, sharing, and unsanctioned apps.",
        ),
    }
    for path, (title, tables, body) in pages.items():
        write(
            path,
            f"""# {title}

{body}

## Tabelas Sentinel
{table_bullet_links(tables, '../sentinel/tables/reference')}
""",
        )
    write(
        "data-sources/README.md",
        """# Data Sources

Data sources describe the type of telemetry and the Sentinel tables that contain it.

## Categorias
- [Identity](identity.md)
- [Endpoint](endpoint.md)
- [Network](network.md)
- [Cloud](cloud.md)
- [SaaS](saas.md)
""",
    )


def generate_templates() -> None:
    write_if_missing(
        "templates/hunt-template.md",
        """# Hunt Title

## Objetivo
What question is this hunt trying to answer?

## Hipótese
What adversary behavior, abuse path, or anomaly do we expect?

## Cadência
Daily, Weekly, Intel, Monthly, or ad hoc.

## Tabelas Sentinel
- Table 1
- Table 2

## Ferramentas
- Tool 1
- Tool 2

## KQL
```kql
// Query here
```

## Fluxo de trabalho do analista
1. Confirm data coverage.
2. Run the query.
3. Review entities and outliers.
4. Enrich and validate.
5. Record outcome.

## Descobertas
- Date:
- Analyst:
- Result:
- Evidence:
- Follow-up:

## Oportunidade de detecção
Should this become an analytic rule, watchlist, workbook, parser, or backlog item?
""",
    )
    write_if_missing(
        "templates/table-template.md",
        """# Table Name

## Hunting Purpose
What security questions can this table answer?

## Fonte de dados
Which tool, platform, or connector feeds this table?

## Campos-chave
| Field | Type | Why It Matters |
| --- | --- | --- |

## Junções Comuns
- Table:
- Join Field:

## Exemplo de caça
- Hunt idea:

## Inicial KQL
```kql
TableName
| where TimeGenerated >= ago(24h)
| take 100
```
""",
    )
    write_if_missing(
        "templates/tool-template.md",
        """# Tool Name

## Categoria
SIEM, EDR, Firewall, WAF, SASE, CSPM, PAM, Cloud, SaaS, or other.

## Tabelas Sentinel
- Table:

## Notas do conector
- Ingestion path:
- Parser:
- Known gaps:

## Uso de caça
- Scenario:

## links KQL
- Query:
""",
    )
    write_if_missing(
        "templates/kql-template.md",
        """# Query Name

## Objetivo
What does this query find?

## Tables
- Table:

## Consulta
```kql
let lookback = 1d;
TableName
| where TimeGenerated >= ago(lookback)
```

## Notas de ajuste
- Thresholds:
- Known false positives:
- Required watchlists:
""",
    )
    write_if_missing(
        "templates/use-case-template.md",
        """# Use Case Title

## Metadados
| Field | Value |
| --- | --- |
| Use Case ID | `UC-000` |
| Status | Draft, Testing, Production, Tuning, Retired |
| Owner |  |
| Source Hunt | Link to hunt page |
| Source KQL | Link to KQL file |

## Objetivo
What behavior should this use case detect?

## Lógica de detecção
```kql
let lookback = 1d;
TableName
| where TimeGenerated >= ago(lookback)
```

## Falsos Positivos
- Scenario:

## Etapas de triagem
1. Review alert entities.
2. Validate source events.
3. Escalate, close, or tune.
""",
    )
    write_if_missing(
        "templates/README.md",
        """# Templates

Use templates to keep every hunt, table, tool, and KQL page consistent.

## Modelos
- [Hunt Template](hunt-template.md)
- [Table Template](table-template.md)
- [Tool Template](tool-template.md)
- [KQL Template](kql-template.md)
- [Use Case Template](use-case-template.md)
""",
    )


def generate_use_cases() -> None:
    write_if_missing(
        "use-cases/README.md",
        """# Use Cases and Detection Development

Use this section to turn successful hunts into repeatable Sentinel analytics, workbooks, watchlists, or operational controls.

## Fluxo de trabalho
1. Start from a completed hunt.
2. Convert the final KQL into scheduled detection logic.
3. Test historical volume and false positives.
4. Define entities, severity, incident grouping, and triage steps.
5. Deploy, tune, and review.

## Modelo
- [Use Case Template](../templates/use-case-template.md)
""",
    )


def generate_root_readme(tables: OrderedDict[str, list[tuple[str, str]]]) -> None:
    content = f"""# CTH Library

Cyber Threat Hunting Library centered on Microsoft Sentinel.

This repository organizes your hunting process around:

```text
Tool or platform -> Sentinel table -> normalized entity -> hunt scenario -> KQL -> finding or detection
```

## Comece aqui
1. [Hunt Calendar](cadence/hunt-calendar.md)
2. [Hunting Cadence](cadence/README.md)
3. [Hunt Library](hunts/README.md)
4. [Sentinel Table Catalog](sentinel/tables/index.md)
5. [KQL Library](sentinel/kql/README.md)
6. [Use Cases](use-cases/README.md)
7. [External Research](external-research/README.md)
8. [Tool Table Map](sentinel/tables/tool-table-map.md)

## Seções principais
- [Cadence](cadence/README.md): Daily, Weekly, Intel, and Monthly hunt process.
- [Hunts](hunts/README.md): Scenario pages mapped to KQL, tools, and tables.
- [Use Cases](use-cases/README.md): Guide for turning hunts into Sentinel detections and monitoring use cases.
- [Sentinel](sentinel/README.md): Table catalog, field normalization, and KQL library.
- [Tools](tools/README.md): Tools mapped to the Sentinel tables they feed.
- [Data Sources](data-sources/README.md): Identity, endpoint, network, cloud, and SaaS telemetry views.
- [Platforms](platforms/README.md): Cloud and operating system context.
- [Methodologies](methodologies/README.md): PEAK, hypothesis, data, intel, LATAM, and model-assisted hunting.
- [External Research](external-research/README.md): Public hunt research mapped into local Sentinel tables, KQL candidates, and use cases.
- [Templates](templates/README.md): Reusable page templates.
- [Scripts](scripts/README.md): Supporting scripts and automation notes.

## Catálogo Sentinel atual
- Unique tables with schema: {len(tables)}
- Primary SIEM: Microsoft Sentinel
- Schema source: `references/sentinel/logmanagement-schema.txt`

## Ritmo Operacional
| Cadence | Goal |
| --- | --- |
| Daily Hunt | Catch active risk and confirm data health. |
| Weekly Hunt | Hunt deeper baselines and recurring scenarios. |
| Intel Hunt | Convert IOCs, TTPs, and new intelligence into searches. |
| Monthly Hunt | Improve coverage, detections, cost, and the roadmap. |
"""
    write("README.md", content)


def main() -> None:
    migrate_placeholders()
    schema = read_schema()
    tables, raw_count, duplicates = parse_schema(schema)
    generate_table_reference(tables)
    generate_table_index(tables, raw_count, duplicates)
    generate_group_pages(tables)
    generate_tool_table_map()
    generate_field_normalization()
    generate_sentinel_readme(tables)
    generate_kql_library()
    generate_hunt_pages()
    generate_cadence()
    generate_methods_scripts_platforms()
    generate_tools()
    generate_data_sources()
    generate_templates()
    generate_use_cases()
    generate_root_readme(tables)
    print(f"Generated library with {len(tables)} unique Sentinel tables.")


if __name__ == "__main__":
    main()
