# computational graph class

from graph_utils import draw_graph
from queue import PriorityQueue

class Graph:

    # constructor
    def __init__(self):
        self.a = 0
        self.nodes = []
        self.edges = {}

    def make_graph(self, outputs):
        pass

    def add_node(self, n):
        self.nodes.append(n)

    def add_edge(self, u, v):
        if self.edges.get(u) is None:
            self.edges[u] = [v]
        else:
            self.edges[u].append(v)

    def print_nodes(self):
        for n in self.nodes:
            print (n)

    def print_edges(self):
        for u, v in self.edges.items():
            print(u, v)

    def draw_graph(self, outfile = "./out.png"):
        edgeslist = []
        # make a list of edges
        for u, vs in self.edges.items():
            for v in vs:
                edgeslist.append((u, v))

        draw_graph(self.nodes, edgeslist)

    def backprop(self):
        pass

    def toposort(self):

        # reverse edges
        rev_edges = {}
        for u, vs in self.edges.items():
            for v in vs:
                if rev_edges.get(v) is None:
                    rev_edges[v] = [u]
                else:
                    rev_edges[v].append(u)
            if rev_edges.get(u) is None:
                rev_edges[u] = []

        indegrees = {}
        # count indegrees
        for u, vs in rev_edges.items():
            for v in vs:
                indegrees[v] = indegrees[v] + 1 if v in indegrees else 1
            indegrees[u] = indegrees[u] if u in indegrees else 0

        # priority queue to serve nodes based on minimum indegrees
        q = PriorityQueue()

        # boot strap priority queue with 0 indegree nodes
        for u, num_indegree in indegrees.items():
            if num_indegree == 0:
                q.put((num_indegree, u))

        assert not q.empty()

        order = []
        visited = {}
        while not q.empty():

            u = q.get()[1]
            order.append(u)

            assert visited.get(u) == None and "Graph is cyclic"

            # remove u's edges to its children
            if rev_edges.get(u) is None:
                continue

            for v in rev_edges.get(u):
                assert indegrees.get(v) is not None
                indegrees[v] = indegrees[v] - 1

                assert indegrees[v] >= 0 and "Node's indegree is -ive"
                if indegrees[v] == 0:
                    q.put((indegrees[v], v))

            # mark visited
            visited[u] = True

        return order
