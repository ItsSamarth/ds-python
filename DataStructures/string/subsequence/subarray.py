
def subArray(arr, n):
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print("\n", end="")


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    print("All Non-empty Subarrays")

    subArray(arr, n)
