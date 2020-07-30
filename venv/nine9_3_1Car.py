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

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

# tesla = ElectricCar("tesla","model's",2016)
# print(tesla.describe_car())
# tesla.battery.describe_battery()



# class User():
#     def __init__(self,first_name,last_name,**user_info):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.user_info = user_info
#         for i in self.user_info:
#
#
#     def describe_user(self):
#         self.username = self.f_name + " " + self.l_name
#         return self.username.title()
#
#     def greet_user(self):
#         print("Hello " + self.username.title() + " my friend")
#
# username1 = User("kobe","bryant")
# username1.describe_user()
# username1.greet_user()

