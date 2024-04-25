text=""

def verifpassw():
 passw=""
 print("Ingrese su password")
 passw=input()
 while passw !="1234":
    print("Su password es incorrecta")
    passw=input()
    
 print("bienvenido usuario admin")

# verifpassw() 
 

def cena():
  cantComida=100

  while cantComida !=0:
    print("Desea comer?")
    cucharada=input()
    if cucharada=="si":
      cantComida=cantComida-25
      print("La cantidad de comida restante es:", cantComida)
    else:
      print("Usted ya dejó de comer")
      cantComida=0


# cena()


op=int(input("Seleccione una opcion: "))
match op:
  case 1:
    verifpassw()
    


