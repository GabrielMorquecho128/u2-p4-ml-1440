import pandas as pd
import numpy as np
# marco morquecho NC 1440
n_filas =5
n_columnas =5
tag_columna = tuple("ABCDE") # etiqueta para las columnas de una tupla
print(tag_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Ganera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es Dataframe
df = pd.DataFrame(matriz, columns= tag_columna)
print("--- La tabla o dataframe --- NC 1440")
print(df)
print("--- marco morquecho NC 1440 ---")