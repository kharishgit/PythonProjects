def subarraySum(nums, k):
    prefix_sum = {0:1}
    count = 0
    new_sum = 0
    for num in nums:
        new_sum +=num
        if (new_sum-k) in prefix_sum:
            count += prefix_sum[new_sum-k]
        prefix_sum[new_sum] = prefix_sum.get(new_sum,0)+1
    return count

print(subarraySum([1, 1, 1], 2))          # Output: 2
print(subarraySum([1, 2, 3], 3))          # Output: 2
print(subarraySum([1, -1, 0], 0))         # Output: 3