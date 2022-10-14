"""
Алгоритм Краскала - алгоритм построения минимального остовного 
дерева "T" взвешенного связного неориентированного графа "G(V, E)"

Дано:    Связный неориентированный граф "G(V, E)".
Задача:  Построить минимальное остовное дерево "T".
"""
from graphs import UGraph


EdgeType = tuple[int, int, int]

class Kruskal:
    def __init__(self, G: UGraph):

        # The edge list of the Graph
        self.__edge: list[EdgeType]   # [(u, v, weight), ...]
        self.__edge= G.edge_list    # type: ignore            
        self.__T: list[EdgeType] = []       # A minimum spanning tree

        self.__run()

    def __run(self) -> None:
        """Run Kruskal's algorithm"""

        edge_list = sorted(self.__edge, key=lambda x: x[0])

        S: set[int] = set()    # Visited verticies
        D: dict[int, list[int]] = {}       # Spanning tree with isolated verticies

        edge = EdgeType
        for edge in edge_list:
            
            _, u, v = edge    # weight, vertice 1, vertice 2
            if u not in S or v not in S:
                
                if u not in S and v not in S:
                    D[u] = [u, v]
                    D[v] = D[u]
                
                if u in S:
                    D[u].append(v)
                    D[v] = D[u]
                else:
                    D[v].append(u)
                    D[u] = D[v]
                    
                self.__T.append(edge)
                S.add(v)
                S.add(u)

        # connecting connected components (maximal connected subgraph)
        for edge in edge_list:
            _, u, v = edge     # weight, vertice 1, vertice 2

            if u not in D[v]:
                
                self.__T.append(edge)
                D[v] += D[u]
                D[u] = D[v]

    @property
    def tree(self) -> list[EdgeType]:
        return self.__T


G = UGraph(6, weighted=True)
G.add_edge(0, 1, 1)
G.add_edge(2, 3, 2)
G.add_edge(4, 5, 3)
G.add_edge(0, 2, 4)
G.add_edge(1, 3, 5)
G.add_edge(2, 4, 6)
G.add_edge(3, 5, 7)
G.add_edge(3, 4, 8)
txt = '''Kruskal's algorithm finds a minimum spanning tree of an undirected edge-weighted graph. '''
print(txt)            

krs = Kruskal(G)
T = krs.tree
print(T)
    
