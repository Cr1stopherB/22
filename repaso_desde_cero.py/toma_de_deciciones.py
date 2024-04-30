print("ingresa un numero:")
num1= int(input())
print("ingresa un 2do numero:")
num2= int(input())
print("ingresa un 3er numero:")
num3= int(input())

if num1>num2 and num1>num3:
    print("El "+ str(num1) + " es el mayor de todos")
elif num2>num3:
    print("El "+ str(num2) + " es el mayor de todos")
else:
    print("El "+ str(num3) + " es el mayor de todos")