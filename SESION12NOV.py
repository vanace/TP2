#leer la dimensión de la matriz:
n = int(input("ingrese el número de filas: "))
m = int(input("ingrese el número de columnas: "))
#Creando una matriz de elementos cero de dimensión nxm:
Matriz = []
for i in range(n):
    Matriz.append([0]*m)

#print(Matriz)
#Leyendo los elementos de la matriz
for i in range(n):
    for j in range(m):
        print("ingrese el elemento (",i,",",j,")de la matriz")
        Matriz[i][j] = float(input())
print(Matriz)

#Sumando los elementos de la matriz leída:
S = 0
for i in range(n):
    for j in range(m):
        S = S + Matriz[i][j]
#print("la suma es: ",S)
#print("el promedio es: ",S/(n*m))

#Sumando los elementos de las filas y llenando una lista F:
F = []
for i in range(n):
    Suma = 0
    for j in range(m):
        Suma = Suma + Matriz[i][j]
    F.append(Suma)
print(F)

#Sumando los elementos de las columnas y llenando una lista C:
C = []
for j in range(m):
    Suma = 0
    for i in range(n):
        Suma = Suma + Matriz[i][j]
    C.append(Suma)
print(C)

#Hallando el menor de los totales columna:
menor =C[0]
for elemento in range(len(C)):
    if C[elemento] < menor:
        menor = C[i]
print("El menor es:",menor)


