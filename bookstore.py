class Book:

    # deklaracja stanu (dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #zachowanie -> funkcje klasy - metody

    def create_book(self):
        print("Utworzono nowy obiekt klasy Book")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return procent/100 * self.cena
