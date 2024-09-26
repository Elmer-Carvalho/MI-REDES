from database.passenger_data import PassengerData
from models.passenger import Passenger


def validateRegistration(data_request: dict) -> dict:
    if not valida_CPF_novo(data_request["cpf"]):
        return {"status": "error", "message": "CPF já cadastrado.", "data": {}}

    if not valida_UserName_novo(data_request["username"]):
        return {"status": "error", "message": "Nome de Usuário já cadastrado.", "data": {}}

    novo_passageiro = Passenger(data_request["cpf"], data_request["username"], data_request["senha"])
    PassengerData.guardarPassageiro(novo_passageiro)
    return {"status": "sucess", "message": "Cadastro realizado com sucesso.", "data": novo_passageiro.to_dict()}

def valida_CPF_novo(cpf: str) -> bool: 
    for key, passageiro in PassengerData.lista_de_passageiros.items():
        if passageiro.cpf == cpf:
            return False
    return True

def valida_UserName_novo(username: str) -> bool:
    if username in PassengerData.lista_de_passageiros:
        return False
    return True
