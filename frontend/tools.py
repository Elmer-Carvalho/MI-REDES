from colorama import init, Fore, Style
import os
import time

def limpar_tela():
    # Detecta o sistema operacional e executa o comando correto
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e macOS
        os.system('clear')

def goodMessage(message: str):
    print(Fore.GREEN + ">>" + message + "<<")
    time.sleep(2)

def badMessage(message: str):
    print(Fore.RED + ">>" + message + "<<")
    time.sleep(2)


def validar_apenas_alpha(text: str):
    if text.replace(" ", "").isalpha():
        return True
    return False