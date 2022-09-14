N = int(input())

stack = []

for _ in range(N):

    command = input().split()

    key = command[0]

    if key == "1":
        value = int(command[1])
        stack.append(value)
    elif key == "2":
        if stack:
            stack.pop()
    elif key == "3":
        if stack:
            print(max(stack))
    elif key == "4":
        if stack:
            print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=', ')
print(stack.pop(), end='')