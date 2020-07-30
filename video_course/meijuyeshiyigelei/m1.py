from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLACK = 4

print(type(VIP.GREEN))
print(type(VIP.GREEN.name))


a = 1
print(VIP(a))