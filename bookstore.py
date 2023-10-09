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

    def nowa_oprawa(self,nowa):
        self.oprawa = nowa

b1 = Book(23,"Wiedźmin","Andrzej Sapkowski",42)
#b1.oprawa = "twarda"
b1.nowa_oprawa("twarda")
b1.print_book()
print(f"rabat: {b1.rabat(15)} zł")

print("_"*50)
b2 = Book(44,"Hobbit","J.R.R Tolkien", 36)
b2.print_book()
print(f"rabat: {b2.rabat(12)} zł")


