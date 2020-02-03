import numpy as np
import ad_numpy as anp
import global_ds as ds
from graph import Graph

a = anp.asarray([1,2,3])
b = anp.asarray([4,5,6])

print ("a ", a, " | b ", b)

c = a + b
d = anp.dot(c, b)

print ("A type : ", type(a), " | Name : ", a.alias)
print ("B type : ", type(b), " | Name : ", b.alias)
print ("C type : ", type(c), " | Name : ", c.alias)
print ("D type : ", type(d), " | Name : ", d.alias)

for r in ds.records:
    print (r)
cgraph = Graph(ds.records)

cgraph.print_nodes()
cgraph.print_edges()
#anp.cgraph.draw_graph()
print ("Topological sort ", cgraph.toposort())
