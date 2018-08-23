# Program to verify full name
import re

 # \s [\f\n\r\t\v]
 # \S  [^\f\n\r\t\v]

name = "Samarth Saxena"

if re.search("\w{2,20}\s\w{2,20}", name):
    print("Fullname is valid")

else:
    print("Invalid Fullname")
