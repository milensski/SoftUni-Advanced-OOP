from collections import deque
line = deque(list(input()))

stack = []


for _ in range(len(line)):
    element = line.popleft()
    if element == "{" or element == '(' or element == '[':
        stack.append(element)
    elif element == ')' and len(stack) > 0:
        if stack[-1] == '(':
            stack.pop()
    elif element == ']' and len(stack) > 0:
        if stack[-1] == '[':
            stack.pop()
    elif element == '}' and len(stack) > 0:
        if stack[-1] == '{':
            stack.pop()
    else:
        line.append(element)
if len(stack) == 0 and len(line) == 0:
    print("YES")
else:
    print("NO")
