#collections.counter()
#A counter is a container that stores elements as dictionary and keys and their counts are stored as dictionary values

from collections import *

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print (Counter(myList))

print(Counter(myList).items())

print(Counter(myList).keys())

print(Counter(myList).values())

#count specific values
counterlist = Counter(myList)
specific = counterlist[3]
print(specific)
print(counterlist.most_common())

counterlist[3] = 10
print(counterlist)


# if you want to find any value which is not in the list then it will not give any error
#but in dictionary you will get errors
