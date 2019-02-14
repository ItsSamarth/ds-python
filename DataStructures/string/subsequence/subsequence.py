# Python 3 code to generate all
# possible subsequences.
# Time Complexity O(n * 2 ^ n)


def printSubsequences(arr, n):
    # number of subsequence (2**n -1)
    opsize = 2 ** n

    # run counter form 000 to 111
    for counter in range(1, opsize):
        for j in range(n):
             # Check if jth bit in the counter
            # is set If set then print jth
            # element from arr[]
            # print(counter)
            # print(1 << j)
            # print(counter & (1 << j))

            if (counter & (1 << j)):
                print(arr[j], end=" ")

        print()


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    print("All Non-empty Subsequences")

    printSubsequences(arr, n)
