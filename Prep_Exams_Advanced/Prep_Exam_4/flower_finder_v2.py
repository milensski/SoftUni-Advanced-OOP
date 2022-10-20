from collections import deque


def remove_items(test_list, item):
    # remove the item for all its occurrences
    c = test_list.count(item)
    for i in range(c):
        test_list.remove(item)

    return test_list


vowels = deque(input().split())
consonants = deque(input().split())



result = ''

words = ["rose",
         "tulip",
         "lotus",
         "daffodil"
         ]
words_dict = {}

for word in words:
    words_dict[word] = list(word)

word_found = False
while vowels and consonants:

    vow = vowels.popleft()
    cons = consonants.pop()

    for word in words_dict:

        if vow in words_dict[word]:
            remove_items(words_dict[word],vow)
        if cons in words_dict[word]:
            remove_items(words_dict[word],cons)

        if len(words_dict[word]) == 0:
            print(f'Word found: {word}')
            word_found = True
            break
    if word_found:
        break

if not word_found:
    print("Cannot find any word!")

if len(vowels) > 0:
    print(f'Vowels left: {" ".join(vowels)}')
if len(consonants) > 0:
    print(f'Consonants left: {" ".join(consonants)}')
