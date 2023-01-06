##MACHINE TEST##

str1 = "a134i4j2"
str2=''

lst2=list(str1)
l=len(str1)
for i in range(l):
    if str1[i].isalpha():
        str2+='a'
    else:
        str2+=str1[i]
l=(list(str2))
g="".join(l).split('a')
print(g)
for i in g:
    if i !='':
       v=int(i)
       print(v)
       if v//10 >1 and v%2==0:
            print("True")
       else:
           print("False")







