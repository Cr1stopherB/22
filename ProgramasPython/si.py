# n = int(input("Introduce un número entero positivo: "))
# for i in range(1, n+1, 2):
#     print(i, end=", ")

# for i in range(2,11,2):
#     print("Imprimo esto "+str(i)+" veces")

amount = float(input("¿Cantidad a invertir? "))
interest = 22.5
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
