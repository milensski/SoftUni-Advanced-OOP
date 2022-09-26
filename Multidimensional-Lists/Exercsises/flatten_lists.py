text = input().split('|')


sub_list = []

for sub in text[::-1]:
    sub_list.extend(sub.split())

print(*sub_list)

