Padrões de Nomes de Funções
Nomes Claros e Descritivos: O nome de uma função deve ser descritivo o suficiente para indicar sua finalidade ou o que ela faz. Por exemplo, calcular_area_circulo é mais descritivo do que simplesmente area.

Letras Minúsculas com Sublinhados: Funções em Python devem ser nomeadas usando letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade. Este estilo é algumas vezes referido como snake_case. Por exemplo, carregar_dados_usuario é um bom exemplo.

Evitar Nomes Genéricos: Nomes como processo, executar, ou fazer_algo são muito genéricos e não fornecem informações suficientes sobre o que a função faz. Prefira nomes que ofereçam um nível adequado de detalhe.

Evitar Abreviações Obscuras: Embora abreviações possam encurtar o nome de uma função, elas podem tornar o código menos acessível para outros desenvolvedores. Por exemplo, calc_media_notas é preferível a cmn.

Prefixos com Verbo: Muitas vezes, funções realizam ações, então é útil iniciar o nome da função com um verbo que descreve essa ação, como obter_, calcular_, processar_, validar_ ou limpar_.

Na Python, a tipagem de funções é facilitada pelo uso de "Type Hints" (Dicas de Tipo), uma característica introduzida no Python 3.5 através do PEP 484. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.