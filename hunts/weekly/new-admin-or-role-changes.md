# Novo administrador ou alterações de função

## Objetivo
Revise as alterações de função privilegiada, política, senha e acesso a credenciais.

## Cadência
Caça Semanal

## Tabelas Sentinel
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)
- [AzureActivity](../../sentinel/tables/reference/AzureActivity.md)
- [CyberArk_AuditEvents_CL](../../sentinel/tables/reference/CyberArk_AuditEvents_CL.md)

## Ferramentas
- [Microsoft Entra ID](../../tools/identity/microsoft-entra-id.md)
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)
- [CyberArk](../../tools/pam/cyberark.md)

## KQL
[`weekly/new-admin-or-role-changes.kql`](../../sentinel/kql/weekly/new-admin-or-role-changes.kql)

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
