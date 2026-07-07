# Revisão da linha de base de identidade

## Objetivo
Revise a postura de identidade, contas inativas, alterações privilegiadas e padrões de login de alto volume.

## Cadência
Caça Mensal

## Tabelas Sentinel
- [IdentityInfo](../../sentinel/tables/reference/IdentityInfo.md)
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)

## Ferramentas
- [Microsoft Entra ID](../../tools/identity/microsoft-entra-id.md)
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`monthly/identity-baseline-review.kql`](../../sentinel/kql/monthly/identity-baseline-review.kql)

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
