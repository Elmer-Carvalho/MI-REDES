import random
import threading

class Flight: 
    quant_voos = 0

    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
        self.empresa_aerea = random.choice(["Gol Transportes Aéreos", "LATAM Airlines Group SA", "Azul Brazilian Airlines"])
        self.quant_assentos = 6
        self.quant_assentos_disponiveis = self.quant_assentos
        self.codVoo = Flight.gerarCod(self.empresa_aerea)
        self.assentos = {}
        for index in range(self.quant_assentos):
            reservado = random.randint(0, 1)
            if reservado:
                self.quant_assentos_disponiveis -= 1
            self.assentos[index] = reservado


    def to_dict(self):
        return {
            "origem": self.origem,
            "destino": self.destino,
            "empresa_aerea": self.empresa_aerea,
            "quant_assentos": self.quant_assentos,
            "assentos": self.assentos,
            "codVoo": self.codVoo
        }
    
    def reservarAssento(self, num_assento: int) -> bool:
        voos_lock = threading.Lock()
        with voos_lock:
            if not self.assentos[num_assento]:
                self.assentos[num_assento] = 1
                self.quant_assentos_disponiveis -= 1
                return True
            return False

    def liberarAssento(self, num_assento: int) -> bool:
        if self.assentos[num_assento]:
            self.assentos[num_assento] = 0
            return True
        return False

    @classmethod
    def gerarCod(cls, nomeEmpresa: str) -> str:
        if cls.quant_voos < 10:
            cod_voo = nomeEmpresa[0] + '00'+ str(cls.quant_voos)
        elif cls.quant_voos < 100:
            cod_voo = nomeEmpresa[0] + '0'+ str(cls.quant_voos)
        else:
            cod_voo = nomeEmpresa[0] + str(cls.quant_voos)
            
        cls.quant_voos += 1
        return cod_voo