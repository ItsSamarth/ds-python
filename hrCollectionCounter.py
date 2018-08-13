#Hackerrank solution for collection counter

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50


#200
from collections import Counter

total_shoes = int(input())
shoes_list = list(map(int, input().split()))
total_customers = int(input())
counter_list = Counter(shoes_list)
sum=0
for i in range(total_customers):
    size, price = map(int, input().split())
    if counter_list[size] > 0:
        print(counter_list[size])
        counter_list[size] -=1
        sum = sum + price
        print("sum", sum)

print(sum)
