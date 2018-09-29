# Ways to implement
# 1 - Bruteforce solution O(N^2)
#2- Kadene Algorithm  O(N)

# IMPLEMENTATION USING KADANE Algorithm
def maxSubArraySum(arr, length):
    max_global = max_current = 0
    for i in range(length):
        max_current = max(a[i], a[i]+max_current)
        if max_current > max_global:
            max_global = max_current

    print(max_global)
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# a = [-2, -3, -1, -4, -6]
a = [1,2,3,4]
maxSubArraySum(a,len(a))
