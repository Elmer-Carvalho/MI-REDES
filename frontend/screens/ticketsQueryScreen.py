from colorama import init, Fore, Style
from tools import *
import time

def ticketsQueryScreen(server_data: dict) -> dict:
    limpar_tela()
    print(Fore.BLUE + "===SUAS PASSAGENS===")


    if "reserved_ticket" in server_data.keys():
        print(Style.BRIGHT + "--> PASSAGENS COMPRADAS:")

        contador = 1
        for id_passagem, passagem in server_data["reserved_ticket"].items():
            print(Fore.GREEN + f"{contador}ª PASSAGEM:")
            print(Fore.GREEN + f"--ID: {passagem['id']}")
            print(Fore.GREEN + f"--CPF: {passagem['id_cliente']}")
            print(Fore.GREEN + f"--ASSENTO: {passagem['assento']}")
            print(Fore.GREEN + f"--CID. ORIGEM: {passagem['voo']['origem']}")
            print(Fore.GREEN + f"--CID. DESTI.: {passagem['voo']['destino']}")
            print(Fore.GREEN + f"--CÓD. VOO.: {passagem['voo']['codVoo']}")
            print(Fore.GREEN + f"--EMPRESA AÉREA.: {passagem['voo']['empresa_aerea']}")


            print(Fore.GREEN + "\n-------\n")
            contador += 1

    if "cart_ticket" in server_data.keys():
        print(Style.BRIGHT + "--> PASSAGENS NO CARRINHO:")

        contador = 1
        for id_passagem, passagem in server_data["cart_ticket"].items():
            print(Fore.YELLOW + f"{contador}ª PASSAGEM:")
            print(Fore.YELLOW + f"--ID: {passagem['id']}")
            print(Fore.YELLOW + f"--CPF: {passagem['id_cliente']}")
            print(Fore.YELLOW + f"--ASSENTO: {passagem['assento']}")
            print(Fore.YELLOW + f"--CID. ORIGEM: {passagem['voo']['origem']}")
            print(Fore.YELLOW + f"--CID. DESTI.: {passagem['voo']['destino']}")
            print(Fore.YELLOW + f"--CÓD. VOO.: {passagem['voo']['codVoo']}")
            print(Fore.YELLOW + f"--EMPRESA AÉREA.: {passagem['voo']['empresa_aerea']}")


            print(Fore.YELLOW + "\n-------\n")
            contador += 1
    
    if not "reserved_ticket" in server_data.keys() and not "cart_ticket" in server_data.keys():
        print("Atualmente você não possui passagens em sua conta")
    

    while True:
        print(Style.BRIGHT + "CONFIRMAR PASSAGEM  [1]\nCANCELAR PASSAGEM   [2]\nVOLTAR AO MENU      [3]")
        option = input(Style.BRIGHT + "OPÇÃO: ").strip()

        if option != "1" and option != "2" and option != "3":
            print(Fore.RED + "Escolha entre as opções 1, 2 ou 3.")
            continue

        if option == "1":
            if "cart_ticket" in server_data.keys():
                print(Style.BRIGHT + "EX: Se quiser a primeira e a segunda passagem, digite: 1 2.")
                option = input(Style.BRIGHT + "Nº das passagens: ").strip()
                option = option.split()
                
                cart_tickets = server_data["cart_ticket"].keys()
                data = {}
                for index in option:
                    if not index.isnumeric():
                        print(Fore.RED + "Digite apenas números.")
                        continue

                    if int(index) >= len(cart_tickets) or int(index) < 1:
                        print(Fore.RED + "Número de passagem inexistente.")
                        continue
                    
                    data[index] = list(cart_tickets)[int(index) - 1]

                return {"screen": "consult", "request": {"type": "purchaseConfirmed", "data_request": data}}
                ...
            else:
                print(Fore.RED + "Você não possui passagens no carrinho")
                continue

        if option == "2":
            if not "reserved_ticket" in server_data.keys() and not "cart_ticket" in server_data.keys():
                print(Fore.RED + "Atualmente você não possui passagens em sua conta")
                continue
            else:
                print(Style.BRIGHT + "Digite os números das passagens que deseja cancelar no seguinte formato:")
                print(Style.BRIGHT + "1-Número da Passagem -> Para as compradas.")
                print(Style.BRIGHT + "2-Número da Passagem -> Para as do carrinho.")
                option = input(Style.BRIGHT + "CANCELAR: ").strip()
                option = [passagens_canceladas.split("-") for passagens_canceladas in option.split()]
                data = {}

                for passagem in option:
                    if passagem[0] == "1" and "reserved_ticket" in server_data.keys():
                        reserved_tickets = list(server_data["reserved_ticket"].keys())
                        if not passagem[1].isnumeric():
                            print(Fore.RED + "Digite corretamente.")
                            break
                        if int(passagem[1]) >= len(reserved_tickets) or int(passagem[1]) < 1:
                            print(Fore.RED + "Digite corretamente.")
                            break
                        key = "0-" + str(passagem[1])
                        data[key] = reserved_tickets[int(passagem[1]) - 1]
                        
                    elif passagem[0] == "2" and "cart_ticket" in server_data.keys():
                        cart_tickets = list(server_data["cart_ticket"].keys())
                        if not passagem[1].isnumeric():
                            print(Fore.RED + "Digite corretamente.")
                            break
                        if int(passagem[1]) >= len(cart_tickets) or int(passagem[1]) < 1:
                            print(Fore.RED + "Digite corretamente.")
                            break
                        key = "1-" + str(passagem[1])
                        data[key] = cart_tickets[int(passagem[1]) - 1]
                    else:
                        print(Fore.RED + "Digite corretamente.")
                        break
                
                if len(data.keys()) == len(option):
                    return {"screen": "consult", "request": {"type": "cancellationConfirmed", "data_request": data}}

        if option == "3":
            return {"screen": "menu", "request": {}}
