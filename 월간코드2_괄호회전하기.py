from collections import deque


def check(lst):
    stack = []
    for i in range(len(lst)):
        if len(stack) == 0:
            if lst[i] == '[' or lst[i] == '{' or lst[i] == '(':
                stack.append(lst[i])
            else:
                return False
        else:
            if lst[i] == '[' or lst[i] == '{' or lst[i] == '(':
                stack.append(lst[i])
            elif lst[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif lst[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif lst[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(q)):
        if check(q):
            answer += 1
        temp = q.popleft()
        q.append(temp)
    return answer