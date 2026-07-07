# Guardicore

## Objetivo
Contexto de segmentação e movimento lateral para tráfego leste-oeste, dependências de aplicativos e aplicação de políticas. O mapeamento Sentinel está pendente.

## Categoria
ZTNA/Segmentation

## Como funciona
- As ferramentas de segmentação observam fluxos entre cargas de trabalho e impõem políticas de comunicação.
- A telemetria pode revelar caminhos internos inesperados que as ferramentas de perímetro nunca veem.
- Use esta página para definir o caminho do conector, o esquema de fluxo, os eventos de política e as tabelas Sentinel, uma vez disponíveis.

## Como esta biblioteca a utiliza
- Mapeia esta ferramenta para as tabelas Sentinel abaixo.
- Usa as tabelas mapeadas para construir caçadas diárias, semanais, intel e mensais.
- Converte descobertas repetidas de alto valor em casos de uso e candidatos à detecção.

## Tabelas Sentinel
- Nenhuma tabela Sentinel confirmada ainda.

## O que revisar
- Nova comunicação entre cargas de trabalho, fluxos leste-oeste negados e violações de políticas.
- RDP, SMB, WinRM, SSH, banco de dados e movimentação de protocolo administrativo entre segmentos incomuns.
- Mudanças nas políticas de segmentação, mudanças no modo de aplicação e exposição de ativos críticos.

## Uso de caça
- Adicionar mapeamento de tabela Sentinel quando o caminho do conector ou do syslog for confirmado

## Coisas de segurança para observar
- O movimento lateral muitas vezes se esconde no tráfego interno se faltar a telemetria leste-oeste.
- Os alertas de segmentação são melhor correlacionados com o contexto do processo de identidade e endpoint.
- Os dados do conector não mapeado devem ser tratados como um item de roteiro para melhores caçadas de movimento lateral.

## Perguntas úteis sobre caça
- Quais hosts iniciaram novos caminhos SMB/RDP/SSH entre segmentos?
- Quais fluxos negados sugerem varredura ou tentativa de movimento lateral?
- Quais servidores críticos possuem caminhos permitidos mais amplos do que o esperado?

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
