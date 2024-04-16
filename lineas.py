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
                    estacion.cruceindex = int(cruce['index'])

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
        def __init__(self, nombre, numero_estacion, cruce=False, cruceindex=None):
            self.nombre = nombre
            self.ide = numero_estacion
            self.cruce = cruce
            self.cruceindex = cruceindex
    
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

def buscar_linea(estacion, doprint = True):
    indices, contador = None,  None
    
    binaria_result = busqueda_binaria(nombres, estacion)

    if binaria_result != -1: # Si la busqueda binaria arroja algo distinto a -1            
        indices = [binaria_result]
        
        indices = busqueda_secuencial(nombres, estacion, binaria_result, indices) # Guarda cuantas veces se encontro y los indices donde se encontro
        contador = len(indices)
        
        if doprint:
            print(f"{estacion} se encuentra {contador} veces\n")

            for i in range(contador): # Imprime las lineas y numeros de estacion donde se encuentra la estacion
                print(f"LINEA: {idl[indices[i]]}, ID DE ESTACION: {ide[indices[i]]}")
            print()    
            
        return indices, contador   
        
    else:
        print(f"La estacion {estacion} no fue encontrada\n")
        return indices, contador

def abajo_inicio(linea_inicio, estacion_inicio, inicio_recorrido_abajo, cruce_inicio):
    salir_verificacion_abajo = None    
    for estacion in range(lineas[linea_inicio-1][estacion_inicio].ide, -1, -1):   
    
        inicio_recorrido_abajo.append(lineas[linea_inicio-1][estacion]) # Añade estaciones al recorrido hasta que se rompe el ciclo

        if lineas[linea_inicio-1][estacion].ide == 0:
            return inicio_recorrido_abajo, cruce_inicio, salir_verificacion_abajo
    
        if lineas[linea_inicio-1][estacion].cruce: # Guarda la primera estacion que es cruce
            cruce_inicio = lineas[linea_inicio-1][estacion] 
            return inicio_recorrido_abajo, cruce_inicio, salir_verificacion_abajo # Sale porque si es cruce no es mismo segmento
        
        if lineas[linea_inicio-1][estacion].nombre == destino_response: # Si en el recorrido se encuentra la estacion de destino imprime el recorrido 
            len_inicio_recorrido_abajo = len(inicio_recorrido_abajo)
            for paso in range(len_inicio_recorrido_abajo):
                if paso == 0:
                    print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {inicio_recorrido_abajo[paso].nombre}.")
                elif paso >0 and paso < len_inicio_recorrido_abajo-1:
                    print(f"Pasar por la estacion: {inicio_recorrido_abajo[paso].nombre}")
                else:
                    print(f"Bajar en la estacion: {inicio_recorrido_abajo[paso].nombre}")
                    salir_verificacion_abajo = True # Si se llego a este punto salir del loop anterior

        if salir_verificacion_abajo: #Si se encuentra la estacion de destino buscando hacia el inicio de la ruta
            return inicio_recorrido_abajo, cruce_inicio, salir_verificacion_abajo

def arriba_inicio(linea_inicio, estacion_inicio, inicio_recorrido_arriba, cruce_inicio, len_linea_inicio):
    salir_verificacion_arriba = None
    for estacion in range(lineas[linea_inicio-1][estacion_inicio].ide, len_linea_inicio): 
            
            inicio_recorrido_arriba.append(lineas[linea_inicio-1][estacion]) # Añade estaciones al recorrido hasta que se rompe el ciclo
            
            if lineas[linea_inicio-1][estacion].cruce:  # Guarda la primera estacion que es cruce
                cruce_inicio = lineas[linea_inicio-1][estacion] 
                return inicio_recorrido_arriba, cruce_inicio, salir_verificacion_arriba # Sale porque si es cruce no es mismo segmento
                
            if lineas[linea_inicio-1][estacion].nombre == destino_response: # Si en el recorrido se encuentra la estacion de destino imprime el recorrido 
                len_inicio_recorrido_arriba = len(inicio_recorrido_arriba)
                for paso in range(len_inicio_recorrido_arriba):
                    if paso == 0:
                        print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {inicio_recorrido_arriba[paso].nombre}.")
                    elif paso >0 and paso < len_inicio_recorrido_arriba-1:
                        print(f"Pasar por la estacion: {inicio_recorrido_arriba[paso].nombre}")
                    else:
                        print(f"Bajar en la estacion: {inicio_recorrido_arriba[paso].nombre}")
                        salir_verificacion_arriba = True # Si se llego a este punto salir del loop anterior
    
                if salir_verificacion_arriba: #Si se encuentra la estacion de destino buscando hacia el final de la ruta
                    return inicio_recorrido_arriba, cruce_inicio, salir_verificacion_arriba

