#hackerank solution for timezone - TIme delta

from datetime import datetime

format = "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input())):
    print(int(abs((datetime.strptime(input(), format) - datetime.strptime(input(), format)).total_seconds() )))
