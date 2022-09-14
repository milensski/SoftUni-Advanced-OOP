import sys
from collections import deque
quantity = int(input())

orders = deque(map(int,input().split()))

max_order = -sys.maxsize

for order in orders:
    if int(order) > max_order:
        max_order = int(order)

while orders:

    if quantity >= orders[0]:
        quantity -= orders[0]
        orders.popleft()
    else:
        break



print(max_order)
if len(orders) > 0:
    print(f'Orders left: {" ".join(list(map(str,orders)))}')
else:
    print("Orders complete")


