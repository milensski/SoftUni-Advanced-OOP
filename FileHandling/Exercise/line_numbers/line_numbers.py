content = ''
symbols = {"-", ",", ".", "!", "?", '\''}

with open('./resources/text.txt', 'r') as file:
    for idx, line in enumerate(file):
        punctoation = 0
        letters = list(line.strip().replace(' ', ''))
        count_letter = 0
        for letter in letters:
            if letter in symbols:
                punctoation += 1
            else:
                count_letter += 1

        content += f'Line{idx + 1}: {line.strip()} ({count_letter})({punctoation})\n'

with open('./resources/output.txt', 'w') as file:
    file.write(content)
