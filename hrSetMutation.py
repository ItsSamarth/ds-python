#hackerank solution for set mutations
#input
 # 16
 # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 # 4
 # intersection_update 10
 # 2 3 5 6 8 9 1 4 7 11
 # update 2
 # 55 66
 # symmetric_difference_update 5
 # 22 7 35 62 58
 # difference_update 7
 # 11 22 35 55 58 62 66

 # output
 # 38
#


_ = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd, _ = input().split()
    s2 = set(map(int, input().split()))
    if(cmd == "intersection_update"):
        s1.intersection_update(s2)
    elif(cmd == "update"):
        s1.update(s2)
    elif(cmd == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(cmd == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))
# 
# a = int(input())
# s1 = set(map(int, input().split()))
# n = int(input())
#
# for i in range (n):
#     operation, i = input().split()
#     s2 = set(map(int, input().split()))
#
#     if(operation == 'intersection_update'):
#         s1.intersection_update(s2)
#     elif(operation == 'update'):
#         s1.update(s2)
#     elif(operation == 'symmetric_difference_update'):
#         s1.update(s2)
#     elif(operation == 'difference_update'):
#         s1.difference_update(s2)
#
#
# print(sum(s1))
