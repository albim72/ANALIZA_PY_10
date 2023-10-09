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
