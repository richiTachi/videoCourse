origin = 0
def go(step):
    global origin
    new_position = origin + step
    origin = new_position
    return new_position

print(go(2))
print(go(3))
print(go(6))
