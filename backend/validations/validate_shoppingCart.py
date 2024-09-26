from database.ticket_data import TicketData
from database.route_data import RouteData
from database.flight_data import FlightData
from models.ticket import Ticket
import time

def validateShoppingCart(data_request: dict) -> dict:
    for codVoo, passagens in data_request["ticket_data"].items():
        voo_selecionado = FlightData.retornarVoo(codVoo)
        for assento in passagens.values():
            if int(assento) not in voo_selecionado.assentos.keys():
                return {
                    "status": "error",
                    "message": "Houveram assentos não identificados",
                    "data": {}
                }

            if voo_selecionado.assentos[int(assento)]:
                return {
                    "status": "error",
                    "message": f"O assento de número {assento} do Voo {voo_selecionado.codVoo} se encontra reservado.",
                    "data": {}
                }
    
    for codVoo, passagens in data_request["ticket_data"].items():
        voo_selecionado = FlightData.retornarVoo(codVoo)
        for assento in passagens.values():
            voo_selecionado.reservarAssento(int(assento))
            nova_passagem = Ticket(cpf=data_request["user_data"]["cpf"], voo=voo_selecionado, assento=int(assento))
            time.sleep(0.05)
            TicketData.guardarNoCarrinho(nova_passagem)

    return {
        "status": "sucess",
        "message": "As passagens foram adicionadas ao carrinho",
        "data": {}
    }
        