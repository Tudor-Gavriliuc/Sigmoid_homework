class eu:
    def __init__(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
    def viorel(self):
        print("Aici a fost Tudor")
Tudor = eu('Tudor','Gavriliuc')
Tudor.viorel()
print(Tudor.nume)