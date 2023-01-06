import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr=[]
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return  sorted_arr

res=heap_sort([12,34,2,23,7])
print(res)
