#TAREA DE PROG 3.1
stay=True
print("Bienvenido al Parking VIP")
while stay:
    print("1.- Ingresar el vehiculo")
    print("2.- Listar vehiculos")
    print("3.- Borrar vehiculo")
    print("4.- Conteo de vehiculos")
    print("5.- Salir")
    op=int(input())
    vehiculos=[]
    patente=[]
    piso1=[]
    piso2=[]
    piso3=[]
    piso4=[]
    match op:
        case 1:
            print("¿En que piso quiere ingresar el vehiculo?")
            print("1-. Piso 1")
            print("2.- Piso 2")
            print("3.- Piso 3")
            print("4.- Piso 4")
            piso_op=int(input())
            print("Por favor ingrese la marca de su vehiculo")
            v=input()
            vehiculos.append(v)
            print("Ingrese la patente de su vehiculo. Siguiendo este formato (AABB99 0 AA8899)")
            p=input()
            patente.append(p)
        case 2:
            print("Elija una opción")
            print("1.- Listar todos los vehiculos")
            print("2.- Listar un piso en especifico")
            op_li_piso=int(input())
            match op_li_piso:
                case 1:
                    print(piso1)
                case 2:
                    print(piso2)
                case 3:
                    print(piso3)
                case 4:
                    print(piso4) 
            print("3.- Volver")
            
        case 3:
            edad=int(input())
        case 4:
            print
        case 5:
            stay=False
        case _:
            print("Usted eligio una opcion que no esta definida")
        