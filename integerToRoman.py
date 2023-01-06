def intToRom(num:int)->str:
    lookup = {
        'I': 1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000,

    }
    op=[]
    for k,v in reversed(lookup.items()):
        while num > 0:
            if v <= num:
                op.append(k)
                num-=v
            else:
                break
    return "".join(op)
res=intToRom(1051)
print(res)
