a=[1,3,5,7,9,12,15,18]
target = 3
l = len(a)
ans = -1
start = 0
end = l-1
while start <= end:
    mid = (start + end) // 2
    if a[mid]==target:
        ans = mid
        break
    elif a[mid] > target:
        end = mid -1
    elif a[mid] < target:
        start = start + 1
print(ans)