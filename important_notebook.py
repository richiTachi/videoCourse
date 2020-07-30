# words = "来吧，你想知道什么？"
# words += "\n告诉你的名字，我告诉你想知道的事情"
#
# message = ""
# words1 = "拜拜了您嘞"
#
# while message != "滚":
#     message = input(words)
#     if message == "滚":
#         message = input(words1)
#         print(message)


# while True:
#     # """进入loop，当loop为true，执行以下操作"""
#
#     num = input("这个数字能不能被3整除?")
#     # """告诉用户，输入一些他想知道的问题"""
#
#     if num == "ok":
#         break
#         # """停止执行的条件"""
#
#     elif int(num) % 3 == 0:
#         print(str(num) + "是可以的")
#     else:
#         print(str(num) + "不可以的")
#         # """以上是循环调价"""
#
# data_base = {
#     "ID":"wenzhi",
#     "password":"w123456789",
# }
# """储存用户的账号和密码"""
#
# ID = input("Please enter your ID:")
# if ID in data_base:
#     password = input("Please enter your password：")
#     if data_base[ID] == password:
#         print("Log into the system")
#     else:
#         ("Please enter correct password")
# else:
#     print("Please enter correct password")



# data_base = [{
#     "id": 1,
#     "name": 'aleko',
#     "psw": 123123
# }, {
#     "id": 2,
#     "name": 'wenzhi',
#     "psw": 123123
# }]
#
# while True:
#
#     id = input("请输入你的id：")
#     is_find = False
#     for i in data_base:
#         if i["id"] == int(id):
#             is_find = True
#             psw = input("请输入密码：")
#             if int(psw) == i["psw"]:
#                 print("登陆成功")
#             else:
#                 print("密码错误")
#
#     if is_find == False:
#      print("未找到该用户")
#     else:
#         break
#
#
#
#
#
# store = []
# # 建立一个信息储存库
# data_bank = {
#     "username":"wenzhi",
#     "password":"correct",
# }
# 建R立一个信息库

# for b in data_bank.values():
#     store.append(b)
#     print(store)
# # 把值遍历出来储存在信息库store
#
# while True:
#     name = input("Please enter your username:")
#     if name in store:
#         break
#     else:
#         print("Please enter your correct username:")
#
# while True:
#     password = input("\nPlease enter your password:")
#     if password == store:
#         print("Log into the system!!!!")
#         break
#
#     else:
#         print("Please enter your correct password")

# def caculate(principal,year):
#     n = 0
#     sum = principal
#     while n < year:
#         n += 1
#         sum = sum * 1.3 + principal
#     return sum
#
# aa = caculate(1000,11)
# print(aa)


# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def describe_car(self):
#         print("This is a " + self.year + self.make.title()
#               + " called " + self.model.title() + ".")
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#
# my_car = Car("lamoborghini","aventador","2018")
# my_car.describe_car()
#
# your_car = Car()

# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def describe_car(self):
#         print("This is a " + self.year + " " +
#             self.make.title() + " called " + self.model.title())
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,)
#
# my_car = Car("lambo","aventador","2019")
# my_car.describe_car()


# while True:
#     msg = input("告诉我一个数字，看看能不能被3整除")
#     if msg == "over":
#         break
#     if int(msg) % 3 == 0:
#         print(msg + "可以被3整除")
#     if int(msg) % 3 != 0:
#         print(msg + "不可以被3整除")


# def isPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return  True
#
# result = []
#
# for i in range(1,101):
#     if isPrime(i):
#         result.append(i)
#
# print(result)
#
# for i in range(1,10):
#     for j in range(1,10):
#         if i == j:
#             print("%d*%d=%d" % (j, i, i * j), end="\n")
#         else:
#             print("%d*%d=%d" % (j, i, i * j), end="\t")
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == j:
#             print("%d*%d=%d" % (j, i, i * j), end="\n")
#         else:
#             print("%d*%d=%d" % (j, i, i * j), end="\t")

