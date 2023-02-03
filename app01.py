from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
import clipboard



servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico) 



#Declarando funções


# Abrir link dos cadidatos

def inicio():


    nome = navegador.find_element('xpath','/html/body/div[1]/div/div[2]/table/tbody/tr[2]/td[1]').text
   

    nome = nome.split(' (')[
        0
    ]
    
    clipboard.copy(nome)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

    pyautogui.click(993,203,duration=1)
    sleep(2)
    pyautogui.click(1087,215,duration=1)
    sleep(1)
    pyautogui.click(1088,271,duration=1)
    sleep(1)
    pyautogui.click(1109,894,duration=1)
    sleep(1)
    pyautogui.click(147,253,duration=1)
    sleep(1)
    pyautogui.click(867,243,duration=1)
    sleep(10)


def clicks():


    nome = navegador.find_element('xpath','/html/body/div[1]/div/div[2]/table/tbody/tr[2]/td[1]').text
   

    nome = nome.split(' (')[
        0
    ]
    
    clipboard.copy(nome)
    
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')

    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')
    
    pyautogui.click(993,203,)
    sleep(2)

    pyautogui.click(1098,896,)
    sleep(1)
    
    pyautogui.doubleClick(256,473,)
    
    sleep(1)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')

    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

    sleep(1)
    

    
    pyautogui.click(781,568,)
    


#Inicio da automação


# Abrir pagina Catho.  
navegador.get('https://seguro.catho.com.br/signin/?layout=b2b')
sleep(3)

# Preencher dados de login 

navegador.find_element('xpath','//*[@id="__next"]/div/main/div/div/div/div/article/div[1]/form/div[1]/div/input').send_keys('caroline.pistore@edesoft.com.br')
sleep(1)

PASSWORD = "3_.fh#u&_%,A7-A&"

navegador.find_element('xpath','//*[@id="__next"]/div/main/div/div/div/div/article/div[1]/form/div[2]/div/input').send_keys(PASSWORD)
sleep(5)    

# Clicar no botão de entrar 
navegador.find_element('xpath','//*[@id="__next"]/div/main/div/div/div/div/article/div[1]/form/button').click()
sleep(7)

# Loop







navegador.get('https://www.catho.com.br/index.php/curriculo/imprimir/?cur_id[]=30947144&vag_id=21123405&usr_id[]=27467153&perfil_id[]=1&status=filtrados&viewEmail=true&origem=area_recrutador')
sleep(1)

inicio()
navegador.get('https://www.catho.com.br/index.php/curriculo/imprimir/?cur_id[]=12005549&vag_id=21123405&usr_id[]=14200833&perfil_id[]=1&status=filtrados&viewEmail=true&origem=area_recrutador')
sleep(1)

clicks()
navegador.get('https://www.catho.com.br/index.php/curriculo/imprimir/?cur_id[]=9339408&vag_id=21123405&usr_id[]=11453727&perfil_id[]=1&status=filtrados&viewEmail=true&origem=area_recrutador')
sleep(1)

clicks()


