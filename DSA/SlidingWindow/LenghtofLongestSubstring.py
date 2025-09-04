# Problem: Longest Substring with At Most K Distinct Characters (LeetCode #340, Medium)
# Description:
#
# Given a string s and an integer k, return the length of the longest substring that contains
# at most k distinct characters.
#
# Example:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The longest substring with at most 2 distinct characters is "ece" (length 3, contains e and c).
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The entire string "aa" has 1 distinct character (a), length 2.
# Input: s = "ccaabbb", k = 2
# Output: 5
# Explanation: Substring "ccaab" has 2 distinct characters (c and a), length 5.


def lengthoflongestsubstringkDistinct(s,k):
    if k==0:
        return 0
    start = 0
    char_count = {}
    max_length = 0
    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0 ) + 1
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start+=1
        max_length = max(max_length,end-start +1)
    return max_length

print(lengthoflongestsubstringkDistinct("eceba", 2))