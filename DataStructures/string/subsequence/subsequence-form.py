# # Python 3 program to count
# subsequences of the form
# a^i b^j c^k


def countSubsequences(str):
    aCount = 0
    bCount = 0
    cCount = 0

    for i in range(len(str)):
        if str[i] == 'a':
            aCount = (1 + 2 * aCount)
        elif str[i] == 'b':
            bCount = aCount + 2 * bCount
        elif str[i] == 'c':
            cCount = bCount + 2 * cCount

    return cCount


if __name__ == "__main__":
    s = "abcabc"
    print(countSubsequences(s))
