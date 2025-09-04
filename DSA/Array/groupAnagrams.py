# Given an array of strings strs, group all the anagrams together. You can return the answer in
# any order. An anagram is a word formed by rearranging the letters of another word, typically using all the
# original letters exactly once.
# Example:
#
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Explanation: "eat", "tea", and "ate" are anagrams (same letters: e, a, t); "tan" and "nat" are
# anagrams (t, a, n); "bat" stands alone.
#
# Constraints:
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.



def groupangram(strs):
    sorted_hash={}
    for s in strs:
        freq = [0] * 26
        for char in s:
            freq[ord(char)-ord('a')]+=1
        keys=tuple(freq)
        if keys in sorted_hash:
            sorted_hash[keys].append(s)
        else:
            sorted_hash[keys]=[s]
    return list(sorted_hash.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupangram(strs))


def groupAnagrams(strs):
    # Create a dictionary to store sorted string -> list of anagrams
    anagram_map = {}

    # Iterate through each string in the input list
    for s in strs:
        # Sort the characters of the string to use as a key
        sorted_s = ''.join(sorted(s))  # e.g., "eat" -> "aet"

        # If the sorted string is already a key, append the original string
        # If not, create a new list with the original string
        if sorted_s in anagram_map:
            anagram_map[sorted_s].append(s)
        else:
            anagram_map[sorted_s] = [s]

    # Return all the grouped anagrams as a list of lists
    return list(anagram_map.values())


# Test it
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
