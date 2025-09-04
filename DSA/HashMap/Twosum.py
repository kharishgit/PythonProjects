def twoSum(nums , target):
    hash_map = {}
    for i, num in enumerate(nums):
        print(hash_map)
        if (target-num) in hash_map:
            return hash_map[target-num],i
        hash_map[num] = i

print(twoSum([3,4,5,1],8))


def twoSum(nums, target):
    # Create an empty dictionary to store number:index pairs
    hash_map = {}

    # Loop through the array with index
    for i in range(len(nums)):
        # Calculate the complement needed
        complement = target - nums[i]

        # If complement exists in hash_map, we found a pair
        if complement in hash_map:
            return [hash_map[complement], i]

        # Otherwise, add the current number and its index to hash_map
        hash_map[nums[i]] = i

    # If no solution is found (though problem guarantees one)
    return []  # This line won't run given the problem constraints


# Test it
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]