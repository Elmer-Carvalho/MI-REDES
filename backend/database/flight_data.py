from models.flight import Flight

class FlightData():
    lista_de_voos = {}

    @classmethod
    def armazenarVoo(cls, voo: Flight):
        cls.lista_de_voos[voo.codVoo] = voo

    @classmethod
    def retornarVoo(cls, codVoo: str) -> Flight:
        return cls.lista_de_voos[codVoo]