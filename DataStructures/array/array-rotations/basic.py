# Program for array rotation
def leftRotateOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    print('Array returned', arr)


def leftRotate(arr, round, n):
    for i in range(round):
        leftRotateOne(arr, n)

# single function for array rotation


def tempArr(arr, n, rotation):
    print(arr[rotation:n] + arr[:rotation])

# Juggling algorithm for array shifting


def jugglingShift(arr, round, n):
    for i in range(gcd(round, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + round
            if k >= n:
                k = k - n
            if k == i:
                break

            arr[j] = arr[k]
            j = k
            arr[j] = temp


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Reversal algorithm for rotation O(N)
def reverseArray(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def reversalAlgo(arr, n, rotation):
    reverseArray(arr, 0, rotation - 1)
    reverseArray(arr, rotation, n - 1)
    reverseArray(arr, 0, n - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    # leftRotate(arr, 2, len(arr))
    jugglingShift(arr, 2, len(arr))
    print(arr)
