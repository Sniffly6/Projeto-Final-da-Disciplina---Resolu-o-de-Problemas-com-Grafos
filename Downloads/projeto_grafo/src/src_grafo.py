from collections import deque
import heapq


class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_aresta(self, origem, destino, peso):

        if origem not in self.adj:
            self.adj[origem] = []

        if destino not in self.adj:
            self.adj[destino] = []

        self.adj[origem].append((destino, peso))
        self.adj[destino].append((origem, peso))

    def bfs(self, inicio):

        visitados = set()
        fila = deque([inicio])

        visitados.add(inicio)

        ordem = []

        while fila:

            atual = fila.popleft()
            ordem.append(atual)

            for vizinho, _ in self.adj[atual]:

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem

    def existe_caminho(self, origem, destino):

        visitados = set()
        fila = deque([origem])

        while fila:

            atual = fila.popleft()

            if atual == destino:
                return True

            if atual not in visitados:

                visitados.add(atual)

                for vizinho, _ in self.adj[atual]:
                    fila.append(vizinho)

        return False

    def dijkstra(self, origem, destino):

        distancias = {
            vertice: float("inf")
            for vertice in self.adj
        }

        anterior = {}

        distancias[origem] = 0

        heap = [(0, origem)]

        while heap:

            distancia_atual, atual = heapq.heappop(heap)

            if atual == destino:
                break

            for vizinho, peso in self.adj[atual]:

                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:

                    distancias[vizinho] = nova_distancia
                    anterior[vizinho] = atual

                    heapq.heappush(
                        heap,
                        (nova_distancia, vizinho)
                    )

        caminho = []

        atual = destino

        while atual in anterior:
            caminho.append(atual)
            atual = anterior[atual]

        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

    def kruskal(self):

        arestas = []

        for origem in self.adj:

            for destino, peso in self.adj[origem]:

                if (destino, origem, peso) not in arestas:
                    arestas.append(
                        (origem, destino, peso)
                    )

        arestas.sort(key=lambda x: x[2])

        pai = {}

        for vertice in self.adj:
            pai[vertice] = vertice

        def find(x):

            if pai[x] != x:
                pai[x] = find(pai[x])

            return pai[x]

        def union(a, b):

            raiz_a = find(a)
            raiz_b = find(b)

            if raiz_a != raiz_b:
                pai[raiz_b] = raiz_a

        arvore = []
        custo_total = 0

        for origem, destino, peso in arestas:

            if find(origem) != find(destino):

                union(origem, destino)

                arvore.append(
                    (origem, destino, peso)
                )

                custo_total += peso

        return arvore, custo_total