def buscar_ruta(inicio, destino, inicio_result, destino_result):
    def print_mismalinea():
                    for estacion in range(len(recorrido_mismalinea_distintosegmento)): #Imprime recorrido
                        if estacion == 0:
                            print(f"Tomar la linea ({nombre_linea[linea_inicio]['inicio']} - {nombre_linea[linea_inicio]['final']}) en la estacion {recorrido_mismalinea_distintosegmento[estacion].nombre}.")
                        elif estacion >0 and estacion < len(recorrido_mismalinea_distintosegmento)-1:
                            print(f"Pasar por la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                        else:
                            print(f"Bajar en la estacion: {recorrido_mismalinea_distintosegmento[estacion].nombre}")
                            return
    
    limpiar_pantalla()
    
    #VARIABLES BUSCAR RUTA--------------------------------------------------------------------------------------
       
    cruce_inicio = None
    cruce_destino = None
    
    inicio_recorrido_arriba = []
    inicio_recorrido_abajo = []
    
    destino_recorrido_abajo = []
    destino_recorrido_arriba = []
    
    recorrido_mismalinea_distintosegmento = []
    
    index_cruce_actual_list = []
    

    #GUARDA EN QUE LINEAS ESTAN--------------------------------------------------------------------------------     
    
    # Guarda la linea y la estacion inicio
    linea_inicio = idl[inicio_result]
    estacion_inicio = ide[inicio_result]
            
    # Guarda la linea y la estacion destino
    linea_destino = idl[destino_result]
    estacion_destino = ide[destino_result]    
    
    # Guarda el tamaño de las lineas
    len_linea_inicio = len(lineas[linea_inicio-1])
    len_linea_destino = len(lineas[linea_destino-1])
    
    #------------------------------------------------------------------------------------------------------------------------------------MISMA LINEA, MISMO SEGMENTO       
    
    if linea_inicio == linea_destino: # Si estan en la misma linea
        
        #----------------------------------------------------------------Busca si el DESTINO esta desde la estacion INICIO hacia INICIO DE RUTA
   
        inicio_recorrido_abajo, cruce_inicio, salir_verificacion_abajo = abajo_inicio(linea_inicio, estacion_inicio, inicio_recorrido_abajo, cruce_inicio) 
        
        if salir_verificacion_abajo:
            return
        #-----------------------------------------------------------------Busca si el DESTINO esta desde la estacion INICIO hacia FINAL DE RUTA        
        
        inicio_recorrido_arriba, cruce_inicio, salir_verificacion_arriba = arriba_inicio(linea_inicio, estacion_inicio, inicio_recorrido_arriba, cruce_inicio, len_linea_inicio)
        if salir_verificacion_arriba:
            return
        
        #-----------------------------------------------------------------------------------------------------------------------------MISMA LINEA, SEGMENTO CONTIGUO    
    
        if cruce_inicio: # Si hay un cruce en el segmento incial de la ruta quiere decir que no estan en el mismo segmento
            
            #---------Busca si la primera estacion de cruce del destino es la misma que la de inicio, desde la estacion DESTINO hacia INICIO DE RUTA
            
            for estacion in range(lineas[linea_destino-1][estacion_destino].ide, -1, -1):      
                destino_recorrido_abajo.append(lineas[linea_destino-1][estacion]) # Añade estaciones al recorrido hasta que se rompe el ciclo
        
                if lineas[linea_destino-1][estacion].cruce: # Guarda la primera estacion que es cruce
                    cruce_destino = lineas[linea_destino-1][estacion]
                    break # Si hay un cruce se sale
            
            destino_recorrido_abajo.reverse() #Invierte el orden del recorrido del destino al cruce
            
            if inicio_recorrido_arriba: #Si el cruce de inicio fue hacia arriba: Invierte el orden del recorrido del destino al cruce--------------
                
                for estaciondestino in range(len(destino_recorrido_abajo)): # Elimina duplicados en el recorrido
                    for estacioninicio in range(len(inicio_recorrido_arriba)):
                        if destino_recorrido_abajo[estaciondestino].nombre == inicio_recorrido_arriba[estacioninicio].nombre:
                            del inicio_recorrido_arriba[estacioninicio]
                
                recorrido_mismalinea_distintosegmento = inicio_recorrido_arriba + destino_recorrido_abajo # Junta los recorridos
                
                print_mismalinea()
                
                       
            elif inicio_recorrido_abajo: # Si el cruce de inicio fue hacia abajo-------------------------------------------------------------------
    
                for estaciondestino in range(len(destino_recorrido_abajo)): #E limina duplicados en el recorrido
                        for estacioninicio in range(len(inicio_recorrido_abajo)):
                            if destino_recorrido_abajo[estaciondestino].nombre == inicio_recorrido_abajo[estacioninicio].nombre:
                                del inicio_recorrido_abajo[estacioninicio]
                
                recorrido_mismalinea_distintosegmento = inicio_recorrido_abajo + destino_recorrido_abajo # Junta los recorridos

                print_mismalinea()
    
            #--------Busca si la primera estacion de cruce es la misma que la del destino, desde la estacion DESTINO hacia FINAL DE RUTA-----------------

            if inicio_recorrido_arriba:  #Si el cruce de inicio fue hacia arriba-----------------------------------------------------------------
            
                for estacion in range(lineas[linea_destino-1][estacion_destino].ide, len_linea_destino): 
                    destino_recorrido_arriba.append(lineas[linea_destino-1][estacion]) # Añade estaciones al recorrido hasta que se rompe el ciclo
                    
                    if lineas[linea_destino-1][estacion].cruce: 
                        cruce_destino = lineas[linea_destino-1][estacion]  # Guarda la primera estacion que es cruce
                        break # Si hay un cruce se sale
                
                destino_recorrido_arriba.reverse() #Invierte el orden del recorrido del destino al cruce
            
            elif inicio_recorrido_abajo: # Si el cruce de inicio fue hacia abajo------------------------------------------------------------------
                
                for estaciondestino in range(len(destino_recorrido_arriba)): #Elimina duplicados en el recorrido
                    for estacioninicio in range(len(inicio_recorrido_arriba)):
                        if destino_recorrido_arriba[estaciondestino].nombre == inicio_recorrido_arriba[estacioninicio].nombre:
                            del inicio_recorrido_arriba[estacioninicio]
                
                recorrido_mismalinea_distintosegmento = inicio_recorrido_arriba + destino_recorrido_arriba # Junta los recorridos
                
                print_mismalinea()
                        
            elif inicio_recorrido_abajo: # Si el cruce de inicio fue hacia abajo-----------------------------------------------------------------
                
                for estaciondestino in range(len(destino_recorrido_arriba)): #Elimina duplicados en el recorrido
                        for estacioninicio in range(len(inicio_recorrido_abajo)):
                            if destino_recorrido_arriba[estaciondestino].nombre == inicio_recorrido_abajo[estacioninicio].nombre:
                                del inicio_recorrido_abajo[estacioninicio]
                
                recorrido_mismalinea_distintosegmento = inicio_recorrido_abajo + destino_recorrido_arriba # Junta los recorridos

                print_mismalinea()


        #------------------------------------------------------------------------------------------------------------------MISMA LINEA SEGMENTO NO CONTIGUO
                
        if cruce_destino.nombre != cruce_inicio.nombre: #Si estan en distinto segmento
            
            recorrido_entre_segmentos = []
            
            if inicio_recorrido_arriba: #-------------------------------------------------------Si el cruce de inicio fue hacia arriba
                destino_recorrido_abajo.reverse() #Invierte el orden del recorrido del destino al cruce                  

                #Busca el primer cruce en la Matriz T
                for column in range(len(matriz_T[cruce_inicio.cruceindex])): #Recorrer las columnas de la matriz T desde 0 hasta la columna del cruce de inicio
                    if column == cruce_destino.cruceindex: # Si la columna es la del cruce de destino
                        index_cruce_actual = matriz_T[cruce_inicio.cruceindex][column] # Guarda el primer cruce de la Matriz T
                        
                        if index_cruce_actual == 99: #Salir cuando no haya mas cruces
                            break
                        
                        index_cruce_actual_list.append(index_cruce_actual) #Añadir el primer cruce al arreglo 
                
                #Busca los demas cruces en la Matriz T
                while index_cruce_actual != 99: #Mientras no se encuentre con "infinito"
                    for column in range(len(matriz_T[cruce_inicio.cruceindex])): #Recorrer el arreglo de la linea donde estan los puntos inicio y final
                        if column == index_cruce_actual:
                            index_cruce_actual = matriz_T[cruce_inicio.cruceindex][column] # Guarda los puntos de la Matriz T
                            
                            if index_cruce_actual == 99:
                                break
                            
                            index_cruce_actual_list.append(index_cruce_actual) #Añadir los demas cruces al arreglo 
                            
                            index_cruce_actual_list.reverse() #Invertir el orden del recorrido para que se imprima correctamente
                
                temp = []
                
                for elemento in index_cruce_actual_list: #Para cada elemento dentro de la lista de cruces
                    for i, linea in enumerate(lineas):
                        for j, estacion in enumerate(linea):
                            if estacion.cruceindex == elemento: 
                                line = i+1
                                stationide = estacion.ide     
                                stationname = estacion.nombre
                                temp.append({"linea": line, "nombre": stationname, "ide": stationide})     
                                # print(f"linea {i+1} estacion {estacion.nombre}")
                                
                for elem in range(len(temp)):
                    print(temp[elem]['nombre'])  
    
                
                #----------------------------------------------------------------------------------------------------JUNTAR E IMPRIMIR FINAL                    
                    
                recorrido_mismalinea_distintosegmento = [inicio_recorrido_arriba[0].nombre] + index_cruce_actual_list + [destino_recorrido_abajo[0].nombre] # Junta los recorridos al primer cruce, entre cruces y del ultimo cruce a la estacion destino
                
                
                
                # for elem in elementos:
                #     print(f"Tomar la línea {}, estación {}")
                #     print(f"Pasarás por las estaciones {}")
                #     print(f"Bajar en la estación {}")
                #     print(f"Trasbordar a la línea {}")
                #     print(f"Pasarás por las estaciones {}")
                #     print(f"Bajar en la estación {}")
                #     print(f"Trasbordar a la línea {}")
                #     print(f"Pasarás por las estaciones {}")

    #-------------------------------------------------------------------------------------------------------------------DISTINTA LINEA                      
    if linea_inicio != linea_destino: # Si estan en distinta linea
        print("HI")          


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

# exportar_lista("Original") # Antes de ordenar los arreglos
# bubble_sort(nombres)
# exportar_lista("Ordenado") # Despues de ordenar los arreglos

for i in range(1, 11): # Crear diccionario con numero de linea y cuantas estaciones tiene
    idlCount[i] = idl.count(i)

agrupar_estaciones()

#--------------------------------INICIO DE PROGRAMA VISUAL---------------------------------
while True:    
    limpiar_pantalla()

    # Mostramos las opciones al usuario
    print("MENU\n")
    print("1) Buscar informacion de una estacion")
    print("2) Encontrar la ruta mas corta entre estaciones")
    print("3) Salir\n")

    opcion_menu = "2" #input("Ingrese la opción que desee: ")
        
    # Manejamos la opción ingresada por el usuario
    if opcion_menu == "1":
        while True:
            limpiar_pantalla()
            response = input("Que estacion deseas buscar?: ").upper().strip()
            print()
            agua, aguados = buscar_linea(response)
            opc = input("Deseas realizar otra busqueda? Y/N: ").upper().strip()
            if opc == "N":
                break
            
    elif opcion_menu == "2":
        limpiar_pantalla()
        contador_incio, contador_destino = 5, 5
        while contador_incio > 0:   
            inicio_response = "HUENTITAN"#input("Ingrese la estacion de partida: ").upper().strip()
            inicio_result = busqueda_binaria(nombres, inicio_response)
            if inicio_result != -1:
                break
            else:
                contador_incio -= 1
                print("Intente de nuevo, tiene {} intentos.".format(contador_incio))

        if contador_incio == 0:
            break
    
        while contador_destino > 0:     
            destino_response = "ESCULTURA"#input("Ingrese la estacion de destino: ").upper().strip()
            destino_result = busqueda_binaria(nombres, destino_response)
            if destino_result != -1:
                break
            else:
                contador_destino -= 1
                print("Intente de nuevo, tiene {} intentos.".format(contador_destino))

        if contador_destino == 0:
            break 
        buscar_ruta(inicio_response, destino_response, inicio_result, destino_result)
        break
    
    elif opcion_menu == "3":
        print("\nCerrando...")
        break
    else:
        print("Opción no válida.")