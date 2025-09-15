target_list = [1, 2, 3, 4]
target=3
count=0
for i in range(len(target_list)):
    for j in range(i,len(target_list)):
        x=target_list[i]
        y=target_list[j]
        if y>x:
            x,y = y,x
        if x-y==target:
            count+=1
print(count)
