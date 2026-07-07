# Elastic Security

## Objetivo
Referência externa SIEM/EDR e fonte de detecção que pode enriquecer as caçadas Sentinel quando alertas ou dados são exportados.

## Categoria
SIEM

## Como funciona
- A Elastic pode coletar dados de endpoint, rede, nuvem e detecção fora de Sentinel.
- Esta biblioteca deve rastrear quais detecções, alertas ou casos do Elastic são encaminhados para Sentinel.
- Use o Elastic como referência de conteúdo somente quando as tabelas e campos Sentinel equivalentes forem mapeados.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- Nenhuma tabela Sentinel confirmada ainda.

## O que revisar
- Lógica de detecção que pode ser traduzida em KQL ou mapeada para tabelas Sentinel existentes.
- Qualidade de encaminhamento de alertas, normalização de campo, mapeamento de entidades e tratamento de alertas duplicados.
- Diferenças de cobertura entre Elastic e Sentinel para endpoint, rede ou fontes de nuvem.

## Uso de caça
- Use como referência externa SIEM se as detecções elásticas forem exportadas para Sentinel

## Coisas de segurança para observar
- O paralelo SIEMs pode criar pontos cegos se os alertas permanecerem em uma plataforma e os incidentes em outra.
- As detecções traduzidas precisam de validação porque os campos EQL/Sigma/Elastic podem não corresponder aos esquemas Sentinel.
- As detecções duplicadas devem ser ajustadas para evitar fadiga de alerta.

## Perguntas úteis sobre caça
- Quais detecções do Elastic não têm caso de uso Sentinel equivalente?
- Quais alertas são encaminhados sem entidades úteis?
- Quais fontes de dados somente Elastic devem ser integradas ou normalizadas em Sentinel?

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
