
def fibonacci():
    num = 0
    current_num = 1
    while True:
        yield num

        num, current_num = current_num, num + current_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
