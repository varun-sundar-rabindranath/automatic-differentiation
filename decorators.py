
from functools import wraps
import ad_numpy as anp
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
                arg.__class__ = anp.wrapped_types[type(arg)]
                arg.wrap_attrs()
                arg.alias = names.get_uniq_name()

        print (func)
        ret = func(*args, **kwargs)

        #print ("primitive func ret type : ", type(ret))
        #print ("anp.ndarray_ ", anp.ndarray_)
        #print ("np.ndarray ", np.ndarray)
        #print (anp.ndarray_ == np.ndarray)

        if anp.wrapped_types.get(type(ret)) is not None:

            print ("ret type : ", type(ret))
            print ("anp.wrapped_types.keys() ", anp.wrapped_types.keys())
            print ("wrapped class : ", anp.wrapped_types[type(ret)])

            # make a wrapped type instead
            ret.__class__ = anp.wrapped_types[type(ret)]
            ret.wrap_attrs()
            ret.alias = names.get_uniq_name()

        if type(ret) in anp.wrapped_types.values() and ret.alias == None:
            ret.alias = names.get_uniq_name()

        return ret

    return wrapper_primitive_
