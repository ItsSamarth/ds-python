# n = int(input())
# scores = list(map(int, input().split()))
# scores.sort()
# print(scores[-2])
# print(scores)

from collections import Counter

if __name__ == '__main__':
    n = int(input())
    scores = Counter(map(int, input().split())).keys()
    scores = sorted(scores)
    print(scores[-2])
