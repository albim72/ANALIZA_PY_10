print("to jest pierwsza linia")
print("druga linia")
print("trzecia linia")

# CTRL+/   - zakomentowanie linii/bloku lub odkomentowanie
# CTRL + D   - duplikacja linii/ bloku
# komentarz prosty - kolekcje pythona

"""
komentarz wieloliniowy - dokumentacyjny
xyz
"""

'''
komentarz wieloliniowy (zwykły)
abc
'''

#lista

imiona = ["Jan","Leon","Karol","Olga","Nadia","Leon","Danuta","Maria","Jan"]
print(imiona)
print(imiona[1])
print(imiona[2:5])
print(imiona[-2])

w = "kalejdoskop"
print(w)
print(type(w))

print(w[0])
print(w[1])
print(w[2:6])

print(imiona[0][2])
parzyste = imiona[::2]
print(parzyste)

wyr1 = "listopad"
wyr2 = "Urszula"

wyr1od = wyr1[::-1]
wyr2od = wyr2[::-1]

print(wyr1, "-",wyr1od)
print(wyr2, "-",wyr2od)

imiona.append("Klara")
print(imiona)
imiona.insert(3,"Bonifacy")
print(imiona)

imiona.remove("Maria")
print(imiona)

imiona.remove("Jan")
print(imiona)

imiona2 = imiona
imiona3 = list(imiona)
imiona4 = imiona[:]

print("_"*40)
print(type(imiona2))
print(imiona)
print(imiona2)
print(imiona3)
print(imiona4)

del imiona[2:5]
print("_"*40)
print(imiona)
print(imiona2)
print(imiona3)
print(imiona4)
