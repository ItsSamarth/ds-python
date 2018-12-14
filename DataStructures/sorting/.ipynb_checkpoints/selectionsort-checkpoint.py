def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        print(i, arr[i])
        for j in range (i+1, n):
            if arr[j] < arr[min]:
                min = j
            print("minimum=",min)
            
        arr[i],arr[min] = arr[min], arr[i]
        print(arr)
        
    



# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

selectionSort(arr)
