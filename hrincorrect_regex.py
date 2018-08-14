#Hackerrank solution for incorrect Regex

import re

try:
    re.compile('.*\+')
    is_valid = True
except re.error:
    is_valid = False

print(is_valid)


# import re
#
# for i in range(int(input())):
#     regx = input()
#     try:
#         re.compile(regx)
#         is_valid = True
#     except re.error:
#         is_valid = False
#     print(is_valid)
