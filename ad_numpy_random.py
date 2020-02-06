import numpy.random as npr
from functools import wraps
from decorators import *

for name, obj in npr.__dict__.items():

    # wrap all values
    if callable(obj) and type(obj) is not type:
        globals()[name] = primitive(obj)
    else:
        globals()[name] = obj
