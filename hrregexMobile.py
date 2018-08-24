import re

for _ in range(int(input())):
    result = re.match("[789]\d{9}$", input())
    if bool(result):
        print("YES")
    else:
        print("NO")
