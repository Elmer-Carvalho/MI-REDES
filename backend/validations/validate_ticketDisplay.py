from database.route_data import RouteData

def validateTicketDisplay(data_request: dict) -> dict:
    if data_request["origin"] not in RouteData.trechos_aereos.keys():
        return {
            "status": "error",
            "message": f"A cidade {data_request['origin']} não foi encontrada",
            "data": {}
        }
    
    if data_request["destination"] not in RouteData.trechos_aereos.keys():
        return {
            "status": "error",
            "message": f"A cidade {data_request['destination']} não foi encontrada",
            "data": {}
        }

    trajeto = RouteData.encontrar_menor_trajeto(data_request["origin"], data_request["destination"])

    if trajeto:
        rotas = {}
        for i in range(len(trajeto) - 1):
            cidade_atual = trajeto[i][0]
            cidade_proxima = trajeto[i+1][0]

            rotas[i] = RouteData.trechos_aereos[cidade_atual][cidade_proxima]["voo"].to_dict()

        return {
            "status": "sucess",
            "message": "",
            "data": rotas
        }
    
    return {
        "status": "error",
        "message": "Não há rota disponível",
        "data": {}
    }