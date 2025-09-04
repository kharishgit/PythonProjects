def binary_search(nums ,val):
   left, right = 0, len(nums)-1
   while left<=right:
       mid = (left+right)//2
       if val == nums[mid]:
           return mid
       elif nums[mid] > val:
           right = mid - 1
       else:
           left = mid + 1
   return -1

print(binary_search([3,5,7,9,12,23,45],23))