#Hackerrank solution to pop(), remove(), discard()

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

n = int(input())
set1 = set(map(int, input().split()))

operations = int(input())

for i in range(operations):
    action = list(input().split())
    if (action[0] == 'pop'):
        set1.pop()
    elif(action[0] == 'remove'):
        set1.remove(int(action[1]))
    elif(action[0] == 'discard'):
        set1.discard(int(action[1]))

print(sum(set1))
