class eu:
    def __init__(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
    def viorel(self):
        print("Aici a fost Tudor")
class tu(eu):
    def __init__(self,nume,prenume,kalian):
        super().__init__(nume,prenume)
        self.kalian = kalian
class noi(eu):
    def __init__(self,nume,prenume,orange):
        super().__init__(nume,prenume)
        self.orange = orange
class voi(eu):
    def __init__(self,nume,prenume,apple):
        super().__init__(nume,prenume)
        self.apple = apple
tudor = voi('Tudor','Gavriliuc','Iphone')
print(tudor.nume)
tudor.viorel()