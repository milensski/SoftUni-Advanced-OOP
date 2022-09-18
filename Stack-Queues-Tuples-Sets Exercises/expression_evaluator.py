from collections import deque
import operator

expression = input().split()


ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

numbers_que = deque()
que_operators = deque()

current_result = None

for element in expression:
    if element not in ops:
        if current_result is not None:
            numbers_que.append(int(element))
        else:
            current_result = int(element)
    else:
        while numbers_que:
            number = numbers_que.popleft()
            current_result = ops[element](int(current_result),int(number))

print(int(current_result))

