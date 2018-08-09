from itertools import *

a=[1,2,3,4,5,6,7,8,9]
b=['a','b','c','d','e','f','g','h','i','j','k','l']
c=['one','two','three','four','five','six','seven','eigth']

# chain
# Group multiple list together

print(list(chain(a,b,c)))


# count
#Print infinte number with .5 increment
# for i in count(1,.5):
#     print(i)

#islice
#give boundation to count()

for i in islice(count(), 0 ,110 , 5):
    print(i)


#compress
#it is used to create binary filter
#if 0 is there then it will skip that position and for 1 it will execute that position

binary_filter = [1,1,0,0,0,0,0,1,1]
print(list(compress(a, binary_filter)))


#filter
#The way filter works that it is choosing TRue or FAlse value

odds = list(filter(lambda x: x % 2 , a))
print(odds)

even = list(filter(lambda x: x % 2 == 0 , a))
print(even)
