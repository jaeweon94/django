import re


val = "0106484248aa"
pattern = r"^01[01678][1-9]\d{6,7}$"


if re.match(pattern, val):
    print('matched')
else:
    print('invalid')