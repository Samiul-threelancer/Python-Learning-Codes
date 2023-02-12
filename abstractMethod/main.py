# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
#
#     def show(self):
#         print('Concrete method')
#
# class Child(Father):
#
#     def disp(self):
#         print('Child Class')
#         print('Defining Abstract method ')
#
# c = Child()
# c.disp()
# c.show()


from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Gun(self):
        print('Gun = AK47')

class Army(DefenceForce):
    def Area(self):
        print('Area = Land')

class AirForce(DefenceForce):
    def Area(self):
        print('AirForce = Sky')

class Navy(DefenceForce):
    def Area(self):
        print('Area = Water')

a = Army()
AF = AirForce()
N =  Navy()
a.Gun()
a.Area()

N.Gun()
N.Area()

AF.Gun()
AF.Area()