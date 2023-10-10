import matplotlib.pyplot as plt

#dane
labels = 'Warszawa','Kraków','Lublin','Katowice','Gdańsk'
sizes = [56,34,26,24,30]
explode = (0,0.1,0,0,0.2)

#wykres
fig,ax = plt.subplots()
ax.pie(sizes,explode=explode, labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
plt.show()
