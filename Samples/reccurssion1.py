def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
inp=int(input("Enter a number"))
res = fact(inp)
print(res)