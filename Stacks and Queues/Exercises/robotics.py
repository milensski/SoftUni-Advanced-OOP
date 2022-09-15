from collections import deque
from datetime import datetime, timedelta

line = deque(input().split(";"))
start_time = input()

time = datetime.strptime(start_time, '%H:%M:%S')


# time = (time + timedelta(seconds=1)).time()

robots = []
products = deque()


while True:
    product = input()

    if product == 'End':
        break

    products.append(product)

while products:
    current_product = products.popleft()
    time = (time + timedelta(seconds=1)).time()

    if line:
        robot = line.popleft()
        name,process_time = robot.split('-')
        robots.append({
            'name': name,
            'process_time': int(process_time),
            'available': time.time()
        })
