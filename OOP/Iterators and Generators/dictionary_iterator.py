class dictionary_iter:


    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if len(self.dictionary) <= self.n:
            raise StopIteration

        result = self.dictionary[self.n]

        self.n += 1

        return result


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)