def words_sorting(*args):
    words = {}

    for word in args:

        value = sum([ord(char) for char in word])

        words[word] = value

    result = ''

    if sum(words.values()) % 2 != 0:
        for key,value in sorted(words.items(), key= lambda x: -x[1]):
            result += f'{key} - {value}\n'
    else:
        for key,value in sorted(words.items()):
            result += f'{key} - {value}\n'


    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
