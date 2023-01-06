from itertools import product
a=[1,2,3,4]
b=[9,8,7,6]
res=(product(a,b))
for i in res:
    print(list(i))