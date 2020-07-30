from enum import Enum,unique

# @unique
class WEEKDAY(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Say = 6


print(WEEKDAY.Sun)
print(WEEKDAY["Sun"])
print(WEEKDAY.Sun.name)
print(WEEKDAY.Sun.value)
print(WEEKDAY(3))

for w in WEEKDAY:
    print(w)

# for name,value in WEEKDAY.__members__.items():
#     print(name,value)