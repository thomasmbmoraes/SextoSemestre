# ex 01: cadastro de cidades conectadas

grafo = {
    "Centro": ["Norte", "Sul"],
    "Norte": ["Centro", "Leste"],
    "Sul": ["Centro"],
    "Leste": ["Norte"]
}


# funcao pra adicionar um bairro (vertice) ao grafo
def adicionar_bairro(grafo, bairro):
    """Adiciona um novo bairro (vértice) ao grafo."""
    if bairro in grafo:
        print(f"O bairro '{bairro}' já está cadastrado.")
    else:
        grafo[bairro] = []
        print(f"Bairro '{bairro}' adicionado.")


# funcao pra adicionar uma estrada (aresta) entre dois bairros
def adicionar_estrada(grafo, bairro1, bairro2):
    """Adiciona uma estrada (aresta não direcionada) entre dois bairros."""
    if bairro1 not in grafo or bairro2 not in grafo:
        print("Erro: os dois bairros precisam estar cadastrados.")
        return
    if bairro1 == bairro2:
        print("Erro: não é possível ligar um bairro a ele mesmo.")
        return
    if bairro2 in grafo[bairro1]:
        print(f"A estrada {bairro1} <-> {bairro2} já existe.")
        return
    # aresta nao direcionada: registra nos dois sentidos
    grafo[bairro1].append(bairro2)
    grafo[bairro2].append(bairro1)
    print(f"Estrada {bairro1} <-> {bairro2} adicionada.")


# funcao pra exibir todos os bairros cadastrados e suas conexoes
def exibir_bairros(grafo):
    """Exibe todos os bairros cadastrados."""
    print("Bairros cadastrados:")
    for bairro in grafo:
        print(f"  - {bairro}")


# funcao pra exibir os vizinhos de um bairro
def exibir_vizinhos(grafo, bairro):
    """Exibe os bairros vizinhos de um bairro informado."""
    if bairro not in grafo:
        print(f"O bairro '{bairro}' não está cadastrado.")
    elif not grafo[bairro]:
        print(f"O bairro '{bairro}' não possui vizinhos.")
    else:
        print(f"Vizinhos de {bairro}: {', '.join(grafo[bairro])}")


# teste de execucao
exibir_bairros(grafo)
print()

adicionar_bairro(grafo, "Oeste")
adicionar_estrada(grafo, "Oeste", "Centro")
adicionar_estrada(grafo, "Oeste", "Sul")
print()

exibir_bairros(grafo)
print()
bairro = input("Informe um bairro para ver seus vizinhos: ")
exibir_vizinhos(grafo, bairro)