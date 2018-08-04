# SWAPPING OF TWO NUMBERS
x,y=10,20
print(x,y)
x,y=y,x
print(x,y)


#REVERSING A STRING
str="samarth"
print("Reverse is", str[::-1])

#CREATING A SINGLE STRING IN THE LIST FROM ALL ELEMENTS
thelist = ["hey", "hello","test"]
newlist = "".join(thelist)
print(newlist)

#CHANINING OF COMPARISION OPERATORS
n=10
result = 1 < n <20
print(result)
result=1> n <= 9
print(result)


#PRINT THE PATH OF IMPORTED MODULES
import os;
import socket;

print(socket)


# MOST FREQUENT VALUE IN THE LIST
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))


#print a string N times
n=2;
a="samarth"
print(a*n)


# check words are anagram or not
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram('samarth' , 'arth'))
print(is_anagram('samarth', 'marthsa'))
