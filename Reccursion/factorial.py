def factorial(n):
    assert n>=0 and  int(n)==n, 'The number must be positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(3))
except Exception as e:
    print(e)