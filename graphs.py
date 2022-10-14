from typing import Iterable

MatrixType = list[list[int | float]]    # The cost matrix oft the directed or undirected graph
FlowType = list[float | int]        
MatrixFlowType = list[list[FlowType]]    # The cost matrix of the graph with a flow
EdgeType = tuple[int | float, int, int] | tuple[int, int]    # Types of edges/arrows of graphs: directed, undirected or graphs with a flow

class Graph:

    def __init__(self, n_verticies: int, gap: int|float =-1,
            weighted: bool = False):

        self._n: int = n_verticies    # Number of verticies in a graph
        self._gap: int|float = gap          # No edge
        self._weighted: bool = weighted    # Weightid graph

        self._matrix: MatrixType     # Cost matrix
        self._matrix = [
                    [0 if i == j else gap for j in range(self._n)
                ] for i in range(self._n)
            ]

    @property
    def adjacency_list(self) -> dict[int, list[int]]:
        """Returns the adjacency list"""

        D: dict = {}   # adjacency list

        for i in range(self._n):
            for j in range(self._n):
                
                if i != j and (self._matrix[i][j] != self._gap):
        
                    if D.get(i):
                        D[i].append(j) 
                    else: 
                        D[i] = [j]
        return D                   
      
    @property    
    def verticies(self) -> list[int]:
        return list(range(self._n))

    @property
    def cost_matrix(self) -> MatrixType:
        return self._matrix

    def __repr__(self):
        text = f"Graph(n_verticies={self._n}, gap={self._gap}, weighted={self._weighted})"
        return text


class UGraph(Graph):
    """The undirected graph"""

    def add_edge(self, u: int, v: int, w: int|None=None) -> None:
        """Adding the new edge to the graph"""
        # __import__('pdb').set_trace()
        if self._weighted and w:
            self._matrix[u][v] = w
            self._matrix[v][u] = w
        else:
            self._matrix[u][v] = 1
            self._matrix[v][u] = 1

    
    @property        
    def edge_list(self) -> list[EdgeType]:
        """Returns the edge list of the Graph"""
        
        edges: list[EdgeType] = []

        for u in range(self._n):
            for v in range(self._n):
                
                w: int | float
                w = self._matrix[u][v]    # Weight of edge (u, v)
                
                if self._weighted:
                    if  u < v and w != self._gap:
                        edge: EdgeType = (w, u, v)
                        edges.append(edge)
                else:
                    if  u < v and w != self._gap:
                        edge: EdgeType = (u, v)
                        edges.append(edge)

        return edges


class DGraph(Graph):
    """Directed Graph"""
        
    def add_arrow(self, u: int, v: int, w: int|None=None):
        """Adding the new edge to the graph"""

        if w and self._weighted:
            self._matrix[u][v] = w

        else:
            self._matrix[u][v] = 1

    @property        
    def arrow_list(self) -> list[EdgeType]:
        """Returns the edge list of the Graph"""
        
        edges: list[EdgeType] = []

        for u in range(self._n):
            for v in range(self._n):
                
                w: int|float = self._matrix[u][v]    # Weight of edge (u, v)
                
                edge: EdgeType
                if  u != v and w != self._gap:

                    if self._weighted:
                        edge = (w, u, v)
                    else:
                        edge = (u, v)

                    edges.append(edge)

        return edges


class FGraph:
    """The flow graph"""

    def __init__(self, n_verticies: int):

        self._n = n_verticies    # Number of verticies in graph
        
        MatrixFlowType = list[list[FlowType]]
        self._matrix: MatrixFlowType
        self._matrix = [
                [[0, 0, 1] for _ in range(self._n)] for _ in range(self._n)
                ]
            
    def add_arrow(self, u: int, v: int, w: list[float|int]) -> None:
        """Adding the new edge to the graph"""

        self._matrix[u][v] = w
        t: FlowType = w[:]
        t[2] *= -1
        self._matrix[v][u] = t

    @property    
    def verticies(self) -> list[int]:
        return list(range(self._n))

    @property
    def cost_matrix(self) -> MatrixFlowType:
        return self._matrix

    def __repr__(self):
        text = f"FGraph(n_verticies={self._n})"
        return text


