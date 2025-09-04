def paranteheses(arr):
    stack = []
    parenthesis_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    for c in arr:
        if c in parenthesis_dict:
            if stack and stack[-1] == parenthesis_dict[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
print(paranteheses('()'))