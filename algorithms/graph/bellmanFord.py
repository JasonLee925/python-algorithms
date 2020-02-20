class Graph:
    def __init__(self):
        self.edge = []
        self.vertex = []
        self.vertex_num = 0

    def add_node(self, node):
        if node not in self.vertex:
            self.vertex.append(node)
            self.vertex_num += 1

    def add_edge(self, vertex1, vertex2, weight):
        self.edge.append([vertex1, vertex2, weight])

    def bellmanFord(self, from_node, end_node):
        result = {}
        for v in self.vertex:
            if v != from_node:
                result[v] = [None, []]
            else:
                result[v] = [0, []]
        current_path = []
        for i in range(self.vertex_num - 1):
            for v1, v2, weight in self.edge:
                if v1 != from_node:
                    current_path = result[v1][1]
                else:
                    current_path = [from_node]

                if result[v1][0] != None:
                    if result[v2][0] is None or result[v1][0] + weight < result[v2][0]:
                        result[v2][0] = result[v1][0] + weight
                        result[v2][1] = current_path[:]
                        result[v2][1].append(v2)
        return result[end_node]


g = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    g.add_node(node)

g.add_edge('A', 'B', -1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('D', 'B', 1)
g.add_edge('D', 'C', 5)
g.add_edge('E', 'D', -3)
g.add_edge('B', 'E', 2)

shortes_path = g.bellmanFord('A', 'E')

print 'path => ', shortes_path[1]
print 'distance =>', shortes_path[0]
