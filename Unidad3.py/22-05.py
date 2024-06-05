lista1=["Pedro", "juan", "diego", 10, 20 , 30]
lista1.append("Chris")
for i in lista1:
    print(i)
#RECORRE LISTA
    
lista2=["Chris", "Bravo"]
lista2.append("Alonso")
lista2.append("Flores")
for i in lista2:
    print(i)

lista3=[22, 45, 55, 444, 66, 33]
lista3.insert(0, "Chris")
lista3.insert(3, "Bravo")
lista3.append(18)      #No es necesario poner indice 8, se remplaza por APPEND porque siempre va alfinal 
lista3.remove(22)
print(lista3)

# Insert: sirve para insertar algun valor a la lista, se introduce primero en que indice se desea insertar
# Remove: sacar elemento de la lista
# Sort: ordena de menor a menor

lista2=[22, 45, 55, 44, 66, 33]
lista2.sort()
print(lista2)



