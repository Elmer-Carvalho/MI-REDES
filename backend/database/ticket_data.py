from models.ticket import Ticket
import time
import datetime

class TicketData:
    lista_de_passagens_confirmadas = {}
    carrinho = {}


    @classmethod
    def monitorarLimTempoNoCarrinho(cls, tempo_limite_em_minutos: int, delay: int):
        while True:
            if cls.carrinho:
                lista_id = list(cls.carrinho.keys())
                for id_passagem in lista_id:
                    data_hora_criado = datetime.datetime.strptime(id_passagem.split("@")[1], "%Y-%m-%d_%H:%M:%S.%f")
                    data_hora_atual = datetime.datetime.now()
                    if (data_hora_atual - data_hora_criado) > datetime.timedelta(minutes=tempo_limite_em_minutos):
                        passagem = cls.carrinho[id_passagem]
                        passagem.voo.liberarAssento(passagem.assento)
                        cls.deletarNoCarrinho(id_passagem)
                        print("[LIBERADO] -", passagem)
            
            time.sleep(delay)



    @classmethod
    def guardarPassagemConfirmadaPorId(cls, id: str):
        cls.lista_de_passagens_confirmadas[id] = cls.carrinho[id]
        cls.deletarNoCarrinho(id)

    @classmethod
    def guardarPassagemConfirmada(cls, passagem: Ticket):
        cls.lista_de_passagens_confirmadas[passagem.id] = passagem
        cls.deletarNoCarrinho(id)
    
    @classmethod
    def deletarPassagemPorID(cls, id):
        if id in cls.lista_de_passagens_confirmadas.keys():
            cls.deletarPassagemConfirmada(id)
        if id in cls.carrinho.keys():
            cls.deletarNoCarrinho(id)
    
    @classmethod
    def retornarPassagemPorID(cls, id):
        if id in cls.lista_de_passagens_confirmadas.keys():
            return cls.lista_de_passagens_confirmadas[id]
        if id in cls.carrinho.keys():
            return cls.carrinho[id]

    @classmethod
    def deletarPassagemConfirmada(cls, id):
        cls.lista_de_passagens_confirmadas.pop(id)


    @classmethod 
    def guardarNoCarrinho(cls, passagem: Ticket):
        cls.carrinho[passagem.id] = passagem
    
    @classmethod
    def deletarNoCarrinho(cls, id: str):
        cls.carrinho.pop(id)

    @classmethod
    def encontrarPassagensConfirmadas(cls, id_passagem: str) -> object:
        return cls.lista_de_passagens_confirmadas[id_passagem]
    
    @classmethod
    def encontrarPassagensNoCarrinho(cls, id_passagem: str) -> object:
        return cls.carrinho[id_passagem]
    
    @classmethod
    def encontrarPassagensDeCliente(cls, cpf: str) -> dict:
        lista_passagens_mantidas = {
            "reserved_ticket": [],
            "cart_ticket": []
        }
        for id_passagem in cls.lista_de_passagens_confirmadas.keys():
            if id_passagem.split("@")[0] == cpf:
                lista_passagens_mantidas["reserved_ticket"].append(cls.lista_de_passagens_confirmadas[id_passagem])
        
        for id_passagem in cls.carrinho.keys():
            if id_passagem.split("@")[0] == cpf:
                lista_passagens_mantidas["cart_ticket"].append(cls.carrinho[id_passagem])
        
        return lista_passagens_mantidas


        
