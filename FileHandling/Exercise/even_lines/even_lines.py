symbols = {"-", ",", ".", "!", "?"}


with open('resources/text.txt', 'r') as file:

    for idx,line in enumerate(file):
        if idx % 2 == 0:
            line_list = []
            for word in line.strip().split():
                for symbol in symbols:
                    if symbol in word:
                        word = word.replace(symbol,'@')
                line_list.append(word)
            line_reversed = list(reversed(line_list))

            with open('resources/output.txt', 'a') as file:
                file.write(' '.join(line_reversed) + '\n')