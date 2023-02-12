class Duck:
    def walk(self):
        print("Duck Duck Duck")

class Horse:
    def halk(self):
        print("Horse Horse")

class Cat:
    def calk(self):
        print("Cat Cat Cat")




def myFunc(obj):

    obj.calk()
    print(obj.calk())


d = Duck()
h = Horse()
C = Cat()
myFunc(C)
print(myFunc())

# def func(a = None, b=None):
#     print(a+b)
#     if a!=None and b!=None:
#         print(a, b)
#
# func(3,2)