class Dog():
    """一次模拟小狗的简单测试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " is rolled over.")

my_dog = Dog("willie","6")
#
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " yeas old.")
my_dog.sit()
my_dog.roll_over()

# class Restaurant():
#     def __init__(self,restaurant_type,cuisine_type):
#
#         self.restaurant_type = restaurant_type
#         self.cuisine_type = restaurant_type
#
#     def describe_restaurant(self):
#         print("The restaurant tpye is " + self.restaurant_type.title()
#               + " and the cuisine is " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("The restaurant is opening!!")
#
# restaurant = Restaurant("chinese","hot pot")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

