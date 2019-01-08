# Python program for implementation of heap Sort 
def heapify(arr, n, i):
    largest = i
    left = 2*i +1
    right = 2*i +2

    #see if left child of the root exists and it is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # see if right child of the root exists and it is greater than root
    if right < n and  arr[largest] < arr[right]:
         largest = right

    #swap root if needed 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest)


def heapSort(arr):
    n = len(arr)

    #build max heap
    for i in range(n,-1,-1):
        # print(i)
        heapify(arr, n, i)

    # one by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0]= arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print("The sorted array is")
    for i in range(len(arr)):
        print(arr[i])