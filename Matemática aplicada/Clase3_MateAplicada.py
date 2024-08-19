#Función para separar precios segun miles ejemplo: Tengo 10000 lo convertira en 10.000 
def formatear_precio_miles(precio):
    return f"{precio:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.');


def calculored(x):
    return 100*x


# Se llama a la biblioteca numpy, para trabajar con arreglos de datos
import numpy as np
# Módulo de la biblioteca scipy que nos permitirá poder resolver ecuaciones no necesariamente lineales
# a través de la función fsolve
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

"""
Ejercicio 4:

Como parte de un proyecto de mejora, en el año $2021$ se instaló un cable de fibra óptica que une España con EEUU. 
El cable tiene un largo de $6.600$ $km$ y fue colocado por un barco a una velocidad de $1,85$ $km/h$.



1.   Determine la forma algebraica de la función que permite determinar el largo del cable instalado (en km) a partir del tiempo transcurrido (en horas). 
     Utilice la instrucción *def* para definir la función en *Python*.
2.   Defina variable dependiente e independiente, indicando unidad de medida.
3.   Determine el dominio contextualizado de la función.
4.   Grafique la función utilizando la biblioteca *Matplotlib* considerando el dominio contextualizado.
5.   ¿Cuántos metros de cable se instalaron al transcurrir $148$ horas? ¿Y transcurridas $2.300$ horas?
6.   Si se han instalado $3.480$ kilometros de cable, ¿cuántas horas llevan de trabajo?
7.   ¿Cuánto tiempo transcurrió para que se completara la obra?

c = np.linspace(0,3570,1)
re = fsolve(nombrefuncion,c)
#Nos permite sacar el resultado para la variable independiente para cualquier funcion


def Calcularlargoinstalado(tiempo):
    #if (1.85*tiempo) > 6600:
    #   return 6600
    return 1.85*tiempo

def CalculartiempoTranscurrido(Largo):
    return Largo/1.85

c = np.arange(0,3570,1);
print(f"\nRespuesta 1: T(h) = 1.85(km/h) * h(h)");
print(f"\nRespuesta 2: \nVariable dependiente = Largo de cable instalado (km)\nVariable independiente = Tiempo transcurrido (h)");
print(f"\nRespuesta 3: [0,{formatear_precio_miles((6600/1.85))}]");
print(f"\nRespuesta 4: Grafico");
print(f"\nRespuesta 5: \n148 horas = {formatear_precio_miles(Calcularlargoinstalado(148))} km de largo instalado\n2300 horas = {formatear_precio_miles(Calcularlargoinstalado(2300))} km de largo instalado");
print(f"\nRespuesta 6: {formatear_precio_miles((CalculartiempoTranscurrido(3480)))} horas transcurridas");
print(f"\nRespuesta 7: {formatear_precio_miles((6600/1.85))} horas transcurridas");

#Grafico respuesta 4
plt.plot(c,Calcularlargoinstalado(c))
plt.title("Largo del cable a traves del tiempo")
plt.xlabel("Tiempo transcurrido(h)")
plt.ylabel("Largo del cable(km)")
plt.grid(True)
plt.show()
print("")
"""

"""
Ejercicio 5:

Un turista ha llegado a Santiago y desea conocer algunos lugares de la ciudad. Ha decidido visitar el Palacio de la Moneda y desde ahí trasladarse al centro comercial 
"Costanera Center", utilizando algún medio de transporte que ofrece la ciudad.

Si se traslada en metro deberá abordar en estación La Moneda y bajar en la estación Tobalaba (9 estaciones). 
La función f(t) permite calcular la distancia recorrida utilizando el metro (en kilómetros) transcurridos t minutos.

f(t) = 0,4t

Si se traslada en bus, el turista podrá observar la ciudad y otros atractivos en su viaje. La función g(t) permite calcular 
la distancia recorrida en bus (en kilómetros) transcurridos t minutos.

g(t) = 0,3t

Según la información anterior:

1. Grafique ambas funciones, indicando el nombre de cada eje junto con su unidad de medida. Para realizar el gráfico utilice la biblioteca *Matplotlib*.
2. Si se sabe que el metro se demora $1,2$ minutos en llegar desde una estación a otra y espera $30$ segundos en cada estación, indique el dominio contextualizado para $f(t)$.
3. Mediante análisis gráfico, indique cuál medio de transporte es más conveniente en términos de tiempo, para el turista. Justifique.
4. Si se sabe que desde estación La Moneda hasta Tobalaba son aproximadamente $6$ kilómetros 
¿cuántos tiempo tardará el turista en llegar a su destino con cada una de las opciones?
"""
"""
def distanciaMetro(x):
    return 0.4*x
def distanciaBus(b):
    return 0.3*b

b = np.arange(0,20,1)
x = np.arange(0,20,1)
plt.plot(x,distanciaMetro(x),label='Metro', color='purple')
plt.plot(b,distanciaBus(b),label='Bus', color='cyan')
plt.legend()
plt.title("Largo del cable a traves del tiempo")
plt.xlabel("Tiempo transcurrido(min)")
plt.ylabel("Distancia recorrida(km)")
plt.grid(True)
print("")

print(f"Respuesta 1: Grafico")
print(f"Respuesta 2: [{0};{formatear_precio_miles(((9*1.2)+(0.5*8)))}]")
print(f"Respuesta 3: En metro")
print(f"Respuesta 4:\nCalculo metro: {formatear_precio_miles(6/0.4)}\nCalculo bus: {formatear_precio_miles(6/0.3)}")
def resolucionmetro(x):
    return (0.4*x) - 6
def resolucionbus(b):
    return (0.3*b) - 6
x = np.linspace(0,30,1)
re = fsolve(resolucionmetro,x)

b = np.linspace(0,30,1)
re2 = fsolve(resolucionbus,b)
print(f"Resolucion segunda forma pregunta 4: metro: {re}, bus {re2}")
plt.show()
"""

"""
Ejercicio 7:

El número de usuarios de una red social se puede modelar mediante la función:

U(t) = 1.000/1+9e^-0.5t

donde t corresponde al tiempo transcurrido en meses.

1.  Defina variable dependiente e independiente, indicando unidad de medida.
2.  Determine la cantidad de usuarios transcurridos $12$ meses.
3.  Grafique la función, utilizando la librería *Matplotlib*, para los primeros dos años de funcionamiento.
4.  ¿Cuánto tiempo debe pasar para que la red social llegue a $800$ usuarios?
"""
def usuarios_meses(t):
    return 1000 / (1 + 9 * np.exp(-0.5 * t))
print(f"Respuesta 1: \nVariable dependiente: Número de usuarios(u)\nVariable independiente: Tiempo transcurrido(meses)")
print(f"Respuesta 2: La cantidad de usuarios despues de 12 meses es: {formatear_precio_miles(usuarios_meses(12))}")
print(f"Respuesta 3: grafico")
def meses_usuarios(x):
    return (1000 / (1 + 9 * np.exp(-0.5 * x))) - 800
x = np.linspace(0,30,1)
re2 = fsolve(meses_usuarios,x)
print(f"Respuesta 4 : Deben pasar {re2[0]:.1f} meses para llegar a los 800 usuarios")

time = np.arange(0,100,0.01)
plt.plot(time,usuarios_meses(time),label='Usuarios', color='cyan')
plt.legend()
plt.title("Largo del cable a traves del tiempo")
plt.xlabel("Tiempo transcurrido(meses)")
plt.ylabel("Usuarios(usuarios)")
plt.grid(True)
plt.show()
print("")