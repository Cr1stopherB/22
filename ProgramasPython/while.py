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



def cantMicros():
  cantMicros=0

  while cantMicros!=3:
    print("Ha pasado una micro?")
    resp=input()

    if resp=="si":
      cantMicros=cantMicros+1

