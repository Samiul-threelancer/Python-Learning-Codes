class Mobile:
    def __init__(self, m):
        self.model = m
    def show_model(self, p):
        self.price = p
        print("Model; ", self.model, "Price; ", self.price )

redme = Mobile("Note 10")


redme.show_model(1000)

# for i in(1, 6):
#     print(i)
