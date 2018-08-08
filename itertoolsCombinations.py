# itertools.combinations(iterable, r)
# This tool returns the  length subsequences of elements from the input iterable.

from itertools import combinations

# print(list(combinations('12345',2)))

# A=['1','1','3','3','3']
# print(list(combinations(A,4)))

print(*(combinations('HACK',2)))
