import socket
import threading
import json
from database.route_data import RouteData
from controller import filterRequests
from database.ticket_data import TicketData

def handle_client(client_socket):
    """Função para lidar com as mensagens do cliente."""
    while True:
        try:
            # Recebe mensagem do cliente
            message = client_socket.recv(4096).decode('utf-8')
            if not message:
                break

            # Converte a mensagem de JSON para dicionário Python
            data = json.loads(message)
            print(f"[RECEBIDO] {data}")


            response = filterRequests(data)

            # Aqui você pode processar os dados recebidos e enviar uma resposta
            client_socket.send(json.dumps(response).encode('utf-8'))

        except ConnectionResetError:
            print("[ERRO] Conexão foi encerrada pelo cliente.")
            break

    client_socket.close()

def start_server():
    
    #POPULA MEU "BANCO DE DADOS" DE ROTAS E VOOS
    RouteData.criarVoos()

    monitor_cart = threading.Thread(target=TicketData.monitorarLimTempoNoCarrinho, args=(1, 10), daemon=True)
    monitor_cart.start()

    """Função principal para iniciar o servidor."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))  # Servidor vai escutar na porta 5555
    server.listen(8)  # Máximo de 8 conexões em fila
    print("[INFO] Servidor iniciado. Aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"[INFO] Conexão estabelecida com {addr}")

        # Cria uma nova thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()