# https: // www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/description/

from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, a, b = map(int, stdin.readline().split())
    x = round((b*n)/(a+b))
    y = n-x
    stdout.write(str(a*x*x + b*y*y) + "\n")
