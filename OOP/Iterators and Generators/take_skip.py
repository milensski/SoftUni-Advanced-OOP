class take_skip:
    COUNT = 0
    TOTAL_RESULT = 0

    def __init__(self, step, count):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if take_skip.COUNT >= self.count:
            raise StopIteration

        result = take_skip.TOTAL_RESULT
        take_skip.TOTAL_RESULT += self.step
        take_skip.COUNT += 1

        return result


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

