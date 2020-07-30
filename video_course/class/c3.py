"""类是现实世界或思维世界中的实体在计算机的反映
   它将数据以及数据上的操作封装在一起"""


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print("This is a " + str(self.year) +
              "'s " + self.make + " called " +
               self.model)

# car_1 = Car("ferrari","califonia",2020)
# car_1.describe_car()


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

result = []

for i in range(2,201):
    if isPrime(i):
        result.append(i)

print(len(result))