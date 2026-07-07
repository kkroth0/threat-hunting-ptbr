#!/usr/bin/env python3
"""Mapeie hipóteses de caça às chamas HEARTH nesta biblioteca de caça Sentinel.

O script lê a pasta HEARTH ``Flames``, extrai os metadados da hipótese,
e escreve uma camada de mapeamento local que conecta cada ideia de busca externa a:

- tabelas Microsoft Sentinel neste repositório
- padrões candidatos KQL reutilizáveis
- candidatos use-case/detection
- cadência de caça recomendada
- relevância LATAM

Os arquivos gerados mantêm intencionalmente o conteúdo de origem HEARTH compacto. Use o
links de fontes para as notas e referências originais.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path("/tmp/HEARTH/Flames")
OUTPUT_ROOT = ROOT / "external-research"
HEARTH_OUTPUT = OUTPUT_ROOT / "hearth"
HEARTH_KQL_OUTPUT = ROOT / "sentinel" / "kql" / "hearth"
SOURCE_BASE_URL = "https://github.com/THORCollective/HEARTH/blob/main/Flames"


KQL_LINKS = OrderedDict(
    [
        (
            "Identity failures followed by success",
            "../../sentinel/kql/daily/identity-failures-followed-by-success.kql",
        ),
        (
            "Endpoint suspicious PowerShell",
            "../../sentinel/kql/daily/endpoint-suspicious-powershell.kql",
        ),
        (
            "Network WAF and firewall blocks",
            "../../sentinel/kql/daily/network-waf-and-firewall-blocks.kql",
        ),
        (
            "New admin or role changes",
            "../../sentinel/kql/weekly/new-admin-or-role-changes.kql",
        ),
        (
            "Rare app and user-agent access",
            "../../sentinel/kql/weekly/rare-app-and-user-agent-access.kql",
        ),
        (
            "Top egress and denied traffic",
            "../../sentinel/kql/weekly/top-egress-and-denied-traffic.kql",
        ),
        (
            "Cloud risk posture",
            "../../sentinel/kql/weekly/cloud-risk-posture.kql",
        ),
        (
            "IOC IP/domain/URL/hash sweep",
            "../../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql",
        ),
        (
            "Trend MITRE mapping hunt",
            "../../sentinel/kql/intel/trend-mitre-mapping-hunt.kql",
        ),
        (
            "High-risk cloud exposure sweep",
            "../../sentinel/kql/intel/high-risk-cloud-exposure-sweep.kql",
        ),
    ]
)


DOMAIN_RULES = OrderedDict(
    [
        (
            "Identity and Access",
            {
                "tables": [
                    "SigninLogs",
                    "AuditLogs",
                    "IdentityInfo",
                    "BehaviorAnalytics",
                    "UserPeerAnalytics",
                ],
                "keywords": [
                    "signin",
                    "sign-in",
                    "sign in",
                    "entra",
                    "azure ad",
                    "aad",
                    "oauth",
                    "mfa",
                    "conditional access",
                    "devicecode",
                    "device code",
                    "token",
                    "prt",
                    "graph",
                    "kerberos",
                    "active directory",
                    "activedirectory",
                    "dcsync",
                    "dc sync",
                    "domain controller",
                    "ad cs",
                    "certificate",
                    "pkinit",
                    "password spray",
                    "brute force",
                    "bruteforce",
                    "valid account",
                    "admin account",
                    "identity",
                    "credential",
                    "account",
                    "user",
                    "privileged",
                ],
            },
        ),
        (
            "Endpoint and OS",
            {
                "tables": [
                    "SecurityEvent",
                    "WindowsEvent",
                    "TrendMicro_XDR_OAT_CL",
                    "TrendMicro_XDR_WORKBENCH_CL",
                ],
                "keywords": [
                    "windows",
                    "powershell",
                    "cmd.exe",
                    "process",
                    "registry",
                    "dll",
                    "driver",
                    "sysmon",
                    "wmi",
                    "dcom",
                    "service",
                    "scheduled task",
                    "task scheduler",
                    "lsass",
                    "rundll32",
                    "regsvr32",
                    "mshta",
                    "wscript",
                    "cscript",
                    "binary",
                    "executable",
                    "malware",
                    "infostealer",
                    "edr",
                    "byovd",
                    "file",
                    "endpoint",
                    "host",
                    "local account",
                    "event id",
                    "4688",
                    "4104",
                    "7045",
                    "4697",
                    "4624",
                    "4720",
                    "4732",
                ],
            },
        ),
        (
            "Linux and Server",
            {
                "tables": [
                    "Syslog",
                    "Heartbeat",
                    "TrendMicro_XDR_OAT_CL",
                    "CommonSecurityLog",
                ],
                "keywords": [
                    "linux",
                    "bash",
                    "sudo",
                    "ssh",
                    "cron",
                    "systemd",
                    "auditd",
                    "execve",
                    "zstd",
                    "tar",
                    "gzip",
                    "xz",
                    "web-service",
                    "/tmp",
                    "/var/tmp",
                    "syslog",
                ],
            },
        ),
        (
            "Network Edge and SASE",
            {
                "tables": [
                    "CommonSecurityLog",
                    "NetskopeEventsNetwork_CL",
                    "NetskopeEventsConnection_CL",
                    "Cloudflare_CL",
                    "NetskopeAlerts_CL",
                ],
                "keywords": [
                    "dns",
                    "c2",
                    "command and control",
                    "beacon",
                    "http",
                    "https",
                    "proxy",
                    "firewall",
                    "vpn",
                    "rdp",
                    "ssh",
                    "smb",
                    "url",
                    "domain",
                    "ip address",
                    "netflow",
                    "connection",
                    "outbound",
                    "egress",
                    "tunnel",
                    "cloudflare tunnel",
                    "workers.dev",
                    "devtunnels",
                ],
            },
        ),
        (
            "Web and Application Edge",
            {
                "tables": [
                    "Cloudflare_CL",
                    "CommonSecurityLog",
                    "AzureDiagnostics",
                    "AppRequests",
                    "AppTraces",
                    "Syslog",
                ],
                "keywords": [
                    "waf",
                    "webshell",
                    "web shell",
                    "weblogic",
                    "peoplesoft",
                    "apache",
                    "nginx",
                    "tomcat",
                    "iis",
                    "public-facing",
                    "public facing",
                    "cve",
                    "exploit",
                    "ssrf",
                    "rce",
                    "http post",
                    "uri",
                    "user-agent",
                    "web server",
                    "apprequests",
                    "java process",
                ],
            },
        ),
        (
            "Cloud and Posture",
            {
                "tables": [
                    "AzureActivity",
                    "AzureDiagnostics",
                    "OrcaAlerts_CL",
                    "NetskopeEventsNetwork_CL",
                ],
                "keywords": [
                    "aws",
                    "gcp",
                    "azure",
                    "cloud account",
                    "cloud control",
                    "cloud resource",
                    "cloud storage",
                    "cloud provider",
                    "cloudtrail",
                    "s3",
                    "bucket",
                    "iam",
                    "kubernetes",
                    "container",
                    "lambda",
                    "storage",
                    "blob",
                    "gcs",
                    "oracle",
                    "key vault",
                    "aks",
                    "subscription",
                    "resource group",
                ],
            },
        ),
        (
            "M365 and SaaS",
            {
                "tables": [
                    "OfficeActivity",
                    "AuditLogs",
                    "SigninLogs",
                    "NetskopeEventsApplication_CL",
                    "NetskopeEventsAudit_CL",
                    "NetskopeEventsPage_CL",
                ],
                "keywords": [
                    "m365",
                    "office 365",
                    "office365",
                    "exchange",
                    "sharepoint",
                    "teams",
                    "onedrive",
                    "mailbox",
                    "inbox",
                    "content compliance",
                    "bcc",
                    "forwarding",
                    "gmail",
                    "email",
                    "phish",
                    "phishing",
                    "oauth app",
                    "saas",
                    "graph activity",
                ],
            },
        ),
        (
            "Threat Intel and Detections",
            {
                "tables": [
                    "ThreatIntelIndicators",
                    "Watchlist",
                    "SecurityAlert",
                    "SecurityIncident",
                    "Anomalies",
                ],
                "keywords": [
                    "ioc",
                    "indicator",
                    "hash",
                    "domain",
                    "url",
                    "ip",
                    "cve",
                    "campaign",
                    "apt",
                    "ransomware",
                    "malware family",
                    "actor",
                    "observed",
                    "known",
                    "threat",
                    "mitre",
                ],
            },
        ),
        (
            "Privileged Access",
            {
                "tables": [
                    "CyberArk_AuditEvents_CL",
                    "AuditLogs",
                    "SecurityEvent",
                    "WindowsEvent",
                ],
                "keywords": [
                    "cyberark",
                    "pam",
                    "safe",
                    "privileged session",
                    "credential retrieval",
                    "domain admin",
                    "enterprise admin",
                    "administrator",
                    "local admin",
                ],
            },
        ),
    ]
)


TACTIC_DOMAIN_WEIGHTS = {
    "credential access": {
        "Identity and Access": 4,
        "Endpoint and OS": 2,
        "Privileged Access": 1,
    },
    "initial access": {
        "Web and Application Edge": 3,
        "Network Edge and SASE": 2,
        "Identity and Access": 1,
    },
    "execution": {"Endpoint and OS": 4, "M365 and SaaS": 1},
    "persistence": {
        "Endpoint and OS": 3,
        "Identity and Access": 1,
        "Cloud and Posture": 1,
    },
    "privilege escalation": {
        "Endpoint and OS": 3,
        "Identity and Access": 2,
        "Privileged Access": 2,
    },
    "defense evasion": {
        "Endpoint and OS": 3,
        "Cloud and Posture": 1,
        "Threat Intel and Detections": 1,
    },
    "lateral movement": {
        "Endpoint and OS": 2,
        "Network Edge and SASE": 2,
        "Identity and Access": 1,
    },
    "command and control": {
        "Network Edge and SASE": 4,
        "Endpoint and OS": 2,
        "Threat Intel and Detections": 1,
    },
    "collection": {
        "Endpoint and OS": 2,
        "Linux and Server": 1,
        "M365 and SaaS": 1,
    },
    "exfiltration": {
        "Network Edge and SASE": 3,
        "Cloud and Posture": 1,
        "M365 and SaaS": 1,
    },
    "discovery": {
        "Endpoint and OS": 2,
        "Identity and Access": 1,
        "Network Edge and SASE": 1,
    },
    "impact": {
        "Endpoint and OS": 2,
        "Network Edge and SASE": 1,
        "Threat Intel and Detections": 1,
    },
}


LATAM_HIGH_KEYWORDS = [
    "latam",
    "latin america",
    "brazil",
    "brasil",
    "mexico",
    "colombia",
    "chile",
    "argentina",
    "peru",
    "pix",
    "boleto",
    "spei",
    "grandoreiro",
    "mekotio",
    "mispadu",
    "metamorfo",
    "amavaldo",
    "banking trojan",
    "banker",
]


LATAM_MEDIUM_KEYWORDS = [
    "phish",
    "infostealer",
    "stealer",
    "ransomware",
    "whatsapp",
    "telegram",
    "oauth",
    "mfa",
    "vpn",
    "cloud",
    "bank",
    "finance",
    "government",
    "retail",
    "payment",
    "public sector",
]


@dataclass(frozen=True)
class Flame:
    id: str
    path: Path
    source_url: str
    title: str
    hypothesis: str
    tactics: tuple[str, ...]
    techniques: tuple[str, ...]
    tags: tuple[str, ...]
    source_format: str


@dataclass(frozen=True)
class FlameMapping:
    flame: Flame
    domains: tuple[str, ...]
    tables: tuple[str, ...]
    tools: tuple[str, ...]
    kql_pattern: str
    seed_kql: tuple[str, ...]
    use_case: str
    cadence: str
    latam_relevance: str
    coverage_status: str
    coverage_notes: str
    priority: str
    priority_score: int
    dedicated_kql_path: str


def clean_text(value: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u2192": "->",
        "\u00a0": " ",
    }
    for source, replacement in replacements.items():
        value = value.replace(source, replacement)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("\\|", "|")
    value = value.replace("`", "")
    value = re.sub(r"\s+", " ", value)
    return value.encode("ascii", errors="ignore").decode("ascii").strip()


def md_cell(value: str) -> str:
    value = clean_text(value)
    value = value.replace("|", "\\|")
    return value


def md_list(values: tuple[str, ...] | list[str]) -> str:
    if not values:
        return "TBD"
    return "<br>".join(md_cell(value) for value in values)


def shorten(value: str, limit: int = 170) -> str:
    value = clean_text(value)
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def normalize_tag(value: str) -> str:
    value = value.strip().strip("#").strip()
    return value.lower().replace(" ", "_")


def normalize_technique(value: str) -> str:
    value = value.strip().strip("#").upper().replace("_", ".")
    match = re.search(r"T\d{4}(?:\.\d{3})?", value)
    return match.group(0) if match else ""


def unique(values: list[str]) -> tuple[str, ...]:
    seen = set()
    ordered = []
    for value in values:
        value = clean_text(value)
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return tuple(ordered)


def find_frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\n(.*?)\n---", text, flags=re.DOTALL)
    if not match:
        return None
    return match.group(1)


def frontmatter_lines(frontmatter: str, key: str) -> tuple[int, list[str]]:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            collected = [line]
            for next_line in lines[index + 1 :]:
                if re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*:", next_line):
                    break
                collected.append(next_line)
            return index, collected
    return -1, []


def yaml_scalar(frontmatter: str, key: str) -> str:
    _, lines = frontmatter_lines(frontmatter, key)
    if not lines:
        return ""

    first = lines[0]
    raw = first.split(":", 1)[1].strip()
    if raw and raw not in {">", ">-", "|", "|-"}:
        body = [raw.strip("'\"")]
        for line in lines[1:]:
            if not line.strip():
                continue
            if line.lstrip().startswith("- "):
                continue
            body.append(line.strip().strip("'\""))
        return clean_text(" ".join(body))

    body = []
    for line in lines[1:]:
        if not line.strip():
            continue
        if line.lstrip().startswith("- "):
            continue
        body.append(line.strip())
    return clean_text(" ".join(body))


def yaml_list(frontmatter: str, key: str) -> tuple[str, ...]:
    _, lines = frontmatter_lines(frontmatter, key)
    values: list[str] = []
    if not lines:
        return tuple()

    raw = lines[0].split(":", 1)[1].strip()
    if raw.startswith("[") and raw.endswith("]"):
        values.extend(item.strip().strip("'\"") for item in raw[1:-1].split(","))

    for line in lines[1:]:
        stripped = line.strip()
        if stripped.startswith("- "):
            values.append(stripped[2:].strip().strip("'\""))
    return unique(values)


def markdown_table_cells(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in line:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            current.append(char)
            continue
        if char == "|":
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    cells.append("".join(current).strip())
    return cells


def parse_table_format(text: str, path: Path) -> Flame:
    row = ""
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = markdown_table_cells(line)
        if len(cells) < 5:
            continue
        first_cell = cells[0].strip().lower()
        second_cell = cells[1].strip().lower()
        if first_cell in {"hunt #", "hunt"} or second_cell.startswith("idea"):
            continue
        if set(first_cell.replace(" ", "")) == {"-"}:
            continue
        if re.fullmatch(r"H\d{3}", cells[0].strip()) or not cells[0].strip():
            row = line
            break
    if not row:
        flame_id = path.stem
        body_match = re.search(
            r"^#\s+H\d{3}\s*\n+(.*?)(?:\n##|\Z)",
            text,
            flags=re.DOTALL | re.MULTILINE,
        )
        hypothesis = clean_text(body_match.group(1)) if body_match else flame_id
        return Flame(
            id=flame_id,
            path=path,
            source_url=f"{SOURCE_BASE_URL}/{path.name}",
            title=flame_id,
            hypothesis=hypothesis,
            tactics=tuple(),
            techniques=unique([normalize_technique(item) for item in re.findall(r"T\d{4}(?:[._]\d{3})?", text)]),
            tags=tuple(),
            source_format="heading",
        )

    cells = markdown_table_cells(row)
    if len(cells) < 5:
        raise ValueError(f"Unexpected table format in {path}")

    flame_id = cells[0].strip() or path.stem
    hypothesis = cells[1].strip()
    tactics = unique([item.strip() for item in re.split(r",|/", cells[2])])
    tag_values = re.findall(r"#([A-Za-z0-9_.-]+)", cells[4])
    tags = tuple(normalize_tag(tag) for tag in tag_values)

    text_for_techniques = " ".join(cells[1:5])
    techniques = unique(
        [
            normalize_technique(item)
            for item in re.findall(r"T\d{4}(?:[._]\d{3})?", text_for_techniques)
        ]
    )

    return Flame(
        id=flame_id,
        path=path,
        source_url=f"{SOURCE_BASE_URL}/{path.name}",
        title=flame_id,
        hypothesis=hypothesis,
        tactics=tactics,
        techniques=techniques,
        tags=tags,
        source_format="table",
    )


def parse_yaml_format(text: str, path: Path, frontmatter: str) -> Flame:
    flame_id = yaml_scalar(frontmatter, "id") or path.stem
    title = yaml_scalar(frontmatter, "title") or flame_id
    hypothesis = yaml_scalar(frontmatter, "hypothesis")
    tactics = yaml_list(frontmatter, "tactics")
    tags = tuple(normalize_tag(tag) for tag in yaml_list(frontmatter, "tags"))
    techniques = unique(
        [
            normalize_technique(item)
            for item in yaml_list(frontmatter, "techniques")
            if normalize_technique(item)
        ]
    )

    if not hypothesis:
        body_match = re.search(r"^#\s+H\d{3}\s*\n+(.*?)(?:\n##|\Z)", text, flags=re.DOTALL | re.MULTILINE)
        hypothesis = clean_text(body_match.group(1)) if body_match else title

    return Flame(
        id=flame_id,
        path=path,
        source_url=f"{SOURCE_BASE_URL}/{path.name}",
        title=title,
        hypothesis=hypothesis,
        tactics=tactics,
        techniques=techniques,
        tags=tags,
        source_format="yaml",
    )


def parse_flame(path: Path) -> Flame:
    text = path.read_text(encoding="utf-8")
    frontmatter = find_frontmatter(text)
    if frontmatter:
        return parse_yaml_format(text, path, frontmatter)
    return parse_table_format(text, path)


def source_files(source: Path) -> list[Path]:
    files = [path for path in source.glob("H*.md") if re.fullmatch(r"H\d{3}\.md", path.name)]
    return sorted(files, key=lambda path: int(path.stem[1:]))


def haystack(flame: Flame) -> str:
    values = [
        flame.id,
        flame.title,
        flame.hypothesis,
        " ".join(flame.tactics),
        " ".join(flame.techniques),
        " ".join(flame.tags),
    ]
    return " ".join(values).lower()


def score_domains(flame: Flame) -> Counter[str]:
    hay = haystack(flame)
    scores: Counter[str] = Counter()

    for domain, config in DOMAIN_RULES.items():
        for keyword in config["keywords"]:
            if keyword in hay:
                scores[domain] += 1

    for tactic in flame.tactics:
        weights = TACTIC_DOMAIN_WEIGHTS.get(tactic.lower(), {})
        for domain, weight in weights.items():
            scores[domain] += weight

    if not scores:
        scores["Threat Intel and Detections"] = 1

    return scores


def infer_domains(flame: Flame) -> tuple[str, ...]:
    scores = score_domains(flame)
    ordered = sorted(
        scores,
        key=lambda domain: (-scores[domain], list(DOMAIN_RULES).index(domain)),
    )
    return tuple(domain for domain in ordered if scores[domain] > 0)[:4]


def infer_tables(flame: Flame, domains: tuple[str, ...]) -> tuple[str, ...]:
    tables: list[str] = []
    for domain in domains:
        tables.extend(DOMAIN_RULES[domain]["tables"])

    hay = haystack(flame)
    if "powershell" in hay or "script" in hay or "encoded" in hay:
        tables.extend(["SecurityEvent", "WindowsEvent", "TrendMicro_XDR_OAT_CL"])
    if "role" in hay or "admin" in hay or "privilege" in hay:
        tables.extend(["AuditLogs", "AzureActivity", "CyberArk_AuditEvents_CL"])
    if "hash" in hay or "ioc" in hay or "indicator" in hay:
        tables.extend(["ThreatIntelIndicators", "Watchlist"])
    if "mailbox" in hay or "inbox" in hay:
        tables.extend(["OfficeActivity", "AuditLogs"])
    if "waf" in hay or "web" in hay or "cve" in hay:
        tables.extend(["Cloudflare_CL", "CommonSecurityLog"])

    return unique(tables)[:12]


def infer_tools(tables: tuple[str, ...]) -> tuple[str, ...]:
    table_tools = OrderedDict(
        [
            ("Microsoft Sentinel", ["SecurityAlert", "SecurityIncident", "ThreatIntelIndicators", "Watchlist", "Anomalies"]),
            ("Microsoft Entra ID", ["SigninLogs", "AuditLogs", "IdentityInfo", "BehaviorAnalytics", "UserPeerAnalytics"]),
            ("Microsoft 365", ["OfficeActivity"]),
            ("Trend Vision One", ["TrendMicro_XDR_OAT_CL", "TrendMicro_XDR_WORKBENCH_CL"]),
            ("Fortigate", ["CommonSecurityLog", "Syslog"]),
            ("Cloudflare", ["Cloudflare_CL"]),
            ("Netskope", ["NetskopeEventsNetwork_CL", "NetskopeEventsConnection_CL", "NetskopeAlerts_CL", "NetskopeEventsApplication_CL", "NetskopeEventsAudit_CL", "NetskopeEventsPage_CL"]),
            ("Orca Security", ["OrcaAlerts_CL"]),
            ("CyberArk", ["CyberArk_AuditEvents_CL"]),
            ("Azure", ["AzureActivity", "AzureDiagnostics"]),
            ("Application Insights", ["AppRequests", "AppTraces", "AppDependencies", "AppExceptions"]),
        ]
    )

    tools: list[str] = []
    table_set = set(tables)
    for tool, tool_tables in table_tools.items():
        if table_set.intersection(tool_tables):
            tools.append(tool)
    return unique(tools)


def has_any(value: str, keywords: list[str]) -> bool:
    return any(keyword in value for keyword in keywords)


def infer_kql_pattern(flame: Flame, domains: tuple[str, ...]) -> str:
    hay = haystack(flame)
    tactics = {tactic.lower() for tactic in flame.tactics}

    if has_any(hay, ["brute force", "bruteforce", "password spray", "failed sign-in", "failed signin", "vpn"]):
        return "Authentication anomaly and brute-force review"
    if has_any(hay, ["oauth", "device code", "devicecode", "token", "prt", "mfa"]):
        return "Identity token/OAuth abuse correlation"
    if has_any(hay, ["registry", "service", "scheduled task", "driver", "dll", "ifeo", "run key"]):
        return "Endpoint persistence and defense-evasion chain"
    if has_any(hay, ["powershell", "script", "mshta", "wscript", "cscript", "cmd.exe"]):
        return "Suspicious script and command execution"
    if has_any(hay, ["c2", "dns", "beacon", "tunnel", "outbound", "egress"]):
        return "Network, DNS, and egress anomaly correlation"
    if has_any(hay, ["webshell", "web shell", "waf", "weblogic", "peoplesoft", "rce", "ssrf", "cve"]):
        return "Public application exploit and webshell review"
    if has_any(hay, ["cloudtrail", "s3", "bucket", "gcp", "aws", "azure", "iam"]):
        return "Cloud control-plane and posture abuse review"
    if has_any(hay, ["mailbox", "inbox", "exchange", "sharepoint", "teams", "onedrive", "content compliance", "bcc", "gmail"]):
        return "M365/SaaS audit and mailbox activity review"
    if has_any(hay, ["hash", "ioc", "indicator", "domain", "url"]):
        return "IOC and indicator sweep"
    if re.search(r"\b(role|administrator|local admin|domain admin|enterprise admin|pam|cyberark)\b", hay):
        return "Administrative and privileged access change review"
    if tactics.intersection({"command and control", "exfiltration"}):
        return "Network, DNS, and egress anomaly correlation"
    if "initial access" in tactics and "Web and Application Edge" in domains:
        return "Public application exploit and webshell review"
    if "collection" in tactics and "M365 and SaaS" in domains:
        return "M365/SaaS audit and mailbox activity review"
    if tactics.intersection({"persistence", "defense evasion", "privilege escalation"}) and "Endpoint and OS" in domains:
        return "Endpoint persistence and defense-evasion chain"
    if tactics.intersection({"execution", "lateral movement"}) and "Endpoint and OS" in domains:
        return "Suspicious script and command execution"
    if "Linux and Server" in domains:
        return "Linux syslog/auditd process and file review"
    return "Hypothesis-specific Sentinel correlation"


def infer_seed_kql(flame: Flame, domains: tuple[str, ...], pattern: str) -> tuple[str, ...]:
    hay = haystack(flame)
    seeds: list[str] = []

    if pattern == "Identity token/OAuth abuse correlation":
        seeds.extend(["Rare app and user-agent access", "Identity failures followed by success"])
    if pattern == "Authentication anomaly and brute-force review":
        seeds.extend(["Identity failures followed by success", "Rare app and user-agent access"])
    if pattern == "Administrative and privileged access change review":
        seeds.append("New admin or role changes")
    if pattern in {"Endpoint persistence and defense-evasion chain", "Suspicious script and command execution"}:
        seeds.extend(["Endpoint suspicious PowerShell", "Trend MITRE mapping hunt"])
    if pattern == "Network, DNS, and egress anomaly correlation":
        seeds.extend(["Network WAF and firewall blocks", "Top egress and denied traffic"])
    if pattern == "Public application exploit and webshell review":
        seeds.extend(["Network WAF and firewall blocks", "High-risk cloud exposure sweep"])
    if pattern == "Cloud control-plane and posture abuse review":
        seeds.extend(["Cloud risk posture", "High-risk cloud exposure sweep"])
    if pattern == "M365/SaaS audit and mailbox activity review":
        seeds.append("Rare app and user-agent access")
    if pattern == "IOC and indicator sweep" or has_any(hay, ["ioc", "indicator", "hash", "domain", "url", "ip address", "cve"]):
        seeds.append("IOC IP/domain/URL/hash sweep")
    if "Endpoint and OS" in domains and "Trend MITRE mapping hunt" not in seeds:
        seeds.append("Trend MITRE mapping hunt")

    return unique(seeds)[:4]


def infer_use_case(flame: Flame, pattern: str) -> str:
    tactic = flame.tactics[0] if flame.tactics else "Threat Hunting"
    focus = shorten(flame.hypothesis, 74)
    return f"UC-{flame.id}: {tactic} - {focus}"


def infer_cadence(flame: Flame) -> str:
    hay = haystack(flame)
    tactics = {tactic.lower() for tactic in flame.tactics}

    if has_any(hay, ["cve", "campaign", "apt", "actor", "malware", "ioc", "indicator", "observed"]):
        return "Intel Hunt"
    if tactics.intersection({"initial access", "command and control", "exfiltration", "impact"}):
        return "Daily Hunt"
    if tactics.intersection({"persistence", "privilege escalation", "defense evasion", "lateral movement", "credential access"}):
        return "Weekly Hunt"
    if has_any(hay, ["coverage", "baseline", "posture", "audit policy"]):
        return "Monthly Hunt"
    return "Intel Hunt"


def infer_latam(flame: Flame) -> str:
    hay = haystack(flame)
    if has_any(hay, LATAM_HIGH_KEYWORDS):
        return "High - regional banking, country, or LATAM-specific tradecraft"
    if has_any(hay, LATAM_MEDIUM_KEYWORDS):
        return "Medium - common LATAM enterprise threat pattern"
    return "Standard - keep for global coverage"


def infer_coverage_status(domains: tuple[str, ...], pattern: str) -> tuple[str, str]:
    if pattern == "Hypothesis-specific Sentinel correlation":
        return (
            "Partial - custom tuning required",
            "A starter KQL exists, but the hypothesis needs analyst tuning for exact fields, joins, and thresholds.",
        )
    if pattern == "Cloud control-plane and posture abuse review":
        return (
            "Starter - validate cloud telemetry",
            "A starter KQL exists, but confirm cloud provider logs, Orca fields, and resource identifiers in Sentinel.",
        )
    if pattern == "M365/SaaS audit and mailbox activity review":
        return (
            "Starter - validate SaaS telemetry",
            "A starter KQL exists, but confirm OfficeActivity, AuditLogs, and Netskope SaaS fields before promotion.",
        )
    if pattern == "Linux syslog/auditd process and file review":
        return (
            "Starter - validate Linux telemetry",
            "A starter KQL exists, but confirm Syslog, auditd, Sysmon-for-Linux, or EDR Linux fields before promotion.",
        )
    primary_domain = domains[0] if domains else ""
    if primary_domain == "M365 and SaaS":
        return (
            "Starter - validate SaaS telemetry",
            "A starter KQL exists, but confirm OfficeActivity, AuditLogs, and Netskope SaaS fields before promotion.",
        )
    if primary_domain == "Cloud and Posture":
        return (
            "Starter - validate cloud telemetry",
            "A starter KQL exists, but confirm cloud provider logs, Orca fields, and resource identifiers in Sentinel.",
        )
    if primary_domain == "Linux and Server":
        return (
            "Starter - validate Linux telemetry",
            "A starter KQL exists, but confirm Syslog, auditd, Sysmon-for-Linux, or EDR Linux fields before promotion.",
        )
    return (
        "Starter KQL - validate in Sentinel",
        "A starter KQL exists using mapped Sentinel tables and hypothesis-specific terms.",
    )


def infer_priority(
    flame: Flame,
    domains: tuple[str, ...],
    pattern: str,
    cadence: str,
    latam_relevance: str,
) -> tuple[str, int]:
    score = 0
    tactics = {tactic.lower() for tactic in flame.tactics}

    if cadence == "Daily Hunt":
        score += 25
    elif cadence == "Weekly Hunt":
        score += 18
    elif cadence == "Intel Hunt":
        score += 12

    if latam_relevance.startswith("High"):
        score += 30
    elif latam_relevance.startswith("Medium"):
        score += 15

    if tactics.intersection({"initial access", "command and control", "exfiltration", "impact"}):
        score += 15
    if tactics.intersection({"credential access", "persistence", "defense evasion", "lateral movement"}):
        score += 10

    if pattern != "Hypothesis-specific Sentinel correlation":
        score += 8
    else:
        score -= 5

    if "Identity and Access" in domains:
        score += 5
    if "Endpoint and OS" in domains:
        score += 5
    if "Network Edge and SASE" in domains:
        score += 4
    if "M365 and SaaS" in domains:
        score += 3

    if score >= 65:
        return "P1", score
    if score >= 45:
        return "P2", score
    if score >= 28:
        return "P3", score
    return "P4", score


def dedicated_kql_path(flame: Flame) -> str:
    return f"sentinel/kql/hearth/{flame.id.lower()}.kql"


def map_flame(flame: Flame) -> FlameMapping:
    domains = infer_domains(flame)
    tables = infer_tables(flame, domains)
    tools = infer_tools(tables)
    pattern = infer_kql_pattern(flame, domains)
    seed_kql = infer_seed_kql(flame, domains, pattern)
    cadence = infer_cadence(flame)
    latam_relevance = infer_latam(flame)
    coverage_status, coverage_notes = infer_coverage_status(domains, pattern)
    priority, priority_score = infer_priority(flame, domains, pattern, cadence, latam_relevance)
    return FlameMapping(
        flame=flame,
        domains=domains,
        tables=tables,
        tools=tools,
        kql_pattern=pattern,
        seed_kql=seed_kql,
        use_case=infer_use_case(flame, pattern),
        cadence=cadence,
        latam_relevance=latam_relevance,
        coverage_status=coverage_status,
        coverage_notes=coverage_notes,
        priority=priority,
        priority_score=priority_score,
        dedicated_kql_path=dedicated_kql_path(flame),
    )


def table_link(table: str) -> str:
    return f"[{table}](../../sentinel/tables/reference/{table}.md)"


def kql_link(name: str) -> str:
    path = KQL_LINKS[name]
    return f"[{name}]({path})"


def dedicated_kql_link(mapping: FlameMapping) -> str:
    relative = "../../" + mapping.dedicated_kql_path
    return f"[{mapping.flame.id}]({relative})"


def source_link(flame: Flame) -> str:
    return f"[{flame.id}]({flame.source_url})"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def generate_external_readme() -> None:
    write(
        OUTPUT_ROOT / "README.md",
        """# External Research

