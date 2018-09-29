
def maxSum(array):
    max_current = max_global=max_positive= 0
    length = len(array)
    for i in range (length):
        if(array[i] > -1):
            max_positive += array[i]
        max_current = max(array[i] , array[i]+max_current)
        if max_current > max_global:
            max_global = max_current

    print(max_global)
    print(max_positive)





# ip = [1,2,3,4]
ip = [-2, -3, -1, -4, -6]   
# 2 -1 2 3 4 -5

maxSum(ip)
