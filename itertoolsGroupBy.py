#itertools.groupby is a tool for grouping the items

#features
#1 - Group consecutive items together
#2 - Group all occurence of an item , given a sorted iterable
#3 - Specify how to group items with a key function

from itertools import groupby

print( [k for k , g  in groupby('AAAABBBCCDAABBB')] )

#make an iterator that returns consecutive keys and groups from the iterable
data1 = [100, 80, 80, 80, 80, 80 , 90, 90 , 85, 85, 85]

keys = []
groups = []
sorted_data = sorted(data1)

for k, g  in groupby(sorted_data):
    keys.append(k)
    # make group list
    groups.append(list(g))

#groups
print('Groups', groups)

#keys
print('Keys', keys)


#count of each element
count_per_group = [len(i) for i in groups]
print('count_per_group', count_per_group)

#adding keys and count to dictionary
zip_values = dict(zip(keys, count_per_group))
print(zip_values)


# Using list comprehension
data2 = 'AAAABBBCCDAABBB'
sorted_data2 = sorted(data2)


# not sorted and sorted
comprehension1 = [k for k, g in groupby(data2)]
print('Group by letter', comprehension1)


comprehension2 = [len(list(g)) for k ,g in groupby(sorted_data2) ]
print('Count per group', comprehension2)
