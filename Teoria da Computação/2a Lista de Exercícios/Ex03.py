# ex 03: construcao da matriz de adjacência

# armazena os veertices em uma linha
vertices = ["A", "B", "C", "D"]
arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]

n = len(vertices)

# matriz quadrada n x n inicializada com zeros
matriz = [[0] * n for _ in range(n)]

# preenchimento (grafo não direcionado -> matriz simétrica)
for origem, destino in arestas:
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1
    matriz[j][i] = 1

# exibição formatada
print("Matriz de Adjacência:\n")
print("    " + "  ".join(vertices))
for i, linha in enumerate(matriz):
    print(f"{vertices[i]} | " + "  ".join(str(v) for v in linha))