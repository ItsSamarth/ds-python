def insertionSort(arr):
    n = len(arr)
    for i in range (n):
        sorted = arr[i]
        j = i-1
        
        while j>= 0 and sorted<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = sorted
    print(arr)



# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

insertionSort(arr)




