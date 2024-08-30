import itertools


def max_num(cost, coupon):
    new_list = [int()]
    nums = len(cost)
    max_list = [int()]
    index = 0
    for i in range(nums):
        if cost[i] >= 100:
            break
        else:
            new_list.append(cost[i])
            index = len(new_list)
    for i in range(coupon):
        if len(new_list) > 0:
            maxim = max(new_list)
            max_list.append(maxim)
            del new_list[new_list.index(maxim)]
        else:
            break
    new_list.clear()
    del cost[0:index]
    return max_list


coupon = 0
a = 0
m = 0
n = int(input())
count = 0
cost = [int(input()) for i in range(n)]
summa = [int()]
max_cost = [int()]


for i in range(len(cost)):
    if cost[i] < 100:
        a = cost[i]
        summa.append(a)
        coupon = 1
        count = count+1
    else:
        a = cost[i]
        summa.append(a)
        coupon = 1
        count = count+1
        break
for i in range(count):
    cost.pop(0)
for lunch in cost:
    if lunch >= 100:
        coupon = coupon+1
for i in range(1, coupon+1):
    max_cost.append(max_num(cost, i))
max_cost.pop(0)
new_list = list(itertools.chain.from_iterable(max_cost))
max_lunch = [int()]
for i in range(coupon):
    mm = max(new_list)
    max_lunch.append(mm)
    del new_list[new_list.index(mm)]

print(max_lunch)










