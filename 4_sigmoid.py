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
class aditional_function(eu):
    def __init__(self,nume,prenume):
        super().__init__(nume,prenume)
    def add(self,a,b):
        print(a+b)
    def dicrease(self,m,n):
        print(m-n)
tudor = voi('Tudor','Gavriliuc','Iphone')
print(tudor.nume)
tudor.viorel()
jora = aditional_function('Jora','Jora')
jora.add(5,6)
jora.dicrease(5,6)