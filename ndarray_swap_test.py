import numpy as np
import ad_numpy as anp
from functools import wraps

#wrap nparray function
def say_something(func):
    @wraps(func)
    def say_something_wrapper(*args, **kwargs):
        ret = func(*args, **kwargs).view(anp.ndarray_)
        ret.wrap_attrs()
        return ret
    return say_something_wrapper

@say_something
def np_array(*args, **kwargs):
    pass

#np.ndarray = anp.ndarray_
np.array = say_something(np.array)

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

print ("type of a ", type(a))
print ("type of b ", type(b))
c = a + b
d = c + a

print ("dot ", anp.dot(d, c))
