def bubble_sort(arr):
    swap_made = True
    while swap_made:
        swap_made = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap_made = True
    return arr

print(bubble_sort([23,45,12,1020,9]))
