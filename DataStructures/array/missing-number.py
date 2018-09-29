#Works for positive integer only


def missingNum(array, k):
    temp =[]
    maximum = max(array)

    array.sort()
    for i in range(1, maximum):
        if i not in array :
            temp.append(i)

    while(k != len(temp)):
        maximum += 1
        temp.append(maximum)

    print(temp)


# def missingNum(array, k):
#     array.sort()
#     n = len(array)
#     #find the first positive number
#     i=0
#     while(i<n and array[i]<= 0):
#         i +=1
#
#     count,curr=0,1
#     while(count<k and i<n):
#         if array[i] != curr:
#             print(curr)
#             count +=1
#         else:
#             i +=1
#             curr +=1
#
#     #Find the missing number after maximum
#     while(count<k):
#         print(curr)
#         curr +=1
#         count +=1




# arr = list(map(int, input().split()))
# k = int(input())

arr = [2 ,3, 4]
k = 3

missingNum(arr, k)
