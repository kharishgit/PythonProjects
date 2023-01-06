str1="adfnjkjdfjnfsjdfjksdfjhiuwewjndjjjjrrr"
lst1=list(str1)
res={}
for i in range(len(lst1)):
    cnt = 0
    for j in range(0,i+1):
        if lst1[i]==lst1[j]:
            cnt+=1

    res[lst1[i]]=cnt
print(res)