# Given an integer array nums and an integer k, return the k most frequent elements. You can
# return the answer in any order.
# Example:
#
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time. The top 2 frequent elements are 1 and 2.
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It’s guaranteed that the answer is unique (i.e., there are enough distinct elements).


def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3,3,3,3],2))




def topKFrequent(nums,k):
    freq={}
    for n in nums:
        freq[n]=freq.get(n,0)+1
    sorted_val = sorted(freq.keys(),key= lambda x:freq[x],reverse=True)
    return sorted_val[:k]

print(topKFrequent([1,1,1,2,2,3,3,3,3],2))