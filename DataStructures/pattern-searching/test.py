def similarityMeasurement(arr, query):
    # Check smallest index
    if query[0] == 2:
        index = 0
        print(arr)
        for i in range(query[1]):
            if arr[index] != arr[i]:
                index = i
        print(index+1)

    elif query[0] == 1:
        arr[query[1]-1] = query[2]


if __name__ == "__main__":
    # n = int(input())
    # arr = list(map(int, input().split()))
    # queries = int(input())
    n = 5
    arr = [1, 2, 1, 1, 4]
    queries = 3

    for i in range(queries):
        query = list(map(int, input().split()))
        similarityMeasurement(arr, query)
