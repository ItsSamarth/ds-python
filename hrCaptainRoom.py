#HACKERRANK- solution for the captain room SET PYthon

group , room = int(input()), list(map(int, input().split()))
set = set(room)
print( ( (sum(set)*group) - sum(room)) // (group-1) )
