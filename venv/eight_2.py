# def describe_pets(animal_type,pets_name):
#     # 定义函数名字
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + " called " + pets_name + ".")
#     # 设定函数内容
# describe_pets("狗","阿乐")
# # 调用函数
# describe_pets("sb","wugou")
# 可以重复调用

# def describe_pets(pets_name,animal_type = "dog"):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + " called " + pets_name + ".")
#
# describe_pets("ale")
# # 如果函数设有默认值，调用函数时输入一个实参可完成调用函数


# def make_shirt(size,logo="I love python"):
#     """制造衣服的尺寸和标志"""
#     print("I would like a " + size + " T-shirt with " + logo + ".")
#
# make_shirt("big")
# make_shirt("middle")
# make_shirt("small","mickey_mouse")

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + " " + last_name
#     # 设定函数内容
#     return full_name.title()
#     # 返回函数内容
# 
# musician = get_formatted_name("jay","chow")
# # 函数内容存储
# print(musician)

# def get_formatterd_name(first_name,last_name,middle_name=" "):
#     """返回整洁的姓名"""
#
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " + last_name
#     else:
#         full_name + first_name + " " + last_name
#     return full_name.title()
#
# musician = get_formatterd_name("jay","chow")
# print(musician)
#
# musician1 = get_formatterd_name("a","b","c")
# print(musician1)

# def build_person(first_name,last_name):
#     """返回一个字典，其中包含有关一个人的信息"""
#
#     person = {"first":first_name,"last":last_name}
#     return person
#
# musician = build_person("jay","chow")
# print(musician)

# def families_members(member,name):
#     """描述家庭成员和他的信息"""
#
#     member = {"member":member,"name":name}
#     return member
#
# members = families_members("father","wenjinhong")
# print(members)

# def get_formatted_name(first,last):
#     """返回整洁的姓名"""
#     full_name = first + " " + last
#     return full_name
# # 定义一个函数，把值返回到函数里面
#
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")
#     # f_name和l_name用于input内容
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(formatted_name)
#     # 调用函数并打印出来

# def get_formatted_name(first,last):
#     """返回整洁的姓名"""
#     full_name = first + " " + last
#     return full_name
#     # 定义函数
#
# while True:
#     print("\nPlease tell me your name:")
#     first_name = input("First name:")
#     if first_name == "q":
#         break
#     last_name = input("Last name:")
#     if last_name == "q":
#         break
    # 设定一个循环，限定条件

    # aa = get_formatted_name(first_name,last_name)
    # 把循环嵌套到函数里，并调用函数
    # print("\nHello, " + aa + "!")



# def get_formatted_name(first,last):
#     full_name = first + " " + last
#     return full_name
#
# while True:
#     print("\nPlease tell me your name:")
#     first_name = input("First name:")
#     if first_name == "q":
#         break
#     last_name = input("Last name:")
#     if last_name == "q":
#         break
#
#     aa = get_formatted_name(first_name,last_name)
#     print("\nHello, " + aa + "!")

def make_album(singer_name,album_name,quantity = " "):
    album = {"singer":singer_name,"album":album_name}
    if quantity:
        album["quantity"] = quantity
    print(album)
    return album

album1 = make_album("周杰伦","七里香")
album2 = make_album("eminem","The slim shady LP")
album3 = make_album("林俊杰","江南",quantity=17)