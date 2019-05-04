

# NORMAL RECURSIVE METHOD TO  SOLVCE PROBLEM
def lcs(x, y, n, m):

    if m == 0 or n == 0:
        return 0
    elif x[n - 1] == y[m - 1]:
        return 1 + lcs(x, y, n - 1, m - 1)
    else:
        return max(lcs(x, y, n, m-1), lcs(x, y, n-1, m))


# SOLVED USING OVERLAPPING SUBPROBLMEMS
def lcs_subproblems(str1, str2):
    m = len(str1)
    n = len(str2)

    # declaring array for storing values
    arr = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0

            elif str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    checkCommonString(arr, str1, str2)
    return arr[m][n]


def checkCommonString(arr, str1, str2):
    temp = []
    i = len(str1)
    j = len(str2)
    while i > 0 and j > 0:
        if arr[i][j] == arr[i][j - 1]:
            j = j - 1
        elif arr[i][j] == arr[i - 1][j]:
            i -= 1
        elif arr[i][j] > arr[i - 1][j] and arr[i][j] > arr[i][j-1]:
            temp.append(str2[j-1])
            i -= 1
            j -= 1
        # print('array position', arr[i][j], i, j)
    print("".join(temp[::-1]))


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    # print("Length of LCS is ", (lcs(X, Y, len(X), len(Y))))
    print("Solved using optimal subproblems in O(mn) Time ", lcs_subproblems(X, Y))
