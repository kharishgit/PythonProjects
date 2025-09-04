def has_duplicates(nums):
    # Outer loop for first number
    for i in range(len(nums)):
        # Inner loop for second number (after i)
        for j in range(i + 1, len(nums)):
            # If numbers match, we found a duplicate
            if nums[i] == nums[j]:
                return True
    # No duplicates found
    return False

# Test the function
nums = [1, 2, 3, 2]
result = has_duplicates(nums)
print(result)  # Should print True