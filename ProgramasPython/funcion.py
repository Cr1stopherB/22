def multiPorDos():
    print("Ingrese un numero")
    num=int(input())
    print(num*2)

# multiPorDos()

def resta5():
    print("Ingrese un numero")
    num=int(input())
    print(num-5)

# resta5()

def suma():
    print("Ingrese el numero 1: ")
    num1=int(input())
    print("Ingrese el numero 2: ")
    num2=int(input())
    print(num1+num2)

# suma()


def suma(num1, num2):
    resultado=num1+num2
    return resultado

# print(suma(2,4))


def multi(num1, num2):
    resul=num1*num2
    return resul

# print("ingrese 3 numeros")
# num1=int(input())
# num2=int(input())
# num3=int(input())

# print(multi(num1,num2,num3))

def divi(num1,num2):
    resul=num1/num2
    return resul

print("Ingrese 2 numeros para que sean divididos")
num1=int(input())
num2=int(input())
print(divi(num1,num2))

print("Seleccione una opcion")
print("1.-Suma")
print("2- Resta")
print("3.- Division")
print("4.- Multiplicacion")
op=int(input())

match op:
    case 1:
        print("Ingrese 2 numeros para que sean divididos")
        num1=int(input())
        num2=int(input())
        print(suma(num1,num2))
    case 2:
    case 3:

    case 4:
        

#LLAMAR A LA FUNCION 

#SIN ARGUMENTO () <-
# <-CUANDO LA FUNCION NO TIEEN ARGUMENTO SE RABAJA DE ESTA FORMA
        
# estudiar }= if for while