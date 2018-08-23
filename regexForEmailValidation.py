#program to validate email
import re

email ="samarth@gmail.com @gmail.com dc.com sk@aol.com"

print("Email Matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))
