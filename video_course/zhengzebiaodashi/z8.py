import re

arr = "A8C3732D86"

def convert(value):
    matched = value.group()
    # print(matched)
    if int(matched) >= 6:
        # print("9")
        return "9"
    else:
        # print("0")
        return "0"

r = re.sub("\d",convert,arr)
print(r)