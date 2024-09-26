from models.flight import Flight
from datetime import datetime


class Ticket:

    def __init__(self, cpf: str, voo: Flight, assento: int):
        self.id = cpf + f"@{datetime.now()}".replace(" ", "_")
        self.id_cliente = cpf
        self.voo = voo
        self.assento = assento

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "voo": self.voo.to_dict(),
            "assento": self.assento
        }
    
