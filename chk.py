# a = [2,5,8,10]
# def square(x):
#     return x **2
#
# b= map(square,a)
# print(type(b))
# print(list(b))
# mul = lambda a,b: (a*b, a/b)
# print(mul(7,8))


# t1 = (1,2,3,45,['hiii'])
# print(type(t1[4]))
# t1[4].append('Dude')
# print(t1)

def can_paliandrome(str):
    hash_str = {}
    for ch in str:
        if ch in hash_str:
            hash_str[ch] += 1
        else:
            hash_str[ch] = 1
    freq = 0
    for val in hash_str.values():
        if val % 2 == 1:
            freq+=1
    if freq <=1:
        return True
    else:
        return False

print(can_paliandrome('alabbb'))
