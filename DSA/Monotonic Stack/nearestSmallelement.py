def nearest_element(arr):
    stack = []
    result = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            print(arr[stack[-1]])
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(i)
    return result

print(nearest_element([4, 2, 5, 3, 7]))