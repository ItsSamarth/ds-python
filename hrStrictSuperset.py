#Hackerrank solution for python strict superset

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
#
# super_set = set(map(int, input().split()))
# flag = False
# t = int(input())
# for i in range(t):
#     set1 = set(map(int, input().split()))
#     if(super_set.issubset(set1) and (len(set1) < len(super_set) )):
#         flag = True
#     else:
#         flag = False
#         break
#
# print(flag)

#solution using python generator
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
