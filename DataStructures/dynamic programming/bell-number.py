def bellNumber(n):
    bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]

        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    print(bell)
    return bell[n][0]


if __name__ == "__main__":
    for i in range(6):
        print("Bell number", i, "is", bellNumber(i))
