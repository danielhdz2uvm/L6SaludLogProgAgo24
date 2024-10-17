import matplotlib.pyplot as plt

# 1. Función para guardar datos en un archivo de texto
def guardar_datos_en_archivo(nombre_alimento, datos, archivo='datos_calidad_alimentos.txt'):
    with open(archivo, 'a') as file:
        file.write(nombre_alimento + ',' + ','.join(map(str, datos)) + '\n')
    print(f"Datos del alimento '{nombre_alimento}' guardados en {archivo}.")

# 2. Función que cargue un formulario de 5 preguntas y el nombre del alimento
def cargar_formulario():
    nombre_alimento = input("Ingrese el nombre del alimento: ")
    
    print("Por favor, responda las siguientes preguntas sobre la calidad de los alimentos:")
    preguntas = [
        "1. ¿El alimento presenta un buen color? (1-5): ",
        "2. ¿El olor del alimento es adecuado? (1-5): ",
        "3. ¿El sabor es agradable? (1-5): ",
        "4. ¿La textura es apropiada? (1-5): ",
        "5. ¿El producto está en buenas condiciones generales? (1-5): "
    ]
    
    respuestas = []
    for pregunta in preguntas:
        while True:
            try:
                respuesta = int(input(pregunta))
                if 1 <= respuesta <= 5:
                    respuestas.append(respuesta)
                    break
                else:
                    print("Por favor, ingrese un valor entre 1 y 5.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
    
    return nombre_alimento, respuestas

# 3. Función que grafique los datos generados
def graficar_datos(datos_totales, nombres_alimentos):
    categorias = ["Color", "Olor", "Sabor", "Textura", "Condición General"]
    plt.figure(figsize=(10, 6))
    
    # Dibujar gráfico de barras para cada alimento
    for idx, (nombre, data) in enumerate(zip(nombres_alimentos, datos_totales)):
        plt.bar([x + idx*0.1 for x in range(5)], data, width=0.1, label=nombre)
    
    plt.xticks(range(5), categorias)
    plt.xlabel('Categorías')
    plt.ylabel('Evaluación (1-5)')
    plt.title('Diagnóstico de Calidad en Alimentos')
    plt.legend()
    plt.show()

# 4. Ciclo while para controlar la ejecución del programa
def ejecutar_programa():
    datos_totales = []
    nombres_alimentos = []
    
    while True:
        # Cargar formulario
        nombre_alimento, respuestas = cargar_formulario()
        
        # Guardar datos en el archivo
        guardar_datos_en_archivo(nombre_alimento, respuestas)
        
        # Agregar respuestas y nombre del alimento a las listas totales
        datos_totales.append(respuestas)
        nombres_alimentos.append(nombre_alimento)
        
        # Preguntar si se desea continuar o salir
        continuar = input("¿Desea ingresar otro diagnóstico? (s/n): ").lower()
        if continuar != 's':
            break
    
    # Graficar los datos generados
    if datos_totales:
        graficar_datos(datos_totales, nombres_alimentos)

# Ejecutar el programa principal
if __name__ == "__main__":
    ejecutar_programa()
