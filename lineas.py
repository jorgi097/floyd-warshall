import os
import csv
  
# Arreglos vacios-------------------------------------------------------------------------
nombres = []
idl = []
ide = []
cruces = []
estaciones = []
lineas = []
nombre_linea = {}

matriz_M = []
matriz_T = []

idlCount = {}

#Funciones--------------------------------------------------------------------------------
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

def es_cruce():
    for linea in lineas:
        for estacion in linea:
            for cruce in cruces:
                if estacion.nombre in cruce.values():
                    estacion.cruce = True

def inicio_final():
    for i, linea in enumerate(lineas):

        estacion_inicio = None
        estacion_final = None
        
        for estacion in linea:
            if estacion.ide == 0:
                estacion_inicio = estacion.nombre
                
            if estacion.ide == len(linea) - 1:
                estacion_final = estacion.nombre
        
        nombre_linea[i+1] = {'inicio': estacion_inicio, 'final': estacion_final}

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
    bubble_sort(nombres)
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

def agrupar_estaciones():
    class Estacion:
        def __init__(self, nombre, numero_estacion, cruce=False):
            self.nombre = nombre
            self.ide = numero_estacion
            self.cruce = cruce
    
    #covierte los datos de las estaciones y nombres en objetos y los junta en la lista de estaciones
    for nombre, numero in zip(nombres, ide):
        estacion = Estacion(nombre, numero)
        estaciones.append(estacion)
        
    #Separa las estaciones en lineas
    inicio, control = 0, 0
    for num_linea, num_estaciones in idlCount.items():
        final = num_estaciones + control
        sublista_linea = []
        lineas.append(estaciones[inicio:final])
        inicio = final
        control = final
    
    es_cruce()
    
    inicio_final()

def buscar_linea():
    while True:
        limpiar_pantalla()
        response = input("Que estacion deseas buscar?: ").upper().strip()
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

            opc = input("Deseas realizar otra busqueda? Y/N: ").upper().strip()
            if opc == "N":
                return
        else:
            print(f"La estacion {response} no fue encontrada\n")
            opc = input("Deseas repetir la busqueda? Y/N: ").upper().strip()
            if opc == "N":
                return

def buscar_ruta():
    limpiar_pantalla()
    #--------------------------------------------------------------------------------------------------------------VARIABLES BUSCAR RUTA
    inicio_response= "SANATORIO"
    destino_response= "TERRANOVA"
    inicio_cruce = None
    destino_cruce = None
    contador_incio, contador_destino = 5, 5
    len_linea_inicio = None
    len_linea_destino = None
    cruce_inicio = None
    cruce_destino = None
    inicio_recorrido_arriba = []
    inicio_recorrido_abajo = []
    destino_recorrido_abajo = []
    destino_recorrido_arriba = []
    salir_verificacion_arriba = None
    salir_verificacion_abajo = None
    recorrido_mismalinea_distintosegmento = []
    
    #------------------------------------------------------------------------------------------------------------INTRODUCE ESTACIONES
    while contador_incio > 0:    
        # inicio_response = input("Ingrese la estacion de partida: ").upper().strip()
        inicio_result = busqueda_binaria(nombres, inicio_response)
        if inicio_result != -1:
            break
        else:
            contador_incio -= 1
            print("Intente de nuevo, tiene {} intentos.".format(contador_incio))
            input()
    if contador_incio == 0:
        return
    
    while contador_destino > 0:     
        # destino_response = input("Ingrese la estacion de destino: ").upper().strip()
        destino_result = busqueda_binaria(nombres, destino_response)
        if destino_result != -1:
            break
        else:
            contador_destino -= 1
            print("Intente de nuevo, tiene {} intentos.".format(contador_destino))
            input()
    if contador_destino == 0:
        return        
    #------------------------------------------------------------------------------------------------------------GUARDA EN QUE LINEAS ESTAN     
    
    # Guarda la linea y la estacion inicio
    linea_inicio = idl[inicio_result]
    estacion_inicio = ide[inicio_result]
            
    # Guarda la linea y la estacion destino
    linea_destino = idl[destino_result]
    estacion_destino = ide[destino_result]    
    
    #------------------------------------------------------------------------------------------------------------MISMA LINEA MISMO SEGMENTO       
    
    if linea_inicio == linea_destino: # Si estan en la misma linea
        len_linea_inicio = len(lineas[linea_inicio-1])
