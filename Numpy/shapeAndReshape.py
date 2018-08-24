#shape tools gives a tuple of dimensions and can be used to change the dimensions of the arrays

import numpy


# Using shape to get array dimensions
array1d = numpy.array([1,2,3,4,5])
print(array1d.shape)
# ans - (5,0 -> 5 rows and 0 col)

array2d = numpy.array([[1,2],[3,4],[6,5]])
print(array2d.shape)


# (b). Using shape to change array dimensions

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape=(3,2)
print(change_array)



# reshape

# The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
print('Reshape array')
reshape_array = numpy.array([1 2 3 4 5 6])
print(numpy.reshape(reshape_array,(3,2)))
