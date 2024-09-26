from database.ticket_data import TicketData

def validatePurchase(data_request: dict) -> dict:
    ids_passagens_compradas = list(data_request.values())
    for id in ids_passagens_compradas:
        TicketData.guardarPassagemConfirmadaPorId(id)
    
    cpf_do_cliente = ids_passagens_compradas[0].split("@")[0]
    list_tickets = TicketData.encontrarPassagensDeCliente(cpf_do_cliente)
    
    
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
        "message": "Passagens Compradas",
        "data": data
    }