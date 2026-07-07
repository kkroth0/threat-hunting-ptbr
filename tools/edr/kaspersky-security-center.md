# Kaspersky Security Center

## Objetivo
Gerenciamento de proteção de endpoint e contexto de administração antivirus/EDR. O mapeamento Sentinel está pendente nesta biblioteca.

## Categoria
EDR

## Como funciona
- Geralmente gerencia políticas de endpoint, eventos de malware, atualizações, quarentena e status de proteção de endpoint.
- A telemetria pode atingir Sentinel por meio de syslog, exportação API, conector personalizado ou outro caminho de encaminhamento SIEM.
- Até que o conector seja confirmado, trate esta página como uma lista de verificação de mapeamento para dados de proteção de endpoint.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- Nenhuma tabela Sentinel confirmada ainda.

## O que revisar
- Detecções de malware, execuções bloqueadas, eventos de quarentena, alterações de políticas e eventos de proteção desativada.
- Agentes desatualizados, falhas signature/update, módulos desabilitados e endpoints não gerenciados.
- Alterações, exclusões, alterações na proteção contra adulteração e edições em massa de políticas no Admin Console.

## Uso de caça
- Adicionar mapeamento de tabela Sentinel quando o caminho do conector ou do syslog for confirmado

## Coisas de segurança para observar
- Lacunas de proteção podem explicar por que as buscas por endpoints perdem atividade.
- Novas exclusões ou proteção desativada podem ser precursoras da execução de malware ou ransomware.
- O mapeamento desta ferramenta em Sentinel deve priorizar a identidade do host, o nome da detecção, a ação, o usuário e o hash do arquivo.

## Perguntas úteis sobre caça
- Quais hosts detectam malware repetidamente, mas nunca criam incidentes Sentinel?
- Quais endpoints desabilitaram a proteção ou falharam nas atualizações?
- Quais exclusões foram adicionadas pouco antes de atividades suspeitas de endpoint?

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
