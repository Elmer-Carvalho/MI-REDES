from colorama import init, Fore, Style
from tools import *
import time

def ticketsPurchaseScreen(server_data: dict, user_data: dict) -> dict:
    while True:
        limpar_tela()
        print(Fore.BLUE + "===PASSAGENS DISPONÍVEIS===")
        for index, voo in server_data.items():
            print(Style.BRIGHT + f"...PASSAGEM {int(index) + 1}:")
            print(Style.BRIGHT + f"  De: {voo['origem']} -> Para: {voo['destino']}")
            print(Style.BRIGHT + f"  CÓD do VOO: {voo['codVoo']}")
            print(Style.BRIGHT + f"  EMPRESA: {voo['empresa_aerea']}")
            print(Style.BRIGHT + f"  ASSENTOS DISPONÍVEIS: ", end="")

            for num_assento, estado in voo["assentos"].items():
                if estado != 1:
                    print(num_assento, end=" ")
            print("\n")
        
        
        print(Style.BRIGHT + "ADICIONAR PASSAGENS AO CARRINHO  [1]")
        print(Style.BRIGHT + "VOLTAR AO MENU                   [2]")

        option = ""
        while True:
            option = input(Style.BRIGHT + "OPÇÃO: ").strip()
            if option != "1" and option != "2":
                print(Fore.RED + "Escolha entre a opção 1 ou 2.")
            else:
                break
            
        if option == "1":
            print(Style.BRIGHT + "Pode comprar mais de 1 passagem por Voo. EX: 1-18 3-4-17 6-29.")
            print(Style.BRIGHT + "O exemplo acima significa: 2 passagens do 1 Voo, sendo o assento 1 e assento 18 + 3 passagens do segundo Voo ...")
            passagens = input(Style.BRIGHT + "Digite as passagens que deseja: ").strip()

            if len(passagens.split()) != len(server_data.keys()):
                print(Fore.RED + "Você deve selecionar pelo menos 1 passagem por Voo")
                time.sleep(2)
                continue
            
            lista_de_passagens = [assentos_por_voo.split("-") for assentos_por_voo in passagens.split()]
            data_request = {"user_data": user_data, "ticket_data": {}}
            for index_1 in range(len(lista_de_passagens)):
                passagens = {}
                for index_2 in range(len(lista_de_passagens[index_1])):
                    passagens[index_2] = lista_de_passagens[index_1][index_2]
                
                data_request["ticket_data"][server_data[str(index_1)]['codVoo']] = passagens
            
            return {
                "screen": "menu",
                "request": {"type": "shoppingCart", "data_request": data_request}
            }
        
        return {"screen": "menu", "request": {}}