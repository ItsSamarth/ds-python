#webscrapping showcase urllib is used to read webpages
import urllib.request
import re

url =""

response = urllib.request.urlopen(url)
html = response.read()
htmlStr = html.decode()

postData = findall("\(\d{3}\) \d{3}-\d{4}", htmlStr)

for item in postData:
    print(item)
