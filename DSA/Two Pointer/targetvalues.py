def find_pair_with_sum(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left] , arr[right]
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return  None

arr = [1, 2, 3, 4, 5, 6]
target = 8
result = find_pair_with_sum(arr, target)  # Output: (2, 6)
print(result)