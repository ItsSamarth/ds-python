from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
print(d)
d['something-else'].append('non-relevent')
d['python'].append('language')

for i in d.items():
    print(i)


#INPUT

# 5 2
# a
# a
# b
# a
# b
# a
# b

#OUTPUT
# 1 2 4
# 3 5

# n,m=map(int, input().split())
# group1, group2 = list() , list()
# for i in range(n):
#     group1.append(input())
#
# for j in range(m):
#     group2.append(input())
#
# d = defaultdict(group1)
# print("Output starts from here")
# for i in group1:
#     if i in d:
#         print(" ".join(map(str, d[i])))
#
#     else:
#         print(-1)


n, m = map(int, input().split())
group1 = defaultdict(list)
group2 =[]

for i in range(n):
    group1[input()].append(i+1)

for i in range(m):
    group2.append(input())

for i in group2:
    if i in group1:
        print(" ".join(map(str, group1[i])))
    else:
        print -1
