# ex 02: grau de cada vértice em um grafo

grafo = {
    "Ana": ["Bruno", "Carlos"],
    "Bruno": ["Ana", "Carlos", "Daniel"],
    "Carlos": ["Ana", "Bruno"],
    "Daniel": ["Bruno"]
}


# funcao pra calcular o grau de um vertice
def grau_vertice(grafo, vertice):
    """Retorna o grau do vértice (número de arestas incidentes)."""
    return len(grafo[vertice])


# percorre todos os vertices e exibe o grau de cada um
print("Grau de cada usuário:")
maior_grau = -1
vertice_maior = None

for vertice in grafo:
    g = grau_vertice(grafo, vertice)
    print(f"  {vertice}: {g} amigo(s)")
    # identifica o vértice de maior grau
    if g > maior_grau:
        maior_grau = g
        vertice_maior = vertice

print(f"\nVértice com maior grau: {vertice_maior} (grau {maior_grau})")