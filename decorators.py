
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
        print (func)
        ret = func(*args, **kwargs)

        #print ("primitive func ret type : ", type(ret))
        #print ("anp.ndarray_ ", anp.ndarray_)
        #print ("np.ndarray ", np.ndarray)
        #print (anp.ndarray_ == np.ndarray)

        if type(ret) == anp.ndarray_ and ret.alias == None:
            ret.alias = names.get_uniq_name()

        if type(ret) is np.ndarray:
            print ("wrapping return types")
            ret.view(anp.ndarray_).wrap_attrs()

        return ret
    return wrapper_primitive_
