# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

n = int(input())
list = []
for i in range(n):
    temp = input().split()
    if temp[0] == 'insert':
        list.insert(int(temp[1]) , int(temp[2]))
    elif temp[0] == 'append':
        list.append(int(temp[1]))
    elif temp[0] == 'remove':
        list.remove(int(temp[1]))
    elif temp[0] == 'sort':
        list.sort()
    elif temp[0] == 'pop':
        list.pop()
    elif temp[0] == 'reverse':
        list.reverse()
    else:
        print(list)
