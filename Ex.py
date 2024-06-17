# def greet():
#     print("Hii")
# def display(other_fun):
#     print("Entering Display")
#     greet()
# display(greet)
# def foo(value):
#     while True:
#         value = yield(value)
# bar=foo(1)
# print(next(bar))
# print(next(bar))
# print(bar.send(2))
import chk
# print("Hello")
# print(__name__)
# lst=[1,4,2,6,9,10]
# target = 14
# n=len(lst)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if lst[i] + lst[j]==target:
#             print (i,j)

# preMap = {1:0,4:1,2:2}
# print(preMap[4])
#
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the slow-runner pointer
        k = 1

        # Go through the array with the fast-runner pointer
        for i in range(1, len(nums)):
            # If we find a new unique element
            if nums[i] != nums[i - 1]:
                # Move it to the next position of the slow-runner pointer
                nums[k] = nums[i]
                # Increment the slow-runner pointer
                k += 1

        return k


# Example usage
solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(f"The number of unique elements is {k}")
print(f"The modified array is {nums[:k]}")