External research pages map public threat hunting ideas into this local Sentinel-centered library.

## Fontes
- [HEARTH Flames Mapping](hearth/README.md): HEARTH hunt hypotheses mapped to Sentinel tables, KQL candidates, use-case candidates, cadence, tools, and LATAM relevance.

## Usage
Use this section as an intake layer. Keep original research linked, then convert validated ideas into local hunt pages, KQL files, and use cases.
""",
    )


def generate_hearth_readme(mappings: list[FlameMapping], source: Path) -> None:
    total = len(mappings)
    tables = Counter(table for mapping in mappings for table in mapping.tables)
    domains = Counter(domain for mapping in mappings for domain in mapping.domains)
    priorities = Counter(mapping.priority for mapping in mappings)
    statuses = Counter(mapping.coverage_status for mapping in mappings)
    top_tables = ", ".join(f"{table} ({count})" for table, count in tables.most_common(8))
    top_domains = ", ".join(f"{domain} ({count})" for domain, count in domains.most_common(6))
    priority_summary = ", ".join(f"{priority} ({priorities[priority]})" for priority in ["P1", "P2", "P3", "P4"] if priorities[priority])
    status_summary = ", ".join(f"{status} ({count})" for status, count in statuses.most_common())

    write(
        HEARTH_OUTPUT / "README.md",
        f"""# HEARTH Flames Mapping

