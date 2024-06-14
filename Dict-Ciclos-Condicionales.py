## Diccionario ## 

#1* Clave
#2* Valor

d = {'Nombre':'Janer','Edad':24,'CC':1007114896}

print(d.keys())
print(d.values())

a =d.get('Edad')
print(a)
print(list(str(a)[0]))

###########################################################

## Condicionales ##

# if
# elif
# else


if 5==5:
    print("Es verdadero_1")
    if 3-2 == 1:
        print("Verdadero_2")
        if 56 < 10:
            print("Verdadero_3")
        else:
            print("Falso_3")
    else:
        print("Falso_2")
else:
    print("Falso_1")

while True:
    numero = int(input("Introduzca un numero: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

while True:
    anno = int(input("Introduzca un numero: "))
    if anno % 4 == 0 and (anno % 100 != 0) or (anno %400 ==0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

#for 
#range

for loro in range(1,1000,15):
    if loro % 3 == 0:
        print(f"{loro} es divisible por 3")
    else:
        print(f"{loro} no es divisible por 3")

Mi_Lista = [1,2,3,4,5,6,7,8,9]

resul = 1
for yeti in Mi_Lista:
    resul *= yeti
    print(resul)


n = int(input("Introduzca un numero: "))
a, b = 0, 1

fibo = []

for i in range(n):
    fibo.append(a)
    a, b = b, a + b
print(fibo)

Peso = float(input("Ingrese su peso: "))
Altura = int(input("Ingrese si altura en metros: "))
IMC = (Peso//2)/((Altura/100)*(Altura/100))
print(IMC)
