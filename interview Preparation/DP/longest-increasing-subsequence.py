# O(N^2)complexity
global maximum


def _lis_substruct(arr, n):

    global maximum

    if n == 1:
        return 1

    # maxendingHere is the length  of lis ending with arr[n-1]
    maxEndingHere = 1
    for i in range(1, n):
        res = _lis_substruct(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis_substruct(arr):
    global maximum

    n = len(arr)

    maximum = 1

    _lis_substruct(arr, n)

    return maximum


# OVERLAPPING SUBPROBLEMS
def lis_subproblem(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    maximum = 0

    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print('Solved using optimal substructure', lis_substruct(arr))
    print('Solved using overlapping subproblems', lis_subproblem(arr))
