def check(s1, s2):
    if sorted(s1) == sorted(s2):
        print('It is an anagram')
    else:
        print("Not anagram")


if __name__ == "__main__":
    s1 = 'samarth'
    s2 = 'samarth'

    check(s1, s2)