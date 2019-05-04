# Given two strings, find if first string is a subsequence of second


# iterative approach

def isSubSequenceIterative(str1, str2, m, n):
    i = 0
    j = 0

    while i < m and j < n:
        if str1[i] == str2[j]:
            i += 1
        j += 1

    return i == m


def isSubSequenceRecursive(str1, str2, m, n):

    if m == 0:
        return True
    if n == 0:
        return False

    # If the last character of two strings are matching
    if str1[m - 1] == str2[n - 1]:
        return isSubSequenceRecursive(str1, str2, m - 1, n - 1)

    # If the last characters are not matching
    return isSubSequenceRecursive(str1, str2, m, n-1)


if __name__ == "__main__":
    string1 = "gksrek"
    string2 = "geeksforgeeks"
    m = len(string1)
    n = len(string2)
    if isSubSequenceRecursive(string1, string2, m, n):
        print("Yes")
    else:
        print("No")
