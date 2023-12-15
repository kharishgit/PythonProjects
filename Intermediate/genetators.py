# def mygen():
#     yield 1
#     yield 2
#     yield 3
# g=mygen()
# print(sum(g))


def mygen(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b
fib = mygen(30)
for i in fib:
    print(i)