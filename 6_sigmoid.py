class naruto:
    def __init__(self,nume):
        self.nume = nume
    def func1(self):
        print("Eu sunt Naruto")
class sasuke(naruto):
    def __init__(self,nume,caracter):
        super().__init__(nume)
        self.caracter = caracter
    def func2(self):
        print("Eu sunt Sasuke")
class sakura(sasuke,naruto):
    def __init__(self,nume,caracter,color):
        super().__init__(nume,caracter)
        self.color = color
    def func3(self):
        print("Eu sunt Sakura")
ion = sakura('Sacura','moale','green')
ion.func1()
print(ion.nume)