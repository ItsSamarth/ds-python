#Hacker rank solution for ordered dictionary

# An ordered dictionary is a dictionary that remembers the order of the keys that were inserted first
#if a new entry overwrites and existing entry the original insertion position is left unchanged

from collections import OrderedDict

ordinary_dictionary ={}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

print(ordinary_dictionary)

ordered_dictionay = OrderedDict()
ordered_dictionay['a'] = 1
ordered_dictionay['b'] = 2
ordered_dictionay['c'] = 3
ordered_dictionay['d'] = 4
ordered_dictionay['e'] = 5

print(ordered_dictionay)


n = int(input())
item_dictionary = OrderedDict()
for i in range(n):
    test = input().rpartition(" ")
    # item_name, net_price = input().split()
    # item_dictionary['item_name'] = int(net_price)

print(test)
