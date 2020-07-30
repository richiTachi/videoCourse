def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza("16","mushrooms")

def city_country(city,country):
    print(city + "," + country)

# aa = city_country("shenzhen","chian")
# print(aa)