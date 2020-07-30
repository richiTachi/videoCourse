origin = 0

def factory(pos):
    def go(step):
        nonlocal pos
        new_position = pos + step
        # pos = new_position
        return new_position
    return go

# f = factory(origin)
# print(f(2))
# print(f(3))
# print(f(6))


origin = 0

def start(pos):
    def go(step):
        nonlocal pos
        new_position = pos + step
        pos = new_position
        return new_position
    return go

s = start(origin)
print(s(2))
print(s(5))
print(s(3))