# matrix multiply and then add the elements in the matrix;
# finally calculate gradients w.r.t to the input

import numpy as np
import ad_numpy as anp
from graph import Graph
import global_ds as ds

a = anp.asarray([[1.0 ,2.0, 3.0], [4.0, 5.0, 6.0]])
b = anp.asarray([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

print ("a ", a, " | b ", b)

c = anp.dot(a, b)

d = anp.sum(c)

print ("c", c)
print ("d", d)

print ("A type : ", type(a), " | Name : ", a.alias)
print ("B type : ", type(b), " | Name : ", b.alias)
print ("C type : ", type(c), " | Name : ", c.alias)
print ("D type : ", type(d), " | Name : ", d.alias)

cgraph = Graph(ds.records)

cgraph.print_nodes()
cgraph.print_edges()
#anp.cgraph.draw_graph()
#print ("Topological sort ", cgraph.toposort())
cgraph.backprop()
cgraph.print_nodes()
