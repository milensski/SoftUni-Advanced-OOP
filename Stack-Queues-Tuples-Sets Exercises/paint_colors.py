from collections import deque

line = deque(input().split())

colors = ['red', 'yellow', 'blue']
secondary_colors = ["orange", "purple", "green"]

# d yel blu e low redd

found_colors = []

while line:

    if len(line) == 1:

        formed_word = line.pop()
        if formed_word in colors or formed_word in secondary_colors:
            found_colors.append(formed_word)
        continue

    else:
        first_word = line.popleft()
        last_word = line.pop()

        if (first_word + last_word) in colors or (first_word + last_word) in secondary_colors:

            found_colors.append(first_word + last_word)

        elif (last_word + first_word) in colors or (last_word + first_word) in secondary_colors:
            found_colors.append(last_word + first_word)

        else:
            first_skip = False
            last_skip = False

            if len(first_word) < 2:
                first_skip = True
            if len(last_word) < 2:
                last_skip = True

            middle = len(line) // 2

            if not first_skip:
                line.insert(middle, first_word[:-1])
            if not last_skip:
                line.insert(middle, last_word[:-1])

for word in found_colors:
    if word == 'orange':
        if 'red' in found_colors and 'yellow' in found_colors:
            continue
        else:
            found_colors.remove(word)
    elif word == 'purple':
        if 'red' in found_colors and 'blue' in found_colors:
            continue
        else:
            found_colors.remove(word)
    elif word == 'green':
        if 'blue' in found_colors and 'yellow' in found_colors:
            continue
        else:
            found_colors.remove(word)

print(found_colors)
