def greet_user():
    """显示简单的问候语"""
    print("Hello")

greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print("Hello,"+ username.title())

greet_user("wenzhi")


def display_message():
    """这章学到什么"""
    print("这章学到函数")

display_message()

def favorite_book(book):
    """最喜欢的书"""
    print("my favorite book is " + book.title())

favorite_book("Harry poter")