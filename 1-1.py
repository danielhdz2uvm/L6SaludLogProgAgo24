# Definir las bibliotecas a utilizar
import numpy as np

#Definir parámetros iniciales
Vx1=float(input("Escribe la velocidad inicial en m/s: "))
ax=float(input("Escribe la aceleración en m/s: "))
t=int(input("Escribe el tiempo en Segundos: "))

#Generar el resultado
vf=Vx1+(ax*t)

print("La velocidad en m/s es: ")
print(vf)
