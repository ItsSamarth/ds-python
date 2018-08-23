#program to verify mobile number using regex
import re

# \w [a-zA-Z0-9]
#\W  [^a-zA-Z0-9]

phn = "412-555a-1212"

if(re.search("\d{3}-\d{3}-d{4}", phn)):
    print("It is a phone number")
else:
    print("Invalid phone number")
