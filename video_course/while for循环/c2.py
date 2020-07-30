a = [["apple","orange","banana"],(1,2,3)]
for x in a:
    for y in x:
        if y == "apple" and y == 2:
            break
        print(y)