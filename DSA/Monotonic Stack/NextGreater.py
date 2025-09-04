def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)-1,-1,-1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result
numbers = [2, 1, 5, 3]
print(next_greater_element(numbers))
