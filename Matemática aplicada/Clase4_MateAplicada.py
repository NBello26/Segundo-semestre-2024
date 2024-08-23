#Función para separar precios segun miles ejemplo: Tengo 10000 lo convertira en 10.000 
def formatear_precio_miles(precio):
    return f"{precio:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.');

#np.log para logaritmos
#np.exp para exponentes

# Se llama a la biblioteca numpy, para trabajar con arreglos de datos
import numpy as np
# Módulo de la biblioteca scipy que nos permitirá poder resolver ecuaciones no necesariamente lineales
# a través de la función fsolve
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math
"""
El consumo de energía (en $kWh$) de un *Data Center* puede ser modelado por la función:

 E(t) = 50*log(t + 1) + 200

donde t corresponde al tiempo (en horas) desde el inicio del monitoreo.

1. Defina variable dependiente e independiente, indicando unidad de medida.
2. Determine el consumo de energía del Data Center después de 5 horas.
3. ¿Luego de cuántas horas el consumo será de 350 kWh?
4. Grafique, utilizando la biblioteca Matplotlib, la función E(t).
"""

"""
def consumoDeEnergia (t):
    return 50 * np.log10((t+1)) + 200
def tiempotranscurrido(t):
    return (50 * np.log10((t+1)) + 200) - 350

print(f"Respuesta 1: \nVariable dependiente: Consumo de energia en kWh (E(t))\nVariable independiente: Tiempo transcurrido en horas(t)");
print(f"\nRespuesta 2: el consumo de energía luego de 5 horas sera -> {formatear_precio_miles(consumoDeEnergia(5))} kWh");
e = np.linspace(0,250,1)
re2 = fsolve(tiempotranscurrido,e)
print(f"Respuesta 3 : luego de {re2[0]:.1f} horas el consumo sera de 350");
print("Respuesta 4:")
t = np.arange(0,24,1);
plt.plot(t,consumoDeEnergia(t));
plt.legend()
plt.grid()
plt.title("Consumo de energía a tarves del tiempo");
plt.xlabel("Tiempo transcurrido(horas)");
plt.ylabel("Consumo de energía(kWh)");
plt.show();
print("");
"""

"""
Ejercicio 10:

En gestión de proyectos, es crucial entender cómo se distribuye la carga de trabajo a lo largo del tiempo para planificar recursos, tiempo y esfuerzos de manera eficiente. 
Un fenómeno común es la disminución exponencial de la carga de trabajo, donde el esfuerzo requerido es mayor al inicio del proyecto y disminuye 
gradualmente a medida que se completan las tareas principales.

Esta disminución exponencial puede modelarse matemáticamente para predecir y gestionar el trabajo de manera efectiva.

Un estudio sobre gestión de proyectos sostiene que la carga de trabajo en un proyecto (en porcentaje) puede ser modelada por la función:

W(t) = 100e^-0.1t

donde $t$ corresponde al tiempo transcurrido (en semanas) desde el inicio del proyecto.

1. Defina variable dependiente e independiente, indicando unidad de medida.
2. Determine la carga de trabajo al inicio del proyecto.
3. ¿Cuál será la carga de trabajo luego de transcurridas $4$ semanas desde el inicio del proyecto?
4. Si el proyecto duró $12$ semanas, ¿es correcto afirmar que la carga de trabajo llegó al $20\%$?
5. ¿Cuántas semanas han pasado desde el inicio del proyecto para que la carga de trabajo sea de $55\%$?
6. Utilizando *Matplotlib*, grafique la función considerando un tiempo máximo de $12$ semanas.
"""

def cargadetrabajo(t):
    return 100 * np.exp(-0.1 * t)
def tiempotranscurridotrabajo(t):
    return (100 * np.exp(-0.1 * t)) - 55
print(f"Respuesta 1: \nVariable dependiente: Carga de trabajo en %(W(t))\nVariable independiente: Tiempo transcurrido en semanas(t)");
print(f"\nRespuesta 2: La carga del trabajo al inicio del proyecto sera -> {cargadetrabajo(0):.2f} %");
print(f"Respuesta 3 : La carga del trabajo al cabo de 4 semanas del proyecto sera -> {cargadetrabajo(4):.2f} %");
print(f"Respuesta 4: La carga del trabajo al cabo de 12 semanas del proyecto sera -> {cargadetrabajo(12):.2f} %");
e = np.linspace(0,100,1)
re2 = fsolve(tiempotranscurridotrabajo,e)
print(f"Respuesta 5 : Luego de {re2[0]:.1f} semanas la carga de trabajo sera de 55%");
print("Respuesta 6:")
t = np.arange(0,12,1);
plt.plot(t,cargadetrabajo(t));
plt.legend()
plt.grid()
plt.title("Carga de trabajo a tarves del tiempo");
plt.xlabel("Tiempo transcurrido(semanas)");
plt.ylabel("Carga de trabajo (%)");
plt.show();
print("");