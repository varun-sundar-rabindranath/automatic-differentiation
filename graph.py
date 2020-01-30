# computational graph class

class Graph:

    # constructor
    def __init__(self):
        self.a = 0
        self.nodes = []
        self.edges = []

    def make_graph(self, outputs):
        pass

    def add_node(self, n):
        self.nodes.append(n)

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def print_nodes(self):
        for n in self.nodes:
            print (n)

    def print_edges(self):
        for e in self.edges:
            print (e)

    def draw_graph(self, outfile = "./out.png"):
        pass
