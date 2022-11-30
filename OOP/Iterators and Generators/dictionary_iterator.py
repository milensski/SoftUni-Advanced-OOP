class dictionary_iter:
    INDEX = 0

    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.dictionary) <= dictionary_iter.INDEX:
            raise StopIteration

        result = self.dictionary[dictionary_iter.INDEX]

        dictionary_iter.INDEX += 1

        return result


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
