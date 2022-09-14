expression = input()

stack = []

for idx, element in enumerate(expression):
    if element == '(':
        stack.append(idx)
    if element == ')':
        last_item = stack.pop()
        print(expression[last_item:idx+1])

