import os # Funciones del sistema operativo

# ARREGLOS ORIGINALES
nombres = [
    "Mirador", "Huentitan", "Zoológico", "Independencia Norte", "San patricio", "Igualdad", "Monumental", "Monte Olivette", "Circunvalación", "Facultad de Medicina", "Juan Alvarez", "Alameda", "San juan de Dios", "Bicentenario", "Niños heroes", "Agua azul", "Cipres", "Heroe de Nacozari", "Lazaro Cardenas", "El dean", "Zona industrial", "López de legaspi", "Clemente Orozco", "Artes plasticas", "Escultura", "Fray Angelico",
     
    "Basilica", "Sanatorio", "Colegio victoria", "Plaza patria", "Terranova", "Colon", "Lienzo charro", "Mezquitan", "Panteon de belen", "Procuraduria", "Facultad de Medicina", "Obrero", "Tapalpita", "EL jaraz", "Plutarco Elias Calles", "Haciendas", "Oblatos", "Bethel", 
    
    "Periferico Norte", "Dermatologico", "Atemajac", "Division norte", "Avila Camacho", "Mezquitan", "Refugio", "Juarez", "Mexicaltzingo", "Whashington", "Santa filomena", "Unidad deportiva", "Urdaneta", "18 de marzo", "Isla raza", "Patria Sur", "España", "Tesoro", "Periferico Sur", 
    
    "Central sur", "Vallarta", "Jardines de la paz", "U. Panamericana", "Juan Palomar", "Seminario", "Camara de comercio", "Minerva", "Centro Magno", "Americas", "Chapultepec", "Paraninfo", "Juarez", "Plaza universidad", "San juan de Dios", "Belisario Dominguez", "Oblatos", "Cristobal de oñate", "San Andres", "San Jacinto", "La aurora", "Tetlan", 
    
    "San Isidro", "Cucea", "Parque", "Seattle", "Zoquipan", "Country", "Hospital General", "Plaza patria", "Colomos", "Plaza Pabellon", "San Javier", "3 De Marzo", "Jardines Universidad", "Ferrocarril", "Seminario", "La Gran Plaza", "San Ignacio", "Estampida", "Chapalita", "Abastos", "Mandarina", "Ruiseñor", "Unidad deportiva", "Plaxa Las Torres", "Cristo Rey", "El dean", "Nogalera", "Alamo", "Textiles", 
    
    "Tabachines", "Centro Cultural", "Zoquipan", "Patria Sur", "Division norte", "Lomas", "Plan De San Luis", "Colon", "Jose Maria Vigil", "Zarco", "Av. Mexico", "Ladron De Guevara", "Americas", "Lafayette", "Chapu", "Monumento", "Santa Eduwiges", "Dia", "Abastos", "Parque De Las Estrellas", "Expo", "Plaza Del Sol", 
    
    "Arco Del Triunfo", "Belenes", "Mercado Del Mar", "Zapopan Centro", "Plaza patria", "Circunvalacion", "Division norte", "Normal", "Santuario", "San juan de Dios", "Independencia Sur", "Plaza de la Bandera", "CUCEI", "Plaza Revolucion", "Rio Nilo", "Tlaquepaque", "Nodo Revolucion", "Central Camionera", 
    
    "Parque Metropolitano", "La estancia", "Guadalupe", "Univa", "Juan Diego", "Estampida", "Inglaterra", "Embajada", "Monumento", "Argentina", "Francia", "Madrid", "Whashington", "Carteros", "Agua azul", "Gonzales Gallo", "CUCEI", "Medrano", "San Rafael", "Poetas", 
    
    "Barranca De Huentitan", "Zoologico Guadalajara", "Independencia Norte", "Lomas Del Paraiso", "Rancho Nuevo", "La experiencia", "El Batan", "Periferico Norte", "La Cantera", "Tabachines", "Constitucion", "CCU", "San Isidro", "Belenes", "Tuzania", "Santa Margarita", "Acueducto", "5 De Mayo", "San Juan De Ocotan", "Vallarta", "Estadio Chivas", "Ciudad Judicial", "Ciudad Granja", "Parque Metropolitano", "Chapalita Inn", "El Colli", "Felipe Ruvalcaba", "Miramar", "Mariano Otero", "El Briseño", "Agricola", "Lopez Mateos", "Iteso", "Terminal De Autobuses", "Periferico Sur", "San Sebastianito", "8 De Julio", "Toluquilla", "Adolf Horn", "Artesanos", "Las Piñatas", "Carretera a Chapala", 
    
    "Circuito Metropolitano", "Escobedo", "Cortijo", "Lomas Del Sur", "Carretera a Tlajomulco", "Concepcion", "Adolf Horn", "Periferico", "Fray Angelico"
 ]
 
