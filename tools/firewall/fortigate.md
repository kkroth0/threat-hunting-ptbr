# Fortigate

## Objetivo
Firewall de rede e telemetria VPN para acesso ao perímetro, aplicação de políticas, eventos UTM e visibilidade de tráfego.

## Categoria
Firewall

## Como funciona
- Os eventos de firewall geralmente chegam em CommonSecurityLog ou Syslog, dependendo do caminho do conector.
- Os campos Política, ação, origem, destino, porta, NAT, VPN e URL são essenciais para a caça.
- Os dados do firewall ficam muito mais fortes quando combinados com informações de identidade, endpoint, Cloudflare, Netskope e ameaças.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)
- [Syslog](../../sentinel/tables/reference/Syslog.md)

## O que revisar
- Falhas de login VPN, logins bem-sucedidos após falhas, novos países e atividade do portal de administração.
- Picos de tráfego negados, verificações internas repetidas, portas de saída incomuns e acompanhamento de políticas.
- Tráfego para IPs/domains malicioso conhecido, destinos recentemente observados e padrões de comando e controle.

## Uso de caça
- Pico de tráfego negado
- Anomalia de conexão de saída
- Correlação IP maliciosa

## Coisas de segurança para observar
- VPN e administração de firewall são alvos comuns de acesso inicial.
- As regras de permissão de saída podem ocultar a exfiltração ou o tunelamento se apenas o tráfego de entrada for revisado.
- A qualidade do analisador é importante: os campos usuário de origem, origem IP, destino, ação e política devem ser confiáveis.

## Perguntas úteis sobre caça
- Quais usuários VPN falharam repetidamente e tiveram sucesso?
- Quais hosts internos conversam com portos ou países externos raros?
- Quais eventos de negação indicam varredura, tentativas de exploração ou exposição mal configurada?

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
