str1= input("Enter string")
spl = str1.split()
print(spl)
lst1=[]
l=len(spl)
print(l)
for i in range(l):
    if i %2 ==1:
        lst1.append(spl[i][::-1])
    else:
        lst1.append(spl[i])
print(' '.join(lst1))