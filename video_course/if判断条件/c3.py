"""一段小程序"""

account = "wenzhi"
password = "123456"

print("Please input your account:")
user_account = input()
print("Please input your password:")
user_password = input()

if user_account == account and user_password == password:
    print("success")
else:
    print("fail")
