class Father:
    def __init__(self):
        print("Father constructor")
    def showF(self):
        print("Father method")


class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son constructor")

    def showS(self):
        print("Son method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter constructor")

    def showD(self):
        print("Daughter method")

D = Daughter()
D.showF()
S = Son()
S.showS()
