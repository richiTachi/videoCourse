import re

qq = "10000001"

r = re.findall("^\d{4,8}$",qq)
print(r)