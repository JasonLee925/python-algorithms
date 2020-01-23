class Graph:
    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict

    def getVertex(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.find_edges()

    def print_graph(self):
        print(self.graph_dict)

    def find_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for sibiling in self.graph_dict[vertex]:
                if {sibiling, vertex} not in edges:
                    edges.append({sibiling, vertex})
        return edges

    def addVertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def addEdge(self, edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.graph_dict:
            self.graph_dict[v1].append(v2)
        else:
            self.graph_dict[v1] = v2
        if v2 in self.graph_dict:
            self.graph_dict[v2].append(v1)
        else:
            self.graph_dict[v2] = v1

    def getNeighbor(self, vertex):
        if vertex not in self.graph_dict:
            return None
        else:
            return self.graph_dict[vertex]

    def bfs(self, vertex, bfs_queue, visited):
        if vertex not in visited:
            visited[vertex] = True
            bfs_queue.append(vertex)
            for neighbor in self.getNeighbor(vertex):
                self.bfs(neighbor, bfs_queue, visited)
            print(bfs_queue[0]),
            del bfs_queue[0]

    def BFSTraversal(self):
        visited = {}
        bfs_queue = []
        self.bfs(self.graph_dict.keys()[0], bfs_queue, visited)


graph_elements = {"a": ["c"],
                  "b": ["c", "e"],
                  "c": ["a", "b", "d", "e"],
                  "d": ["c"],
                  "e": ["c", "b"],
                  "f": []
                  }
graph = Graph(graph_elements)
graph.addVertex('g')
graph.addEdge({'f', 'd'})
graph.addEdge({'g', 'f'})

print('Following is Breadth First Traversal:')
graph.BFSTraversal()
