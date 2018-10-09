# https://www.hackerrank.com/challenges/camelcase/problem
import re
def camelcase(str):
    result = re.findall('[A-Z][a-z]*', str)
    print(len(result))




if __name__ == '__main__':
    s = input()
    camelcase(s)
