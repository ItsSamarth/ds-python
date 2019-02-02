# Using Counter() in Python to find minimum character removal to make two strings anagram

from collections import Counter

def removeChars(s1, s2):
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    #extract keys form the dictionary
    keys1 = dict1.keys()
    keys2 = dict2.keys()

    print(keys1)
    print(keys2)

    #count the number of keys in both list
    count1 = len(keys1)
    count2 = len(keys2)

    print(count1)
    print(count2)

    #convert the list of keys in set  to find common keys
    set1 = set(keys1)
    print(set1)

    commonkeys = len(set1.intersection(keys2))

    if commonkeys == 0:
        return count1 + count2
    else:
        return (max(count1, count2) - commonkeys)




if __name__ == "__main__":
    str1 ='bcadeh' 
    str2 ='hea'
    print (removeChars(str1, str2)) 