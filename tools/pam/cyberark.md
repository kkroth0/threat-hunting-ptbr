# CyberArk

## Objetivo
Acesso privilegiado, cofre, cofre, conta, recuperação de credenciais e telemetria de auditoria de sessão privilegiada.

## Categoria
PAM

## Como funciona
- Os eventos de auditoria registram acesso privilegiado à conta, alterações seguras, atividades de sessão, alterações de política e operações de credenciais.
- A telemetria PAM deve ser associada a dados de identidade, endpoint e incidentes para buscas por abuso de privilégios.
- O contexto CyberArk ajuda a distinguir atividades privilegiadas autorizadas do uso incomum de credenciais.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [CyberArk_AuditEvents_CL](../../sentinel/tables/reference/CyberArk_AuditEvents_CL.md)

## O que revisar
- Recuperação de credenciais fora do horário normal, cofres incomuns, falhas repetidas e novos acessos a contas privilegiadas.
- Alterações seguras de associação, alterações de política, anomalias de senha checkout/checkin e lacunas de gravação de sessão.
- Atividade privilegiada seguida de alterações de endpoint, nuvem ou identidade.

## Uso de caça
- Revisão de sessão privilegiada
- Mudança de política segura ou de conta
- Recuperação incomum de credenciais

## Coisas de segurança para observar
- As credenciais privilegiadas têm alto impacto mesmo quando a identidade de origem parece legítima.
- Contas de segurança e de serviço precisam de linhas de base separadas dos usuários administradores normais.
- Os eventos PAM são mais valiosos quando correlacionados com as ações executadas após a recuperação da credencial.

## Perguntas úteis sobre caça
- Quais contas privilegiadas foram acessadas por novos usuários ou de novos locais?
- Quais cofres tiveram adesão ou alterações de política?
- Quais verificações de credenciais são seguidas por endpoint incomum ou administração de nuvem?

## Fluxo de trabalho do analista
1. Confirme se o conector está íntegro e se a tabela esperada está recebendo dados.
2. Revise os campos mais importantes: hora, usuário, host, origem IP, destino, ação, gravidade, política e evento bruto.
3. Crie uma linha de base para atividades normais por usuário, ativo, aplicativo, política e local.
4. Procure comportamentos raros, novos, de alto risco ou acorrentados.
5. Documente as descobertas e promova lógica estável em [Casos de uso](../../use-cases/README.md).

## Lista de verificação de maturidade
- O proprietário da fonte de dados é conhecido.
- As tabelas Sentinel e os campos-chave esperados estão documentados.
- As suposições do analisador e a normalização de campo são revisadas.
- Pelo menos uma busca diária ou semanal utiliza esta fonte de dados.
- Falsos positivos e notas de ajuste são capturados após cada caçada.

## Páginas da biblioteca relacionadas
- [Mapa da tabela de ferramentas](../../sentinel/tables/tool-table-map.md)
- [Normalização de campo](../../sentinel/tables/field-normalization.md)
- [Biblioteca KQL](../../sentinel/kql/README.md)
- [Biblioteca de caça](../../hunts/README.md)
