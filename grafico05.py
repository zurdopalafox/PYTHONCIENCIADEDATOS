import matplotlib.pyplot as plt

productos=[]
ventas = []
for i in range(1,6):
   prod   = input ("Introduzca el nombre catálogo de los productos: ")
   num = int(input("Introduzca las ventas: "))
   productos.append(prod)
   ventas.append(num)

plt.pie(ventas, labels=productos) 
plt.show()            


