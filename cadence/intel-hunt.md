# Caça Intelectual

## Objetivo
Traduza rapidamente novas informações em pesquisas nas tabelas Sentinel.

## Gatilhos
- Novo IOCs da inteligência de ameaças.
- Novo CVE relevante para ativos expostos.
- Alerta ou relatório do fornecedor com TTPs.
- Nova campanha direcionada ao seu setor.
- Incidente interno ou padrão suspeito que requer pesquisa histórica.

## Runbook
1. Normalize IOCs em `ThreatIntelIndicators` ou em uma lista de observação.
2. Varra tabelas de rede, endpoint, nuvem, identidade e fornecedores.
3. Evitar qualquer ocorrência em entidades e eventos relacionados.
4. Registre se a informação é relevante, ruidosa ou acionável.
5. Promova a lógica estável em uma regra analítica ou busca recorrente.

## Consultas
- [`ioc-ip-domain-url-hash-sweep.kql`](../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql)
- [`trend-mitre-mapping-hunt.kql`](../sentinel/kql/intel/trend-mitre-mapping-hunt.kql)
- [`high-risk-cloud-exposure-sweep.kql`](../sentinel/kql/intel/high-risk-cloud-exposure-sweep.kql)
