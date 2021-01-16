
import numpy as np

a=3.09700e+03
b=8.55900e+03
c=3.66200e+03
d=[[a,b,c]]
# d[0][0]=int(d[0][0])
# print(d[0][0])
# print(type(d[0][0]))
# print(d)

d=np.array([[a,b,c]]).tolist()
print(d)
print(type(d))
print(type(d[0][0]))
#
# d.astype(np.float)
#
d[0][0]=int(d[0][0])
print(d[0][0])
print(type(d[0][0]))
print(d)

# a=[[3.09700e+03, 8.55900e+03, 3.66200e+03]]