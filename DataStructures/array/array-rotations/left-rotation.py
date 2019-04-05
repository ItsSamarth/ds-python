# n, d = input().strip().split()
# inputList = list(map(int, input().strip().split()))
n, d = 5, 9
inputList = [1, 2, 3, 4, 5]
inputMList = inputList[int(d):] + inputList[:int(d)]
print(inputList[int(d):])
print(inputList[:int(d)])
print(inputMList)
[print(i, end=" ") for i in inputMList]
