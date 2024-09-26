from models.passenger import Passenger

class PassengerData:
    lista_de_passageiros = {}

    @classmethod
    def guardarPassageiro(cls, passageiro: Passenger):
        cls.lista_de_passageiros[passageiro.username] = passageiro

    @classmethod
    def deletarPassageiro(cls, cpf):
        cls.lista_de_passageiros.pop(passageiro.username)






