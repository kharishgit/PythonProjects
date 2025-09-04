# Problem: Maximum Average Subarray I (LeetCode #643, Easy)
# Description:
#
# Given an integer array nums and an integer k, find the maximum average of any contiguous subarray of
# length k. Return the maximum average value.
#
# Example:
#
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: Subarray [12, -5, -6, 50] has sum 12 + (-5) + (-6) + 50 = 51, average = 51 / 4 = 12.75,
# which is the maximum for any subarray of length 4.
# Input: nums = [5], k = 1
# Output: 5.0
# Explanation: Only one subarray of length 1, [5], has average 5 / 1 = 5.0.
# Input: nums = [-1], k = 1
# Output: -1.0
# Explanation: Subarray [-1] has average -1 / 1 = -1.0.

def findMaxAverage(nums,k):
    current_max = sum(nums[:k])
    max_avg = current_max
    for i in range(k,len(nums)):
        current_max = current_max + nums[i] - nums[i-k]
        max_avg = max(max_avg,current_max)
    return max_avg/k

print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))