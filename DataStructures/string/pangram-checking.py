def checkPangram(s):
    list =[]
    for i in range(26):
        list.append(False)

    for c in s.lower():
        if not c == " ":
            #make the corresponding entry true
            list[ord(c) - ord('a')] = True

    #check if any character is missing then return false
    for ch in list:
        if ch == False:
            return False
    return True

def missingCharacter(s):
    list= []
    for i in range(26):
        list.append(False)
    
    for c in s.lower():
        if not c == " ":
            list[ord(c) - ord('a')] = True
    

    #check for missing characters
    alph_ord = ord('a')
    for ch in list:
        if ch == False:
            print(chr(alph_ord))
        alph_ord+=1



if __name__ == "__main__":
    # sentence ="The quick brown fox jumps over the little lazy dog"
    sentence ="The quick brown fox jumps over the little"
    missingCharacter(sentence)
    # if (checkPangram(sentence)): 
    #     print("It is a valid pangram")
    # else: 
    #     print("Not pangram")