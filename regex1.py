import re

nameAge = """
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21 """

ages = re.findall(r'\d{1,3}', nameAge)
print(ages)
names = re.findall(r'[A-Z][a-z]*', nameAge)
print(names)

ageDict={}
x=0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1

print(ageDict)
