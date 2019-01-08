# Search in an almost sorted array

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
# Output: 2 
# Output is index of 40 in given array

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
# Output: -1
# -1 is returned to indicate element is not present

def binarySearch(arr, left,right,key):
    if right >= 1:
        mid = int(left + (right - 1)/2)

        if arr[mid] == key:
            return mid

        if (mid > left and arr[mid-1] == key):
            return (mid-1)
        
        if (mid < right and arr[mid+1] == key):
            return (mid+1)

        if(arr[mid] > key):
            return binarySearch(arr, left, mid-2, key)

        if(arr[mid] < key):
            return binarySearch(arr, mid+2, right, key)

    return -1



if __name__ == "__main__":
    arr = [3, 2, 10, 4, 40] 
    n = len(arr)
    key = 4

    result = binarySearch(arr, 0, n-1,key) 

    if result == -1:
        print('Element is not present in the array')

    else:
        print('Element is present at index', result)