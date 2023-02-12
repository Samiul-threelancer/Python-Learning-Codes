class Parent:
    money = 1000

    def dis(self):
        print("I am parent class")

class Child(Parent):

    def show(self):
        print("I am child Class")
class grandChild(Child):

    def show1(self):
        print("I am grand Child")

c = grandChild()
c.show()
c.dis()
c.show1()