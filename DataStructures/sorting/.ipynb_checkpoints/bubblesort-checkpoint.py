def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]> arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    
    print(arr)





# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]),  
