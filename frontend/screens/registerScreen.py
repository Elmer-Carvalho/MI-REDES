from colorama import init, Fore, Style
from tools import limpar_tela
import time

def registerScreen() -> dict:
    while True:
        limpar_tela()
        print(Fore.BLUE + "===CADASTRO===")
        cpf = input(Style.BRIGHT + "CPF: ").strip()
        username = input(Style.BRIGHT + "USERNAME: ").strip()
        senha = input(Style.BRIGHT + "SENHA: ").strip()

        if not valida_CPF(cpf):
            print(Fore.RED + "CPF Inválido")
            time.sleep(2)
            continue
        
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
                "request": {"type": "register", "data_request": {"cpf": cpf, "username": username, "senha": senha}}
        }


def valida_UserName(username: str) -> bool:
    if not username.replace(" ", "").isalpha():
        return False
    return True

def valida_senha(senha: str) -> bool:
    if len(senha) < 5:
        return False
    return True

def valida_CPF(cpf: str) -> bool:
    if len(cpf) < 11 or not cpf.isnumeric():
        return False
    return True