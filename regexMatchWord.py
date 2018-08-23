#Program to match word with particular pattern
import re

str ="Sat, hat, mat, pat"
allstr = re.findall("[Shmp]at", str)

for i in allstr:
    print(i)
