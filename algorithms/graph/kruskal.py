class Graph:
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.edge = []

    def add_edge(self, vertex1, vertex2, weight):
        self.edge.append([vertex1, vertex2, weight])

    def union(self, dict, new_item):
        union_result = list(set(dict) | set(new_item))
        return union_result

    def kruskalMST(self):
        mst = {}
        union_vertex = []
        self.edge = sorted(self.edge, key=lambda item: item[2])

        for edge in self.edge:
            if not mst:
                mst[(edge[0], edge[1])] = edge[2]
                union_vertex = self.union(union_vertex, [edge[0], edge[1]])
            else:
                if not (edge[0] in union_vertex and edge[1] in union_vertex):
                    mst[(edge[0], edge[1])] = edge[2]
                    union_vertex = self.union(union_vertex, [edge[0], edge[1]])

        return mst


g = Graph(4)
g.add_edge('a', 'b', 10)
g.add_edge('a', 'c', 6)
g.add_edge('a', 'd', 5)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 4)

print g.kruskalMST()
