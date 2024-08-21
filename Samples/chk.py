def gen():
    for i in range(5):
        yield i
x=gen()
print(next(x))
print(next(x))
print(next(x))
print(type(gen()))