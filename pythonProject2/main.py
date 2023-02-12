#
# def myfunc(score):
#     if score == 1:
#         return 1
#     else:
#         # print("Number=", score)
#         return (score+myfunc(score-1))
#
#
# num = 10
# print("Summation of", num, "is", myfunc(num))



# a= "passed"
# b= "failed"
# return a if score>50 else b



import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return bool(string)

print("This is a string=",not(is_allowed_specific_char("ABCDEFabcdef123450")))
print("This is a string=",not(is_allowed_specific_char("*&%@#!}{")))



















