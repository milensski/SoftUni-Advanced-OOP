class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.idx = -1

    def __iter__(self):

        return self

    def __next__(self):
        if self.number - 1 == self.idx:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx % len(self.sequence)]


result = sequence_repeat('abc', 1)
for item in result:
    print(item, end='')
