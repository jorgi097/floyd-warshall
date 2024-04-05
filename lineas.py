import os
import csv
  
# Arreglos vacios
nombres = []
idl = []
ide = []

cruces = []

matriz_M = []
matriz_T = []

idlCount = {}

#Funciones
def importar_matriz(nombre_archivo, matriz):
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            row = [int(cell) for cell in row] 
            matriz.append(row)
                 
def exportar_matriz(nombre_archivo, matriz):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        for row in matriz:
            writer.writerow(row)
       
def importar_lista(nombre_archivo, arreglo):
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            arreglo.extend(fila)

def exportar_lista(nombre):
    miarchivo = nombre + ".txt"

    with open(miarchivo, "w", encoding="utf-8") as archivo: # Abre / Crea el archivo en modo escritura
        archivo.write("i      |Linea  |Estacion |Nombre\n")
        archivo.write("-------|-------|---------|----------------------\n")
        for i in range(len(nombres)):
            linea_formateada = "{:<7}|{:<7}|{:<9}|{:<25}\n".format(i, idl[i], ide[i], nombres[i])
            archivo.write(linea_formateada)

def importar_cruces(nombre_archivo, lista):
    with open(nombre_archivo, 'r', newline="", encoding='utf-8') as archivo:
        dictreader = csv.DictReader(archivo)
        for row in dictreader:
            lista.append(row)

def limpiar_pantalla():
    if os.name == 'nt':  # nt = Windows
        os.system('cls')
    elif os.name != 'nt': # De lo contrario es Unix/Linux/Mac
        os.system('clear')

def floyd_warshall(n):    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz_M[i][k] + matriz_M[k][j] < matriz_M[i][j]:
                    matriz_M[i][j] = matriz_M[i][k] + matriz_M[k][j]
                    matriz_T[i][j] = k

def es_cruce(nombre):
    result = any(nombre in diccionario.values() for diccionario in cruces)
    return result

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

def busqueda_secuencial(arr, elemento, posicion, indices):   
    indices_arriba = []
    indices_abajo = []

    for i in range(posicion + 1, len(arr)): # Busca hacia arriba en el array usando busqueda secuencial
        if arr[i] == elemento:
            indices_arriba.append(i)
    
    for i in range(posicion -1, -1, -1): # Busca hacia abajo en el array usando busqueda secuencial
        if arr[i] == elemento:
            indices_abajo.append(i)
            
    indices = indices_abajo + indices + indices_arriba
    return indices

def buscar_linea():
    while True:
        limpiar_pantalla()
        response = input("Que estacion deseas buscar?: ").upper()
        print()

        binaria_result = busqueda_binaria(nombres, response)

        if binaria_result != -1: # Si la busqueda binaria arroja algo distinto a -1            
            indices = [binaria_result]
            
            indices = busqueda_secuencial(nombres, response, binaria_result, indices) # Guarda cuantas veces se encontro y los indices donde se encontro
            contador = len(indices)
            
            print(f"{response} se encuentra {contador} veces\n")

            for i in range(contador): # Imprime las lineas y numeros de estacion donde se encuentra la estacion
                print(f"LINEA: {idl[indices[i]]}, ID DE ESTACION: {ide[indices[i]]}")
            print()

            opc = input("Deseas realizar otra busqueda? Y/N: ").upper()
            if opc == "N":
                return
        else:
            print(f"La estacion {response} no fue encontrada\n")
            opc = input("Deseas repetir la busqueda? Y/N: ").upper()
            if opc == "N":
                return

