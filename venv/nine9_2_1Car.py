# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descripive_name(self):
#         a_car = str(self.year) + " " + self.make + " " + self.model
#         return a_car.title()
#
# my_car = Car("lamborghini","lp700","2019")
# print(my_car.get_descripive_name())




class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        a_car = self.make + " " + self.model + " " + str(self.year)
        return a_car.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

# my_car = Car("lamborghini","aventador",2020)
# print(my_car.describe_car())
# my_car.odometer_reading = 2323
# my_car.read_odometer()


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def describe_car(self):
#         a_car = self.make + " " + self.model + " " + str(self.year)
#         return a_car.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it")
#
#     def update_odometer(self,mileage):
#         self.odometer_reading = mileage

# my_car = Car("lamborghini","aventador",2020)
# print(my_car.describe_car())
# my_car.update_odometer(2990)
# my_car.read_odometer()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        a_car = self.make + " " + self.model + " " + str(self.year)
        return a_car.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

# my_car = Car("lamborghini","aventador",2020)
# print(my_car.describe_car())
#
# my_car.update_odometer(3000)
# my_car.read_odometer()
#
# my_car.increment_odometer(100)
# my_car.read_odometer()