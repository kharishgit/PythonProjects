overlap_list = [(1, 3), (2, 4), (5, 7)]
n=len(overlap_list)
count=0
for i in range(n):
    for j in range(i+1,n):
        if overlap_list[i][0] <= overlap_list[j][1] and overlap_list[j][0]<=overlap_list[i][1]:
            count+=1
print(count)