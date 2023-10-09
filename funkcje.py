#przykład 1

n=100
def policz(a,b,c=8,y=3.4):
    global n
    n = (a+b)*y - c + n
    return  n

print(policz(2,6,7,2))
print(policz(2,6,7))
print(policz(2,6))

print(policz(2,3,c=12,y=8.9))
print(n)

#przykład 2

def ranking(jez1, jez2, jez3):
    print(f'ranking języków programowania - miejsca -> 3:{jez3}, 2: {jez2}, 3:{jez1}')

ranking("Python","Java","C#")


def rank(*lang,nrrank):
    print(f'ranking języków programowania nr {nrrank} - miejsca -> 3:{lang[2]}, 2: {lang[1]}, 3:{lang[0]}')

rank("Python","Java","JavaScript","C#",nrrank=45)
rank("Python","Java","Perl","JavaScript","C#","Ruby",nrrank=47)

lng = ("Python","Java","JavaScript","PHP")
rank(lng[0],lng[1],lng[2],lng[3],nrrank=4)


#przykład 3
#funkcja anonimowa, lambda

print((lambda e:e**7)(4.5))

b = lambda a,b:a+b**(a-4)
print(b(16,4))

def multi(n):
    return lambda a:a*n

print(multi(6)(5))

#przykład 4
num = [67,2,5,-17,0,122,34,56,118,-100,0,98,-4,13]

parzyste_n = list(filter(lambda x:x%2==0,num))
print(parzyste_n)

cube = list(map(lambda x:x**3,num))
print(cube)


import time
blista = [m**4 for m in range(10_000_000)] #list comprehension

start = time.perf_counter() #czas [s] który upłynął  od 1.1.1970
print(start)
print(sum(blista))

end = time.perf_counter()
print(end)

print(f'wykonanie listy trwało: {end - start} s')

#przykład 5

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum-minimum
    liczbael = len(lista)
    return [minimum,maksimum,rozstep,liczbael]


wynik = pokaz_statystyki(num)
print(wynik)
print(type(wynik))

mini,maxi,roz,le = pokaz_statystyki(num)

print(f"wartość max = {maxi}, wartość min = {mini}, rozstęp = {roz}, liczba elementów: {le}")
