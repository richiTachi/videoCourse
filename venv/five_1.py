cars = ['lamborghini','mercedes','bmw','audi']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = ['bmw','audi','xiali','xiandai']
my_car = 'ferrari'
if my_car not in car:
    print('yeah!' + my_car.title() + ' is my car!')

alien_colors = 'red'

if alien_colors == 'green':
    print('you can get 5 points')
elif alien_colors == 'yellow':
    print('you can get 10 points')
elif alien_colors == 'red':
    print('you can get 15 points')

