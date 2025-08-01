def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


print(gcd(48,18))

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
        print(a,b)
    return a
print(gcd(7,13))