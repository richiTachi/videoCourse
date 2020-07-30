# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#         # 设定函数
#
# usernames = ["a","b","c"]
# greet_users(usernames)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_models = unprinted_designs.pop()

        print("Printing models: " + current_models)
        completed_models.append(current_models)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["iphone case","robot pendant","dodecahedron"]
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)