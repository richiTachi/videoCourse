# from nine9_2_1Car import Car
#
# my_new_car = Car("ferrari","488",2019)
# print(my_new_car.describe_car())
#
#
# from nine9_3_1Car import ElectricCar
#
# my_tesla = ElectricCar("tesla","model's",2016)
#
# print(my_tesla.describe_car())
# my_tesla.battery.describe_battery()


# from nine9_3_1Car import Car,ElectricCar
#
# a_car = Car("lambo","aventador",2018)
# print(a_car.describe_car())
#
# b_car = ElectricCar("tesla","model's",2016)
# print(b_car.describe_car())

import nine9_3_1Car

a_car = nine9_3_1Car.Car("lambo","aventador",2018)
print(a_car.describe_car())

b_car = nine9_3_1Car.ElectricCar("tesla","model's",2016)
print(b_car.describe_car())