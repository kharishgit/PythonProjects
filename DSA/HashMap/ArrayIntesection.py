# Problem 2: Intersection of Two Arrays II (LeetCode #350, Easy)
# Description:
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
# should appear as many times as it appears in both arrays, and you can return the result in any order.
#
# Example:
#
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2, 2]
# Explanation: 2 appears twice in both arrays, so include it twice.
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
# Explanation: 4 and 9 appear once in both arrays (result order doesn’t matter).
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: []
# Explanation: No common elements.





def intersect(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    count = {}
    for num in num1:
        count[num] = count.get(num, 0) + 1
    result = []
    for num in num2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result

print(intersect([1, 2, 2, 1], [2, 2]))          # Output: [2, 2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))    # Output: [4, 9]
print(intersect([1, 2], [3, 4]))