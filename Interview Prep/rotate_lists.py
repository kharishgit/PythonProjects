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