#Python program to find largest number from the given
#values function that return the largest possible number

def largestNumber(array):
    extval , ans =[],""
    l = len(str(max(array)))+1

    for i in array:
        temp = str(i)*l
        extval.append((temp[:l:], i))

    extval.sort(reverse=True)

    for i in extval:
        ans += str(i[1])

    return ans




a = [1, 34, 3, 98, 9, 76,
        45, 4, 12, 121]
print(largestNumber(a))