#----------------------------------------------------------------------------------------------------------------De la estacion inicio hacia abajo
        for estacion in range(lineas[linea_inicio-1][estacion_inicio].ide, -1, -1):   
        
            inicio_recorrido_abajo.append(lineas[linea_inicio-1][estacion])
        
            if lineas[linea_inicio-1][estacion].cruce: 
                cruce_inicio = lineas[linea_inicio-1][estacion] # Guarda la estacion que es cruce
                break # Si hay un cruce se sale
            
            if lineas[linea_inicio-1][estacion].nombre == destino_response: # Si esta en el mismo segmento imprime las estaciones 
                len_inicio_recorrido_abajo = len(inicio_recorrido_abajo)
                for paso in range(len_inicio_recorrido_abajo):
                    if paso == 0:
                        print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {inicio_recorrido_abajo[paso].nombre}.")
                    elif paso >0 and paso < len_inicio_recorrido_abajo-1:
                        print(f"Pasar por la estacion: {inicio_recorrido_abajo[paso].nombre}")
                    else:
                        print(f"Bajar en la estacion: {inicio_recorrido_abajo[paso].nombre}")
                        salir_verificacion_abajo = True # Si se llego a este punto salir del loop anterior
    
            if salir_verificacion_abajo:
                break
        
#---------------------------------------------------------------------------------------------------------------De la estacion inicio hacia arriba        
        for estacion in range(lineas[linea_inicio-1][estacion_inicio].ide, len_linea_inicio): 
            
            inicio_recorrido_arriba.append(lineas[linea_inicio-1][estacion]) #Guarda el recorrido
            
            if lineas[linea_inicio-1][estacion].cruce: 
                cruce_inicio = lineas[linea_inicio-1][estacion] # Guarda la estacion que es cruce
                break # Si hay un cruce se sale
                
            if lineas[linea_inicio-1][estacion].nombre == destino_response: # Si esta en el mismo segmento imprime las estaciones
                len_inicio_recorrido_arriba = len(inicio_recorrido_arriba)
                for paso in range(len_inicio_recorrido_arriba):
                    if paso == 0:
                        print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {inicio_recorrido_abajo[paso].nombre}.")
                    elif paso >0 and paso < len_inicio_recorrido_arriba-1:
                        print(f"Pasar por la estacion: {inicio_recorrido_arriba[paso].nombre}")
                    else:
                        print(f"Bajar en la estacion: {inicio_recorrido_arriba[paso].nombre}")
                        salir_verificacion_arriba = True # Si se llego a este punto salir del loop anterior
    
            if salir_verificacion_arriba:
                break
         
#------------------------------------------------------------------------------------------------------------------------MISMA LINEA DISTINTO SEGMENTO    
    
        if cruce_inicio: # Si hay un cruce en el segmento incial de la ruta quiere decir que no estan en el mismo segmento
            len_linea_destino = len(lineas[linea_destino-1])
 
