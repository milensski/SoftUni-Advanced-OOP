from collections import deque

bowl_ramen = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while bowl_ramen and customers:

    ramen = bowl_ramen[-1]
    customer = customers[0]

    if ramen == customer:
        bowl_ramen.pop()
        customers.popleft()


    elif ramen > customer:
        bowl_ramen[-1] -= customer
        customers.popleft()

    elif customer > ramen:
        customers[0] -= ramen
        bowl_ramen.pop()

if len(customers) <= 0:
    print('Great job! You served all the customers.')
    if len(bowl_ramen) > 0:
        print(f'Bowls of ramen left: {", ".join(map(str, bowl_ramen))}')

else:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f'Customers left: {", ".join(map(str, customers))}')
