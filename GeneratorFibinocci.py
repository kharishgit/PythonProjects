def fibinocci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,b+a
x=fibinocci(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# for i in fibinocci(50):
#     print(i)
