tc= int(input())
n= int(input())
size=[]
ef=[]
fish=[]
for i in range(tc):
    for j in range(n):
        a,b = map(int, input().split())
        size.append(a,b)
        ef.append(b)
    print(size)
    print(ef)
