import os
import csv

# Arreglos vacios
nombres = []
idl = []
ide = []
        
# Definicion de funciones        
def importar_csv(nombre_archivo, arreglo):
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            arreglo.extend(fila)

def exportar_txt(nombre): # Guarda archivos con la informacion de las lineas y estaciones
    miarchivo = nombre + ".txt"

    with open(miarchivo, "w", encoding="utf-8") as archivo: # Abre / Crea el archivo en modo escritura
        archivo.write("i      |Linea  |Estacion |Nombre\n")
        archivo.write("-------|-------|---------|----------------------\n")
        for i in range(len(nombres)):
            linea_formateada = "{:<7}|{:<7}|{:<9}|{:<25}\n".format(i, idl[i], ide[i], nombres[i])
            archivo.write(linea_formateada)

def limpiar_pantalla():
    if os.name == 'nt':  # nt = Windows
        os.system('cls')
    elif os.name != 'nt': # De lo contrario es Unix/Linux/Mac
        os.system('clear')

def bubble_sort(arr): 
    n = len(arr)

    for i in range(n):
        for j in range(n -i -1):
            if arr[j] > arr[j + 1]: # Verifica cuando cambiar el nombre de la estacion
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Cambia los nombres de la estacion
                ide[j], ide[j + 1] = ide[j + 1], ide[j] # Cambia los valores de estacion junto con el nombre
                idl[j], idl[j + 1] = idl[j + 1], idl[j] # Cambia los valores de linea junto con el nombre
    return arr

def busqueda_binaria(arr, elemento):
    izquierda, derecha = 0, len(arr)

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # //2 es una division que solo regresa enteros
        valor_medio = arr[medio]

        if valor_medio == elemento:
            return medio  # El elemento fue encontrado, devuelve su índice
        elif valor_medio < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # El elemento no está presente en la lista

def busqueda_secuencial(arr, elemento, posicion):
    global contador
    
    for i in range(posicion + 1, len(arr)): # Busca hacia arriba en el array usando busqueda secuencial
        if arr[i] == elemento:
            contador += 1
            indices.append(i)
    
    for i in range(posicion -1, -1, -1): # Busca hacia abajo en el array usando busqueda secuencial
        if arr[i] == elemento:
            contador += 1
            indices.append(i)


# Importar arreglos      
importar_csv("Nombres_Original.csv", nombres)
importar_csv("idL_Original.csv", idl)
importar_csv("idE_Original.csv", ide)

#Arreglo a mayuscula
nombres = [nombre.upper() for nombre in nombres]


exportar_txt("Original") # Antes de ordenar los arreglos

bubble_sort(nombres)

# exportar_txt("Ordenado") # Despues de ordenar los arreglos


#--------------------------------INICIO DE PROGRAMA VISUAL--------------------------------
while True:
    limpiar_pantalla()

    response = input("Que estacion deseas buscar? ").upper()
    print()

    binaria_result = busqueda_binaria(nombres, response)

    if binaria_result != -1: # Si la busqueda binaria arroja algo distinto a -1
        
        contador = 1
        indices = [binaria_result]
        
        busqueda_secuencial(nombres, response, binaria_result) # Ejecuta la busqueda secuencial y guarda cuantas veces se encontro en total el termino y los indices donde se encontro

        print(f"{response} se encuentra {contador} veces\n")

        for i in range(contador): # Imprime las lineas y numeros de estacion donde se encuentra la estacion
            print(f"LINEA: {idl[indices[i]]}, ID DE ESTACION: {ide[indices[i]]}")
        print()

        opc = input("Deseas realizar otra busqueda? Y/N: ").upper()
        if opc == "N":
            print("\nCerrando ...")
            break
    else:
        print(f"La estacion {response} no fue encontrada\n")
        opc = input("Deseas repetir la busqueda? Y/N: ").upper()
        if opc == "N":
            print("\nCerrando...")
            break