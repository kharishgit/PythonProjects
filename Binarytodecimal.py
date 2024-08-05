def binaryToDecimal(s):
    i=0
    result = 0
    for dig in s[::-1]:
        result = result + int(dig) * (2 ** i)
        i+=1
    return result

print(binaryToDecimal("10100"))
