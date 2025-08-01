# Description: Given a list of integers and an integer k, rotate the list to
# the right by k positions. If k is larger than the list length, the effective rotation is k % len(nums).
#
# Input:
#
#     A list of integers nums.
#     An integer k (number of positions to rotate).
#
# Output:
#
#     The rotated list (modify the input list in-place or return a new list).

# Input: nums = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
# Explanation: Rotate right by 2: [1,2,3,4,5] → [5,1,2,3,4] → [4,5,1,2,3].
#
# Input: nums = [1, 2, 3], k = 4
# Output: [3, 1, 2]
# Explanation: Effective rotation is k % len(nums) = 4 % 3 = 1, so rotate right by 1.



#Optimal solution
def rotate_list(nums, k):
    if not nums:
        return nums
    length = len(nums)
    k = k % length  # Effective rotation
    if k == 0:
        return nums
    result = nums[-k:] + nums[:-k]
    return result

def rotate_list(nums,k):
    l = len(nums)
    if k>l:
        k=k%l

    v = nums[k+1:] + nums[:k+1]
    return v


print(rotate_list([1, 2, 3],4))