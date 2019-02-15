# Ugly Numbers

# simple method


def maxDivide(num, divisor):
    while num % divisor == 0:
        num = num / divisor

    return num


def isUgly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)

    return 1 if n == 1 else 0


def getNthUglyNo(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if isUgly(i):
            count += 1

    return i


# Dynamic programming solution O(n)
def getNthUglyNoDP(n):
    ugly = [0] * n
    i2 = i3 = i5 = 0
    next_multiple_2 = 2
    next_multiple_3 = 3
    next_multiple_5 = 5

    for i in range(1, n):
        ugly[i] = min(next_multiple_2, next_multiple_3, next_multiple_5)

        if ugly[i] == next_multiple_2:
            i2 += 1
            next_multiple_2 = ugly[i2] * 2

        if ugly[i] == next_multiple_3:
            i3 += 1
            next_multiple_3 = ugly[i3] * 3

        if ugly[i] == next_multiple_5:
            i5 += 1
            next_multiple_5 = ugly[i5] * 5

    return ugly[-1]


if __name__ == "__main__":
    # no = getNthUglyNo(150)
    no = getNthUglyNoDP(150)
    print("150th ugly no. is ", no)
