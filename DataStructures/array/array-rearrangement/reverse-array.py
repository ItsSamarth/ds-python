
# Iterative approach


def reverseList(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# recursive approach


def recursiveReverseList(arr, start, end):
    if start >= end:
        return

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    recursiveReverseList(arr, start+1, end-1)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    # reverseList(A, 0, len(A)-1)
    recursiveReverseList(A, 0, len(A)-1)
    print("Reversed list is")
    print(A)