def buscar_ruta():
    limpiar_pantalla()
    inicio_response = input("Ingrese la estacion de partida: ").upper()
    destino_response = input("Ingrese la estacion de destino: ").upper()
    # inicio_response = "SAN JUAN DE DIOS"
    # destino_response = "PLAZA PATRIA"
    
       
    inicio_result = busqueda_binaria(nombres, inicio_response)
    destino_result = busqueda_binaria(nombres, destino_response)
    
    if inicio_result != -1 & destino_result != -1:
        indices_inicio = [inicio_result]
        indices_inicio = busqueda_secuencial(nombres, inicio_response, inicio_result, indices_inicio)
        indices_destino = [destino_result]
        indices_destino = busqueda_secuencial(nombres, destino_response, destino_result, indices_destino)
        len_inicio = len(indices_inicio)
        len_destino = len(indices_destino)
        inicio_cruce = es_cruce(inicio_response)
        destino_cruce = es_cruce(destino_response)
        inicio_lineas = []
        inicio_estaciones = []
        destino_lineas = []
        destino_estaciones = []
        
        if inicio_response == destino_response:
            print("Ingreso la misma ruta dos veces. Intente de nuevo.")
        
        if not inicio_cruce:
            for i in range(len_inicio):
                linea = idl[indices_inicio[i]]
                estacion = ide[indices_inicio[i]]
                inicio_lineas.append(linea)
                inicio_estaciones.append(estacion)
        else:
            k
        
        
        if not destino_cruce:
            for i in range(len_destino):
                linea = idl[indices_destino[i]]
                estacion = ide[indices_destino[i]]
                destino_lineas.append(linea)
                destino_estaciones.append(estacion)
    


# Importar arreglos---------------------------------------------------------------------      
importar_lista("Nombres_Original.csv", nombres)
importar_lista("idL_Original.csv", idl)
importar_lista("idE_Original.csv", ide)
importar_matriz("M_Original.csv", matriz_M)
importar_matriz("T_Original.csv", matriz_T)
importar_cruces("Cruces.csv", cruces)


# Modificar arreglos----------------------------------------------------------------------
n = len(matriz_M) 
floyd_warshall(n)
# exportar_matriz('M_Final.csv', matriz_M)
# exportar_matriz('T_Final.csv', matriz_T)                       
nombres = [nombre.upper() for nombre in nombres]
cruces = [{clave: valor.upper() for clave, valor in diccionario.items()} for diccionario in cruces]
ide = [int(id) for id in ide]
idl = [int(id) for id in idl]
# exportar_lista("Original") # Antes de ordenar los arreglos
#bubble_sort(nombres)
#exportar_lista("Ordenado") # Despues de ordenar los arreglos
for i in range(1, 11):
    idlCount[i] = idl.count(i)

class Estacion:
    def __init__(self, nombre, numero_estacion, cruce=False):
        self.nombre = nombre
        self.ide = numero_estacion
        self.cruce = cruce

estaciones = []
lineas = []

#covierte los datos de las estaciones y nombres en objetos y los junta en la lista de estaciones
for nombre, numero in zip(nombres, ide):
    estacion = Estacion(nombre, numero)
    estaciones.append(estacion)

#Separa las estaciones en lineas
for num_linea, num_estaciones in idlCount.items():
    sublista_linea = []
    for i in range(0, num_estaciones):
        sublista_linea.append(estaciones[i])
    lineas.append(sublista_linea)

#-----------------------------------------------------------------------------------------

for i, linea in enumerate(lineas):
    print(f"-------------------Lineas{i}---------------------------")
    for estacion in linea:
        print("s")
input()





#--------------------------------INICIO DE PROGRAMA VISUAL--------------------------------
while True:    
    limpiar_pantalla()

    # Mostramos las opciones al usuario
    print("MENU\n")
    print("1) Buscar informacion de una estacion")
    print("2) Encontrar la ruta mas corta entre estaciones")
    print("3) Salir\n")

    opcion_menu = input("Ingrese la opción que desee: ")
        
    # Manejamos la opción ingresada por el usuario
    if opcion_menu == "1":
        buscar_linea()
    elif opcion_menu == "2":
        buscar_ruta()
    elif opcion_menu == "3":
        print("\nCerrando...")
        break
    else:
        print("Opción no válida.")