This folder maps HEARTH Flames hunt hypotheses into this Microsoft Sentinel threat hunting library.

Source folder used locally: `{source}`

Canonical source: [THORCollective HEARTH Flames](https://github.com/THORCollective/HEARTH/tree/main/Flames)

## Arquivos Gerados
- [Flames Index](flames-index.md): HEARTH IDs, tactics, techniques, tags, and compact hypothesis summaries.
- [Flames to Sentinel Map](flames-to-sentinel-map.md): Sentinel tables, tools, KQL candidates, use-case candidates, cadence, and LATAM relevance for every Flame.
- [Coverage Tracker](coverage-tracker.md): coverage status, priority, dedicated KQL starter, and validation notes for every Flame.
- [KQL Candidate Patterns](kql-candidate-patterns.md): reusable Sentinel KQL design patterns to convert the mapped Flames into working hunts.
- [Coverage Summary](coverage-summary.md): coverage counts by domain, table, cadence, technique, and LATAM relevance.
- [Dedicated HEARTH KQL Starters](../../sentinel/kql/hearth/README.md): one generated starter KQL candidate per HEARTH Flame.

## Escopo
- HEARTH Flames mapped: {total}
- Top mapped domains: {top_domains}
- Top mapped Sentinel tables: {top_tables}
- Priority queue: {priority_summary}
- Coverage status: {status_summary}

## Como usar
1. Pick a HEARTH ID from the map.
2. Confirm the mapped Sentinel tables are ingesting data.
3. Open the dedicated HEARTH KQL starter or matching reusable pattern.
4. Validate table availability, field names, thresholds, and expected business behavior.
5. Run the hunt with your environment baseline and LATAM context.
6. If the signal repeats with acceptable false positives, create a use case from [Use Case Template](../../templates/use-case-template.md).

## Notas
The mapping is a local analysis layer. It summarizes HEARTH content and links back to the original source instead of copying the full source notes. Dedicated KQL files are starter candidates and still need Sentinel validation before detection promotion.
""",
    )


def generate_index(mappings: list[FlameMapping]) -> None:
    rows = [
        "| ID | Tactics | Techniques | Tags | Hypothesis Summary |",
        "| --- | --- | --- | --- | --- |",
    ]
    for mapping in mappings:
        flame = mapping.flame
        rows.append(
            "| "
            + " | ".join(
                [
                    source_link(flame),
                    md_list(list(flame.tactics)),
                    md_list(list(flame.techniques)),
                    md_list(list(flame.tags[:8])),
                    md_cell(shorten(flame.hypothesis, 190)),
                ]
            )
            + " |"
        )

    write(
        HEARTH_OUTPUT / "flames-index.md",
        "# HEARTH Flames Index\n\n"
        "Compact index of HEARTH Flames entries with source links.\n\n"
        + "\n".join(rows),
    )


def generate_sentinel_map(mappings: list[FlameMapping]) -> None:
    rows = [
        "| ID | Domains | Sentinel Tables | Tools | KQL Candidate | Dedicated KQL | Seed KQL | Coverage | Priority | Use Case Candidate | Cadence | LATAM |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for mapping in mappings:
        seed = "<br>".join(kql_link(name) for name in mapping.seed_kql) if mapping.seed_kql else "New focused KQL"
        rows.append(
            "| "
            + " | ".join(
                [
                    source_link(mapping.flame),
                    md_list(list(mapping.domains)),
                    "<br>".join(table_link(table) for table in mapping.tables),
                    md_list(list(mapping.tools)),
                    md_cell(mapping.kql_pattern),
                    dedicated_kql_link(mapping),
                    seed,
                    md_cell(mapping.coverage_status),
                    md_cell(f"{mapping.priority} ({mapping.priority_score})"),
                    md_cell(mapping.use_case),
                    md_cell(mapping.cadence),
                    md_cell(mapping.latam_relevance),
                ]
            )
            + " |"
        )

    write(
        HEARTH_OUTPUT / "flames-to-sentinel-map.md",
        "# HEARTH Flames To Sentinel Map\n\n"
        "Every HEARTH Flame is mapped to local Sentinel data, tools, KQL direction, a dedicated starter KQL, use-case candidacy, cadence, and LATAM relevance.\n\n"
        "Dedicated KQL files are starter candidates generated from available mapped data. Validate table availability, field names, thresholds, and false positives in Sentinel before promoting a use case.\n\n"
        + "\n".join(rows),
    )


def generate_coverage_summary(mappings: list[FlameMapping]) -> None:
    domains = Counter(domain for mapping in mappings for domain in mapping.domains)
    tables = Counter(table for mapping in mappings for table in mapping.tables)
    cadences = Counter(mapping.cadence for mapping in mappings)
    patterns = Counter(mapping.kql_pattern for mapping in mappings)
    latam = Counter(mapping.latam_relevance for mapping in mappings)
    statuses = Counter(mapping.coverage_status for mapping in mappings)
    priorities = Counter(mapping.priority for mapping in mappings)
    techniques = Counter(technique for mapping in mappings for technique in mapping.flame.techniques)

    def counter_table(title: str, counter: Counter[str], limit: int | None = None) -> str:
        rows = [f"## {title}", "| Item | Count |", "| --- | --- |"]
        items = counter.most_common(limit)
        for item, count in items:
            rows.append(f"| {md_cell(item)} | {count} |")
        return "\n".join(rows)

    content = "\n\n".join(
        [
            "# HEARTH Flames Coverage Summary",
            f"Total Flames mapped: {len(mappings)}",
            counter_table("Domains", domains),
            counter_table("Sentinel Tables", tables),
            counter_table("Cadence", cadences),
            counter_table("Coverage Status", statuses),
            counter_table("Priority", priorities),
            counter_table("KQL Candidate Patterns", patterns),
            counter_table("LATAM Relevance", latam),
            counter_table("Top MITRE Techniques", techniques, limit=40),
        ]
    )
    write(HEARTH_OUTPUT / "coverage-summary.md", content)


def generate_coverage_tracker(mappings: list[FlameMapping]) -> None:
    rows = [
        "| Priority | ID | Coverage Status | Dedicated KQL | Pattern | Tables | Notes | Use Case Candidate |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    ordered = sorted(
        mappings,
        key=lambda mapping: (
            {"P1": 1, "P2": 2, "P3": 3, "P4": 4}.get(mapping.priority, 9),
            -mapping.priority_score,
            int(mapping.flame.id[1:]),
        ),
    )
    for mapping in ordered:
        rows.append(
            "| "
            + " | ".join(
                [
                    md_cell(f"{mapping.priority} ({mapping.priority_score})"),
                    source_link(mapping.flame),
                    md_cell(mapping.coverage_status),
                    dedicated_kql_link(mapping),
                    md_cell(mapping.kql_pattern),
                    md_list(list(mapping.tables[:8])),
                    md_cell(mapping.coverage_notes),
                    md_cell(mapping.use_case),
                ]
            )
            + " |"
        )

    write(
        HEARTH_OUTPUT / "coverage-tracker.md",
        "# HEARTH Coverage Tracker\n\n"
        "This tracker shows the current hunt engineering maturity for every HEARTH Flame in this Sentinel library.\n\n"
        "Coverage status means a starter KQL exists and is mapped to available Sentinel tables. It does not mean the query has been tested or promoted into a production analytic rule.\n\n"
        + "\n".join(rows),
    )


def kql_json(values: tuple[str, ...] | list[str]) -> str:
    return json.dumps(list(values), ensure_ascii=True)


def extract_hunt_terms(mapping: FlameMapping, limit: int = 22) -> tuple[str, ...]:
    stopwords = {
        "about",
        "across",
        "actor",
        "actors",
        "adversary",
        "adversaries",
        "after",
        "against",
        "based",
        "before",
        "being",
        "candidate",
        "could",
        "data",
        "detect",
        "domain",
        "event",
        "events",
        "from",
        "have",
        "host",
        "hosts",
        "hunt",
        "into",
        "local",
        "mapped",
        "might",
        "their",
        "these",
        "they",
        "this",
        "threat",
        "using",
        "with",
    }
    tactic_terms = {clean_text(tactic).lower() for tactic in mapping.flame.tactics}
    terms: list[str] = []

    for technique in mapping.flame.techniques:
        terms.append(technique)

    for tag in mapping.flame.tags:
        tag = normalize_tag(tag)
        if tag and tag not in tactic_terms and not tag.startswith("t"):
            terms.append(tag.replace("_", " "))

    text = " ".join([mapping.flame.title, mapping.flame.hypothesis])
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9_.:/\\@%-]{3,}", text)
    for token in tokens:
        cleaned = clean_text(token).strip(".,;:()[]{}")
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if lowered in stopwords:
            continue
        if lowered.startswith("http"):
            continue
        if len(lowered) < 4:
            continue
        terms.append(cleaned)

    if not terms:
        terms.extend([mapping.flame.id] + list(mapping.flame.techniques) + list(mapping.flame.tags))

    return unique(terms)[:limit]


def kql_union_tables(mapping: FlameMapping) -> str:
    tables = list(mapping.tables)
    if not tables:
        tables = ["SecurityEvent", "WindowsEvent", "CommonSecurityLog"]
    return ",\n    ".join(tables)


def kql_lookback(mapping: FlameMapping) -> str:
    if mapping.cadence == "Daily Hunt":
        return "1d"
    if mapping.cadence == "Weekly Hunt":
        return "7d"
    if mapping.cadence == "Monthly Hunt":
        return "30d"
    return "14d"


def kql_metadata_comment(mapping: FlameMapping) -> str:
    hypothesis = shorten(mapping.flame.hypothesis, 220)
    return "\n".join(
        [
            f"// HEARTH {mapping.flame.id} - starter KQL candidate",
            f"// Source: {mapping.flame.source_url}",
            f"// Hypothesis: {hypothesis}",
            f"// Pattern: {mapping.kql_pattern}",
            f"// Coverage: {mapping.coverage_status}",
            f"// Priority: {mapping.priority} ({mapping.priority_score})",
            f"// Tables: {', '.join(mapping.tables)}",
            "// Validate table availability, field names, thresholds, and false positives before using as a detection.",
        ]
    )


def generic_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntId = "{mapping.flame.id}";
let sourceUrl = "{mapping.flame.source_url}";
let huntTerms = dynamic({kql_json(terms)});
union withsource=SourceTable isfuzzy=true
    {kql_union_tables(mapping)}
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = huntId, SourceUrl = sourceUrl
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def auth_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let failureThreshold = 8;
let huntTerms = dynamic({kql_json(terms)});
let failures =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType != "0"
    | summarize
        FailedAttempts = count(),
        FailureIPs = make_set(IPAddress, 20),
        FailureApps = make_set(AppDisplayName, 20),
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
        FirstSuccess = min(TimeGenerated)
        by UserPrincipalName;
let authFindings =
    failures
    | where FailedAttempts >= failureThreshold
    | join kind=inner successes on UserPrincipalName
    | where LastFailure <= FirstSuccess
    | extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}";
authFindings
| project HuntId, SourceUrl, UserPrincipalName, FailedAttempts, Successes, FailureIPs, SuccessIPs, FailureApps, SuccessApps, LastFailure, FirstSuccess
| order by FailedAttempts desc"""


def identity_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(terms)});
union withsource=SourceTable isfuzzy=true
    SigninLogs,
    AuditLogs,
    OfficeActivity
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
    or SearchBlob has_any ("deviceCode", "oauth", "refresh token", "consent", "service principal", "Microsoft Graph")
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def endpoint_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    extra_terms = [
        "powershell",
        "cmd.exe",
        "wscript",
        "cscript",
        "mshta",
        "rundll32",
        "regsvr32",
        "CurrentVersion\\Run",
        "Scheduled",
        "Service",
        "Registry",
    ]
    if mapping.kql_pattern == "Endpoint persistence and defense-evasion chain":
        extra_terms.extend(["Image File Execution Options", "SilentProcessExit", "Debugger", "Driver", "DLL"])
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(unique(list(terms) + extra_terms))});
union withsource=SourceTable isfuzzy=true
    SecurityEvent,
    WindowsEvent,
    TrendMicro_XDR_OAT_CL,
    TrendMicro_XDR_WORKBENCH_CL
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def network_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    extra_terms = ["dns", "http", "https", "ssh", "rdp", "smb", "tunnel", "beacon", "c2", "block", "deny"]
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(unique(list(terms) + extra_terms))});
union withsource=SourceTable isfuzzy=true
    CommonSecurityLog,
    Cloudflare_CL,
    NetskopeEventsNetwork_CL,
    NetskopeEventsConnection_CL,
    NetskopeAlerts_CL
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| summarize
    Events = count(),
    FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated),
    Samples = make_set(SearchBlob, 3)
    by HuntId, SourceUrl, SourceTable
