#Program to find noble integer inside the array
#Noble Integer - Count of greater elements is equal to value



#Double loop iteration O(n^2)
def nobleInteger(array, length):
    for i in range(0,length):
        count = 0
        for j in range(0, length):
            if(array[i] < array[j]):
                count +=1

        if(count == array[i]):
            print('Noble Integer', array[i])



#Efficient way - array(size) - index - 1 = number
#Complexity Reduced - O(nlogn)

a = [6,1,2,4]
nobleInteger(a, len(a))
