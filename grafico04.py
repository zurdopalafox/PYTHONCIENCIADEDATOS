import matplotlib.pyplot as plt

Equipos = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Sevilla", "Valencia"]
Valores = [50, 400, 66, 20, 50]



plt.pie(Valores, labels=Equipos)
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.title("PIE - Puntos por equipo")
plt.savefig('images/pie.png')
plt.show()