import csv

from src_grafo import Grafo


def carregar_grafo(arquivo):

    grafo = Grafo()

    with open(
        arquivo,
        encoding="utf-8"
    ) as csvfile:

        leitor = csv.DictReader(csvfile)

        for linha in leitor:

            origem = linha["origem"]
            destino = linha["destino"]
            distancia = int(linha["distancia"])

            grafo.adicionar_aresta(
                origem,
                destino,
                distancia
            )

    return grafo


def main():

    grafo = carregar_grafo(
        "../dados/estradas.csv"
    )

    print("=" * 50)
    print("BUSCA EM LARGURA (BFS)")
    print("=" * 50)

    bfs = grafo.bfs("Jundiai")

    print("Ordem de visita:")
    print(bfs)

    print()

    print("=" * 50)
    print("VERIFICAÇÃO DE CONECTIVIDADE")
    print("=" * 50)

    conectado = grafo.existe_caminho(
        "Jundiai",
        "Ribeirao Preto"
    )

    print(
        "Existe caminho entre Jundiai e Ribeirao Preto?",
        conectado
    )

    print()

    print("=" * 50)
    print("DIJKSTRA")
    print("=" * 50)

    caminho, distancia = grafo.dijkstra(
        "Jundiai",
        "Santos"
    )

    print("Menor caminho:")
    print(" -> ".join(caminho))

    print(
        f"Distância total: {distancia} km"
    )

    print()

    print("=" * 50)
    print("KRUSKAL (AGM)")
    print("=" * 50)

    arvore, custo = grafo.kruskal()

    for origem, destino, peso in arvore:
        print(
            f"{origem} - {destino}: {peso} km"
        )

    print()
    print(
        f"Custo total da AGM: {custo} km"
    )


if __name__ == "__main__":
    main()