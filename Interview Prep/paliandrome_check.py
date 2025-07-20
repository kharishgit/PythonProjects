def is_paliandrome(s):
    words = []
    for chr in s:
        if chr.isalnum():
            words.append(chr.lower())
    return words == words[::-1]


if __name__ == '__main__':
    print(is_paliandrome("A man, a plan, a canal: Panama"))
    print(is_paliandrome("0P"))

##Optimal solution

def palindrome(s):
    filtered = [c.lower() for c in s if c.isalnum() ]
    return filtered == filtered.reverse()

if __name__ == '__main__':
    print(is_paliandrome("A man, a plan, a canal: Panama"))

##Two pointer

def is_palindrome(s):
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
    return True
if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
