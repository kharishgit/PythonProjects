# s='AAAHHHJNHYUIKLLLLKKKKJIII'
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# print(l)
# for ch in l:
#     print('{} occurs {} times in input'.format(ch,s.count(ch)))

# s='AAAHHHJNHYUIKLLLLKKKKJIII'
# d={}
# for ch in s:
#     d[ch] = d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print(k,v)


# s="AABCDADC"
# d={}
# output=''
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#     output=output+str(v)+k
# print(output)

# s='ABCCDAABBBD'
# d={}
# op=''
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#     op=op+k+str(v)
# print(op)

# squares = {x: x ** 2 for x in range(1, 6)}
# print(squares)

s='ajilksdjoeunknsioUU'
d={}
v={'a','e','i','o','u','A','E','I','O','U'}
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(k,v)

