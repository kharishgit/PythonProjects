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

####  Another Method #######


# def sort (nums):
#     for i in range (len (nums ) -1 ,0 ,-1):
#         for j in range (i) :
#             if nums [j] >nums[j + 1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#
#
# nums = [5, 3, 8, 6, 7, 2]
# sort(nums)
# print(nums)