from models.flight import Flight
from database.flight_data import FlightData
import heapq

class RouteData:
    trechos_aereos = {
        "Rio Branco": {
            "Manaus": {"distância": 555, "tempo": 1.5},
            "Brasília": {"distância": 2_830, "tempo": 6},
            "Porto Velho": {"distância": 500, "tempo": 1.3}
        },
        "Maceió": {
            "Recife": {"distância": 260, "tempo": 0.5},
            "Salvador": {"distância": 500, "tempo": 1.2},
            "Brasília": {"distância": 1_650, "tempo": 3.5}
        },
        "Macapá": {
            "Belém": {"distância": 260, "tempo": 0.6},
            "Manaus": {"distância": 1_300, "tempo": 2.5}
        },
        "Manaus": {
            "Rio Branco": {"distância": 555, "tempo": 1.5},
            "Macapá": {"distância": 1_300, "tempo": 2.5},
            "Brasília": {"distância": 2_500, "tempo": 5},
            "São Paulo": {"distância": 3_600, "tempo": 6.5}
        },
        "Salvador": {
            "Maceió": {"distância": 500, "tempo": 1.2},
            "Recife": {"distância": 200, "tempo": 0.5},
            "Belo Horizonte": {"distância": 600, "tempo": 1.5},
            "Brasília": {"distância": 1_100, "tempo": 2},
            "Feira de Santana": {"distância": 100, "tempo": 0.3}
        },
        "Fortaleza": {
            "Natal": {"distância": 280, "tempo": 0.7},
            "João Pessoa": {"distância": 400, "tempo": 1},
            "Brasília": {"distância": 1_600, "tempo": 3.5},
            "Salvador": {"distância": 1_000, "tempo": 2}
        },
        "Brasília": {
            "Rio de Janeiro": {"distância": 930, "tempo": 2},
            "São Paulo": {"distância": 1_000, "tempo": 2},
            "Belo Horizonte": {"distância": 740, "tempo": 1.5},
            "Salvador": {"distância": 1_100, "tempo": 2},
            "Fortaleza": {"distância": 1_600, "tempo": 3.5},
            "Goiânia": {"distância": 210, "tempo": 0.5}
        },
        "Vitória": {
            "Belo Horizonte": {"distância": 500, "tempo": 1.2},
            "Rio de Janeiro": {"distância": 400, "tempo": 1},
            "São Paulo": {"distância": 800, "tempo": 1.5}
        },
        "Goiânia": {
            "Brasília": {"distância": 210, "tempo": 0.5},
            "Belo Horizonte": {"distância": 560, "tempo": 1.5},
            "São Paulo": {"distância": 1_000, "tempo": 2},
            "Palmas": {"distância": 800, "tempo": 1.5}
        },
        "São Luís": {
            "Belém": {"distância": 560, "tempo": 1.3},
            "Teresina": {"distância": 300, "tempo": 0.8}
        },
        "Cuiabá": {
            "Campo Grande": {"distância": 690, "tempo": 1.5},
            "Brasília": {"distância": 1_400, "tempo": 3},
            "Goiânia": {"distância": 800, "tempo": 2}
        },
        "Campo Grande": {
            "Cuiabá": {"distância": 690, "tempo": 1.5},
            "São Paulo": {"distância": 1_000, "tempo": 2.5},
            "Brasília": {"distância": 1_000, "tempo": 2},
            "Curitiba": {"distância": 800, "tempo": 1.8}
        },
        "Belo Horizonte": {
            "Vitória": {"distância": 500, "tempo": 1.2},
            "Salvador": {"distância": 600, "tempo": 1.5},
            "Brasília": {"distância": 740, "tempo": 1.5},
            "Goiânia": {"distância": 560, "tempo": 1.5},
            "Uberlândia": {"distância": 540, "tempo": 1.2}
        },
        "Belém": {
            "Macapá": {"distância": 260, "tempo": 0.6},
            "São Luís": {"distância": 560, "tempo": 1.3},
            "Brasília": {"distância": 2_200, "tempo": 4.5}
        },
        "João Pessoa": {
            "Natal": {"distância": 400, "tempo": 1},
            "Recife": {"distância": 120, "tempo": 0.3},
            "Brasília": {"distância": 1_500, "tempo": 3}
        },
        "Curitiba": {
            "São Paulo": {"distância": 400, "tempo": 1},
            "Belo Horizonte": {"distância": 600, "tempo": 1.5},
            "Florianópolis": {"distância": 300, "tempo": 0.8},
            "Porto Alegre": {"distância": 700, "tempo": 1.5}
        },
        "Recife": {
            "Maceió": {"distância": 260, "tempo": 0.5},
            "João Pessoa": {"distância": 120, "tempo": 0.3},
            "Salvador": {"distância": 200, "tempo": 0.5},
            "Fortaleza": {"distância": 800, "tempo": 1.7}
        },
        "Teresina": {
            "São Luís": {"distância": 300, "tempo": 0.8},
            "Fortaleza": {"distância": 540, "tempo": 1.2}
        },
        "Rio de Janeiro": {
            "São Paulo": {"distância": 360, "tempo": 1},
            "Brasília": {"distância": 930, "tempo": 2},
            "Belo Horizonte": {"distância": 400, "tempo": 1},
            "Vitória": {"distância": 400, "tempo": 1}
        },
        "Natal": {
            "Fortaleza": {"distância": 280, "tempo": 0.7},
            "João Pessoa": {"distância": 400, "tempo": 1},
            "Brasília": {"distância": 1_600, "tempo": 3.5},
            "Recife": {"distância": 300, "tempo": 0.7}
        },
        "Porto Alegre": {
            "Curitiba": {"distância": 700, "tempo": 1.5},
            "São Paulo": {"distância": 1_100, "tempo": 2},
            "Belo Horizonte": {"distância": 1_400, "tempo": 2.5}
        },
        "Porto Velho": {
            "Rio Branco": {"distância": 500, "tempo": 1.3},
            "Brasília": {"distância": 2_000, "tempo": 4},
            "Manaus": {"distância": 760, "tempo": 1.8}
        },
        "Boa Vista": {
            "Manaus": {"distância": 700, "tempo": 1.5},
            "Macapá": {"distância": 1_100, "tempo": 2}
        },
        "Florianópolis": {
            "Curitiba": {"distância": 300, "tempo": 0.8},
            "São Paulo": {"distância": 500, "tempo": 1.2},
            "Porto Alegre": {"distância": 500, "tempo": 1.2}
        },
        "São Paulo": {
            "Rio de Janeiro": {"distância": 360, "tempo": 1},
            "Brasília": {"distância": 1_000, "tempo": 2},
            "Curitiba": {"distância": 400, "tempo": 1},
            "Manaus": {"distância": 3_600, "tempo": 6.5},
            "Campinas": {"distância": 90, "tempo": 0.3},
            "Ribeirão Preto": {"distância": 313, "tempo": 1.1}
        },
        "Aracaju": {
            "Salvador": {"distância": 350, "tempo": 1},
            "Brasília": {"distância": 1_300, "tempo": 3},
            "Maceió": {"distância": 294, "tempo": 1}
        },
        "Palmas": {
            "Goiânia": {"distância": 800, "tempo": 1.5},
            "Brasília": {"distância": 1_200, "tempo": 2.5}
        },
        "Campinas": {
            "São Paulo": {"distância": 90, "tempo": 0.3},
            "Ribeirão Preto": {"distância": 313, "tempo": 1.1},
            "Curitiba": {"distância": 400, "tempo": 1.2}
        },
        "Uberlândia": {
            "Brasília": {"distância": 420, "tempo": 1},
            "Belo Horizonte": {"distância": 540, "tempo": 1.2},
            "São Paulo": {"distância": 600, "tempo": 1.3}
        },
        "Ribeirão Preto": {
            "São Paulo": {"distância": 313, "tempo": 1.1},
            "Campinas": {"distância": 313, "tempo": 1.1},
            "Curitiba": {"distância": 620, "tempo": 1.5}
        },
        "Feira de Santana": {
            "Salvador": {"distância": 100, "tempo": 0.3},
            "Recife": {"distância": 834, "tempo": 2},
            "Brasília": {"distância": 1_356, "tempo": 3}
        },
        "Maringá": {
            "Curitiba": {"distância": 440, "tempo": 1},
            "São Paulo": {"distância": 610, "tempo": 1.3},
            "Brasília": {"distância": 1_200, "tempo": 2.5}
        },
        "Londrina": {
            "Curitiba": {"distância": 380, "tempo": 1},
            "São Paulo": {"distância": 490, "tempo": 1.2},
            "Brasília": {"distância": 1_090, "tempo": 2.3}
        }
    }
 
    @classmethod
    def criarVoos(cls):
        for origem, value in cls.trechos_aereos.items():
            for destino, dados in value.items():
                novo_voo = Flight(origem, destino)
                dados["voo"] = novo_voo
                FlightData.armazenarVoo(novo_voo)

        
    
    @classmethod
    def encontrar_menor_trajeto(cls, origem, destino):
        # Inicialização do dicionário de distâncias
        distancias = {cidade: float('inf') for cidade in cls.trechos_aereos}
        distancias[origem] = 0
        
        # Inicialização da fila de prioridade
        fila_prioridade = [(0, origem, [])]  # (distância_acumulada, cidade_atual, caminho_percorrido)
        
        while fila_prioridade:
            # Obtemos a cidade com a menor distância acumulada
            distancia_atual, cidade_atual, caminho_atual = heapq.heappop(fila_prioridade)
            
            # Se já chegamos ao destino, retornamos o caminho
            if cidade_atual == destino:
                caminho_atual.append((cidade_atual, distancia_atual))
                return caminho_atual
            
            # Evitar loops, continuamos se já encontramos uma distância menor anteriormente
            if distancia_atual > distancias[cidade_atual]:
                continue
            
            # Verificamos os vizinhos da cidade atual
            for cidade_vizinha, dados in cls.trechos_aereos[cidade_atual].items():
                distancia_vizinha = dados['distância']
                nova_distancia = distancia_atual + distancia_vizinha
                
                voo = dados["voo"]
                
                # Verificar se o voo tem assentos disponíveis
                if voo.quant_assentos_disponiveis > 0:
                    # Se a nova distância for menor, atualizamos e adicionamos à fila
                    if nova_distancia < distancias[cidade_vizinha]:
                        distancias[cidade_vizinha] = nova_distancia
                        novo_caminho = caminho_atual + [(cidade_atual, distancia_atual, voo.codVoo)]
                        heapq.heappush(fila_prioridade, (nova_distancia, cidade_vizinha, novo_caminho))
        
        # Se não há caminho possível
        return None


