def search(s, pat):
    n = len(s)
    m = len(pat)

    for i in range(n-m):
        if s[i:m+i] == pat:
            print('Pattern found at Index', i)


if __name__ == "__main__":
    s = 'AABAACAADAABAAABAA'
    pat = 'AABA'
    search(s, pat)

