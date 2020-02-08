# computational graph class

from graph_utils import draw_graph
from queue import PriorityQueue
from record import Record
from node import Node
import ad_numpy as anp

class Graph:

    # constructor
    def __init__(self, records):
        self.nodes = {}
        self.edges = {}

        # construct graph from records
        for k, r in records.items():
            n = Node()
            n.make_node(args = r.args, kwargs = r.kwargs, outputs = r.outputs, op = r.op, name = r.name)
            self.add_node(n)

            # edges are between the inputs and the outputs
            # get alias names of stuff in args and kwargs
            edge_src = list(filter(lambda arg : type(arg) in anp.wrapped_types.values(), list(r.args))) + \
                       list(filter(lambda arg : type(arg) in anp.wrapped_types.values(), r.kwargs.values()))

            for u in edge_src:
                self.add_edge(u.alias, r.outputs.alias)

    def add_node(self, n):
        assert self.nodes.get(n.name) is None and "Node of this name already available"
        assert n.name is not None and "Node has no name"
        self.nodes[n.name] = n

    def add_edge(self, u, v):
        if self.edges.get(u) is None:
            self.edges[u] = [v]
        else:
            self.edges[u].append(v)

    def print_nodes(self):
        for n in self.nodes.values():
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

        draw_graph(self.nodes.values(), edgeslist)

    def backprop(self):
        # Algorithm
        # 1. toposort
        # // working with the top node
        # 2. from the top; seed it; i.e. gradient w.r.t to itself is 1
        # 3. calculate gradients w.r.t. the inputs; search the global
        #    datastructure for the appropritate grad function
        # // move on to the next node
        # 4. calculate gradient w.r.t. to it by adding from its parents
        # 5. again calculate gradiets w.r.t. the inputs;
        # 6. move on to the next node and so on

        # 1. toposort
        backprop_order = self.toposort()

        for node_alias in backprop_order:
            assert self.nodes.get(node_alias) is not None and "No such node"
            backprop_node = self.nodes.get(node_alias)

            # gradient of self w.r.t the output of concern
            if node_alias == backprop_order[0]:
                # topnode; seed it
                backprop_node.grad = 1.0
            else:
                # sum from parents; since we are going backwards
                # the actual edges are the parents
                g = 0.0
                for parent_name in self.edges[backprop_node.name]:
                    parent = self.nodes.get(parent_name)
                    if parent.grad_wrt_args.get(backprop_node.name) is not None:
                        g = g + parent.grad_wrt_args.get(backprop_node.name)
                    if parent.grad_wrt_kwargs.get(backprop_node.name) is not None:
                        g = g + parent.grad_wrt_kwargs.get(backprop_node.name)
                backprop_node.grad = g

            assert backprop_node.grad_fn is not None and "can't calc. gradient"

            # gradients w.r.t the inputs
            backprop_node.grad_wrt_args = \
                    backprop_node.grad_fn(backprop_node.inputs["args"], \
                                          backprop_node.inputs["kwargs"], \
                                          backprop_node.outputs, \
                                          backprop_node.grad)

            # TODO : Impl gradients w.r.t kwargs


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
