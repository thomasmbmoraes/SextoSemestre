# ex 05: analise de uma rede de computadores

grafo = {
    "PC1": ["PC2", "PC3"],
    "PC2": ["PC1", "PC4", "PC5"],
    "PC3": ["PC1"],
    "PC4": ["PC2", "PC5"],
    "PC5": ["PC2", "PC4", "PC6"],
    "PC6": ["PC5"]
}


# funcao para calcular o numero de vertices
def numero_vertices(grafo):
    return len(grafo)


# funcao para calcular o grau de um vertice
def grau(grafo, vertice):
    return len(grafo[vertice])


# funcao para calcular o numero de arestas
def numero_arestas(grafo):
    # em grafo nao direcionado, cada aresta e contada duas vezes
    # |E| = soma dos graus / 2
    return sum(grau(grafo, v) for v in grafo) // 2


# funcao para calcular o grau de todos os vertices
def graus(grafo):
    return {v: grau(grafo, v) for v in grafo}


# funcao para identificar os vertices de maior grau
def vertices_maior_grau(grafo):
    g = graus(grafo)
    maior = max(g.values())
    return [v for v in g if g[v] == maior], maior


# funcao para identificar os vertices isolados
def vertices_isolados(grafo):
    return [v for v in grafo if grau(grafo, v) == 0]


# funcao para verificar se o grafo é conexo
def eh_conectado(grafo):
    """Busca em largura (BFS) a partir de um vértice: o grafo é conexo
    se todos os vértices forem alcançados."""
    if not grafo:
        return True
    inicio = next(iter(grafo))
    visitados = {inicio}
    fila = [inicio]
    while fila:
        atual = fila.pop(0)
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    return len(visitados) == len(grafo)


# teste de execucao
print(f"1. Número de vértices: {numero_vertices(grafo)}")
print(f"2. Número de arestas: {numero_arestas(grafo)}")

print("3. Grau de cada vértice:")
for v, g in graus(grafo).items():
    print(f"     {v}: {g}")

maiores, valor = vertices_maior_grau(grafo)
print(f"4. Vértice(s) com maior grau: {', '.join(maiores)} (grau {valor})")

isolados = vertices_isolados(grafo)
print(f"5. Vértices isolados: {', '.join(isolados) if isolados else 'nenhum'}")

print(f"6. A rede é totalmente conectada? {'Sim' if eh_conectado(grafo) else 'Não'}")