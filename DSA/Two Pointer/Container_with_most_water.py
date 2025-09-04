# Problem: Container With Most Water (LeetCode #11, Medium)
# Description:
#
# Given an integer array height where height[i] represents the height of a vertical line at index i,
# find two lines that, together with the x-axis, form a container that holds the most water.
# The container’s width is the distance between the indices, and its height is the minimum of the two
# line heights. Return the maximum area of water the container can hold.
#
# Example:
#
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: Choose lines at indices 1 (height[1] = 8) and 8 (height[8] = 7).
# Width = 8 - 1 = 7, Height = min(8, 7) = 7, Area = 7 * 7 = 49.
# No other pair of lines holds more water.
# Input: height = [1, 1]
# Output: 1
# Explanation: Width = 1 - 0 = 1, Height = min(1, 1) = 1, Area = 1 * 1 = 1.
# Input: height = [4, 3, 2, 1, 4]
# Output: 16
# Explanation: Choose indices 0 (height[0] = 4) and 4 (height[4] = 4).
# Width = 4 - 0 = 4, Height = min(4, 4) = 4, Area = 4 * 4 = 16.
# Constraints:
#
# 2 <= height.length <= 10^5
# 0 <= height[i] <= 10^4



def maxareawater(height):
    left = 0
    right = len(height) - 1
    maxarea = 0
    while left <= right:
        width = right - left
        area = width * min(height[right], height[left])
        maxarea = max(maxarea, area)
        if height[left] <= height[right]:
            left+=1
        else:
            right-=1
    return maxarea

print(maxareawater([4, 3, 2, 1, 4]))