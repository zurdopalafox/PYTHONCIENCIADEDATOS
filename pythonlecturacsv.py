import pandas as pd


   


df_csv = pd.read_csv("data/datos.csv", delimiter=';', header=0)
print(df_csv)
print(df_csv.head())
print(df_csv.head(7))
print(df_csv.tail())
print(df_csv.tail(7))

diccionario = df_csv.to_dict(orient='records')

for elemento in diccionario:
    print(elemento)
    print(elemento["nombre"])
    print(elemento["edad"])
    print(elemento["genero"])
    print(elemento["ocupacion"])    


df_media = df_csv['edad'].mean()
print(df_media)

df_grupo = df_csv.groupby('ocupacion')

print(df_grupo.size())

