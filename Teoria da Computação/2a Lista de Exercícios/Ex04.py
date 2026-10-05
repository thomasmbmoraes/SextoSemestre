# ex 04: sistema de rotas com grafos ponderados

grafo = {
    "Ribeirão Preto": {
        "Sertãozinho": 20,
        "Cravinhos": 18
    },
    "Sertãozinho": {
        "Ribeirão Preto": 20,
        "Barrinha": 12
    },
    "Cravinhos": {
        "Ribeirão Preto": 18
    }
}

# funcao para adicionar uma cidade
def adicionar_cidade(grafo, cidade):
    if cidade not in grafo:
        grafo[cidade] = {}
        print(f"Cidade '{cidade}' adicionada.")

# funcao para adicionar uma rota com distância
def adicionar_rota(grafo, origem, destino, distancia):
    if origem not in grafo:
        adicionar_cidade(grafo, origem)
    if destino not in grafo:
        adicionar_cidade(grafo, destino)
        
    grafo[origem][destino] = distancia
    grafo[destino][origem] = distancia
    print(f"Rota entre '{origem}' e '{destino}' adicionada ({distancia} km).")

# funcao para consultar a distância entre duas cidades
def consultar_distancia(grafo, cidade1, cidade2):
    if cidade1 in grafo and cidade2 in grafo[cidade1]:
        print(f"A distância entre '{cidade1}' e '{cidade2}' é de {grafo[cidade1][cidade2]} km.")
    else:
        print(f"Não existe rota direta entre '{cidade1}' e '{cidade2}'.")

# funcao para exibir todas as rotas cadastradas
def exibir_rotas(grafo):
    print("\n--- Rotas Cadastradas ---")
    rotas_exibidas = set()
    for origem in grafo:
        for destino, distancia in grafo[origem].items():
            pair = tuple(sorted([origem, destino]))
            if pair not in rotas_exibidas:
                print(f"{origem} <---> {destino}: {distancia} km")
                rotas_exibidas.add(pair)

# teste de execucao
adicionar_rota(grafo, "Barrinha", "Sertãozinho", 12)
consultar_distancia(grafo, "Ribeirão Preto", "Sertãozinho")
consultar_distancia(grafo, "Ribeirão Preto", "Barrinha")
exibir_rotas(grafo)