n,m  = map(int, input().split())
arr  = input().split()
set1 =  set(input().split())
set2 = set(input().split())
happiness = 0

for i in range(n):
    if(arr[i] in set1):
        happiness+=1
    elif(arr[i] in set2):
        happiness-=1

print(happiness)
