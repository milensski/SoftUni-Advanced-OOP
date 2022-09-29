def operate(*args):
    operator = args[0]

    def add():
        return sum(args[1::])

    def diff():
        result = 0
        for num in args[1::]:
            result -= num
        return result

    def multyply():
        result = 1
        for arg in args[1::]:
            result *= arg
        return result

    def divide():
        result = 1
        for arg in args[1::]:
            result /= arg
        return int(result)

    if operator == '+':
        return add()
    elif operator == '-':
        return diff()
    elif operator == '*':
        return multyply()
    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))

print(operate("/", 1, 4))
