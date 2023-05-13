T200= float(input("Escribe porcentaje % retenido en el tamiz 200: ")) # se ingresa el porcentaje que pasa por el tamiz #200
if T200>50: #se usa la funcion if para conocer si el porcentaje es mayor o menor  al 50%
    print("Es un suelo de tipo Grueso") #se clasifica el suelo como suelo Grueso
    T4= float(input("Escribe porcentaje % retenido en el tamiz # 4: "))#se ingresa el porcentaje que pasa por el tamiz #4     
    cu=float(input("Escribe el valor de coeficiente de uniformidad (Cu): ")) #se ingresa el vaslor de coeficiente de  uniformidad
    cc=float(input("Escribe el valor de coeficiente de curvatura (Cc): ")) #se ingresa el valor de coeficienete de curvatura
    if T4>50: # Se clasifican como Grava
      if T200<5: # porcentaje menor al 5%, se clasifica como Gravas limpias
        if cu>=4 and (cc<3 or cc>1):#se clasifica usando valores de cc y cu
          print("GW (Grava bien graduada)")#se imprime  el tipo de suelo
        elif cu<4 and (cc>3 or cc<1):#se clasifica usando valores de cc y cu
          print("GP (Grava mal graduada)")#se imprime  el tipo de suelo
        else:
          print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion         
      elif T200>12: #porcenetaje mayor al 12%, se clasifican como Gravas con finos
        IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad
        if  IP>7:#se clasifica usando el IP
          print("GC (Grava Arcillosa)")#se imprime  el tipo de suelo
        elif IP<4:#se clasifica usando el IP
          print("GM (Grava limosa)")#se imprime  el tipo de suelo
        else:
          print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion 
      else: # porcentaje de finos entre 5% y 12, se clasifica como gravas limpias y con finos 
        IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad
        if cu>=4 and (cc>=1 and cc<=3):
          if IP<4:#se clasifica usando el IP
            print("GW-GM (Grava bien graduada con limo)")#se imprime  el tipo de suelo
        elif cu>=4 and (cc>=1 and cc<=3):
          if IP>7:#se clasifica usando el IP
            print("GW-GC (Grava bien graduada con arcilla)")#se imprime  el tipo de suelo
        else:
          print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion
        if cu<4 and (cc<1 and cc>3):
          if IP<4:#se clasifica usando el IP
            print("GP-GM (Grava mal graduada con limo)")#se imprime  el tipo de suelo
          else:
            if IP>7:#se clasifica usando el IP
              print("GP-GC (Grava mal graduada con arcilla)")#se imprime  el tipo de suelo                                 
    else: #se calsifican como arenas
       if T200<5:
         if cu>=6 and 1<=cc <=3:
           print("SW (Arena bien graduada)")#se imprime  el tipo de suelo
         elif cu<6 and (1>cc or cc>3):
           print("SP (Arena mal graduada)")#se imprime  el tipo de suelo
         else:
           print("No aplica a la calsificacion")#se imprime que no entra en la clasificacion
       elif T200>12:
         IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad
         if IP<4:#se clasifica usando el IP
           print("SM (Arena limosa)")#se imprime  el tipo de suelo
         elif IP>7:#se clasifica usando el IP
           print("SC (Arena arcillosa)")#se imprime  el tipo de suelo
         else:
           print("No aplica a ninguna clasificacion") #se imprime que no entra en la clasificacion
       else:
         if (cu>=6 and 1<=cc <=3):
           IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad
           if IP<4:#se clasifica usando el IP
             print("SW_SM (Arena bien graduada con limo)")#se imprime  el tipo de suelo
           elif IP>7:#se clasifica usando el IP
             print("SW_SC (Arena bien graduada con arcilla)")#se imprime  el tipo de suelo
           else:
             print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion
         elif cu<6 and (1>cc or cc>3):
           IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad
           if IP<4:#se clasifica usando el IP
             print("SP_SM (Arena mal graduada con limo)")#se imprime  el tipo de suelo
           elif IP>7:#se clasifica usando el IP
             print("SP_SC (Arena mal graduada con arcilla)") #se imprime  el tipo de suelo
           else:
             print("No aplica a la clasfificacion")#se imprime que no entra en la clasificacion
         else:
           print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion                
else:  
  print("Se clasifican como finos")#se clasifica el suelo como finos
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

LL=float(input("Ingresa el valor del limite liquido (LL): ")) #se ingresa el valor del limite liquido
IP=float(input("Ingrese el valor del indice de plasticidad(IP): "))# se ingresa el valor de indice de plasticidad

