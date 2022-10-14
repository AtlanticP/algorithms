"""
Поиск в глубину - рекурсивный алгоритм обхода графа. 

Дано: Связный неориентированный граф "G(V, E)". 
Задача: обойти все вершины графа. Вычислить в циклы "c" в графе "G".
"""
from typing import Iterable
from graphs import UGraph

class Dfs:

    def __init__(self, G: UGraph, u: int):
        self.__adj_list: dict[int, list[int]] = G.adjacency_list    # The adjacency list
        self.__cycles: list[Iterable[int]]= []
        self.__run(u, [])

    def __run(self, u: int, stack: list[int]) -> None:

        # Cycle detection
        if u in stack:
        
            cycle: list[int] = [u]
            
            while True:
                v = stack.pop()
                cycle.append(v)
                
                if u == v:
                    break

            if len(cycle) > 3:    # (0, 1, 0)
                cycle.reverse()
                self.__cycles.append(tuple(cycle))
                
            return
        
        stack.append(u)

        alist: list[int] | None     # list of adjacent verticies of u
        alist = graph.adjacency_list.get(u)    

        if alist:
            for u in alist:
                self.__run(u, stack.copy())

    @property
    def cycles(self) -> list[tuple[int]]:
        """Return list of cycles in the graph and remove duplicates"""

        cycles = []
        cycle: Iterable[int]
        for cycle in self.__cycles:
            s_cycles: list[set[int]]    # List of new added set of cycles
            s_cycles = [set(cycle) for cycle in cycles] 

            if set(cycle) not in s_cycles:
                cycles.append(cycle)

        return cycles

if __name__ == "__main__":

    # Create undirected graph
    graph = UGraph(8, weighted=False)
    graph.add_edge(0, 2)
    graph.add_edge(1, 0)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 0)
    graph.add_edge(4, 1)
    graph.add_edge(4, 6)
    graph.add_edge(5, 3)
    graph.add_edge(6, 7)
    graph.add_edge(7, 4)

    cycles_expected: list[Iterable[int]]
    cycles_expected = [(0, 1, 4, 2, 0), (0, 1, 4, 2, 5, 3, 0), (4, 6, 7, 4), 
            (0, 2, 4, 1, 0), (0, 2, 5, 3, 0)]

    start: int = 0

    dfs = Dfs(graph, start)

    expected_cycles = {(0, 1, 4, 2, 0), (0, 1, 4, 2, 5, 3, 0), 
            (4, 6, 7, 4), (0, 2, 5, 3, 0)}
    cycles = set(dfs.cycles)
    msg: str = "There is one wrong cycle at least"

    assert expected_cycles, cycles

    print("The adjacency list of the graph:", graph.adjacency_list)
    print("Cycles: ", dfs.cycles)

