class Passenger:
    
    def __init__(self, cpf: str, username: str, senha: str):
        self.cpf = cpf
        self.username = username
        self.senha = senha
        self.lista_passagens = {}


    def receberPassagem(self, id_passagem: str, passagem):
        self.lista_passagens[id_passagem] = passagem

    def deletarPassagem(self, id_passagem):
        self.lista_passagens.pop(id)

    def verificarPassagensCanceladas(self, lista_de_passagens_mantidas) -> list:
        lista_passagens_canceladas = []
        for id_passagem in self.lista_passagens.keys():
            if id_passagem not in lista_de_passagens_mantidas.keys():
                lista_passagens_canceladas.append(self.lista_passagens[id])
                deletarPassagem(id_passagem)
        
        return lista_passagens_canceladas
    
    def to_dict(self) -> dict:
        return {
            "cpf": self.cpf,
            "username": self.username,
            "senha": self.senha,
            "lista_passagens": {id_passagem: passagem.to_dict() for id_passagem, passagem in self.lista_passagens.items()}
        }