if __name__ == '__main__':
    
    # Directed graph with the a flow
    n_verticies = 5

    fg = FGraph(5)
    fg.add_arrow(0, 1, [20, 0, 1])
    fg.add_arrow(0, 2, [30, 0, 1])
    fg.add_arrow(0, 3, [10, 0, 1])
    fg.add_arrow(1, 2, [40, 0, 1])
    fg.add_arrow(1, 4, [30, 0, 1])
    fg.add_arrow(2, 3, [10, 0, 1])
    fg.add_arrow(2, 4, [20, 0, 1])
    fg.add_arrow(3, 4, [20, 0, 1])

    # True cost matrix of the flow graph
    flow_matrix: MatrixFlowType
    flow_matrix = [[[0,0,1], [20,0,1], [30,0,1], [10,0,1], [0,0,1]],
     [[20,0,-1], [0,0,1], [40,0,1], [0,0,1], [30,0,1]],
     [[30,0,-1], [40,0,-1], [0,0,1], [10,0,1], [20,0,1]],
     [[10,0,-1], [0,0,1], [10,0,-1], [0,0,1], [20,0,1]],
     [[0,0,1], [30,0,-1], [20,0,-1], [20,0,-1], [0,0,1]],
]

    assert len(fg.verticies) == n_verticies, "Something wrong with number of verticies in a flow graph"
    assert flow_matrix == fg.cost_matrix, "Something wrong with creating cost matrix in a flow graph"
        
    dg = DGraph(8, weighted=False)
    dg.add_arrow(0, 1)
    dg.add_arrow(0, 2)
    dg.add_arrow(2, 3)
    dg.add_arrow(2, 4)
    dg.add_arrow(3, 4)
    dg.add_arrow(4, 0)
    dg.add_arrow(5, 1)
    dg.add_arrow(6, 5)
    dg.add_arrow(6, 4)
    dg.add_arrow(7, 5)
    dg.add_arrow(7, 6)

    adjacency_list: dict[int, list[int]]
    adjacency_list = {0: [1, 2], 2: [3, 4], 3: [4], 4: [0], 5: [1], 6: [4, 5], 7: [5, 6]}
    assert dg.adjacency_list == adjacency_list, "something wrong with the adjacency list in the directed graph"    

    arrow_list = {(0, 1), (0, 2), (2, 3), (2, 4), (3, 4), (4, 0), (5, 1), (6, 4), (6, 5), (7, 5), (7, 6)}
    assert set(dg.arrow_list) == arrow_list, "something wrong with the arrow list in the directed graph"

    # Test adjacency matrix in a directed graph
    dwg = DGraph(5, gap=0, weighted=True)
    dwg.add_arrow(0, 1, 5)
    dwg.add_arrow(0, 2, 3)
    dwg.add_arrow(0, 3, 6)
    dwg.add_arrow(2, 3, 2)
    dwg.add_arrow(3, 1, 1)
    dwg.add_arrow(1, 4, 10)
    dwg.add_arrow(3, 4, 4)

    adjacency_matrix_true: MatrixType = [    
        [0, 5, 3, 6, 0],
        [0, 0, 0, 0, 10],
        [0, 0, 0, 2, 0],
        [0, 1, 0, 0, 4],
        [0, 0, 0, 0, 0]

    ]

    assert adjacency_matrix_true == dwg.cost_matrix, "Something wrong with the adjacency matrix in the directed graph"
    
    # Test cost matrix in an undirected graph
    ud_cost_matrix_true: MatrixType = [
        [0, 5, 3, 6, -1],
        [5, 0, -1, 1, 10],
        [3, -1, 0, 2, -1],
        [6, 1, 2, 0, 4],
        [-1, 10, -1, 4, 0]
    ]
    ud_edge_list_true: list[EdgeType]
    ud_edge_list_true = [
     (5, 0, 1), (3, 0, 2), (6, 0, 3), (1, 1, 3), 
     (10, 1, 4), (2, 2, 3), (4, 3, 4)
     ]
    
    n_verticies = len(ud_cost_matrix_true)

    uwg = UGraph(n_verticies, weighted=True)
    uwg.add_edge(0, 1, 5)
    uwg.add_edge(0, 2, 3)
    uwg.add_edge(0, 3, 6)
    uwg.add_edge(2, 3, 2)
    uwg.add_edge(3, 1, 1)
    uwg.add_edge(1, 4, 10)
    uwg.add_edge(3, 4, 4)
    
    assert len(uwg.verticies) == n_verticies, "Something wrong with a number of verticies in the undirected graph"
    cond = (ud_cost_matrix_true == uwg.cost_matrix)
    assert cond, "Something wrong with a cost matrix in the undirected graph"
    assert ud_edge_list_true == uwg.edge_list, "Something wrong with an edge list in the undirected graph"

    # The undirected graph
    ug = UGraph(6, weighted=True)
    ug.add_edge(0, 1, 1)
    ug.add_edge(2, 3, 2)
    ug.add_edge(4, 5, 3)
    ug.add_edge(0, 2, 4)
    ug.add_edge(1, 3, 5)
    ug.add_edge(2, 4, 6)
    ug.add_edge(3, 5, 7)
    ug.add_edge(3, 4, 8)

    expected_list = [(1, 0, 1), (4, 0, 2), (5, 1, 3), (2, 2, 3), (6, 2, 4), (8, 3, 4), (7, 3, 5), (3, 4, 5)]
    assert expected_list == ug.edge_list, "Something wrong with an edge list in the undirected graph"

