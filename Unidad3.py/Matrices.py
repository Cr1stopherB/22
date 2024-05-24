
#una matriz son listas dentro de una lista 
# matriz1=[
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print(matriz1[1][2])

#El primer corechete indica a la lista o matriz 1 que serian [4, 5, 6] y el otro corchete indica el indice que esta el elemento correspondiente

# for elemento in matriz1:
#     print(elemento)

# while True:
#     nombre=input("ingrese su nombre: ")
#     apellido=input("ingrese su apellido: ")
#     listaNombres=[]
#     listaApellido=[]
#     listaNombres.append(nombre)
#     listaApellido.append(apellido)
#     print(listaNombres)
#     print(listaApellido)


# Pedir al usuario que ingrese 3 nombres
nombres = []
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

# Encontrar el nombre con mayor cantidad de caracteres
nombre_mas_largo = nombres[0]
for nombre in nombres:
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre

# Mostrar el nombre con mayor cantidad de caracteres
print("El nombre con mayor cantidad de caracteres es:", nombre_mas_largo)
