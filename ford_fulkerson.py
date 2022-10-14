"""
Алгоритм Форда-Фалкерсона.

Дано: Граф G(V, E) с пропускной способностью c(u, v). 
Задача: Найти максисальный поток из источника s в t.
"""

from graphs import FGraph, FlowType, MatrixFlowType
from copy import deepcopy


class FordFulk:
    """ The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) 
    is a greedy algorithm that computes the maximum flow in 
    a flow network
    """

    def __init__(self, G: FGraph) -> None:
        self.__n_verticies: int = len(G.verticies)    # The number of verticies
        self.__matrix: MatrixFlowType = deepcopy(G.cost_matrix)    # The cost matrix

    def __get_max_vertex(self, u: int, V: set) -> int:
        """Get max neighbor of the current vertice"""
        
        mx_weight: int | float = 0
        mx_vertex: int = -1

        for v in range(self.__n_verticies):
            
            if v in V:
                continue
            
            arc: FlowType = self.__matrix[u][v]
            
            if arc[2] == 1:
            
                if arc[0] > mx_weight:
                    mx_weight = arc[0]
                    mx_vertex = v
            else:
                
                if arc[1] > mx_weight:
                    mx_weight = arc[1]
                    mx_vertex = v
            
        return mx_vertex

    def __get_max_flow(self, arrows: list[tuple[int | float, int, int]]
                       ) -> int | float:
        """Get the max value of visited arrows"""
        return min(*[arrow[0] for arrow in arrows])

    def __update_graph(self, arrows: list[tuple[float | int, int, int]], 
            f: int | float) -> None:
        """Update values of visited arrows in the graph"""

        for arrow in arrows:
            
            if arrow[1] == -1:    # The initial vertice
                continue
            
            _, u, v = arrow     # Arrow: weight, from, to
            sgn = self.__matrix[u][v][2]    # The sign of the flow
            
            self.__matrix[u][v][0] -= f*sgn
            self.__matrix[u][v][1] += f*sgn
            
            self.__matrix[v][u][0] -= f*sgn
            self.__matrix[v][u][1] += f*sgn
            
    def run(self, start: int, end: int) -> float | int:
        
        v: int = -2
        F: list[int | float] = []    # Flows

        while v != -1:
            
            u: int = start
            S: list[tuple[int | float, int, int]]    # Arrows: weight, from, to
            S = [(float("inf"), -1, u)]
            V: set[int] = {u}    # Visited verticies
            
            while u != end:

                v = self.__get_max_vertex(u, V)

                if v == -1:
                    if u == start:
                        break
                    else:
                        u = S.pop()[1]
                        continue

                direction: int | float
                direction = self.__matrix[u][v][2]

                if direction == 1:
                    w = self.__matrix[u][v][0]
                else:
                    w = self.__matrix[u][v][1]

                S.append((w, u, v))
                V.add(v)

                if v == end:

                    F.append(self.__get_max_flow(S))
                    self.__update_graph( S, F[-1])

                    break

                u = v

        return sum(F)


if __name__ == "__main__":
    
    fgraph = FGraph(5)
    fgraph.add_arrow(0, 1, [20, 0, 1])
    fgraph.add_arrow(0, 2, [30, 0, 1])
    fgraph.add_arrow(0, 3, [10, 0, 1])
    fgraph.add_arrow(1, 2, [40, 0, 1])
    fgraph.add_arrow(1, 4, [30, 0, 1])
    fgraph.add_arrow(2, 3, [10, 0, 1])
    fgraph.add_arrow(2, 4, [20, 0, 1])
    fgraph.add_arrow(3, 4, [20, 0, 1])

    ff: FordFulk = FordFulk(fgraph)
    max_flow: float | int = ff.run(0, 4)

    expected_flow = 60
    assert max_flow == expected_flow, "Wrong flow"

    print("Maximum flow is", max_flow)
