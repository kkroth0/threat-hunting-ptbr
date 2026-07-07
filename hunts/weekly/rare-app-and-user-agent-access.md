# Acesso raro a aplicativos e agentes de usuários

## Objetivo
Encontre combinações app/user-agent novas ou raras para usuários na última semana.

## Cadência
Caça Semanal

## Tabelas Sentinel
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)
- [OfficeActivity](../../sentinel/tables/reference/OfficeActivity.md)
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)

## Ferramentas
- [Microsoft Entra ID](../../tools/identity/microsoft-entra-id.md)
- [Microsoft 365](../../tools/saas/microsoft-365.md)
- [Netskope](../../tools/sase/netskope.md)

## KQL
[`weekly/rare-app-and-user-agent-access.kql`](../../sentinel/kql/weekly/rare-app-and-user-agent-access.kql)

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
