from collections import deque

eggs = deque(map(int, input().split(', ')))  # !20!, 13, -7, 7
papers = deque(map(int, input().split(', '))) # 10, 5, 20, 15, 7, !9!


count_boxes = 0

while eggs and papers:

    egg = eggs[0]
    paper = papers[-1]

    if egg <= 0:
        eggs.popleft()
        continue

    if egg == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    if egg + paper > 50:
        eggs.popleft()
        papers.pop()
        continue

    if egg + paper <= 50:
        count_boxes += 1
        eggs.popleft()
        papers.pop()
        continue


if count_boxes > 0:
    print(f'Great! You filled {count_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")


if len(eggs) > 0:
    print(f'Eggs left: {", ".join(map(str,eggs))}')
if len(papers) > 0:
    print(f'Pieces of paper left: {", ".join(map(str,papers))}')

