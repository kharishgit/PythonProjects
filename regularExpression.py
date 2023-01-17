import re

text = "Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

pattern = '[5-9]+'

match = re.findall(pattern,text)
print(match)