# itertools.combinations_with_replacement(iterable, r)
# This tool returns r length subsequence of elements from the input iterable allowing  individual elements to be repeated more than once

from itertools import combinations_with_replacement, combinations

# print(list(combinations_with_replacement('12345',2)))
# print(list(combinations('12345',2)))


a = 'HACK'
b = 2

# print(list(combinations_with_replacement(sorted(a),b)))
[print( (''.join(i)) for i in combinations_with_replacement(sorted(a), int(b) ))]


for i in combinations_with_replacement(sorted(a), int(b)):
    print(''.join(i))
