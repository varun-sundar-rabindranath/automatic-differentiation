# feedforward nn; just a series of matrix multiply and sum
# finally perform a backprop on the sum
import numpy as np
import ad_numpy as anp
import ad_numpy_random as anpr
from graph import Graph
import global_ds as ds

print ("anpr seed ", anpr.seed)

anpr.seed(0)

x = anpr.rand(4, 1)
w1 = anpr.rand(6, 4)
w2 = anpr.rand(5, 6)
w3 = anpr.rand(2, 5)

print ("x ", x, type(x))
print ("w1 ", w1, type(w1))
print ("w2 ", w2, type(w2))
print ("w3 ", w3, type(w3))
