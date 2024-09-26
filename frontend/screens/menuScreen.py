from colorama import init, Fore, Style
from tools import limpar_tela
import time


def menuScreen(user_data: dict) -> dict:
    while True:
        limpar_tela()
        print(Fore.BLUE + "===MENU===")
        print(Style.BRIGHT + "PESQUISAR NOVAS PASSAGENS  [1]\nCONSULTAR SUAS PASSAGENS   [2]\nSAIR                       [3]")
        option = input(Style.BRIGHT + "OPÇÃO: ").strip()

        if option != '1' and option != '2' and option != '3':
            print(Fore.RED + "Escolha entre a opção 1, 2 ou 3.")
            time.sleep(2)
            continue

        if option == '1':
            return {"screen": "search", "request": {}}
        
        if option == '2':
            return {
                    "screen": "consult",
                    "request": {"type": "consult", "data_request": {"username": user_data["username"], "cpf": user_data["cpf"]}}
                }

        if option == '3':
            return {"screen": "home", "request": {}}
            