| order by Events desc"""


def cloud_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    extra_terms = ["roleAssignments", "delete", "write", "storage", "bucket", "iam", "diagnosticSettings", "critical", "high"]
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(unique(list(terms) + extra_terms))});
union withsource=SourceTable isfuzzy=true
    AzureActivity,
    AzureDiagnostics,
    OrcaAlerts_CL,
    NetskopeEventsNetwork_CL
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def m365_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    extra_terms = ["New-InboxRule", "Set-InboxRule", "Mailbox", "Consent", "service principal", "SharePoint", "Teams", "OneDrive", "BCC", "forward"]
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(unique(list(terms) + extra_terms))});
union withsource=SourceTable isfuzzy=true
    OfficeActivity,
    AuditLogs,
    SigninLogs,
    NetskopeEventsApplication_CL,
    NetskopeEventsAudit_CL
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def web_kql_body(mapping: FlameMapping) -> str:
    terms = extract_hunt_terms(mapping)
    extra_terms = ["POST", "GET", "webshell", "cmd=", "whoami", "bash", "powershell", "rce", "ssrf", "jndi"]
    return f"""{kql_metadata_comment(mapping)}
let lookback = {kql_lookback(mapping)};
let huntTerms = dynamic({kql_json(unique(list(terms) + extra_terms))});
union withsource=SourceTable isfuzzy=true
    Cloudflare_CL,
    CommonSecurityLog,
    AzureDiagnostics,
    AppRequests,
    AppTraces,
    Syslog
