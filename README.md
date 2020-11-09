# IMD BOT
Automatizando sua nota do IMD TEC/FIC.

## Requesitos
* Um dos navegadores a seguir:
  * [Chrome](https://www.google.com/chrome/)
  * [Firefox](https://www.mozilla.org/firefox/new/)
  
## Utilização
### Windows
1. [Download](https://github.com/TheusKhan/imd_bot/archive/master.zip).
2. Extraia.
3. [Configure](#configurando/atualizando-o-chromedriver/geckodriver)  o webdriver.
4. Execute `run.bat`.
5. ["Iniciar"](#menu)

### Linux
1. [Download](https://github.com/TheusKhan/imd_bot/archive/master.zip).
2. [Configure](#configurando/atualizando-o-chromedriver/geckodriver)  o webdriver.
3. Extraia o BOT.
4. Execute `$ pip install -r requirements.txt` na pasta do BOT.
5. Execute `$ python BOT.py`.
6. ["Iniciar"](#menu)

* Caso o navegador abra e feche:
  * Atualize o navegador instalado chrome/firefox e
  * [Atualize](#configurando/atualizando-o-chromedriver/geckodriver)  o webdriver.

## Configurando/atualizando o Chromedriver/Geckodriver
* Qual devo utilizar?
  * Caso você utilize o Chrome, use o chromedriver.
  * Caso você utilize o Firefox, use o geckodriver.

1. Decida qual navegador irá utilizar.
2. Verifique a versão do seu navegador.
  2.1 Caso utilize o Chrome, digite na barra de pesquisa: `chrome://version`
  2.2 Caso utilize o Firefox, verifique em: `Menu>Ajuda>Sobre o Firefox`
2. Acesse o site do [chromedriver](https://chromedriver.chromium.org/downloads)/[geckodriver](https://github.com/mozilla/geckodriver/releases) e baixe a versão correspondente ao do seu navegador.
3. Se vier compactado, descompacte.
3. Adicionar o driver ao path do sistema.
3.1 Linux - colocar no path do sistema.
3.2 Windows - colocar o .exe dentro da pasta do BOT é o suficiente.
## Menu
* Iniciar - Irá iniciar e será necessário definir um login e senha na primeira execução.
* [Mudar login, senha e TEC/FIC](#configurações) - As configurações do BOT.
* Sair - Irá fechar tudo e sair.

## Configurações
* Login - É possível mudar o login.
* Senha - É possível mudar a senha.
* Alternar entre IMD TEC ou IMD FIC - Alterna entre os cursos suportados do BOT. O curso TEC é o padrão. (Não há garantia que funcione corretamente no FIC mas deve ter algum suporte!)
* Alternar entre os módulos Básico e Intermediário. - Alterna entre os módulos do curso TEC (Recomendado o Básico para caso queira utilizar o FIC!)
* Apagar todos os parâmetros - Limpa o login e senha.

## Nota
Esse BOT faz parte de um projeto de aprendizado de programação. Erros, bugs e códigos mal escritos podem fazer parte. No entanto, a funcionalidade primária é garantida.

A base e ideia da criação surgiram a partir de uma antiga versão de um [BOT de Stopots](https://github.com/Lucas8x/stopots-bot) do [Lucas8x](https://github.com/Lucas8x/).
Um muito obrigado!