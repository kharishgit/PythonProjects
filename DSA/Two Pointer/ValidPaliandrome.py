import re
def ispaliandrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
    cleaned = cleaned.lower().strip()
    left = 0
    right = len(cleaned) - 1
    while left <= right:
        if cleaned[left]==cleaned[right]:
            left+=1
            right-=1

        else:
            return False
    return True

print(ispaliandrome("A man, a plan, a canal: Panama"))

