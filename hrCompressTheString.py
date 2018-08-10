#hackerrank solution to compress the string solution by using itertools

from itertools import groupby

input = '1222311'
keys=[]
groups= []


for k,g in groupby(input):
    keys.append(int(k))
    groups.append(list(g))



print(keys)
print(groups)

# for i in groups:
#     print(list(len(i))

count_per_group = list(len(i) for i in groups)
print(count_per_group)


#concatinating the data
zip_values = list(zip(count_per_group, keys ))
print(zip_values)

for i in zip_values:
    print(i , end=' ')


# Editor code

for i,j in groupby(map(int, list(input()))):
    print(tuple([len(list(j)), i]) , end = " ")
