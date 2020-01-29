# computational graph class

class Graph:

    # constructor
    def __init__(self):
        self.a = 0
        self.nodes = []

    def make_graph(self, outputs):
        pass

    def add_node(self, n):
        self.nodes.append(n)

    def print_nodes(self):
        for n in self.nodes:
            print (n)
