def negative_positive_sum(*args):
    negative_sum = 0
    positive_sum = 0
    for num in args:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num


    return negative_sum, positive_sum

sequence = [int(x) for x in input().split()]



negative_sum, positive_sum = negative_positive_sum(*sequence)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")