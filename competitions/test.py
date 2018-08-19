tc = int(input())

for i in range(tc):
    sum=0
    count=0
    months=0
    d,a,m,b,x = map(int, input().split())
    while(d<x):
        # print("coming inside")
        rem = (x-d)//a
        if(rem > m):
            print("1st section")
            d=d+a*m+b
            months +=m+1
        else:
            print("2nd sec")
            if rem==0:
                d=d+a*1
                months += 1
            else:
                d=d+a*rem
                months += rem
        print(d)
        print("months",m)
    print(months)
