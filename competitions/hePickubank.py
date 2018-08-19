tc = int(input())
for i in range(tc):
     d,a,m,b,x = map(int, input().split())
     x=x-d
     temp = x// ((m*a)+b)
     div =( x % ((m*a)+b) )
     if div % a == 0:
         temp2 = div // a
     else:
         temp2 = div//a +1
     print((m+1)*temp + temp2 )
