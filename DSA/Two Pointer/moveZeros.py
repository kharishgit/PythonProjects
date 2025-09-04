# Move Zeroes (LeetCode #283, Easy)
# Description:
#
# Given an integer array nums, move all 0’s to the end of the array while maintaining the relative
# order of the non-zero elements. You must do this in-place without making a copy of the array.
#
# Example:
#
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Explanation: Non-zero elements [1, 3, 12] stay in their relative order, and 0’s are moved to the end.
# Input: nums = [0]
# Output: [0]
# Explanation: Single 0 stays as is.
# Input: nums = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation: No 0’s, so no changes.


def nonZeros(nums):
    non_zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i]= nums[i], nums[non_zero_pos]
            non_zero_pos+=1
    return nums
print(nonZeros([0, 0, 1, 0, 0, 3, 12]))