def cartaPlasticidad(LL,IP):

    # Con los datos del limite liquido y el Indice de plasticidad se grafica la ubicación del suelo en la carta de plasticidad.
    plt.plot(LL,IP,'ro')
    plt.vlines(LL,0,60,'k','--')
    plt.annotate(' LL ',(LL,55))
    plt.annotate(' IP ', (20,IP + 2))
    plt.hlines(IP,0,100,'k','--')

    # Se establecen los limites de los ejes x,y.
    plt.xlim(0,100)
    plt.ylim(0,60)

    # Para graficar las lineas de la carta de plasticidad utilizamos las ecuaciones conocidas para la Linea A y la Linea U:
    x=np.array([0,100])
    LineaA =0.73*(x-20)
    LineaU = 0.9*(x-8)
    plt.annotate('Linea A', (90,50),rotation=38) # Etiqueta de la linea A
    plt.annotate('Linea U', (60,45),rotation=45) # Etiqueta de la linea U

    # Estas lineas gráfican las lineas A y U de forma estética
    plt.plot(x, LineaA, 'darkblue', label = "Linea A" )
    plt.plot(x, LineaU, 'k:', label = "Linea U")

    # Graficamos lineas frontera de la carta de plasticidad donde se encuentran los suelos CL-ML
    plt.hlines(7,15.7,29.5,'m')
    plt.hlines(4,12.4,25.5,'m')

    # Estas lineas permiten que se muestren en la gráfica las etiquetas de las diferentes zonas.

    region_MH = np.array([[50,0], [50,22], [100,58], [100,0]])
    region_ML = np.array([[25.5,4], [12.4,4], [8,0], [20,0], [50,0], [50,22]])
    region_CH = np.array([[50,22], [100,58], [100,60], [75,60], [50,38]])
    region_CL_ML = np.array([[29.5,7], [15.7,7], [12.4,4], [25.5,4]])
    region_CL = np.array([[15.7,7], [29.5,7], [50,22], [50,38]])

    path_MH = mpath.Path(region_MH)
    path_CH = mpath.Path(region_CH)
    path_CL = mpath.Path(region_CL)
    path_CL_ML = mpath.Path(region_CL_ML)
    path_ML = mpath.Path(region_ML)

    point = np.array([LL,IP])
    if path_MH.contains_point(point):
        print('El punto se encuentra en la zona MH')
    elif path_CH.contains_point(point):
        print('El punto se encuentra en la zona CH')
    elif path_CL.contains_point(point):
        print('El punto se encuentra en la zona CL')
    elif path_CL_ML.contains_point(point):
        print('El punto se encuentra en la zona CL-ML')
    elif path_ML.contains_point(point):
        print('El punto se encuentra en la zona ML')
    else:
        print('El punto no se encuentra en la carta de plasticidad')


    plt.annotate('CL-ML', (15,5))
    plt.annotate('MH', (80,20))
    plt.annotate('CL', (30,15))
    plt.annotate('CH', (62,40))
    plt.annotate('ML', (35,5))
    plt.annotate('NO EXISTE', (15,35))

    # Divide la gráfica cuando el limite liquido es igual a 50 para diferenciar si el suelo es de plasticidad alta o baja
    plt.vlines(50,0,60,'g')

    # Estas lineas mejoran la estetica de la gráfica, hacen que se sombreen las diferentes zonas de la carta de plasticidad
    # Dentro de las variables de la d a la m se guardan las coordenadas que delimitan cada zona.
    d=[50,50,100,100]
    e=[0,22,58,0]
    plt.fill(d,e,'pink')
    f=[25.5,12.4,8,20,50,50]
    g=[4,4,0,0,0,22]
    plt.fill(f,g,'lightgray')
    h=[50,100,100,75,50]
    i=[22,58,60,60,38]
    plt.fill(h,i,'lightgreen')
    j=[29.5,15.7,12.4,25.5]
    k=[7,7,4,4]
    plt.fill(j,k,'m')
    l=[15.7,29.5,50,50]
    m=[7,7,22,38]
    plt.fill(l,m,'bisque')

    # Se grafica la grilla, el titulo y las etiquetas de los ejes.

    plt.grid()
    plt.title("Carta de plasticidad",fontsize=10)
    plt.xlabel("Limite liquido",fontsize=10)
    plt.ylabel("Indice de plasticidad",fontsize=10)
    plt.legend()
    plt.show()
cartaPlasticidad(LL,IP)  