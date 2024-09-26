from database.ticket_data import TicketData
from database.route_data import RouteData
from models.passenger import Passenger
from models.ticket import Ticket


def validateCancellation(data_request: dict) -> dict:
    id_passagens_canceladas = list(data_request.values())
    cpf_do_cliente = id_passagens_canceladas[0].split("@")[0]

    for id in id_passagens_canceladas:
        passagem = TicketData.retornarPassagemPorID(id)
        passagem.voo.liberarAssento(passagem.assento)

        TicketData.deletarPassagemPorID(id)
        
    list_tickets = TicketData.encontrarPassagensDeCliente(cpf_do_cliente)
    
    data = {}
    
    if list_tickets["reserved_ticket"]:
        data["reserved_ticket"] = {reservedTicket.id: reservedTicket.to_dict() for reservedTicket in list_tickets["reserved_ticket"]}
    
    if list_tickets["cart_ticket"]:
        data["cart_ticket"] = {reservedTicket.id: reservedTicket.to_dict() for reservedTicket in list_tickets["cart_ticket"]}

    return {
        "status": "sucess",
        "message": "Passagens Canceladas",
        "data": data
    }