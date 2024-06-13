diccionario = {"nombre": "Cesar Huispe", 
               "fonos": [
                    988778882, 
                    988877776, 
                    877666333], 
               "activo": True}
print(diccionario)

for h in diccionario:
    valor=diccionario[h]
    print(h, ":", valor)

diccionario = {"nombre": "Cesar Huispe", 
               "fonos": [
                    988778882, 
                    988877776, 
                    877666333], 
               "activo": True}
vari=input("Que elemento desea que se imprima por pantalla? : ")
print(diccionario[vari])