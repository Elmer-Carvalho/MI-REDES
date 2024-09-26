from database.ticket_data import TicketData
from models.ticket import Ticket

def validateTicketQuery(data_request: dict) -> dict:
    list_tickets = TicketData.encontrarPassagensDeCliente(data_request["cpf"])

    if not list_tickets["reserved_ticket"] and not list_tickets["cart_ticket"]:
        return {
            "status": "error",
            "message": "Você não tem passagens reservadas",
            "data": {}
        }

    data = {}
    
    if list_tickets["reserved_ticket"]:
        data["reserved_ticket"] = {reservedTicket.id: reservedTicket.to_dict() for reservedTicket in list_tickets["reserved_ticket"]}
    
    if list_tickets["cart_ticket"]:
        data["cart_ticket"] = {reservedTicket.id: reservedTicket.to_dict() for reservedTicket in list_tickets["cart_ticket"]}

    return {
        "status": "sucess",
        "message": "",
        "data": data
    }