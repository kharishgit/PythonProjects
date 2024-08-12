def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

# print(selection_sort([4,3,67,2,1]))
numbers = [3, 1, 4, 2]
selection_sort(numbers)
print(numbers)