import matplotlib.pyplot as plt

diassemana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
temperaturas = []

for i in diassemana:
   temper   = input (f"Introduzca la temperatura del día {i} : ")
   temperaturas.append(temper)

plt.plot(diassemana, temperaturas, label="Semana1")
temperaturas2 = [11,15,28,-5 -2, 100,80,50]
plt.plot(diassemana,temperaturas2, label="Semana2")
plt.legend()    # Para imprimir
plt.title("Temperaturas de la semana")
plt.xlabel("Día Semana")
plt.ylabel("Temperatura (°C)")
plt.show()
