import numpy as np
import ad_numpy as anp

a = anp.asarray([1,2,3])
b = anp.asarray([4,5,6])

print ("a ", a, " | b ", b)

c = a + b
d = anp.dot(a, b)

print ("A type : ", type(a), " | Name : ", a.alias)
print ("B type : ", type(b), " | Name : ", b.alias)
print ("C type : ", type(c), " | Name : ", c.alias)
print ("D type : ", type(d), " | Name : ", d.alias)

print ("g.a : ", anp.cgraph.a)
