# https://www.hackerrank.com/challenges/quicksort1/problem
def quickSort(arr):
    left=[]
    right=[]
    pivot=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    left.append(pivot)
    return (left+right)

if __name__ == '__main__':
    n = 5

    arr = [4, 5, 3, 7, 2]

    result = quickSort(arr)

    print(result)
