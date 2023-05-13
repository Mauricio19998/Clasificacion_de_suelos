import matplotlib.pyplot as plt   
import numpy as np  
import pandas as pd


def carta_plasticidad(Limite_liquido,Indice_plasticidad):
    
    
    # con los datos del limite liquido y l indice de plasticidad se grafica la ubicacion del suelo en la carta de plasticidad
    plt.plot(Limite_liquido,Indice_plasticidad,'ro')
    plt.vlines(Limite_liquido,0,60,'m','--')
    plt.annotate(' LL ', (Limite_liquido,30))
    plt.annotate(' IP ', (20,Indice_plasticidad + 2))
    plt.hlines(Indice_plasticidad, 0, 100, 'g', '--')

    # # Se establecen los limites de los ejes x,y
    plt.xlim(0,100)
    plt.ylim(0,60)

    #Para la grafica de lineas de la carta de plasticidad
    x=np.array([0,100])
    LineaA =0.73*(x-20)
    LineaU = 0.9*(x-8)


    ## estas lineas grafican las lineas A y U
    plt.plot(x, LineaA, 'darkblue', label = "Linea A")
    plt.plot(x, LineaU, 'y', label = "Linea U")


    plt.annotate('Linea A', (90,50), rotation=38) #Etiqueta
    plt.annotate('Linea U', (60,45), rotation=45) #Etiqueta

    # graficamos lineas de frontera de la carta de plasticidad
    plt.hlines(7,15.7,29.5,'m')
    plt.hlines(4,12.4,25.5,'m')
    plt.annotate(' CL-ML ',(15,5))
    plt.annotate(' MH ', (80,20))
    plt.annotate(' CL ', (30,15))
    plt.annotate(' CH ', (62,40))
    plt.annotate(' ML ', (35,5))
    plt.annotate(' NO EXISTE ', (15,35))

    #Dentro de las variables de las d a la m
    d=[50,50,100,100]
    e=[0,22,58,0]
    plt.fill(d,e, 'orange')

    plt.grid()
    plt.title("Carta de plasticidad", fontsize=10)
    plt.xlabel("Limite liquido", fontsize=10)
    plt.ylabel("Indice de plasticidad", fontsize=10)
    plt.show()

    print('x')