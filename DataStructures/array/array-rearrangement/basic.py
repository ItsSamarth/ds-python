# Rearrage an array such that arr[i] = i
def fix(arr, n):
    for i in range(n):
        if arr[i] != -1 and arr[i] != i:
            x = arr[i]
            print(x)

            while arr[x] != x and arr[x] != -1:
                # store the value form the desired place
                y = arr[x]
                print(y)
                arr[x] = x
                x = y
                print(arr)


def hashFix(arr, n):
    s = set()

    for i in range(n):
        s.add(arr[i])

    for i in range(n):
        # check if item is present in the set
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1

    print(arr)


if __name__ == "__main__":
    A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

    hashFix(A, len(A))

    # for i in range(0, len(A)):
    #     print(A[i], end=' ')
