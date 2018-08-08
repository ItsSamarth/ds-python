# itertools.permutations(iterable[,r])
# This tool returns successive r length permutations of elements in an iterable
# Permutations are printed in lexographic sorted order

from itertools import permutations

print(list(permutations(['a','b','c'])))

print(list(permutations(['1', '2', '3'])))

print(list(permutations(['1','2','3'],2)))

print(list(permutations(['a', 'b','c'],2)))

print(list(permutations('abc',3)))


# HACKER RANK SOLUTION TO THE PROBLEM

a, b = input().split()
[print(''.join(i)) for i in permutations(sorted(a), int(b))]

for c in permutations(sorted(a), int(b)):
    print(''.join(c))
