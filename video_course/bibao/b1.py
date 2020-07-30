def curve_pre():
    a = 25
    def curve(x):
        return a*x**2
    return curve

f = curve_pre()
print(f(2))
print(f.__closure__)
print(f.__closure__[0].cell_contents)