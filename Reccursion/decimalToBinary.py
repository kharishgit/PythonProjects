def decimalToBinary(n):
    if n==0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(1023))