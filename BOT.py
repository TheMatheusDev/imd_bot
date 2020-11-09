import os
import time
import json
from random import randrange
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import locale
import platform

locale.setlocale(locale.LC_ALL, '')
sistema = platform.system()


def init_web_driver():
    try:
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        if sistema == 'Windows':
            web_driver = webdriver.Firefox(executable_path='geckodriver.exe', capabilities=firefox_capabilities)  # v23
            return web_driver
        else:
            web_driver = webdriver.Firefox(executable_path='geckodriver', capabilities=firefox_capabilities)  # v23
            return web_driver
    except Exception as e:
        print(f'Failed to initialize Geckodriver: {e}')
        try:
            options = webdriver.ChromeOptions()
            chrome_args = ['--log-level=3', '--silent', '--disable-extensions', '--disable-popup-blocking',
                           '--disable-blink-features', '--disable-blink-features=AutomationControlled']
            for arg in chrome_args:
                options.add_argument(arg)
                if sistema == 'Windows':
                    web_driver = webdriver.Chrome('chromedriver.exe', options=options)  # v81.0.4044.69
                    return web_driver
                else:
                    web_driver = webdriver.Chrome('chromedriver', options=options)  # v81.0.4044.69
                    return web_driver
        except Exception as e:
            print(f'Falha ao iniciar Chromedriver: {e}')
            print('Instale/Atualize o seu Firefox/Chrome ou Geckodriver/Chromedriver.')
            time.sleep(5)
            quit()


# Cria o arquivo de configurações na primeira execução
def create_default_files():
    if not (os.path.exists('config.json')):
        data = {
            "login": "",
            "senha": "",
            "website": "TEC",
            "modulo": "Básico"
        }
        with open('config.json', 'w') as config_file:
            json.dump(data, config_file, indent=2)


# Leitor do arquivo de configurações. Lê e retorna o metodo especificado.
def get_config_setting(setting):
    try:
        with open('config.json') as config_file:
            data = json.load(config_file)
            return data[setting]
    except Exception as e:
        print(f'Failed get json setting. Error: {e}')


# Limpa chat
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menu de configurações (A opção 2 do menu principal)
def open_config_menu():
    with open('config.json', 'r+') as config_file:
        data = json.load(config_file)
        while True:
            print(f' 1 - Mudar login [Atual: {data["login"]}]\n',
                  f'2 - Mudar senha [Atual: {data["senha"]}]\n',
                  f'3 - Alternar entre IMDTEC e IMDFIC [Atual: {data["website"]}]\n',
                  f'4 - Alternar entre os módulos Básico e Intermediário [Atual: {data["modulo"]}]\n',
                  f'5 - Apagar todos os parâmetros\n',
                  '0 - Voltar.')
            option_to_config = input('> ')
            cls()

            if option_to_config == '1':
                print('0 - Voltar.')
                login_input = input('Login: ')
                try:
                    if login_input != '':
                        data['login'] = login_input
                        cls()
                    else:
                        cls()
                        print('\nÉ obrigatório preencher o login!\n')
                except Exception:
                    pass

            elif option_to_config == '2':
                print('0 - Voltar.')
                senha_input = input('Senha: ')
                try:
                    if senha_input != '':
                        data['senha'] = senha_input
                        cls()
                    else:
                        cls()
                        print('\nÉ obrigatório preencher a senha!\n')
                except:
                    pass

            elif option_to_config == '3':
                if data['website'] == 'TEC':
                    data['website'] = 'FIC'
                else:
                    data['website'] = 'TEC'

            elif option_to_config == '4':
                if data['modulo'] == 'Básico':
                    data['modulo'] = 'Intermediário'
                else:
                    data['modulo'] = 'Básico'

            elif option_to_config == '5':
                data['login'], data['senha'] = '', ''
                cls()
                print(f'Todos os parâmetros resetados! Login: {data["login"]}; Senha: {data["senha"]}.\n')

            elif option_to_config == '0':
                cls()
                break

            else:
                print('Opção Inválida.\n')

            config_file.seek(0)
            json.dump(data, config_file, indent=2)
            config_file.truncate()


# Configurações pela primeira vez
def config_before_start():
    with open('config.json', 'r+') as config_file:
        data = json.load(config_file)
        while "" in (data['login'], data['senha']):
            print('É obrigatório definir os seguintes parâmetros abaixo:\n\n',
                  f'1 - Definir login [Atual: {data["login"]}]\n',
                  f'2 - Definir senha [Atual: {data["senha"]}]\n',
                  f'3 - Alternar entre IMDTEC e IMDFIC [Atual: {data["website"]}]\n',
                  f'4 - Alternar entre os módulos Básico e Intermediário [Atual: {data["modulo"]}]')
            option_to_config = input('> ')
            cls()
            if option_to_config == '1':
                login_input = input('Login: ')
                data['login'] = login_input
                cls()

            elif option_to_config == '2':
                senha_input = input('Senha: ')
                data['senha'] = senha_input
                cls()

            elif option_to_config == '3':
                if data['website'] == 'TEC':
                    data['website'] = 'FIC'
                else:
                    data['website'] = 'TEC'

            elif option_to_config == '4':
                if data['modulo'] == 'Básico':
                    data['modulo'] = 'Intermediário'
                else:
                    data['modulo'] = 'Básico'

            else:
                print('Opção Inválida.\n')

            config_file.seek(0)
            json.dump(data, config_file, indent=2)
            config_file.truncate()
            continue


