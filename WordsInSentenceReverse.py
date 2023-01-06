sent = input("Enter the string")
spl = sent.split()
lst1=[]
for word in spl:
    lst1.append(word[::-1])
print(' '.join(lst1))