def twoSum(nums , target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target-num in hash_map:
            return hash_map[target-num],i
        hash_map[num] = i
    print(hash_map)
print(twoSum([3,4,5,1],8))