class eu:
    def __init__(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
        self.color = 'green'
    def viorel(self):
        print("Aici a fost Tudor")
class tu(eu):
    def __init__(self,nume,prenume,kalian):
        super().__init__(nume,prenume)
        self.kalian = kalian
class change(eu):
    def __init__(self,nume,prenume,orange):
        super().__init__(nume,prenume)
        self.orange = orange
    def change_color(self,newcolor):
        self.color = newcolor
        print("Verdele s-a transformat in {}".format(self.color))
matei = change('matei','matei',5)
matei.change_color('azuriu')