#hackerank solution for subset 

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

t = int(input())
for i in range(t,0,-1):
    a = int(input())
    s1 = set(map(int, input().split()))

    b = int(input())
    s2= set(map(int, input().split()))

    print(s1.issubset(s2))
