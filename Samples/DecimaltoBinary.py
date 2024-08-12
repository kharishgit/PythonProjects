# int(bin(20).replace('0b',""))
 


def decimalToBinary(n):
    l = []
    while n > 0:
        rem = n % 2
        l.append(rem)
        n = n // 2
    return (l[::-1])

print(decimalToBinary(20))