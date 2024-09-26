from colorama import init, Fore, Style
from tools import limpar_tela
import time

def homeScreen() -> dict:
    # Inicializa o colorama
    init(autoreset=True)

    while True:
        limpar_tela()
        print(Fore.BLUE + "===SISTEMA DE COMPRAS DE PASSAGENS===")
        print(Style.BRIGHT + "\n..LOGIN    [1]\n..CADASTRO [2]")
        option = input(Style.BRIGHT + "OPÇÃO: ").strip()

        if option != '1' and option != '2':
            print(Fore.RED + "Escolha entre a opção 1 ou opção 2!")
            time.sleep(2)
            continue

        if option == '1':
            return {"screen": "login", "request": "", "user_data": {}}
        return {"screen": "register", "request": "", "user_data": {}}
        



