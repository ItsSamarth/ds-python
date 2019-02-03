# Native algorithm for pattern searching


def search(pat, s):
    i = 0
    j = 0

    while i < len(s) and j < len(pat):
        if s[i] == pat[j]:
            j += 1
        else:
            j = 0

        if j == len(pat):
            print('Pattern found at index', i-j+1)
            j = 0

        i += 1


def optimalNaiveSearch(pat, txt):
    m = len(pat)
    n = len(txt)
    i = 0

    while i <= n-m:
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
            j += 1

        if j == m:
            print("Pattern found at index" + str(i))
            i = i+m

        elif j == 0:
            i = i+1
        else:
            i = i + j


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
    optimalNaiveSearch(pat, txt)
