class countdown_iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.n = self.count

        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration

        result = self.n
        self.n -= 1
        return result



iterator = countdown_iterator(10)

for item in iterator:
    print(item, end=' ')

print()

for item in iterator:
    print(item, end=' ')