from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass


class Child1(Father):
    def disp1(self):
        print("Child 1 Class")
        print("Disp1 abstract method")

class grandChild(Child1):
    def disp2(self):
        print(" Grand Child Class")
        print("Disp2 abstract method")

gc = grandChild()
gc.disp1()
gc.disp2()

