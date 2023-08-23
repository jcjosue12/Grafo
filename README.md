# Grafo
Programa para matemáticas discretas 
Explicación 
Importar bibliotecas:

    import networkx as nx
    import matplotlib.pyplot as plt
//Aquí estamos importando las bibliotecas `networkxnetworkxy matplotlib.pyplot, que se utilizarán para crear y mostrar el gráfico.//

Definición de la clase Grafo:

    class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice_origen, vertice_destino):
        self.grafo[vertice_origen].append(vertice_destino)
        self.grafo[vertice_destino].append(vertice_origen)

    # ... (otros métodos)
//AquíGrafo, que tiene métodos para agregar vértices y aristasDFS, BFSy mostrar_grafoque implementar//

 Método mostrar_grafo:
    
    def mostrar_grafo(self):
        G = nx.Graph()
        for vertice, vecinos in self.grafo.items():
            for vecino in vecinos:
                G.add_edge(vertice, vecino)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
//Este método crea un objeto `nx.Graph()de NetworkX y agrega aristas a este objeto en función de las conexionesself.grafo. Luego, utilice nx.draw()para visualizar el graplt.show()de Matplotlib.//

Codigo principal:

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
//Este es el bloque principal del programa. Aquí creamos una instancia de la clase Grafo, luego solicitamos al usuario ingresar el número de nodos

Después de configurar el DFS y BFS para realizar los recorridosmostrar_grafopara visualizar el gráfico.
