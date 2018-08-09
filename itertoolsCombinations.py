# itertools.combinations(iterable, r)
# This tool returns the  length subsequences of elements from the input iterable.

from itertools import combinations

# print(list(combinations('12345',2)))

# A=['1','1','3','3','3']
# print(list(combinations(A,4)))

# print(*(combinations('HACK',2)))
num =2

for j in range(1,num+1):
    for i in combinations(sorted('HACK'), j):
        print(''.join(i))
