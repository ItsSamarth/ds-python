# https://www.hackerrank.com/challenges/insertionsort2/problem?h_r=next-challenge&h_v=zen


def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]< arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        print(arr)


if __name__ == '__main__':
    n = 6

    arr = [1, 4, 3, 5, 6, 2]

    insertionSort2(n, arr)
