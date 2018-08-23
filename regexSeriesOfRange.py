# Program to match series of range characters
# [h-m] -> words who comes between h and m would be listed here

import re

str ="Sat, hat, mat, pat"
someStr = re.findall("[h-z]at", str)

for i in someStr:
    print(i)

anotherstr = re.findall("[^h-m]at", str)

# caret symbol means that everything appart from h to m  would come

for i in anotherstr:
    print(i)
