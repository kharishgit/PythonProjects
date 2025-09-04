def calculate(s):
    stack = []
    num = 0
    result = 0
    sign = 1
    i=0
    while i<len(s):
        char = s[i]
        if char.isdigit():
            num = (num * 10) +int(char)
        elif char in '+-':
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            stack.append((result,sign))
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            prev_result, prev_sign = stack.pop()
            result = prev_result + prev_sign * result
        i+=1
    result += sign * num
    return result

print(calculate('(1+(4+5+2)-3)+(6+8)'))