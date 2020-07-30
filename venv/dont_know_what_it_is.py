def profits(invest,year):
    n = 0
    sum = invest
    while n < year:
        n += 1
        sum = sum * 1.3 +invest
    return sum


print(profits(100, 12))

