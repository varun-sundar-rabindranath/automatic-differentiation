import numpy as np
import ad_numpy as anp
import names
from functools import wraps

#wrap nparray function
def say_something(func):
    @wraps(func)
    def say_something_wrapper(*args, **kwargs):
        ret = func(*args, **kwargs).view(anp.ndarray_)
        ret.wrap_attrs()
        if ret.alias is None:
            ret.alias = names.get_uniq_name()

        return ret
    return say_something_wrapper

@say_something
def np_array(*args, **kwargs):
    pass

#np.ndarray = anp.ndarray_
np.array = say_something(np.array)

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

print ("a's alias ", a.alias)
print ("b's alias ", b.alias)

c = a + b

print ("c's alias ", c.alias)

d = c + a

print ("d's alias ", d.alias)

f = anp.dot(d, c)



