class methodOverloading:

    def show(self, a):
        print("", a)

    def show(self, b):
        print("", b)

obj = methodOverloading()
# obj.show(5)
obj.show(555)