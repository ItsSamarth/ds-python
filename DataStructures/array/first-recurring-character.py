#program to find the first reccuring character from the given string

def first_recurring(str):
    counts={}
    for char in str:
        if char in counts:
            return char

        counts[char] = 1

    return None




# str = "DBCABA"
str = "ABBA"
result=first_recurring(str)
print(result)
