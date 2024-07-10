import numpy as np
array = np.array([1,3,4,33,67,44,74,26,84,45,34,22,57])
# newarr = np.sort(array)
# print(newarr[len(array)-1] * newarr[len(array)-2] )


max1,max2 = 0 , 0
for num in array:
    if num > max1:
        max2=max1
        max1=num
    elif num <max1 and num > max2:
        max2=num

print(max1 * max2)

