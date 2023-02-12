# try:
#     for i in [1, 2, 3]:
#             i = i**2
# except:
#     print("wrong values to multiply")
#
# else:
#     print(i)
#homework
# X = 5
# Y = 3
# try:
#     z = X/Y
# except:
#     print('Zero Division error')
# else:
#     print(z)

# def ask():
#     while True:
#
#         try:
#             values = int(input("PLease provide an integer: "))
#
#         except:
#             print("Type error")
#             continue
#         else:
#             square = values * values
#             print(f"Sqaure value is : {square}")
#             break
#
# ask()

# for i in range(6):\
#     print(f" {i}")

# from datetime import datetime
# try:
#     mydatetime =  datetime.now()
#     mydatetime2 = datetime(2021, 12, 3)
# except:
#     print("Incorrect month or date")
#
# else:
#     print(mydatetime-mydatetime2)
# import re
# text= 'my phone number is 01521-503628'
# # phone = re.search(r'\d\d\d\d\d-\d\d\d\d\d\d', text)
# phone = re.search(r'\d{5}-\d{6}', text)
#
# phone
# print(phone.group())


# def hello():
#     print('the hello() func')
#
#     def greet():
#         print("greet() func")
#
#     def welcome():
#         print('welcome() func')
#     greet()
#     welcome()
# hello()


import sqlite3
conn = sqlite3.connect('customer.db')
