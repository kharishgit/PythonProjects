lst =[12,34,2,78,10,17]
n=len(lst)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]= lst[j+1],lst[j]
print(lst)