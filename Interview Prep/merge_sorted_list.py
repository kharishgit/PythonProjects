def merge_sorted_lists(nums1, nums2):
    return sorted(set(nums1 +nums2))

print(merge_sorted_lists([1, 3, 5],[2, 4, 5]))
