import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt # Se importa la librería
#se hace una lista para poder poner los nombres de los tamices
tamiz = pd.Series(['1 1/2"','1"','3/4"','3/8"','No.4','No.10','No.20','No.40','No.60','No.100','No.200'])
#Se hace una lista con el valor de la malla de los tamices en mm
tamaño_particulas = pd.Series([
    37.5, #abertura tamiz 1 1/2"
    25.4, #abertura tamiz 1"
    19, #abertura tamiz 3/4"
    9.51, #abertura tamiz 3/8"
    4.76, #abertura tamiz No.4
    2, #abertura tamiz No.10
    0.841, #abertura tamiz No.20
    0.420, #abertura tamiz No.40
    0.250, #abertura tamiz No.60
    0.149, #abertura tamiz No.100
    0.074 #abertura tamiz No.200
])

#Se crea una variable para almacenar los valores de los porcentajes de partículas que pasan por cada tamiz
porcentaje_pasa = pd.Series([
    100, #porcentaje de partículas que pasan por el tamiz 1 1/2"
    100, #porcentaje de partículas que pasan por el tamiz 1"
    100, #porcentaje de partículas que pasan por el tamiz 3/4"
    100, #porcentaje de partículas que pasan por el tamiz 3/8"
    100, #porcentaje de partículas que pasan por el tamiz No.4
    86.5, #porcentaje de partículas que pasan por el tamiz No.10
    52, #porcentaje de partículas que pasan por el tamiz No.20
    38.4, #porcentaje de partículas que pasan por el tamiz No.40
    23, #porcentaje de partículas que pasan por el tamiz No.60
    8.5, #porcentaje de partículas que pasan por el tamiz No.100
    2.1 #porcentaje de partículas que pasan por el tamiz No.200
])

#se tabulan los límites superior e inferior máximo permitidos por el INVIAS
#limite superior
limite_superior_ejey = pd.Series([100,100,100,100,100,100,100,85,60,30,10])
limite_superior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15]) 

#limite inferior
limite_inferior_ejey = pd.Series([100,100,100,100,100,95,80,50,25,10,2])
limite_inferior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15])

#Se crea una variable para poder organizar los datos en forma de tabla
tabla = pd.DataFrame({
    'tamiz': tamiz,
    'tamaño particulas(mm)': tamaño_particulas,
    'porcentaje pasa': porcentaje_pasa,
    'Limite superior y': limite_superior_ejey,
    'limite superior x': limite_superior_ejex,
})

print(tabla)
# se grafica la grafica y los valores de los limites
plt.scatter(limite_superior_ejex,limite_superior_ejey)
plt.plot(limite_superior_ejex,limite_superior_ejey, label = "Límite superior")
plt.scatter(limite_inferior_ejex,limite_inferior_ejey, label = "Límite superior")
plt.plot(limite_inferior_ejex,limite_inferior_ejey, label = "Límite inferior")
plt.scatter(tamaño_particulas,porcentaje_pasa, label = "Límite superior")
plt.plot(tamaño_particulas,porcentaje_pasa, label = "granulometria")
plt.grid(color='grey', lw = 0.5)
plt.xscale('log',base=10)
plt.gca().invert_xaxis()
plt.title("DISTRIBUCION GRANULOMETRICA", fontsize=15, color = "black")
plt.xlabel("Tamaño de partícula (mm)",fontsize=12)
plt.ylabel("Porcentaje que pasa (%)",fontsize=12)
plt.ylim(0,110) #Se establecen el limte maximo del eje y
plt.annotate("Limite superior",(0.5,65))
plt.annotate("Limite inferior",(4,30))
plt.show()