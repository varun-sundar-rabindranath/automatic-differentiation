
from functools import wraps
import ad_numpy as anp
from node import Node
import numpy as np
import names

def print_args(func):

    def wrapper_print_args(*args, **kwargs):

        args_lst = list(args)
        for arg in args_lst:
            print("Arg ", arg)
        for kw in kwargs.keys():
            print("KW : ", kw, " | ", kwargs[kw])

        return func(*args, **kwargs)

    return wrapper_print_args

def say_adnp(func):

    def wrapper_say_adnp(*args, **kwargs):
        print ("ADNP primitve")
        return func(*args, **kwargs)

    return wrapper_say_adnp

def primitive(func):
    @wraps(func)
    def wrapper_primitive_(*args, **kwargs):

        # what if the inputs are of wrapped types ?
        args_lst = list(args)
        for arg in args_lst:
            if anp.wrapped_types.get(type(arg)) is not None:

                # should we scalar wrap this ?
                if anp.scalar_wrapper_types.get(type(arg)) is not None:
                    arg = anp.scalar_wrapper_types.get(type(arg))(arg)
                else:
                    arg = arg.view(anp.wrapped_types.get(type(arg)))
                # assign wrappers and unique names
                arg.wrap_attrs()
                arg.alias = names.get_uniq_name()

        #print (func)
        ret = func(*args, **kwargs)

        #print ("ret type ", type(ret), " | ", anp.wrapped_types.get(type(ret)))

        if anp.wrapped_types.get(type(ret)) is not None:

            if anp.scalar_wrapper_types.get(type(ret)) is not None:
                ret = anp.scalar_wrapper_types.get(type(ret))(ret)
            else:
                ret = ret.view(anp.wrapped_types.get(type(ret)))

            ret.wrap_attrs()
            ret.alias = names.get_uniq_name()

        if type(ret) in anp.wrapped_types.values() and ret.alias == None:
            ret.alias = names.get_uniq_name()

        # make a node for the graph
        if func.__class__.__name__ == "function":
            # only functions are nodes
            n = Node()
            n.make_node(args = args, kwargs = kwargs, outputs = ret, op = func, name = ret.alias)
            anp.cgraph.add_node(n)

        #print ("Node : ", n)

        return ret

    return wrapper_primitive_
