N = int(input())

journal = {}

for _ in range(N):
    student, grade = input().split()
    grade = round(float(grade), 2)

    if student not in journal:
        journal[student] = []

    journal[student].append(grade)

for student, grades in journal.items():
    avg = sum(grades) / len(grades)

    grades_to_string = [f'{grade:.2f}' for grade in grades]

    print(f'{student} -> {" ".join(grades_to_string)} (avg: {avg:.2f})')
