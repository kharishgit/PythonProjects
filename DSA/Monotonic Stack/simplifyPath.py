def simplifyPath(path):
    stack = []
    for token in path.split('/'):
        if token == '' or token == '.':
            continue
        elif token == '..':
            if stack:
                stack.pop()
        else:
            stack.append(token)
    return '/' + '/'.join(stack)

print(simplifyPath("/a/./b/../../c/"))