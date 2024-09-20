def can_paliandrome(str):
    hash_str = {}
    for ch in str:
        if ch in hash_str:
            hash_str[ch] += 1
        else:
            hash_str[ch] = 1
    freq = 0
    for val in hash_str.values():
        if val % 2 == 1:
            freq+=1
    if freq <=1:
        return True
    else:
        return False

print(can_paliandrome('alabblc'))