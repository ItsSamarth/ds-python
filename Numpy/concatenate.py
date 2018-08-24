# Concatenate
#
# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
import numpy


array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1,array_2,array_3)))


#concatinating multiple dimension arrays

array_111 = numpy.array([[1,2,3],[0,0,0]])
array_222 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_111 , array_222), axis =1))
