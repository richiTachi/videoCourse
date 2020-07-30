import re
s = "python1111java678php"

r = re.findall("[a-z]{3,6}",s)
print(r)
