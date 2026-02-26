import matplotlib.pyplot as plt

x= ["Atletico de Madrid", "Real Madrid", "Barcelona", "Sevilla", "Valencia"]
y= [-400, 400, 66, 20, 50]



plt.bar(x, y)
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.title("BARRAS - Puntos por equipo")
plt.savefig('images/barras.png')
plt.show()

plt.plot(x, y)
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.title("PLOT - Puntos por equipo")
plt.show()