# https://www.hackerrank.com/challenges/quicksort2/problem
def partition(arr):
    pivot = arr[0]
    low=[]
    high=[]
    for i in range (1,len(arr)):
        if arr[i] < pivot:
            low.append(arr[i])
        elif arr[i] > pivot:
            high.append(arr[i])
    return low,pivot,high

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    low, pivot, high = partition(arr)
    # print(low)
    # print(high)
    print(low+ [pivot]+high)
    return quick_sort(low)+[pivot]+quick_sort(high)


m = 7
ar = [5, 8, 1, 3, 7, 9, 2]
print(quick_sort(ar))
