"""
Алгоритм Дейкстры поиска кратчайших путей от заданной вершины графа до остальных.

Дано:   взвешенный ориентированный граф G(V, E) без дуг отрицательного веса. 
Задача: найти кратчайшие пути от заданной вершины "а" графа "G"
        до всех остальных вершин этого графа.
"""
from queue import PriorityQueue
from graphs import DGraph

CostsType = dict[int, float | int]

class Dijkstra:
    def __init__(self, G: DGraph, start: int) -> None:
        self.__n: int = len(G.verticies)    # The number of verticies
        self.__matrix: list[list[int]] = G.cost_matrix    # type: ignore

        self.__D: CostsType    # Path costs
        self.__D = {v: float('inf') for v in range(self.__n)}
        self.__D[start] = 0

        self.__run()

    def __run(self) -> None:
        """Run the Dijkstra's algorithm"""
       
        pq = PriorityQueue()    # Unvisited container 
        pq.put((0, start))
        U = {start}    # Visited set
        
        while not pq.empty():
            
            dist, u = pq.get()
            U.add(u)
            
            for v in range(self.__n):
                
                w = self.__matrix[u][v]
                
                if w != -1 and v not in U:
                    
                    old_cost = self.__D[v]
                    new_cost = dist + self.__matrix[u][v]
                    
                    if  new_cost < old_cost:
                        
                        self.__D[v] = new_cost
                        pq.put((new_cost, v))
                        
    @property
    def costs(self) -> CostsType:
        """Returns the path costs"""
        return self.__D

if __name__ == '__main__':
    
    txt = "Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph." 
    print(txt)
    
    G = DGraph(5, weighted=True)
    G.add_arrow(0, 1, 5)    # (u, v, weight)
    G.add_arrow(0, 2, 3)
    G.add_arrow(0, 3, 6)
    G.add_arrow(2, 3, 2)
    G.add_arrow(3, 1, 1)
    G.add_arrow(1, 4, 10)
    G.add_arrow(3, 4, 4)    
    
    start = 0
    djk = Dijkstra(G, start)
    costs = djk.costs    
    print(f'Initial vertex is {start}. Costs are:')
    print(costs)

