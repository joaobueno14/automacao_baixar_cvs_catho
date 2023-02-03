Automação feita em Python com o objetivo de baixar vários PDFs da pagina da Catho em série.

Pacotes do Python usados:

Time,
Selenium,
ChromeDriverManager,
Pyautogui,
Clipboard

Como usar:

Por se tratar da primeira versão até aqui, o código não está compilado, então você precisara instalar o Python 64bits e também os pacotes citados a cima.

Etapa 01: com seu editor de código aberto cole suas chaves de login nos campos das variáveis 'EMAIL' e 'LOGIN'

Etapa 02: copie seus links dos CVS da Catho,para ajudar a agilizar você pode usar a extensão 'Copy All URLs' no chrome.

Etapa 03: Na linha 115 do código você vera o comentário 'loop' é nele que você vai colar os links, mas antes você vai precisar concatenar da seguinte maneria: 'navegador.get('seu link ')
sleep(1)'

Etapa 04: Obeserve que temos duas funções declaradas no código, a 'inicio' e 'clicks' a inicio só deve ser chamada no primeiro link, já os demais links seguem a mesma estrutura:

'navegador.get('seu link ')
sleep(1)'

clicks()