def aleatorio(min, max):  # Função para definir qual materia escolher
    num = randrange(min, max)
    return num


class Botoes:
    class Login:
        campo_login = '//*[@class="v-text-field__slot"]//input'
        campo_senha = '//*[@id="input-21"]'
        continue_1 = '//*[@id="app"]/div/main/div/div/div/div[3]/div/div/div[1]/div/div/v-card-action/button/span'
        continue_2 = '//*[@id="app"]/div/main/div/div/div/div[3]/div/div/div[2]/div/div/form/v-card-action/button'
        # Tela de login após errar
        erro_login = '/html/body/div[1]/div[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/form/div[1]/input'
        erro_senha = '//*[@id="password"]'
        erro_botao = '//*[@id="loginbtn"]'

    class Conteudo:
        acessar_conteudo = '//*[@id="app"]/div[2]/nav/div[1]/div/div[3]/a[3]'
        acessar_aula = f'/html/body/div[1]/div[2]/ul/li[{aleatorio(1, 10)}]/div[1]/div/div[2]/a'

        # Módulo Básico
        acessar_materia_b = f'/html/body/div[1]/div[2]/ul/li[{aleatorio(2, 6)}]/div/div/a'

        # Módulo Intermediário
        acessar_materia_i = f'/html/body/div[1]/div[2]/ul/li[{aleatorio(1, 2)}]/div/div/a'


def tela_login(Botoes):
    # Tela de login.
    # Login usuário
    try:
        wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Login.campo_login)))
        browser.find_element_by_xpath(Botoes.Login.campo_login).send_keys(get_config_setting('login'))
        browser.find_element_by_xpath(Botoes.Login.continue_1).click()
    except:
        print('Ocorreu um erro durante o login, por favor tente novamente.')
        pass


def tela_senha(Botoes):
    # Login da senha
    try:
        wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Login.campo_senha)))
        browser.find_element_by_xpath(Botoes.Login.campo_senha).send_keys(get_config_setting('senha'))
        browser.find_element_by_xpath(Botoes.Login.continue_2).click()
    except:
        pass

def erro_login(Botoes):
    try:
        wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Login.erro_login)))
        browser.find_element_by_xpath(Botoes.Login.erro_login).send_keys(get_config_setting('login'))
        browser.find_element_by_xpath(Botoes.Login.erro_senha).send_keys(get_config_setting('senha'))
        browser.find_element_by_xpath(Botoes.Login.erro_botao).click()
    except:
        pass


# Tela principal do IMDTEC (Acesso ao material, Moodle, bugs, etc.)
def material(Botoes):
    # Clica em Material
    wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Conteudo.acessar_conteudo)))
    browser.find_element_by_xpath(Botoes.Conteudo.acessar_conteudo).click()

    # Desce a página
    browser.execute_script("window.scrollBy(0,250)", "")
    # Clica na disciplina aleatoria
    if get_config_setting('modulo') == "Básico":
        wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Conteudo.acessar_materia_b)))
        browser.find_element_by_xpath(Botoes.Conteudo.acessar_materia_b).click()
    else:
        wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Conteudo.acessar_materia_i)))
        browser.find_element_by_xpath(Botoes.Conteudo.acessar_materia_i).click()
    # Clica na aula
    browser.execute_script("window.scrollBy(0,250)", "")
    wait.until(ec.presence_of_element_located((By.XPATH, Botoes.Conteudo.acessar_aula)))
    browser.find_element_by_xpath(Botoes.Conteudo.acessar_aula).click()
    browser.execute_script("window.scrollBy(0,250)", "")


    # Espera entre (3 minutos) e (6 minutos e 30 segundos).
    cls()
    while True:
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(f"Tempo restante na página:", timeformat, end='\r')
                time.sleep(1)
                t -= 1
            cls()
            print('Passando página...')
            time.sleep(1)
            cls()


        countdown(aleatorio(180, 390))
        # Clica no botão de próxima página
        prox = ActionChains(browser)
        try:
            prox.send_keys('d').perform()
            browser.execute_script("window.scrollBy(0,250)", "")
        except:
            prox.send_keys('a').perform()
            browser.execute_script("window.scrollBy(0,250)", "")

if __name__ == "__main__":
    create_default_files()
    browser = Chrome()
    while True:
        option = input('Opções:\n'
                       '1 - Iniciar.\n'
                       '2 - Mudar login, senha e TEC/FIC.\n'
                       '3 - Sair.\n'
                       '> ')
        cls()

        if option == '1':
            if "" in (get_config_setting('login'), get_config_setting('senha')):
                config_before_start()

            login = get_config_setting('login')
            senha = get_config_setting('senha')
            if get_config_setting('website') == 'TEC':
                url = 'https://imdtec.imd.ufrn.br/?login=true'
            else:
                url = 'https://imdfic.imd.ufrn.br/?login=true'
            browser.get(url)

            wait = WebDriverWait(browser, 10)
            tela_login(Botoes)
            tela_senha(Botoes)
            try:
                material(Botoes)
            except:
                erro_login(Botoes)
                material(Botoes)

        elif option == '2':
            cls()
            open_config_menu()

        elif option == '3':
            cls()
            browser.quit()
            exit()
        else:
            print('Opção Inválida\n')
