# Node class for graph

from ad_numpy import wrapped_types, grad_fn_mapping

class Node:

    def __init__(self):

        self.inputs = {"args" : None, "kwargs" : None}
        self.outputs = None
        self.op = None
        self.name = None
        self.grad_fn = None
        self.grad = 0.0
        self.grad_wrt_args = {}
        self.grad_wrt_kwargs = {}
        self.inputs_order = {}

    def make_node(self, *, args, kwargs, outputs, op, name):
        self.inputs = {"args" : args, "kwargs" : kwargs}
        self.outputs = outputs
        self.op = op
        self.name = name

        # assign the grad function mapping
        if grad_fn_mapping.get(self.op) is None:
            print ("Grad function not implemented for ", self.op)
            assert False and "You are a failure"

        self.grad_fn = grad_fn_mapping[self.op]

        # what is the position of every input ?
        #if (self.inputs["args"] is not None):
        #    args_lst = list(self.inputs["args"])
        #    for i in range(len(args_lst)):
        #        if type(args_lst[i]) in wrapped_types.values():
        #            self.inputs_order[args_lst[i].alias] = i

        #if (self.inputs["kwargs"] is not None):
        #    kwargs_lst = list(self.inputs["kwargs"].values())
        #    for i in range(len(kwargs_lst)):
        #        if type(kwargs_lst[i]) in wrapped_types.values():
        #            self.inputs_order[kwargs_lst[i].alias] = i

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
        s = s + " Grad function : " + str(self.grad_fn) + "\n"
        s = s + " Grad : " + str(self.grad) + "\n"
        s = s + " Grad wrt args : " + (self.grad_wrt_args) + "\n"

        return s
