import csv

matriz_M = []
matriz_T = []


def importar_matriz(nombre_archivo, matriz):
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            row = [int(cell) for cell in row] 
            matriz.append(row)
            
        
def guardar_matriz(nombre_archivo, matriz):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        for row in matriz:
            writer.writerow(row)


importar_matriz("M_Original.csv", matriz_M)
importar_matriz("T_Original.csv", matriz_T)
            
n = len(matriz_M)            
       
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matriz_M[i][k] + matriz_M[k][j] < matriz_M[i][j]:
                matriz_M[i][j] = matriz_M[i][k] + matriz_M[k][j]
                matriz_T[i][j] = k


guardar_matriz('M_Final.csv', matriz_M)
guardar_matriz('T_Final.csv', matriz_T)