#---------------------------------------------------------------------------------------------------------------------De la estacion destino hacia abajo
            
            for estacion in range(lineas[linea_destino-1][estacion_destino].ide, -1, -1):      
                destino_recorrido_abajo.append(lineas[linea_destino-1][estacion])
        
                if lineas[linea_destino-1][estacion].cruce: 
                    cruce_destino = lineas[linea_destino-1][estacion] # Guarda la estacion que es cruce
                    break # Si hay un cruce se sale
        
            if cruce_destino.nombre == cruce_inicio.nombre:
                if inicio_recorrido_abajo and inicio_recorrido_arriba: #Si el cruce de inicio fue hacia arriba
                    destino_recorrido_abajo.reverse() #Invierte el orden del recorrido del destino al cruce
                    
                    for estaciondestino in range(len(destino_recorrido_abajo)): #Elimina duplicados en el recorrido
                        for estacioninicio in range(len(inicio_recorrido_arriba)):
                            if destino_recorrido_abajo[estaciondestino].nombre == inicio_recorrido_arriba[estacioninicio].nombre:
                                del inicio_recorrido_arriba[estacioninicio]
                    
                    recorrido_mismalinea_distintosegmento = inicio_recorrido_arriba + destino_recorrido_abajo # Junta los recorridos
                    
                    for estacion in range(len(recorrido_mismalinea_distintosegmento)): #Imprime recorrido
                        if estacion == 0:
                            print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {recorrido_mismalinea_distintosegmento[estacion].nombre}.")
                        elif estacion >0 and estacion < len(recorrido_mismalinea_distintosegmento)-1:
                            print(f"Pasar por la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        else:
                            print(f"Bajar en la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        
                        
                elif inicio_recorrido_abajo: # Si el cruce de inicio fue hacia abajo
                    destino_recorrido_abajo.reverse() #Invierte el orden del recorrido del destino al cruce

                    for estaciondestino in range(len(destino_recorrido_abajo)): #Elimina duplicados en el recorrido
                            for estacioninicio in range(len(inicio_recorrido_abajo)):
                                if destino_recorrido_abajo[estaciondestino].nombre == inicio_recorrido_abajo[estacioninicio].nombre:
                                    del inicio_recorrido_abajo[estacioninicio]
                    
                    recorrido_mismalinea_distintosegmento = inicio_recorrido_abajo + destino_recorrido_abajo # Junta los recorridos

                    for estacion in range(len(recorrido_mismalinea_distintosegmento)): #Imprime recorrido
                        if estacion == 0:
                            print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {recorrido_mismalinea_distintosegmento[estacion].nombre}.")
                        elif estacion >0 and estacion < len(recorrido_mismalinea_distintosegmento)-1:
                            print(f"Pasar por la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        else:
                            print(f"Bajar en la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
        
        
    
#---------------------------------------------------------------------------------------------------------------------De la estacion destino hacia arriba
       
            for estacion in range(lineas[linea_destino-1][estacion_destino].ide, len_linea_destino): 
                destino_recorrido_arriba.append(lineas[linea_destino-1][estacion]) #Guarda el recorrido
                
                if lineas[linea_destino-1][estacion].cruce: 
                    cruce_destino = lineas[linea_destino-1][estacion] # Guarda la estacion que es cruce
                    break # Si hay un cruce se sale
            
            if cruce_destino.nombre == cruce_inicio.nombre:
                if inicio_recorrido_abajo and inicio_recorrido_arriba: #Si el cruce de inicio fue hacia arriba
                    destino_recorrido_arriba.reverse() #Invierte el orden del recorrido del destino al cruce
                    
                    for estaciondestino in range(len(destino_recorrido_arriba)): #Elimina duplicados en el recorrido
                        for estacioninicio in range(len(inicio_recorrido_arriba)):
                            if destino_recorrido_arriba[estaciondestino].nombre == inicio_recorrido_arriba[estacioninicio].nombre:
                                del inicio_recorrido_arriba[estacioninicio]
                    
                    recorrido_mismalinea_distintosegmento = inicio_recorrido_arriba + destino_recorrido_arriba # Junta los recorridos
                    
                    for estacion in range(len(recorrido_mismalinea_distintosegmento)): #Imprime recorrido
                        if estacion == 0:
                            print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {recorrido_mismalinea_distintosegmento[estacion].nombre}.")
                        elif estacion >0 and estacion < len(recorrido_mismalinea_distintosegmento)-1:
                            print(f"Pasar por la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        else:
                            print(f"Bajar en la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        
                elif inicio_recorrido_abajo: # Si el cruce de inicio fue hacia abajo
                    destino_recorrido_arriba.reverse() #Invierte el orden del recorrido del destino al cruce

                    for estaciondestino in range(len(destino_recorrido_arriba)): #Elimina duplicados en el recorrido
                            for estacioninicio in range(len(inicio_recorrido_abajo)):
                                if destino_recorrido_arriba[estaciondestino].nombre == inicio_recorrido_abajo[estacioninicio].nombre:
                                    del inicio_recorrido_abajo[estacioninicio]
                    
                    recorrido_mismalinea_distintosegmento = inicio_recorrido_abajo + destino_recorrido_arriba # Junta los recorridos

                    for estacion in range(len(recorrido_mismalinea_distintosegmento)): #Imprime recorrido
                        if estacion == 0:
                            print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {recorrido_mismalinea_distintosegmento[estacion].nombre}.")
                        elif estacion >0 and estacion < len(recorrido_mismalinea_distintosegmento)-1:
                            print(f"Pasar por la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        else:
                            print(f"Bajar en la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")        



                       


#----------------------------------------------------------------------------------------------------------------------------AQUI VA FLOYD CON MATRIZ T
        
        


# Importar arreglos-----------------------------------------------------------------------    
importar_lista("Nombres_Original.csv", nombres)
importar_lista("idL_Original.csv", idl)
importar_lista("idE_Original.csv", ide)
importar_matriz("M_Original.csv", matriz_M)
importar_matriz("T_Original.csv", matriz_T)
importar_cruces("Cruces.csv", cruces)

#Limpiar pantalla-------------------------------------------------------------------------
limpiar_pantalla()

# Modificar arreglos----------------------------------------------------------------------
n = len(matriz_M) 
floyd_warshall(n)
# exportar_matriz('M_Final.csv', matriz_M)
# exportar_matriz('T_Final.csv', matriz_T)    
                   
nombres = [nombre.upper().strip() for nombre in nombres] # Todo a mayusculas
cruces = [{clave: valor.upper().strip() for clave, valor in diccionario.items()} for diccionario in cruces] # Todo a mayusculas

ide = [int(id) for id in ide] # Todo a entero
idl = [int(id) for id in idl] # Todo a entero

#exportar_lista("Original") # Antes de ordenar los arreglos
# bubble_sort(nombres)
# exportar_lista("Ordenado") # Despues de ordenar los arreglos

for i in range(1, 11): # Crear diccionariO con numero de linea y cuantas estaciones tiene
    idlCount[i] = idl.count(i)

agrupar_estaciones()

#------------------------------------------------------------------------------------------





#--------------------------------INICIO DE PROGRAMA VISUAL---------------------------------
while True:    
    limpiar_pantalla()

    # Mostramos las opciones al usuario
    print("MENU\n")
    print("1) Buscar informacion de una estacion")
    print("2) Encontrar la ruta mas corta entre estaciones")
    print("3) Salir\n")

    opcion_menu = "2"#input("Ingrese la opción que desee: ")
        
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