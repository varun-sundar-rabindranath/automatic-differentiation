# matrix multiply and then add the elements in the matrix;
# finally calculate gradients w.r.t to the input

import numpy as np
import ad_numpy as anp
from graph import Graph
import global_ds as ds

a = anp.asarray([1,2,3])
b = anp.asarray([4,5,6])

print ("a ", a, " | b ", b)

c = anp.dot(a, b)

print ("A type : ", type(a), " | Name : ", a.alias)
print ("B type : ", type(b), " | Name : ", b.alias)
print ("C type : ", type(c), " | Name : ", c.alias)

cgraph = Graph(ds.records)

cgraph.print_nodes()
cgraph.print_edges()
#anp.cgraph.draw_graph()
print ("Topological sort ", cgraph.toposort())

cgraph.backprop()

cgraph.print_nodes()
