
from functools import wraps
import ad_numpy as anp
import numpy as np
from record import Record
import names
import global_ds as ds

def print_args(func):

    def wrapper_print_args(*args, **kwargs):

        args_lst = list(args)
        for arg in args_lst:
            print("Arg ", arg)
        for kw in kwargs.keys():
            print("KW : ", kw, " | ", kwargs[kw])

        return func(*args, **kwargs)

    return wrapper_print_args

def print_args_kwargs(args, kwargs):

    args_lst = list(args)
    for arg in args_lst:
        print("Arg ", arg)
    for kw in kwargs.keys():
        print("KW : ", kw, " | ", kwargs[kw])

def say_adnp(func):

    def wrapper_say_adnp(*args, **kwargs):
        print ("ADNP primitve")
        return func(*args, **kwargs)

    return wrapper_say_adnp

def wrap_thing(thing):

    # do we have a wrapper for this thing's  type ?
    if anp.wrapped_types.get(type(thing)) is not None:

        # should we scalar wrap this ?
        if anp.scalar_wrapper_types.get(type(thing)) is not None:
            thing = anp.scalar_wrapper_types.get(type(thing))(thing)
        else:
            thing = thing.view(anp.wrapped_types.get(type(thing)))

        # assign wrappers and unique names
        thing.wrap_attrs()
        thing.alias = names.get_uniq_name()

    return thing

def wrap_args(args):

    args_lst = list(args)

    args_lst = map(lambda arg: wrap_thing(arg), args_lst)

    return tuple(args_lst)

def wrap_kwargs(kwargs):

    for k, v in kwargs.items():
        kwargs[k] = wrap_thing(v)

    return kwargs


def primitive(func):
    @wraps(func)
    def wrapper_primitive_(*args, **kwargs):

        #print_args_kwargs(args, kwargs):

        # what if the inputs are of wrapped types ?
        args = wrap_args(args)
        kwargs = wrap_kwargs(kwargs)

        #print (func)
        ret = func(*args, **kwargs)

        ret = wrap_thing(ret)

        # the return value type is sometimes inferred from the type of
        # the inputs; then, the names dont get assigned
        #assert type(ret) in anp.wrapped_types.values()
        if type(ret) in anp.wrapped_types.values() and ret.alias == None:
            ret.alias = names.get_uniq_name()

        # record operation
        if func.__class__.__name__ == "function":
            ds.records[ret.alias] = Record(args, kwargs, ret, func.__name__, ret.alias)

        return ret

    return wrapper_primitive_
