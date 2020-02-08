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

print ("x ", x, type(x), x.alias)
print ("w1 ", w1, type(w1), w1.alias)
print ("w2 ", w2, type(w2), w2.alias)
print ("w3 ", w3, type(w3), w3.alias)

# forward pass
l1_output = anp.dot(w1, x)
l2_output = anp.dot(w2, l1_output)
l3_output = anp.dot(w3, l2_output)
# scalar output for forward pass
o = anp.sum(l3_output)

# print records
#for k, v in ds.records.items():
#    print (v)

# create graph
cgraph = Graph(ds.records)
#cgraph.print_nodes()
#cgraph.print_edges()

cgraph.backprop()

cgraph.print_nodes()
