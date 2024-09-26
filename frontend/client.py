if __name__ == "__main__":
    import socket
    import json
    import time
    from controller import filterScreens
    from tools import *


    def start_client():
        """Função principal para iniciar o cliente."""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("server", 5555))  # Conectando ao servidor na mesma máquina

        state = {"screen": "home"}
        while True:
            
            new_state = filterScreens(state)

            if new_state["request"]:
                client.send(json.dumps(new_state["request"]).encode("utf-8"))

                # Recebe resposta do servidor
                response = client.recv(4096).decode('utf-8')
                server_data = json.loads(response)


                if server_data["status"] == "sucess":
                    if server_data["message"]:
                        goodMessage(server_data["message"])

                    state["server_data"] = server_data["data"]
                    
                    if state["screen"] == "login" or state["screen"] == "register":
                        state["user_data"] = {
                            "cpf": server_data["data"]["cpf"],
                            "username": server_data["data"]["username"],
                            "senha": server_data["data"]["senha"]
                        }

                    state["screen"] = new_state["screen"]


                else:
                    if server_data["message"]:
                        badMessage(server_data["message"])

                    if state["screen"] == "login":
                        state["screen"] = "home"

                    continue

            state["screen"] = new_state["screen"]

start_client()
