import matplotlib.pyplot as plt
from statistics import mean, median, mode, variance, stdev

def calcular_estadisticas(datos):
    """Calcula y muestra estadísticas básicas."""
    media = mean(datos)
    mediana = median(datos)
    try:
        moda = mode(datos)
    except:
        moda = "No hay moda"
    rango = max(datos) - min(datos)
    varianza = variance(datos)
    desviacion_std = stdev(datos)
    
    print("\n--- Resultados Estadísticos ---")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Rango: {rango}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_std}")
    
    return media, mediana, moda, rango, varianza, desviacion_std

def generar_grafica(datos):
    """Genera un gráfico de los datos."""
    plt.figure(figsize=(8,6))
    plt.hist(datos, bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title("Histograma de los datos")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()

def leer_datos_manual():
    """Permite al usuario ingresar los datos manualmente."""
    try:
        datos = list(map(float, input("Ingrese los datos separados por comas: ").split(',')))
        return datos
    except ValueError:
        print("Error: Asegúrese de ingresar solo números.")
        return []

def main():
    while True:
        print("\n--- Análisis Estadístico ---")
        
        datos = leer_datos_manual()
        
        if datos:
            calcular_estadisticas(datos)
            generar_grafica(datos)
        
        continuar = input("¿Desea realizar otro análisis? (s/n): ").lower()
        if continuar != 's':
            print("Fin del programa.")
            break

# Ejecuta el programa principal
if __name__ == "__main__":
    main()