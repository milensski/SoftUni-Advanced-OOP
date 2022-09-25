rows, cols = [int(x) for x in input().split()]

text = input()

counter = 0

for row in range(rows):
    temp = ''
    if row % 2 == 0:
        for col in range(cols):
            temp += text[counter % len(text)]
            counter += 1
        print(temp)
    else:
        for col in range(cols):
            temp += text[counter % len(text)]
            counter += 1
        print(temp[-1::-1])
