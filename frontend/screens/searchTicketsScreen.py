from colorama import init, Fore, Style
from tools import limpar_tela, validar_apenas_alpha
import time

def searchTicketsScreen() -> dict:
    while True:
        limpar_tela()
        print(Fore.BLUE + "===PESQUISAR PASSAGEM===")
        origin = input(Style.BRIGHT + "Origem: ").strip()
        destination = input(Style.BRIGHT + "Destino: ").strip()

        if not validar_apenas_alpha(origin):
            print(Fore.RED + "Cidade de Origem Inválida")

        
        if not validar_apenas_alpha(destination):
            print(Fore.RED + "Cidade de Destino Inválida")

        if not validar_apenas_alpha(destination) or not validar_apenas_alpha(origin):
            while True:
                option = input(Style.BRIGHT + "Voltar ao Menu? [S/N] - ").strip().upper()[0]
                if option == "S":
                    return {"screen": "menu", "request": {}}
                if option == "N":
                    break
                continue
            continue
        
        return {
            "screen": "displayTicketsForPurchase",
            "request": {"type": "search", "data_request": {"origin": origin, "destination": destination}}
        }
