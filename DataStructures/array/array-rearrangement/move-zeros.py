# Move all zeroes to end of array
def pushZerosToEnd(arr, n):
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    print(arr)

#  move Zeros to end in one iteration


def moveZerosToEnd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
            print(arr)


if __name__ == "__main__":
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    print(arr)
    moveZerosToEnd(arr, n)
    print("Array after pushing all zeros to end of array:")
    print(arr)
