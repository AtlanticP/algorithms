"""
Алгоритм Флойда-Уоршела

Дано: Граф "G=(V, E)".
Задача: Поиск кратчайших путей.
Сложность: O(V**3)
"""

from copy import deepcopy
from graphs import UGraph, Graph

def floyd(G: Graph) -> tuple[list[list[int|float]], list[list[int]]]:

    n = len(G.verticies)
    cost_matrix: list[list[int|float]]
    cost_matrix = deepcopy(G.cost_matrix)

    paths = [[j for j in range(n)] for _ in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
    
                new_cost = cost_matrix[i][k] + cost_matrix[k][j]
                old_cost = cost_matrix[i][j]
    
                if new_cost < old_cost:
                    
                    cost_matrix[i][j] = new_cost
                    paths[i][j] = k

    return cost_matrix, paths


if __name__ == '__main__':

    txt = "the Floyd–Warshall algorithm (also known as Floyd's algorithm, the Roy–Warshall algorithm, the Roy–Floyd algorithm, or the WFI algorithm) is an algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles)."
    print(txt)

    G = UGraph(5, gap=float('inf'), weighted=True)
    G.add_edge(0, 1, 5)
    G.add_edge(0, 2, 3)
    G.add_edge(0, 3, 6)
    G.add_edge(2, 3, 2)
    G.add_edge(3, 1, 1)
    G.add_edge(1, 4, 10)
    G.add_edge(3, 4, 4)

    cost_matrix, paths = floyd(G)    
    print("Initial graph:")
    for edge in G.cost_matrix:
        print(edge)
    print()

    print("Modified graph")

    for line in cost_matrix:
        print(line)
        
    def get_path(paths, start, end):

        path = [end]
        v = end
        
        while  v != start:
            v = paths[v][start]
            path.append(v)
        
        path.reverse()
        
        return path

    start = 4
    end = 0
    path = get_path(paths, start, end)
