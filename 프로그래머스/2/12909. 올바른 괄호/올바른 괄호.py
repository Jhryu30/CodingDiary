def solution(s):
    answer = True
    stack = []
    s = list(s)
    for current in s:
        if current=='(':
            stack.append(current)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top==current:
                return False
    if stack:
        return False
    return True