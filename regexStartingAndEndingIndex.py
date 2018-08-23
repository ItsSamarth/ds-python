# Program to get the starting and ending index of a particular starting
import re

str ="we need to inform him with the latest information"

for i in re.finditer("inform", str):
    loctuple = i.span()
    print(loctuple)
