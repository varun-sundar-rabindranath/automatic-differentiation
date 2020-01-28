# Node class for graph

class Node:

    def __init__(self):

        self.inputs = None
        self.outputs = None
        self.op = None

    def make_node(self, *, inputs, outputs, op):
        self.inputs = inputs
        self.outputs = outputs
        self.op = op
