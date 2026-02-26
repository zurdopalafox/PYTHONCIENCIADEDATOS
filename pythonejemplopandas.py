import pandas as pd
datos = {
    "Nombres": ["Ana", "Carlos", "Beatriz", "David"],
    "Edad": [25, 30, 22, 35],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}

df = pd.DataFrame(datos)
print(df)
#Podemos filtrar los datos si lo deseamos
print("Dataframe filtrado por edad mayor a 25")
df_filtrado = df[df["Edad"] > 25]
print(df_filtrado) 

print("Dataframe Ordenado por Edad (Ascendente)")
df_ordenado = df.sort_values(by="Edad")
print(df_ordenado)

print("Dataframe Ordenado por Edad (Descendente)")
df_ordenado = df.sort_values(by="Edad", ascending=False)
print(df_ordenado)
