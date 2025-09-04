target_list = [1,1,1]
count=0
for i in range(len(target_list)):
    for j in range(i):
        if target_list[i] + target_list[j] == 2:
            count+=1
print(count)