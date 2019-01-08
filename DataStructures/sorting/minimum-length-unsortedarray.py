def printUnsorted(arr, n):
    for s in range(n-1):
        if arr[s] > arr[s+1]:
            break
    
    if s == n-1:
        print("Array is completed sorted")
        exit()

    for e in range (n-1,-1,-1):
        if arr[e] < arr[e-1]:
            break

    print(s)
    print(e)
    min = arr[s]
    max = arr[s]

    for i in range(s+1, e+1):
        if arr[i]<min:
            min = arr[i]
        if arr[i]> max:
            max = arr[i]

    for i in range(s):
        if min < arr[i]:
            s=i

    for j in range(n-1,e,-1):
        if max > arr[j]:
            e = j


    print ("The unsorted subarray which makes the given array") 
    print ("sorted lies between the indexes %d and %d"%( s, e)) 



if __name__ == "__main__":
    arr =[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    arr_size = len(arr)
    printUnsorted(arr, arr_size)