| where TimeGenerated >= ago(lookback)
| extend SearchBlob = tostring(pack_all())
| where SearchBlob has_any (huntTerms)
| extend HuntId = "{mapping.flame.id}", SourceUrl = "{mapping.flame.source_url}"
| project TimeGenerated, HuntId, SourceTable, SourceUrl, SearchBlob
| order by TimeGenerated desc"""


def kql_body(mapping: FlameMapping) -> str:
    if mapping.kql_pattern == "Authentication anomaly and brute-force review":
        return auth_kql_body(mapping)
    if mapping.kql_pattern == "Identity token/OAuth abuse correlation":
        return identity_kql_body(mapping)
    if mapping.kql_pattern in {
        "Endpoint persistence and defense-evasion chain",
        "Suspicious script and command execution",
        "Linux syslog/auditd process and file review",
    }:
        return endpoint_kql_body(mapping)
    if mapping.kql_pattern == "Network, DNS, and egress anomaly correlation":
        return network_kql_body(mapping)
    if mapping.kql_pattern == "Cloud control-plane and posture abuse review":
        return cloud_kql_body(mapping)
    if mapping.kql_pattern == "M365/SaaS audit and mailbox activity review":
        return m365_kql_body(mapping)
    if mapping.kql_pattern == "Public application exploit and webshell review":
        return web_kql_body(mapping)
    return generic_kql_body(mapping)


def generate_hearth_kql(mappings: list[FlameMapping]) -> None:
    for mapping in mappings:
        write(ROOT / mapping.dedicated_kql_path, kql_body(mapping))

    priorities = Counter(mapping.priority for mapping in mappings)
    statuses = Counter(mapping.coverage_status for mapping in mappings)
    rows = [
        "| Priority | ID | KQL | Pattern | Status | Main Tables |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    ordered = sorted(
        mappings,
        key=lambda mapping: (
            {"P1": 1, "P2": 2, "P3": 3, "P4": 4}.get(mapping.priority, 9),
            -mapping.priority_score,
            int(mapping.flame.id[1:]),
        ),
    )
    for mapping in ordered:
        local = Path(mapping.dedicated_kql_path).name
        rows.append(
            "| "
            + " | ".join(
                [
                    md_cell(f"{mapping.priority} ({mapping.priority_score})"),
                    source_link(mapping.flame),
                    f"[{local}]({local})",
                    md_cell(mapping.kql_pattern),
                    md_cell(mapping.coverage_status),
                    md_list(list(mapping.tables[:6])),
                ]
            )
            + " |"
        )

    priority_summary = ", ".join(f"{priority} ({priorities[priority]})" for priority in ["P1", "P2", "P3", "P4"] if priorities[priority])
    status_summary = ", ".join(f"{status} ({count})" for status, count in statuses.most_common())
    write(
        HEARTH_KQL_OUTPUT / "README.md",
        f"""# HEARTH KQL Starters

