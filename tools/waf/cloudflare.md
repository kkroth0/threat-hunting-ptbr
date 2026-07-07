# Cloudflare

## Objetivo
Edge, CDN, DNS, bot, WAF e telemetria de aplicativos públicos para serviços voltados para a Internet.

## Categoria
WAF

## Como funciona
- Os eventos Cloudflare mostram solicitações antes de atingirem a infraestrutura de origem.
- Ação WAF, regra ID, URI, host, agente do usuário, origem IP, país, pontuação do bot e status de origem ajudam a explicar o tráfego de ataque.
- Cloudflare é mais forte quando correlacionado com logs de aplicativos, acesso de identidade, logs de firewall e cronogramas de incidentes.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)

## O que revisar
- blocos WAF, desafios gerenciados, pontuações de bot, mudanças de pontuação de ataque e anomalias de origem ASN/country.
- Preenchimento de credenciais, passagem de caminho, testes SSRF, RCE, acesso ao webshell e ocorrências repetidas de endpoint de login.
- Aplicativos públicos com alto volume de ataques, erros de origem, tentativas de desvio ou nomes de host desprotegidos.

## Uso de caça
- pico de ataque WAF
- Anomalia na pontuação do bot
- Preenchimento de credenciais contra aplicativos públicos

## Coisas de segurança para observar
- O tráfego bloqueado é útil, mas o tráfego bem-sucedido ou desafiado pode mostrar uma investigação que posteriormente contorna os controles.
- As buscas de aplicativos públicos devem comparar a telemetria de borda com os logs origin/app para detectar a exploração após a visibilidade WAF.
- Regras de permissão, regras de página, lógica de trabalho e alterações DNS podem criar exposição se não forem controladas.

## Perguntas úteis sobre caça
- Quais URIs recebem padrões de exploração repetidos de fontes distribuídas?
- Quais fontes ASNs ou países são novos para um aplicativo?
- Quais regras WAF são barulhentas, ignoradas ou protegem endpoints críticos?

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
