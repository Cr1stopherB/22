import random

nombres=["Chris", "Maximiliano", "Alberto"]
edades=[]
for i in range(len(nombres)):
    num=random.randint(1, 99)
    edades.append(num)

for e in range(len(nombres)):
    print("Su nombre es:", nombres[e], " y su edad es: ", str(edades[e]))