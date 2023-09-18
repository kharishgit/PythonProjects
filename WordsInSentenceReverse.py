sent = input("Enter the string")
spl = sent.split()
print(spl)
lst1=[]
for word in spl:
    lst1.append(word[::-1])
print(' '.join(lst1))


