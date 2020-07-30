from c4 import Human

class Student(Human):
    # def __init__(self,name,age):
    #     super().__init__(name,age)
    # sum = 0
    # name = "000"
    # age = 0

    # def __init__(self,name1,age):
    #     # 构造函数
    #     # 初始化对象的属性
    #     self.name = name1
    #     self.age = age
    #     self.score = 0
        # print(self.name + " " + str(self.age))
        # self.__class__.sum += 1
        # print("当前班级学生人数为：" + str(self.__class__.sum))


    def do_homework(self):
        print(("homework"))

    def marking(self,score):
        if score < 0:
            return False
        self.__score = score
        print(self.name + "得到的分数为：" +
              str(self.score))

    # @classmethod
    # def plus_sum(cls):
    #     cls.sum += 1
    #     print("当前班级学生人数为：" + str(cls.sum))
    #
    # @staticmethod
    # def add(x,y):
    #     print("This is a static method")


    # def print_file(self):
    #     print("name: " + self.name)
    #     print("age: " + str(self.age))
student1 = Student("石敢当",18)
print(Student.sum)
print(student1.sum)
print(student1.name)
print(student1.age)
student1.get_name()