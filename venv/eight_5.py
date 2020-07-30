# def make_pizza(*toppings):
# 当不确定实参的具体数量，可用（*实参）
#     """打印顾客点的所有配料"""
#     print(toppings)
#
# make_pizza("pepperoni")
# make_pizza("mushrooms","green peppers","extra cheese")

# def make_pizza(*toppings):

#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("-" + topping)
# make_pizza("pepperoni")
# make_pizza("mushrooms","green peppers","extra cheese")

# def make_pizza(size,*toppings):
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("-" + topping)

# make_pizza("15","mushrooms")

def build_profile(first_name,last_name,**userinfo):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    # **info的两个星号让python创建一个名为info的字典

    profiles = {}
    profiles["firs_name"] = first_name
    profiles["last_name"] = last_name
    for key,value in userinfo.items():
        profiles[key] = value
    return profiles

user_profile = build_profile("albert","einstein",loction="princeton",field="physics")
print(user_profile)
