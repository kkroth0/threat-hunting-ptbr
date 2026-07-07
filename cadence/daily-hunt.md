# Caça Diária

## Objetivo
Identifique o risco ativo antecipadamente e verifique se os dados necessários para a caça ainda estão íntegros.

## Timebox sugerido
30 a 60 minutos.

## Runbook
1. Revise incidentes ou alertas altos e médios.
2. Verifique as falhas de identidade seguidas de sucesso.
3. Revise a atividade suspeita de script de endpoint.
4. Revise os blocos WAF, firewall e SASE.
5. Confirme a integridade do conector e do agente.

## Consultas
- [`identity-failures-followed-by-success.kql`](../sentinel/kql/daily/identity-failures-followed-by-success.kql)
- [`high-severity-alerts-and-incidents.kql`](../sentinel/kql/daily/high-severity-alerts-and-incidents.kql)
- [`endpoint-suspicious-powershell.kql`](../sentinel/kql/daily/endpoint-suspicious-powershell.kql)
- [`network-waf-and-firewall-blocks.kql`](../sentinel/kql/daily/network-waf-and-firewall-blocks.kql)
- [`data-source-health.kql`](../sentinel/kql/daily/data-source-health.kql)
