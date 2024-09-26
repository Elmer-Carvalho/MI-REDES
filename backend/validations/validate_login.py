from database.passenger_data import PassengerData

def validateLogin(data_request: dict) -> dict:
    if data_request["username"] in PassengerData.lista_de_passageiros:
        if PassengerData.lista_de_passageiros[data_request["username"]].senha == data_request["senha"]:
            return {"status": "sucess", "message": "Login realizado com sucesso.", "data": PassengerData.lista_de_passageiros[data_request["username"]].to_dict()}
    return {"status": "error", "message": "Login não foi possível.", "data": {}}
