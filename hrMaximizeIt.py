
n,m=input().split()
max_list=[]
list = []

# for i in range (int(n)):
#     print("Coming inside")
#     list = input().split()
#     print("Your list is", list)
#     # max.append(max(list))
#
#
# maximum = max(list)
# print("Maixmum of your list is", maximum)
# print(max)

# a = [int(x) for x in input().split()]
# print(max(a))
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10

for i in range (int(n)):
    list = [ int(x) for x in input().split()]
    max_list.append(max(list))
    list.clear()

# print(max_list)

sum = 0

for j in max_list:
    sum = sum + j**2


print(sum % int(m))
