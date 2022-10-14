"""
Поиск в ширину - алгоритм обхода графа.

Дано:    связный неориентированный граф "G(V, E)". 
Задача:  обойти все вершины графа "G".
"""

from graphs import UGraph
import time


class Bfs:

    def __init__(self, G: UGraph, init_vert: int) -> None:
        self.__adj_list: dict[int, list[int]]
        self.__adj_list= G.adjacency_list   # The adjacency list of the graph

        self.__run(init_vert)

    def __run(self, start: int):
        
        self.__visited: list[int] = [start]    # Visited verticies
        self.__queue = [start]
        
        while self.__queue:
            
            u = self.__queue.pop(0)
            time.sleep(0.5)
            print(f"Обошел вершину: {u}")
            
            for v in self.__adj_list[u]:
        
                if v not in self.__visited:
                    self.__queue.append(v)
                    self.__visited.append(v) 
                    
    @property
    def visited(self) -> list[int]:
        return self.__visited       

if __name__ == '__main__':
    
    G = UGraph(5)
    G.add_edge(0, 1, 5)
    G.add_edge(0, 4, 3)
    G.add_edge(0, 3, 6)
    G.add_edge(4, 3, 2)
    G.add_edge(3, 1, 1)
    G.add_edge(1, 2, 10)
    G.add_edge(3, 2, 4)
    
    bfs = Bfs(G, 0)
    assert bfs.visited == [0, 1, 3, 4, 2], 'Неверный поиск в ширину'

