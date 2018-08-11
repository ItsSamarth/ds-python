#Hackerrank solution for set union operation
#input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

#output
# 13

a = int(input())
set1 = set(map(int, input().split()))

b = int(input())
set2 = set(map(int, input().split()))

print(set1|set2)
print(set1 ^ set2)

print(len(set1 | set2))
