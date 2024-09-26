from colorama import init, Fore, Style
from tools import limpar_tela
import time

def loginScreen() -> dict:
    while True:
        limpar_tela()
        print(Fore.BLUE + "===LOGIN===")
        username = input(Style.BRIGHT + "USERNAME: ").strip()
        senha = input(Style.BRIGHT + "SENHA: ").strip()

        if not valida_UserName(username):
            print(Fore.RED + "Username Inválido")
            time.sleep(2)
            continue

        if not valida_senha(senha):
            print(Fore.RED + "Senha Inválido")
            time.sleep(2)
            continue
        
        
        return {
                "screen": "menu",
                "request": {"type": "login", "data_request": {"username": username, "senha": senha}},
                "user_data": {}
            }
            


def valida_UserName(username: str) -> bool:
    if not username.replace(" ", "").isalpha():
        return False
    return True

def valida_senha(senha: str) -> bool:
    if len(senha) < 5:
        return False
    return True