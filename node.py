# Node class for graph

class Node:

    def __init__(self):

        self.inputs = {"args" : None, "kwargs" : None}
        self.outputs = None
        self.op = None
        self.name = None

    def make_node(self, *, args, kwargs, outputs, op, name):
        self.inputs = {"args" : args, "kwargs" : kwargs}
        self.outputs = outputs
        self.op = op
        self.name = name

    def __str__(self):

        s = ""
        s = s + "--- Node : " + self.name + " --- \n"


        if (self.inputs["args"] is not None):
            args_lst = list(self.inputs["args"])
            for arg in args_lst:
                s = s + " Arg : " + str(arg) + "\n"

        if (self.inputs["kwargs"] is not None):
            for kw in self.inputs["kwargs"].keys():
                s = s + " KW : " + kw  + str(self.inputs["kwargs"][kw]) + "\n"

        s = s + " Outputs : " + str(self.outputs) + "\n"
        s = s + " Opeeration : " + str(self.op) + "\n"

        return s
