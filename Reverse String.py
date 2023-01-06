str1="Aswathy"
r=(reversed(str1))
op=''.join(r)
print(op)



#Using While
i = len(str1)-1
op=''
while i >= 0:
    op=op+(str1[i])
    i-=1
print(op)