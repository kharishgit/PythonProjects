def bubble_sort(arr):
    for i in range(len(arr)-1):

        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
    return arr
print(bubble_sort([6,3,8,2,1]))