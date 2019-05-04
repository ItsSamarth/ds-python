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


# Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
def rearrangeArr(arr):
    tempArr = sorted(arr)
    mid = len(arr) // 2
    right = mid+1
    left = mid
    temp = []
    temp.append(tempArr[left])
    while left >= 0 and right < len(arr):
        left -= 1
        temp.append(tempArr[right])
        temp.append(tempArr[left])
        right += 1
        print(temp)

    return temp


def rearrangeArrMain(arr):
    n = len(arr)
    evenPos = n // 2
    oddPos = n - (n // 2)
    tempArr = sorted(arr)

    index = 0
    # fill odd positions
    while oddPos-1 >= 0:
        # odd pos
        arr[index] = tempArr[oddPos-1]
        index += 2
        oddPos -= 1
    index = 1
    while evenPos-1 >= 0:
        arr[index] = tempArr[n-evenPos]
        index += 2
        evenPos -= 1

    # fill even postitions
    # while oddPos
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr = [1, 2, 1, 4, 5, 6, 8, 8]
    # leftRotate(arr, 2, len(arr))
    # jugglingShift(arr, 2, len(arr))
    # print(rearrangeArr(arr))
    print(rearrangeArrMain(arr))
    # print(arr)
