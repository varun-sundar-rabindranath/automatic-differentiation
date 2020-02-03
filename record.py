# defines a record of information for graph construction

class Record:

    def __init__(self, args, kwargs, outputs, op, name):
        self.args = args
        self.kwargs = kwargs
        self.outputs = outputs
        self.op = op
        self.name = name

    def __str__(self):

        s = ""
        s = s + "--- Record : " + self.name + " --- \n"


        if (self.args is not None):
            args_lst = list(self.args)
            for arg in args_lst:
                s = s + " Arg : " + str(arg) + "\n"

        if (self.kwargs is not None):
            for kw in self.kwargs.keys():
                s = s + " KW : " + kw  + str(self.kwargs[kw]) + "\n"

        s = s + " Outputs : " + str(self.outputs) + "\n"
        s = s + " Operation : " + str(self.op) + "\n"
        return s
