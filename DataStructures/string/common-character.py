# Python code to print common characters of two Strings in alphabetical order
from collections import Counter

def common(s1, s2):

    #convert both string into the counter dictonary
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    commonDict = dict1 & dict2
    if len(commonDict) == -1:
        print(0)
        return -1

    #get the list of common elements
    commonChars = list(commonDict.elements())
    commonChars = sorted(commonChars)

    print(commonChars)

    print(''.join(commonChars))



if __name__ == "__main__":
    str1 = 'geeks'
    str2 = 'forgeeks'
    common(str1, str2) 