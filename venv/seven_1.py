# words = 'If you tell us who you are, we can personalize the message you see.'
# words += 'What is your first name?'
#
# name = input(words)
# print('\nHello ,' + name + '!')
#
# age = input('What is your age?')
# print('老子今年' + age)

# number = int(input("告诉我一个数字，看看能不能被3整除"))
# message = ""
#
# if number % 3 == 0:
#     print("\n" + str(number) + "可以")
# else:
#     print("\n" + str(number) + "不可以")





# words = "你们来说一些东西"
# words += "\n我来当一下复读机"
#
# message = ""
#
# while message != "滚":
#     message = input(words)
#
#     if message == "滚":
#         print(message)

# words = "你们来说一些东西"
# words += "\n我来当一下复读机"
#
# active = True
#
# while active:
#     message = input(words)
#
#     if message == "滚":
#         active = False
#     else:
#         print(message)

# words = "\n这个喝不喝？"
# # words += "\n那个喝不喝？"
#
# message = "喝"
# while True:
#     city = input(words)
#
#     if city == "阿乐":
#         print(message)
#         break

# num = 0
#
# while num <= 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#
#     print(num)

#
# words = input("Welcome to the cinema.")
# words += input("\nHow old are you?")
# x = input(int)
# message = ""
#
#
# while x < 3:
#     message = input("That's free for you")







# unconfirmed_users = ["a","b","c"]
# confirmed_users = []
#
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print("Verifying user: " + current_users.title())
#
#     confirmed_users.append(current_users)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)


# responses = {}
#
# polling_active = True
# while polling_active:
#     name = input("What's your name?")
#     response = input("Which city would you like to visit?")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respond?(yes/no)")
#     if repeat == "no":
#         polling_active = False
#
# print("\n--- Poll Results")
# for name,response in responses.items():
#     print(name + " would you like to visit " + response + ".")
#
# print(responses)

# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# words = "让我们听听MC光光的歌吧"
# # words += "\n听到pussy sweet就换"
# # message = ""
# # while message != "pussy sweet":
# #     message = input(words)
# #     print(message)



# ticket = int(input("How old are you?"))
#
# if ticket < 3:
#     print("You're free")
#
# if 3 < ticket < 12:
#     print("Cost 10$")
# if ticket > 12:
#     print("Cost 15$")

# words = "让我们听听周杰伦的歌"
# words += "\n听到退后就不听了"
#
# message = ""
# while message != "退后":
#     message = input(words)
#     print(message)

# while True:
#     num_string = input("说一个数字，老子告诉你能不能被3整除")
#     if num_string == "老子不问了":
#         print("好的，滚吧你")
#         break
#     elif int(num_string) % 3 == 0:
#         print(str(num_string) + "可以哟")
#     else:
#         print("傻逼，" + str(num_string) + "不可以的")

