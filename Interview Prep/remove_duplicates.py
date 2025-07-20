# def remove_duplicates(nums):
#     hash = {}
#     for i in nums:
#         if isinstance(i,int):
#             hash[i]=hash.get(i,0)+1
#     return len(hash.keys())
#
# print(remove_duplicates([1, 1, 2, 2, 3]))


def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:

            nums[write] = nums[read]
            write += 1
    return write

# Test cases
nums = [1, 1, 2, 2, 3]
print(remove_duplicates(nums))  # Output: 3
print(nums[:3])                # Output: [1, 2, 3]
nums = [0, 0, 0]
print(remove_duplicates(nums))  # Output: 1
print(nums[:1])                # Output: [0]