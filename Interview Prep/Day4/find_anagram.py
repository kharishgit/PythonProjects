def is_anagram(s,t):
    return sorted(s.lower())==sorted(t.lower())
print(is_anagram("Lis7ten","Silen7t"))



def is_anagram(s, t):
    # Filter alphanumeric characters and convert to lowercase
    s_filtered = [c.lower() for c in s if c.isalnum()]
    t_filtered = [c.lower() for c in t if c.isalnum()]
    # Check lengths first
    if len(s_filtered) != len(t_filtered):
        return False
    # Count frequencies
    freq = {}
    for c in s_filtered:
        freq[c] = freq.get(c, 0) + 1
    for c in t_filtered:
        freq[c] = freq.get(c, 0) - 1
        if freq[c] == 0:
            del freq[c]
    return len(freq) == 0

# Test cases
print(is_anagram("Lis7ten", "Silen7t"))  # Output: True
print(is_anagram("A man!", "Man! a"))     # Output: True
print(is_anagram("Hello", "World"))       # Output: False