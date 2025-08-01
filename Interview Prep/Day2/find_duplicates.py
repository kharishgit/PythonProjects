def find_duplictes(nums):
   hash = {}
   for n in nums:
       hash[n]= hash.get(n,0)+1
   dup =[]
   for k,v in hash.items():
       if v>1:
           dup.append(k)
   return dup
print(find_duplictes([4, 3, 2, 7, 8, 2, 3, 1]))

## Optimal code
def find_duplicates(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    duplicates = [k for k, v in freq.items() if v > 1]
    return sorted(duplicates)
