# tc= int(input())
# n= int(input())
# size=[]
# ef=[]
# fish=[]
# for i in range(tc):
#     for j in range(n):
#         a,b = map(int, input().split())
#         size.append(a,b)
#         ef.append(b)
#     for k in range(n):
#         for l in range(n):
#             if(size[j]<=ef[i]):
#                 size.remove(size[j])
#                 ef
#         if(size[i]<ef[i]):
#
#     print(size)
#     print(ef)

tc = int(input())
n = int(input())
fish=[]
index=[]
for i in range(n):
    fish.append(input().split())
fish = sorted(fish)
for i in range(len(fish)):
    for j in range(len(fish)):
        if(fish[i][1] >= fish[j][0] and i !=j):
            index.append(j)   #ef>= size

for i in index:
    fish.remove(fish[i])

print(len(fish))
