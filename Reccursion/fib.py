hash = {0:0,1:1}

def fib(n):
    if n in hash:
        return hash[n]
    hash[n]=fib(n-1) + fib(n-2)
    return hash[n]

print(fib(45))