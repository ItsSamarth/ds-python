# itertools.product()
# This tool compute the cartesian product of input tables
#Ex- product(a,b) is same as ((x,y) for x in A for y in B)
from itertools import product

print (list(product([1,2,3],repeat = 2)))

print( list(product([1,2,3],[3,4])))

A=[[1,2,3] , [3,4,5]]
print(list(product(*A)))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))


# Taking Input from list
a = list(map(int, input().split()))

# multiple ways to print
print(*product(a,b))
print(*itertools.product(A,B))