This folder contains one generated starter KQL candidate per HEARTH Flame.

These files are based on the Sentinel tables currently mapped in this repository. They are not production detections until they are tested in your Sentinel workspace.

## Escopo
- Dedicated starter KQL files: {len(mappings)}
- Priority queue: {priority_summary}
- Coverage status: {status_summary}

## Como usar
1. Start with P1 and P2 hunts.
2. Confirm the referenced tables are ingesting data.
3. Run the query with the default lookback.
4. Tune terms, fields, joins, thresholds, and allowlists.
5. Promote stable logic into a use case or analytic rule.

## Índice
{chr(10).join(rows)}
""",
    )


def generate_kql_patterns() -> None:
    write(
        HEARTH_OUTPUT / "kql-candidate-patterns.md",
        """# HEARTH KQL Candidate Patterns

These are reusable Sentinel KQL starting patterns for the HEARTH Flames mapping. They are candidates, not production detections. Validate table availability, field names, noise, and expected business behavior before promoting them into use cases.

# Nº 1. Anomalia de autenticação e revisão de força bruta
Mapped Flames with brute force, password spray, VPN authentication, failed sign-in bursts, or suspicious success-after-failure behavior should start from `SigninLogs`, VPN/firewall logs in `CommonSecurityLog`, and identity context from `IdentityInfo`.

