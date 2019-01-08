def superiorSubstring(str, n):
    dict ={}
    for x in str:
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = 1
    dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
    print(dict)
    if(2*dict[0][1] + 1 > n):
        print(n)
    else:
        print(2*dict[0][1] + 1 )




if __name__ == "__main__":
    tc = int(input())
    while tc:
        str_len = int(input())
        str = list(input())
        print(str)
        superiorSubstring(str, str_len)
        tc-=1