idl=[
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
     3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
     4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
     8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
     9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
     10, 10, 10, 10, 10, 10, 10, 10, 10
 ]
 
ide = [
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
     0, 1, 2, 3, 4, 5, 6, 7, 8
 ]


for i, nombre in enumerate(nombres): # Transforma el arreglo a mayusculas
    nombres[i] = nombre.upper()


#DEFINICION DE FUNCIONES
def clear_screen():
    if os.name == 'nt':  # nt = Windows
        os.system('cls')
    elif os.name != 'nt': # De lo contrario es Unix/Linux/Mac
        os.system('clear')


def guardar(nombre): # Guarda archivos con la informacion de las lineas y estaciones
    miarchivo = nombre + ".txt"

    with open(miarchivo, "w", encoding="utf-8") as archivo: # Abre / Crea el archivo en modo escritura
        archivo.write("i      |Linea  |Estacion |Nombre\n")
        archivo.write("-------|-------|---------|----------------------\n")
        for i in range(len(nombres)):
            linea_formateada = "{:<7}|{:<7}|{:<9}|{:<25}\n".format(i, idl[i], ide[i], nombres[i])
            archivo.write(linea_formateada)


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
        medio = (izquierda + derecha) // 2      # //2 es una division que solo regresa enteros
        valor_medio = arr[medio]

        if valor_medio == elemento:
            return medio  # El elemento fue encontrado, devuelve su índice
        elif valor_medio < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # El elemento no está presente en la lista


def busqueda_secuencial(arr, elemento, posicion):
    cont = 1 # Inicia en 1 porque si la funcion fue ejecutada es porque se encontro ya una vez con la busqueda binaria
    indices = [posicion] # El primer elemento del array es el indice que fue encontrado en la busqueda binaria

    for i in range(posicion -1, -1, -1): # Busca hacia arriba en el array usando busqueda secuencial
        if arr[i] == elemento:
            cont += 1
            indices.append(i)

    for i in range(posicion + 1, len(arr)): # Busca hacia abajo en el array usando busqueda secuencial
        if arr[i] == elemento:
            cont += 1
            indices.append(i)

    return cont, indices

# INICIO DEL PROGRAMA
guardar("Original") # Guarda un archivo como tabla de los arreglos originales

bubble_sort(nombres) # Ordena los arreglos

guardar("Ordenado") ## Guarda un archivo como tabla de los arreglos ordenados


#----------------------INICIO DE PROGRAMA VISUAL----------------------
clear_screen()

while True:
    clear_screen()

    response = input("QUE ESTACIÓN DESEA BUSCAR? ").upper()
    print()

    result = busqueda_binaria(nombres, response)


    if result != -1: # Si la busqueda binaria arroja el indice donde fue encontrado y no un -1
        
        contador, indices = busqueda_secuencial(nombres, response, result) # Ejecuta la busqueda secuencial y guarda cuantas veces se encontro en total el termino y los indices donde se encontro

        print(f"{response} se encuentra {contador} veces\n")

        for i in range(contador): # Imprime las lineas y numeros de estacion donde se encuentra la estacion
            print(f"Línea: {idl[indices[i]]}, Id de Estacion: {ide[indices[i]]}")
        print()

        opc = input("Deseas realizar otra busqueda? Y/N: ").lower()
        if opc == "n":
            print("CERRANDO PROGRAMA...")
            break
    else:
        print(f"La estacion {response} no fue encontrada\n")
        opc = input("Deseas repetir la busqueda? Y/N: ").lower()
        if opc == "n":
            print("CERRANDO PROGRAMA...")
            break