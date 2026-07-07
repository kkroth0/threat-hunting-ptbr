# Caça Semanal

## Objetivo
Encontre um comportamento que precise de uma linha de base maior do que a busca diária pode fornecer.

## Timebox sugerido
2 a 4 horas.

## Runbook
1. Revise as alterações privilegiadas de funções, políticas e credenciais.
2. Revise a postura da nuvem e as atividades arriscadas do plano de controle.
3. Procure aplicativos raros e acesso de agente de usuário.
4. Revise as principais saídas, tráfego negado e destinos incomuns.
5. Converta descobertas repetidas em listas de observação, ajustes ou candidatos de detecção.

## Consultas
- [`new-admin-or-role-changes.kql`](../sentinel/kql/weekly/new-admin-or-role-changes.kql)
- [`cloud-risk-posture.kql`](../sentinel/kql/weekly/cloud-risk-posture.kql)
- [`rare-app-and-user-agent-access.kql`](../sentinel/kql/weekly/rare-app-and-user-agent-access.kql)
- [`top-egress-and-denied-traffic.kql`](../sentinel/kql/weekly/top-egress-and-denied-traffic.kql)
