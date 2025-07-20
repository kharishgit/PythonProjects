def find_substring(s, p):
    l1=len(s)
    l2=len(p)
    if l2>l1:
        return -1
    for i in range(l1):
        if p == s[i:i+l2]:
            return i
    return -1

print(find_substring("hello","ll"))



def find_substring(s, p):
    len_s = len(s)
    len_p = len(p)
    if len_p > len_s:
        return -1
    for i in range(len_s - len_p + 1):
        if s[i:i + len_p] == p:
            return i
    return -1

# Test cases
print(find_substring("hello", "ll"))      # Output: 2
print(find_substring("python", "xyz"))    # Output: -1
print(find_substring("aaa", "aa"))        # Output: 0





