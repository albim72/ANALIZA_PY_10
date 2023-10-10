#Zbuduj ramkę pandas reprezentującą następującą tabelę
#kolumny: miesiąc(liczba), wartość sprzedaży, procent średniej sprzedaży z ostatnich 5 lat
#ramkę wstaw jako arkusz o nazwie sprzedaz, sformatuj odpwoiednio kolumny uwzględniając symbol % w ostatniej
#Nagłowki kolumn pogrubione

import pandas as pd
import xlsxwriter

df = pd.DataFrame({
    'Miesiąc':[1,2,3,4,5,6,7,8,9,10,11,12],
    'Wartość sprzedaży':[2340,1340,2002,1700,6700,5500,1200,1780,2300,2500,1230,1000],
    'Procent':[.47,.24,.43,.321,1.136,1.02,.20,.44,.47,.49,.21,.17]
})

writer = pd.ExcelWriter('procenty.xlsx', engine='xlsxwriter')
df.to_excel(writer,sheet_name='proc')

workbook = writer.book
worksheet = writer.sheets['proc']
format1 = workbook.add_format({'num_format':'#.##00'})
format2 = workbook.add_format({'num_format':'0.0%'})

worksheet.set_column(2,2,22,format1)
worksheet.set_column(3,3,None,format2)

writer.save()
