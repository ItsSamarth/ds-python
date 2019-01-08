# Concatenated string with uncommon characters in Python
def uncommonConcat(s1, s2):
    # convert both the string into the set
    set1 = set(str1)
    set2 = set(str2)

    #take the intersaction of two sets to get the list of common characters
    common = list(set1 & set2)

    #seprate out the character in the string which is not common in both
    result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]
    print(''.join(result))

if __name__ == "__main__":
    str1 = 'aacdb'
    str2 = 'gafd'
    uncommonConcat(str1,str2) 