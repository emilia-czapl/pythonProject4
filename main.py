import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie1
# x=np.linspace(0,2,100)
#
# s= np.sin(x)
# p= np.cos(x)
# plt.plot(x, s, label="sin(x)")
# plt.plot(x, p, label="cos(x)")
# plt.show()



# Zadanie2

# xlsx= pd.ExcelFile('ceny1.xlsx')
# df4= pd.read_excel(xlsx, header=0)
# print(df4)
# print
# print(df4.agg({'Wartosc': ['sum']}))
# print(df4.agg({'Wartosc': ['mean']}))
# print(df4[df4['Rodzaje'] == 'ryz'].agg({'Wartosc': ['mean']}))
# print(df4[df4['Rodzaje'] == 'maka'].agg({'Wartosc': ['mean']}))
#
#
# plt.subplot(1, 2, 2)
# x = df4['Rok'].unique()
# ryz = df4[(df4.Rodzaje == 'ryz')].groupby('Rok').agg({'Wartosc':['sum']}).values
# maka = df4[(df4.Rodzaje == 'maka')].groupby('Rok').agg({'Wartosc':['sum']}).values
# plt.plot(x, ryz, label="ryz")
# plt.plot(x, maka, label="maka")
# plt.xlabel('Rok')
# plt.ylabel('Cena')
# plt.title('Cena produktów w danym roku')
# plt.legend()
# plt.text(2010,4,'123')
#
#
# plt.show()
# #
# #
# Zrobienie wykresu na podstawie wektoru!! np f(1/x) lub z wartości przedziałów lub liczby całkowite!!! umiescic na wykresie kilka elementów
#  2 i 3 xadane wczytanie plików . Cała ramka danych . Ramka danych wczytywana oddzielnie!. zwrac uwagę co wartości oddziela wiersze- czyli średnik

# Zadanie 3

# xlsx= pd.ExcelFile('ceny2.xlsx')
# df4= pd.read_excel(xlsx, header=0)
# print(df4)
#
#
# print(df4.agg({'Wartosć': ['sum']}))
# print(df4.agg({'Wartość': ['mean']}))
# print(df4[df4['Rodzaje towarów'] == ' ryż - za 1kg'].agg({'Wartość': ['mean']}))
# print(df4[df4['Rodzaje towarów'] == 'mąka pszenna - za 1kg'].agg({'Wartość': ['mean']}))





# Zadanie 3

# df4 = pd.read_csv('ceny.csv', header=0, sep=';', decimal='.')
# print(df4)
# print(df4.sort_values('Wartosc'))
# print(df4[df4['Rodzaje towarów i usług'] == 'jabłka - za 1kg '].agg({'Wartosc': ['sum']}))
# print(df4[df4['Rodzaje towarów i usług'] == 'pomarańcze - za 1kg'].agg({'Wartosc': ['mean']}))

#Kolumnowy
# fig, (ax1, ax2) = plt.subplots(1,2, )
# data = {'A': 35, 'B': 46 , 'C': 14, 'D': 41 ,'E': 40}
# data2 = {'A': -31, 'B': -34 , 'C': -38, 'D': -33 ,'E': -30}
#
# y = np.arange(0,40,10)
# z = np.arange(-30, 0, 10)
# osx = list(data.keys())
# wart1 = list(data.values())
# osx2 = list(data2.keys())
# wart2 = list(data2.values())
#
# color1 = ('powderblue', 'pink', 'coral', 'grey', 'darkviolet')
# color2 = ('violet', 'cyan','cyan','peru','olive'  )
#
# ax1.barh(osx, wart1, color = color1)
# ax2.barh(osx2, wart2, color = color2)
# ax1.set_title("Wykres lewy")
# ax2.set_title("Wykres prawy")
# plt.show()


# x = np.arange(-5, 6)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[0,21]')
# plt.show()

 # Zadanie 4 kina
# xlsx= pd.ExcelFile('kina4.xlsx')
# df4= pd.read_excel(xlsx, header=0)
# print(df4)

# plt.subplot(1, 2, 1)
# grouped = df4.groupby('Rok')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Wartosc').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red', 'blue'])
# plt.xlabel('Gestor')
# plt.ylabel('Wartosc')
# plt.show()


# plt.subplot(1, 3, 3)
# x = df4['Rok'].unique()
#
#
# miejskie = df4[(df4.Gestor == 'miejskie')].groupby('Rok').agg({'Wartosc':['sum']}).values
# woj = df4[(df4.Gestor == 'wojewodzkie miejsca na widowni')].groupby('Rok').agg({'Wartosc':['sum']}).values
# plt.plot(x, miejskie, label="miejskie")
# plt.plot(x, woj, label="wojewodzkie miejsca na widowni")
# plt.xlabel('Rok')
# plt.show()


xlsx= pd.ExcelFile('kraj.xlsx')
df4= pd.read_excel(xlsx, header=0)
print(df4)

df_zone = df4.groupby(by ='Kraje')
print(df_zone)
df2 = df_zone.get_group('Afryka')
df3 = df_zone.get_group('Ameryka')
print(df2,df3)

dfland = df4.groupby('Kraje')
# dfarea = dfland.agg({ Kraje== 'Afryka': ['sum']})
# # print(dfarea)
# print(df_zone.groupby('Kraje').agg({'Africa': ['sum']}))

# df1 = df4.groupby('Kraje').agg({'Religia': ['size']})
# print(df1)
# df1.plot(kind = 'bar', xlabel = 'Kraje', ylabel = 'ilosc krajów', title = 'ilosc krajow w strefach', legend = False )
# plt.show()

# Zad 1 J
# x = np.arange(-5,6,1)
# y = (x**2)+ (2*(x**2))
# plt.xlim(-5,5,1)
# plt.plot(x,y)
# plt.xlabel('Oś x')
# plt.ylabel('Oś y')
# plt.title('Wykres liniowy f(x)= x3+2x2')
# plt.show()
#
# Zad 2 J
# df = pd.read_csv('flags.csv', sep=";", decimal=".")
# print(df)
# df_zone = df.groupby(by ='Zone')
# print(df_zone)
# df2 = df_zone.get_group('NE')
# df3 = df_zone.get_group('NW')
#
# dfland = df.groupby('Landmass')
# dfarea = dfland.agg({'Area': ['sum']})
# print(dfarea)
#
# dfarea.plot(kind = 'pie', subplots=True, title = 'Wykres obszarow', fontsize = 14, autopct = '%.2f%%')
#
# plt.show()

# Zad. 3

# df1 = df.groupby('Zone').agg({'Country': ['size']})
# print(df1)
# df1.plot(kind = 'bar', xlabel = 'Zone', ylabel = 'ilosc krajow', title = 'ilosc krajow w strefach', legend = False )
# plt.show()


# 3 m

# df1 = df4.groupby('Religia').agg({'Kraje': ['size']})
# print(df1)
# df1.plot(kind = 'pie', subplots = True,  title = 'Religie', autopct='%.2f %%', fontsize=14 )
# plt.show()

