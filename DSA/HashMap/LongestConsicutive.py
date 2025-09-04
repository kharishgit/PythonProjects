# Problem: Longest Consecutive Sequence (LeetCode #128, Medium)
# Description:
#
# Given an unsorted array of integers nums, find the length of the longest consecutive sequence (a sequence of numbers where each number increases by 1, e.g., 1, 2, 3, 4). Return the length of the longest such sequence.
#
# Example:
#
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4], with length 4.
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Explanation: The longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8], length 9.
# Input: nums = []
# Output: 0
# Explanation: Empty array, no sequence.

def longest_consecutive(nums):
    nums = set(nums)
    max_length = 0
    for num in nums:
        if num - 1 not in  nums:
            current_num = num
            current_length = 1
            while current_num + 1 in nums:
                current_num +=1
                current_length +=1
            max_length = max(max_length,current_length)
    return max_length


print(longest_consecutive([100, 4, 200, 1, 3, 2]))        # Output: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # Output: 9
print(longest_consecutive([]))