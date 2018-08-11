#Hackerank solution to symmetric difference

#input
# 4
# 2 4 5 9
# 4
# 2 4 11 12

#output
# 5
# 9
# 11
# 12

a = int(input())
set1 = set(map(int, input().split()))

b = int(input())
set2 = set(map(int, input().split()))

output = set1 ^ set2
print(output)
for i in output:
    print(i)
