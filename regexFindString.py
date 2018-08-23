#program to find a word in string

import re

text = "we all need to inform him the latest information"
allinform = re.findall("inform", text)

if(re.search("inform", text)):
    print("There is a inform")

for i in allinform:
    print(i)
