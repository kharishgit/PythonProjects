num_list=[2,4,6]
count=0
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        count=count+(num_list[i] * num_list[j])
print(count)