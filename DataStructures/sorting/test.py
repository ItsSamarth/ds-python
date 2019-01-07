

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        leftArray = arr[:mid]
        rightArray = arr[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        # print(leftArray)
        # print(rightArray)
        i = j =k =0

        #copy data to temp array left and right
        print(leftArray)
        print(rightArray)
        while i< len(leftArray) and j< len(rightArray):
            print(leftArray[i]) 
            print(rightArray[j])
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i+=1
            else:
                arr[k] = rightArray[j]
                j+=1

            k+=1
        #check if any element is left
        while i < len(leftArray):
            arr[k] = leftArray[i]
            i+=1
            k+=1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j+=1
            k+=1
            
           
        

if __name__ == '__main__':
    arr = [12,11,13,5,6,7]
    print('Given array is', end='\n')
    print(arr)
    mergeSort(arr)
