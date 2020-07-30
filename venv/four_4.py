# players = ['kobe','allen','T-mac','lebron','KD']
#
# print('Here are the retired basketball players list:')
# for player in players[:3]:
#     print(player.title())




# cars = ['lamborghini','ferrari','mclaren','rolls-royce','mercedes','porsche','dodge']
# print('The first three items in the list are:')
# for car in cars[:3]:
#     print(car.title())
#
# print("Three items from the middle of the list are:")
# for car in cars[3:6]:
#     print(car.title())

my_cars = ['lamborghini','ferrari','mclaren','rolls-royce']
friend_cars = my_cars[:]
print(my_cars)
print(friend_cars)

my_cars.append('mercedes')
friend_cars.append('porsche')
print(my_cars)
print(friend_cars)

print('\nThere are cars that i have:')
for my_car in my_cars:
    print(my_car.title())

print('\nThere are cars that my friend have:')
for friend_car in friend_cars:
    print(friend_car.title())