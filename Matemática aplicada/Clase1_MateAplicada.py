#EA1 Funciones y sus aplicaciones (Dominio y recorrido de una función, imagen y pre imagen, función lineal)
#EA2 Arreglos y bucles (Suceción aritmética y geométrica, matriz, etc)

#4 talleres, se quedan las 3 mejores notas(CP, 10% c/u), Dos pruebas(P, 35% c/u), un examen (E, 40%)
#Asistencia = 70%
#Correo profesora: n.espana@profesor.duoc.cl


#Función para separar precios segun miles ejemplo: Tengo 10000 lo convertira en 10.000 
def formatear_precio_miles(precio):
    return f"{precio:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.')


# Se llama a la biblioteca numpy, para trabajar con arreglos de datos
import numpy as np
# Módulo de la biblioteca scipy que nos permitirá poder resolver ecuaciones no necesariamente lineales
# a través de la función fsolve
from scipy.optimize import fsolve

# Se declara el nombre de la función (C) con su respectiva variable independiente
def C(e):
# Se retorna el valor resultante luego de reemplazar el valor de "e" en la expresi ́on algebraica de la función
    return 40-10*e-0;
# Con un print(C(valor)). En pantalla, se muestrará el resultado de haber reemplazado "e"
print(C(100));

# Se le asigna a un arreglo t valores desde 0 hasta 50 con un espacio de distancia. Por lo tanto, este vector
# contiene solo el elemento 0
t = np.linspace(0, 50, 1);

# Se le asigna a un arreglo sol, la(s) solución(es) entre la expresión retornada en def y el arreglo t.
# Como este  ́ultimo arreglo contiene solo el elemento 0, entonces fsolve busca la solución entre la expresión 40-10*e-0 y 0, evaluando a traves del arreglo t valores 
# desde 0 hasta 50
sol = fsolve(C,t);
print(sol[0]);

"""
Ejercicio:
Una red transmite datos a 100 megabits por segundo. Crea una función utilizando *Python* que permita calcular la cantidad de datos transmitidos en una cierta cantidad de tiempo (en segundos). Luego utiliza la función y calcula cuántos datos se transmiten en:

45 segundos
1,5 minutos
1 hora
"""

def calculored(x):
    return 100*x

print(f"Resultado para 45 segundos = {calculored(45)}");
print(f"Resultado para 1,5 minutos = {calculored(90)}");
print(f"Resultado para 1 hora = {calculored(3600)}");