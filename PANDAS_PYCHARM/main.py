import pandas as pd

dane = {
    'jabłko':[3,12,6,1],
    'pomarańcze':[2,1,0,9],
    'banan':[0,5,4,2],
    'gruszka':[3,3,3,6]
}

owocframe = pd.DataFrame(dane)
print(owocframe)

owocframe = pd.DataFrame(dane,index=['Jan','Anna','Olga','Olaf'])
print(owocframe)
print("_____________  OWOCE JANA  _________________")
print(owocframe.loc['Jan'])

owocframe.to_csv('owoce.csv')

newframe = pd.read_csv('owoce.csv')

print(newframe)
print("_"*40)
dffirma = pd.read_csv("firma.csv",index_col=0)

print(dffirma)

