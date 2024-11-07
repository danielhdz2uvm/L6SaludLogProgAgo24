import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros iniciales
N0 = int(input("Introduce la población inicial de bacterias: "))
r = float(input("Introduce la tasa de crecimiento (por ejemplo, 0.3 para 30% de crecimiento): "))
intervalos = int(input("Introduce el número de intervalos de tiempo: "))

# Generar tiempo y población para cada intervalo
tiempo = np.arange(0, intervalos + 1)
poblacion = N0 * np.exp(r * tiempo)

# Graficar el crecimiento bacteriano
plt.figure(figsize=(10, 6))
plt.plot(tiempo, poblacion, marker='o', linestyle='-', color='b', label="Crecimiento Bacteriano")
plt.title("Crecimiento Exponencial de Bacterias")
plt.xlabel("Tiempo (intervalos)")
plt.ylabel("Cantidad de Bacterias")
plt.legend()
plt.grid(True)
plt.show()

# Bucle para continuar o salir
for i in range(intervalos):
    continuar = input("Escribe 's' para salir o presiona Enter para continuar observando el crecimiento: ")
    if continuar.lower() == 's':
        print("Programa finalizado por el usuario.")
        break
    print(f"Tiempo: {tiempo[i]}, Población estimada: {poblacion[i]:.2f}")
