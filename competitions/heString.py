# Write your code here
from itertools import groupby
n = int(input())
str = input()

key=''
max=0
for k,g in groupby(sorted(str)):
    length = len(list(g))
    if(max<length):
        max = length
        key = k

print(len(str) - max)
