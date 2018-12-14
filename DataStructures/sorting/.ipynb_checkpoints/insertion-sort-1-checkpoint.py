# https://www.hackerrank.com/challenges/insertionsort1/problem
def insertionSort1(n, arr):

   temp = arr[n-1]
   arr[n-1] = arr[n-2]

   for i in range(n-2, -1 , -1):

       if(temp< arr[i]):
           arr[i+1] = arr[i]
       else:
           arr[i+1] = temp
           print("breaks",*arr)
           break

       print(*arr)
       if i == 0 and arr[i]> temp:
           arr[1] = arr[0]
           arr[0] = temp
           print(*arr)
           # arr[i] = temp
       # result = ','.join(map(str, arr))


if __name__ == '__main__':
    n = 10
    # arr = [2,4,6,8,3]
    # arr= [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23]
    arr =[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    insertionSort1(n, arr)
