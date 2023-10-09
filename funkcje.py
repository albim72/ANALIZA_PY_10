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
