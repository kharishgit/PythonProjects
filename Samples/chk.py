
a=[2,5,1,0,23,6]
l = len(a)
for i in range(l):
        # print(a[i])
    for j in range(i+1, l):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)