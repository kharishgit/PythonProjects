def product(nums):
    n = len(nums)
    answer=[1]*n
    for i in range(1,n):
        answer[i]=answer[i-1] * nums[i-1]
    right_product = 1
    for i in range(n-1,-1,-1):
        answer[i]*=right_product
        right_product*=nums[i]
    return answer




nums = [1, 2, 3, 4]
print(product(nums))


def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n

    # Left products
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    print("L",left)
    # Right products
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    print("R",right)
    # Combine
    return [left[i] * right[i] for i in range(n)]


# Test it
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]