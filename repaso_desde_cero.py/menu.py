
stay=True
gasto=0
while stay:
 print("1.- Escriba su nombre: ")
 print("2.- Ingrese sus gatos")
 print("3.- Ingrese su edad")
 print("4.- Ver resultados")
 print("5.- Para salir")
 opcion=int(input())
 
 match opcion:
     case 1:
         nombre=input()
     case 2:
         gasto=gasto+int(input())
     case 3:
         edad=int(input())
     case 4:
         print(f"Hola {nombre} usted ha gastado {gasto} ")
     case 5:
         stay=False
     case _:
         print("Usted eligio una opcion que no esta definida")
        
    

#GUION BAJO ES PARA LA OPCION QUE NO ESTÁ DEFINIDA