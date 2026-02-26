import matplotlib.pyplot as plt

x= ["Atletico de Madrid", "Real Madrid", "Barcelona", "Sevilla", "Valencia"]
y= [-400, 400, 66, 20, 50]



plt.scatter(x, y)
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.title("Scatter - Puntos por equipo")
plt.savefig('images/scatter.png')
plt.show()

