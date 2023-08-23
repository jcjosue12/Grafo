import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice_origen, vertice_destino):
        self.grafo[vertice_origen].append(vertice_destino)
        self.grafo[vertice_destino].append(vertice_origen)

    def DFS(self, vertice, visitados):
        visitados.add(vertice)
        print(vertice, end=" ")

        for vecino in self.grafo[vertice]:
            if vecino not in visitados:
                self.DFS(vecino, visitados)

    def BFS(self, vertice):
        visitados = set()
        cola = [vertice]

        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.add(actual)
                print(actual, end=" ")
                cola.extend(vecino for vecino in self.grafo[actual] if vecino not in visitados)

    def mostrar_grafo(self):
        G = nx.Graph()
        for vertice, vecinos in self.grafo.items():
            for vecino in vecinos:
                G.add_edge(vertice, vecino)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    grafo = Grafo()

    num_nodos = int(input("Ingrese el número de nodos: "))
    for i in range(num_nodos):
        grafo.agregar_vertice(i)

    num_aristas = int(input("Ingrese el número de aristas: "))
    for _ in range(num_aristas):
        origen, destino = map(int, input("Ingrese arista (origen destino): ").split())
        grafo.agregar_arista(origen, destino)

    nodo_inicio = int(input("Ingrese el nodo de inicio para el recorrido: "))

    print("\nRecorrido DFS:")
    grafo.DFS(nodo_inicio, set())

    print("\nRecorrido BFS:")
    grafo.BFS(nodo_inicio)

    print("\nMostrando grafo:")
    grafo.mostrar_grafo()
