# Postura de risco na nuvem

## Objetivo
Revise descobertas de postura de nuvem de alto risco e atividades suspeitas no plano de controle.

## Cadência
Caça Semanal

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [AzureActivity](../../sentinel/tables/reference/AzureActivity.md)
- [AzureDiagnostics](../../sentinel/tables/reference/AzureDiagnostics.md)

## Ferramentas
- [Orca Security](../../tools/cspm/orca-security.md)
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`weekly/cloud-risk-posture.kql`](../../sentinel/kql/weekly/cloud-risk-posture.kql)

## Fluxo de trabalho do analista
1. Confirme a integridade da fonte de dados nas tabelas acima.
2. Execute KQL com o lookback padrão.
3. Revise as principais entidades, valores discrepantes e padrões repetidos.
4. Enriqueça usuários, hosts, IPs, URLs, hashes ou recursos de nuvem suspeitos.
5. Registre a decisão: benigna, suspeita, incidente, candidato a detecção ou item de ajuste.

## Resultado Esperado
- Descobertas confirmadas ou falsos positivos documentados.
- Notas de ajuste para limites, listas de permissões, listas de observação ou melhorias no analisador.
- Detecção ou acompanhamento de incidentes quando o comportamento se repete ou apresenta impacto.