```kql
let lookback = 1d;
let failureThreshold = 8;
let failures =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType != "0"
    | summarize
        FailedAttempts = count(),
        FailureIPs = make_set(IPAddress, 20),
        FailureApps = make_set(AppDisplayName, 20),
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
        FirstSuccess = min(TimeGenerated)
        by UserPrincipalName;
failures
| where FailedAttempts >= failureThreshold
| join kind=inner successes on UserPrincipalName
| where LastFailure <= FirstSuccess
| project UserPrincipalName, FailedAttempts, Successes, FailureIPs, SuccessIPs, FailureApps, SuccessApps, LastFailure, FirstSuccess
| order by FailedAttempts desc
```

## 2. Token de identidade e abuso de OAuth
Mapped Flames with device code, OAuth, token theft, Graph, MFA bypass, or suspicious client-app usage should start from `SigninLogs`, `AuditLogs`, `IdentityInfo`, and `OfficeActivity`.

```kql
let lookback = 7d;
SigninLogs
| where TimeGenerated >= ago(lookback)
| where ResultType == "0"
| where AuthenticationProtocol has_any ("deviceCode", "oauth", "ropc")
    or AppDisplayName has_any ("Azure CLI", "Microsoft Graph", "Office", "PowerShell")
| summarize
    FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated),
    IPs = make_set(IPAddress, 20),
    Apps = make_set(AppDisplayName, 20),
    Resources = make_set(ResourceDisplayName, 20)
    by UserPrincipalName, UserAgent, Location
| order by LastSeen desc
```

## 3. Mudanças administrativas e de acesso privilegiado
Mapped Flames involving admin roles, privileged access, PAM, CA changes, or account creation should start from `AuditLogs`, `AzureActivity`, `SecurityEvent`, and `CyberArk_AuditEvents_CL`.

```kql
let lookback = 7d;
union isfuzzy=true
(
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | where OperationName has_any ("role", "admin", "credential", "application", "policy")
    | project TimeGenerated, Source = "AuditLogs", Actor = tostring(InitiatedBy.user.userPrincipalName), OperationName, TargetResources, Result
),
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any ("roleAssignments", "write", "delete")
    | project TimeGenerated, Source = "AzureActivity", Actor = Caller, OperationName = OperationNameValue, TargetResources = ResourceId, Result = ActivityStatusValue
),
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4720, 4722, 4728, 4732, 4738, 4670, 4672)
    | project TimeGenerated, Source = "SecurityEvent", Actor = SubjectUserName, OperationName = tostring(EventID), TargetResources = TargetUserName, Result = Activity
)
| order by TimeGenerated desc
```

## 4. Processo de endpoint e execução de script
Mapped Flames involving PowerShell, script hosts, WMI/DCOM, suspicious command lines, ClickFix, or LOLBins should start from `SecurityEvent`, `WindowsEvent`, and `TrendMicro_XDR_OAT_CL`.

