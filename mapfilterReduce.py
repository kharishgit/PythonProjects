from functools import reduce
lst = [1,2,3,4,5,7,3]
eve = list(filter(lambda x:x%2==0,lst))
print(eve)
dou = list(map(lambda x:x*2,eve))
print(dou)

red = reduce(lambda a,b:a+b,dou)
print(red)