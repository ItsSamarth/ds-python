from difflib import SequenceMatcher
def longestSubstring(s1, s2):
    #initlize sequence matcher object with input string 
    seqMatch = SequenceMatcher(None, s1, s2)

    #find match of longest substring
    # output will be like Match(a=0, b=0, size=5) 

    match = seqMatch.find_longest_match(0, len(s1), 0, len(s2))
    print(match)

    #print the longest substring
    if match.size != 0:
        print(str1[match.a : match.a+ match.size])

    else:
        print("No longest common substring found")


if __name__ == "__main__":
    str1 ="lets hope for the best"
    str2 = "hope is a light in a darkness"
    longestSubstring(str1, str2)