```kql
let lookback = 3d;
let suspiciousTerms = dynamic(["powershell", "-enc", "frombase64string", "iex", "downloadstring", "wmic", "mshta", "rundll32", "regsvr32", "wscript", "cscript"]);
union isfuzzy=true
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID == 4688
    | extend CommandLine = tostring(CommandLine)
    | project TimeGenerated, Source = "SecurityEvent", Computer, Account, ProcessName, ParentProcessName, CommandLine
),
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | extend CommandLine = tostring(coalesce(detail_processCmd_s, detail_objectCmd_s, detail_parentCmd_s))
    | project TimeGenerated, Source = "Trend Vision One", Computer = detail_endpointHostName_s, Account = detail_processUser_s, ProcessName = detail_processName_s, ParentProcessName = detail_parentName_s, CommandLine
)
| where CommandLine has_any (suspiciousTerms) or ProcessName has_any (suspiciousTerms)
| order by TimeGenerated desc
```

## 5. Persistência de endpoint e evasão de defesa
Mapped Flames involving services, registry keys, IFEO, Run keys, drivers, scheduled tasks, DLL search order, or security tool impairment should start from endpoint event tables and Trend Vision One.

```kql
let lookback = 7d;
let persistenceTerms = dynamic(["CurrentVersion\\\\Run", "Image File Execution Options", "SilentProcessExit", "CurrentControlSet\\\\Services", "Scheduled Tasks", "Debugger", "MonitorProcess"]);
union isfuzzy=true
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4657, 4697, 7045, 4698)
    | extend Details = tostring(EventData)
    | project TimeGenerated, Source = "SecurityEvent", Computer, Account, EventID, Details
),
(
    WindowsEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4657, 4697, 7045, 4698)
    | extend Details = tostring(EventData)
    | project TimeGenerated, Source = "WindowsEvent", Computer, Account = tostring(EventData.SubjectUserName), EventID, Details
),
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | extend Details = strcat(detail_processCmd_s, " ", detail_objectRegistryKey_s, " ", detail_objectFilePath_s)
    | project TimeGenerated, Source = "Trend Vision One", Computer = detail_endpointHostName_s, Account = detail_processUser_s, EventID = detail_eventId_d, Details
)
| where Details has_any (persistenceTerms)
| order by TimeGenerated desc
```

## 6. Rede, DNS e correlação de saída
Mapped Flames involving C2, DNS, tunneling, dead-drop resolvers, proxy traffic, VPN, or exfiltration should start from `CommonSecurityLog`, `NetskopeEventsNetwork_CL`, `NetskopeEventsConnection_CL`, and `Cloudflare_CL`.

```kql
let lookback = 7d;
let suspiciousDomains = dynamic(["trycloudflare.com", "workers.dev", "devtunnels.ms", "rentry.co", "telegra.ph"]);
union isfuzzy=true
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), SrcIp = SourceIP, DstIp = DestinationIP, DstPort = DestinationPort, Url = RequestURL, User = SourceUserName, Action = DeviceAction
),
(
    NetskopeEventsNetwork_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Netskope Network", SrcIp = srcip, DstIp = dstip, DstPort = dstport, Url = ur_normalized, User = user, Action = action
),
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Cloudflare", SrcIp = ClientIP_s, DstIp = OriginIP_s, DstPort = int(null), Url = ClientRequestURI_s, User = RequestHeaders_cf_access_user_s, Action = SecurityAction_s
)
| where Url has_any (suspiciousDomains) or Action has_any ("block", "challenge", "deny")
| summarize Events = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Users = make_set(User, 20) by Source, SrcIp, DstIp, tostring(DstPort), Url, Action
| order by Events desc
```

## 7. Exploração de aplicativos públicos e revisão do Webshell
Mapped Flames involving CVEs, WAF, public application exploit, webshells, PeopleSoft, WebLogic, IIS, or app-server process behavior should start from `Cloudflare_CL`, `CommonSecurityLog`, `AzureDiagnostics`, `AppRequests`, `AppTraces`, and `Syslog`.

```kql
let lookback = 7d;
let exploitTerms = dynamic(["/PSEMHUB/", "/PSIGW/", "cmd=", "whoami", "powershell", "bash", "wget", "curl", "jndi", "xml"]);
union isfuzzy=true
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Cloudflare", ClientIP = ClientIP_s, Uri = ClientRequestURI_s, Action = SecurityAction_s, UserAgent = ClientRequestUserAgent_s
),
(
    AppRequests
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "AppRequests", ClientIP = ClientIP, Uri = Url, Action = ResultCode, UserAgent = tostring(Properties)
),
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), ClientIP = SourceIP, Uri = RequestURL, Action = DeviceAction, UserAgent = RequestClientApplication
)
| where Uri has_any (exploitTerms) or UserAgent has_any (exploitTerms)
| order by TimeGenerated desc
```

## 8. Plano de controle de nuvem e abuso de postura
Mapped Flames involving AWS/GCP/Azure IAM, bucket hijacking, exposed services, cloud storage, or cloud control-plane changes should start from `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL`, and any provider logs routed into Sentinel.

```kql
let lookback = 14d;
union isfuzzy=true
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any ("delete", "write", "roleAssignments", "storageAccounts", "diagnosticSettings")
    | project TimeGenerated, Source = "AzureActivity", Actor = Caller, Operation = OperationNameValue, Resource = ResourceId, Result = ActivityStatusValue
),
(
    OrcaAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where risk_level_s in~ ("critical", "high", "medium")
    | project TimeGenerated, Source = "Orca", Actor = cloud_account_name_s, Operation = alert_category_s, Resource = asset_name_s, Result = status_s
)
| order by TimeGenerated desc
```

## 9. Revisão de auditoria M365 e SaaS
Mapped Flames involving mailbox abuse, OAuth apps, SaaS file access, inbox rules, or suspicious app usage should start from `OfficeActivity`, `AuditLogs`, `SigninLogs`, and Netskope SaaS tables.

```kql
let lookback = 7d;
let suspiciousOps = dynamic(["New-InboxRule", "Set-InboxRule", "Add-MailboxPermission", "Consent to application", "Add service principal"]);
union isfuzzy=true
(
    OfficeActivity
    | where TimeGenerated >= ago(lookback)
    | where Operation has_any (suspiciousOps)
    | project TimeGenerated, Source = "OfficeActivity", User = UserId, Operation, ClientIP, ObjectId, ResultStatus
),
(
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | where OperationName has_any (suspiciousOps)
    | project TimeGenerated, Source = "AuditLogs", User = tostring(InitiatedBy.user.userPrincipalName), Operation = OperationName, ClientIP = tostring(InitiatedBy.user.ipAddress), ObjectId = tostring(TargetResources), ResultStatus = Result
),
(
    NetskopeEventsApplication_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Netskope Application", User = user, Operation = activity, ClientIP = srcip, ObjectId = object, ResultStatus = action
)
| order by TimeGenerated desc
```

## 10. IOC e varredura de indicador
Mapped Flames with hashes, domains, URLs, IPs, malware names, or campaign indicators should usually start from the existing [IOC IP/domain/URL/hash sweep](../../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql), then add source-specific joins only where needed.

## 11. Promoção para caso de uso
When a mapped Flame produces repeatable signal:

1. Create a page from [Use Case Template](../../templates/use-case-template.md).
2. Record the HEARTH ID as the external research source.
3. Keep the Sentinel tables and seed KQL from the mapping.
4. Add triage steps, false positives, entity mapping, severity, and suppression logic.
5. Test in Sentinel before enabling an analytic rule.
""",
    )


def generate_all(source: Path) -> None:
    files = source_files(source)
    if not files:
        raise FileNotFoundError(f"No H###.md files found under {source}")

    flames = [parse_flame(path) for path in files]
    mappings = [map_flame(flame) for flame in flames]

    generate_external_readme()
    generate_hearth_readme(mappings, source)
    generate_index(mappings)
    generate_sentinel_map(mappings)
    generate_coverage_tracker(mappings)
    generate_hearth_kql(mappings)
    generate_kql_patterns()
    generate_coverage_summary(mappings)

    print(f"Mapped {len(mappings)} HEARTH Flames into {HEARTH_OUTPUT}")
    print(f"Generated {len(mappings)} HEARTH KQL starters into {HEARTH_KQL_OUTPUT}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Map HEARTH Flames into this Sentinel library.")
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Path to the HEARTH Flames folder.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generate_all(args.source)


if __name__ == "__main__":
    main()
