#Hackerank solution introduction to sets

def average(array):
    arr = set(array)
    print(arr)
    print(sum(arr))
    print(len(arr))



n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
