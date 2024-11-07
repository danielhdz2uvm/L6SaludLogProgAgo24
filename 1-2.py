# Definir las bibliotecas a utilizar
import numpy as np

#Definir parámetros iniciales
x1=int(input("Escribe el punto inicial: "))
Vx1=int(input("Escribe la velacidad inicial m/s: "))
t=int(input("Escribe el tiempo en segundos: "))
ax=int(input("Escribe la aceleración de x en segundos: "))


#Generar el resultado
xf=x1+(Vx1*t)+((1/2*ax)*(t**2))

print("Movimiento rectilinea uniforme: ")
print(xf)
