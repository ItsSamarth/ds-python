# Ways to implement
# 1 - Bruteforce solution O(N^2)
#2- Kadene Algorithm  O(N)

# IMPLEMENTATION USING KADANE Algorithm
def maxSubArraySum(arr, length):
    max_global = max_current = arr[0]
    for i in range(length-1):
        max_current = max(a[i], a[i]+max_current)
        if max_current > max_global:
            max_global = max_current

    print(max_global)
    
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a,len(a))
