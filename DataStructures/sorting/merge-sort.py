# Python program for implementation of MergeSort
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftArray = arr[:mid]
        rightArray = arr[mid:]

        MergeSort(leftArray)
        MergeSort(rightArray)

        i=j=k=0
        while i<len(leftArray) and j< len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i+=1
            else:
                arr[k] = rightArray[j]
                j+=1

            k+=1
        while i< len(leftArray):
            arr[k] = leftArray[i]
            i+=1
            k+=1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j+=1
            k+=1



if __name__ == "__main__":
    arr=[38,27,43,3,9,82,10]
    MergeSort(arr)

    print('Array after merge sort')
    print(arr)