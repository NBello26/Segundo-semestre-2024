#Función para separar precios segun miles ejemplo: Tengo 10000 lo convertira en 10.000 
def formatear_precio_miles(precio):
    return f"{precio:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.');


def calculored(x):
    return 100*x


# Se llama a la biblioteca numpy, para trabajar con arreglos de datos
import numpy as np
# Módulo de la biblioteca scipy que nos permitirá poder resolver ecuaciones no necesariamente lineales
# a través de la función fsolve
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

"""
Codigo para sacar valor variable dependiente
# Se le asigna a un arreglo t valores desde 0 hasta 50 con un espacio de distancia. Por lo tanto, este vector
# contiene solo el elemento 0
t = np.linspace(0, 50, 1);

# Se le asigna a un arreglo sol, la(s) solución(es) entre la expresión retornada en def y el arreglo t.
# Como este  ́ultimo arreglo contiene solo el elemento 0, entonces fsolve busca la solución entre la expresión 40-10*e-0 y 0, evaluando a traves del arreglo t valores 
# desde 0 hasta 50
sol = fsolve(C,t);
print(sol[0]);
"""

"""
Ejercicio 2:

Utilizando la función definida en el problema $1$, genera un listado que muestre los datos transmitidos para tiempos 
desde 0 hasta 1.000 segundos con incrementos de 100 segundos.

lista = [["segundos","mb"]];
for i in range(0,1100,100):
    lista.append([i,calculored(i)]);
    print(f"A los {i} segundos {calculored(i)} mb transmitidos");
print(lista)
"""

"""
Ejercicio 3:

La **latencia** de una red corresponde al tiempo que tarda un paquete de datos en viajar desde el punto de origen al destino. En otras palabras, es el tiempo que transcurre
desde que se envía una solicitud de un dispositivo hasta que se recibe una respuesta del servidor u otro dispositivo.
La latencia puede verse afectada por la velocidad de transmisión de los datos a través de los cables o conexiones inalámbricas, la distancia física entre los dispositivos, el 
tiempo que tarda un computador en procesar o reenviar los datos, etc.
En redes de comunicación, como las videoconferencias, juegos en línea y transmisión de datos en tiempo real, es deseable una baja latencia, de lo contrario pueden 
existir retrasos en la comunicación y afectar negativamente la experiencia del usuario.

Según el contexto mencionado, crea una función en *Python* que permita calcular la **latencia real** de una red dada una latencia estimada. 
Suponga que la latencia real es un 20% mayor a la latencia estimada.

Calcule la latencia real para una latencia estimada de:

a)   $200$ milisegundos.

b)   $149$ milisegundos.

c)   $74$ milisegundos.

def CalculoLatencia(latencia):
    return latencia*1.2;
print(f"Respuesta a) {CalculoLatencia(200):.2f}");
print(f"Respuesta b) {CalculoLatencia(149):.2f}");
print(f"Respuesta c) {CalculoLatencia(74):.2f}");

"""

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

"""

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