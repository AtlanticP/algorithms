"""
Алгоритм Прима - алгоритм построения минимального остовного 
дерева "T" взвешенного связного неориентированного графа "G(V, E)"

Дано:    Связный неориентированный граф "G(V, E)".
Задача:  Построить минимальное остовное дерево "T".
"""

from graphs import UGraph
import random 

EdgeType = tuple[float|int, int, int] 

class Prim:

    def __init__(self, G: UGraph, init_vertex: int) -> None:
        self.__n: int = len(G.verticies)    # The number of verticies

        # The edge list: [(weight, u, v), ...]
        self.__edges: list[EdgeType] = G.edge_list    # type: ignore

        self.__S: set[int] = set()    # Visited
        self.__S.add(init_vertex)
        self.__T: list[EdgeType] = []    # The spanning tree

        self.__run()

    def __get_min(self) -> EdgeType:
        """Find the minimum-weight edge that grows the tree"""
        
        mnm_edge: EdgeType = (float('inf'), -1, -1)    # The initial "min" 
        
        for v in self.__S:

            edge: EdgeType
            for edge in self.__edges:

                cond1: bool
                cond1 = (edge[1] == v or edge[2] == v)     # The edge connected the tree

                cond2: bool
                cond2 = (edge[1] not in self.__S 
                        or edge[2] not in self.__S)   # No cycles

                if cond1 and cond2 and edge[0] < mnm_edge[0]:
                    mnm_edge = edge

        return mnm_edge

    def __run(self):
        """Run Prim's algorithm"""

        while len(self.__S) < self.__n:
            edge: EdgeType = self.__get_min()    # type: ignore

            if edge[0] == float('inf'):
                break
            
            self.__T.append(edge)
            self.__S.add(edge[1])
            self.__S.add(edge[2])

    @property
    def tree(self) -> list[EdgeType]:
        return self.__T


SEED = 32
G = UGraph(6, weighted=True)
G.add_edge(0, 1, 1)     # (u, v, weight)
G.add_edge(2, 3, 2)
G.add_edge(4, 5, 3)
G.add_edge(0, 2, 4)
G.add_edge(1, 3, 5)
G.add_edge(2, 4, 6)
G.add_edge(3, 5, 7)
G.add_edge(3, 4, 8)

n = len(G.verticies)
random.seed(SEED)
init_vertex: int = random.randint(0, n-1)    # initial vertex

print("The edge list of the Graph (weight, u, v):", G.edge_list)
print("The initial vertex:", init_vertex)

prim = Prim(G, init_vertex)
T = prim.tree

print("Minimum spanning tree of weighted undirected graph:", T)    
    
sm = sum(map(lambda x: x[0], T))    # Sum of the spanning tree
assert 16 == sm, "Something wrong with Prim's algorithm"

