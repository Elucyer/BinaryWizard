#print("hola mundo")


#enteros 
#print(5+1)
#print(7-9)





mi_lista_a=[1,2,3,4,5,6,7,8,9,3,4,2]
mi_lista_b=["perro","hola","amor","muerte","miedo","carro","moto"]
enteros=[12121,244,2434,45464,46567]

#print(mi_lista_a[3])
#print(mi_lista_a[-7])



#print(len(mi_lista_a)) cantida de numero, palabras y lo que haya en la lista


#print(max(mi_lista_a))     numero maximo de la lista 
#print(min(mi_lista_a))     numero minimo de la lista 


#print(mi_lista_a[3]*mi_lista_a[4]) 


#mi_lista_a.extend(enteros)
#print(mi_lista_a) para que se me vea reflejado tegno que poner el comando y luego imprimir 

#mi_lista_a.append(34)
#print(mi_lista_a) agrega directamente lo que sea 

#print(mi_lista_a.index(2)) digo el valor y me trae la posicion

#mi_lista_a.pop(4)
#print(mi_lista_a) elimina la posicion 

#mi_lista_a.clear()
#print(mi_lista_a) elimina la lista 

#mi_lista_a.sort()
#print(mi_lista_a) ordenar de menor a mayor

#mi_lista_a.reverse()
#print(mi_lista_a)

#mi_lista_a1=list(set(mi_lista_a))
#print(mi_lista_a1) crea una nueva lista sin duplicados 

# 1)Se debe devolver la miltiplicacion de los numero del 1 al 9
#2)Se debe imprimir la lista en pantalla y solo debe aparecer la palabra "imprimir"
#3)Se debe imprimir en pantalla la combina de palabras "Hola", "Soy Janer" y tengo 24 anos, jugando con los valores de la lista 
#4)Se debe ordenar la lista de mayor a menor eliminando los valores string
#--5)Se debe elminar listar el total de valores que contiene la lista
#6)Se debe realizar al menos una operacion basica de cada operacion con los valores de la lista
#7)Se debe separar los elementos strign de los elementos enteros y mostrarlos en pantalla en dos listas diferentes
Mi_Lista_p = [4,3,2,1,6,5,7,5,"Hola","Soy Janer","Imprimir", 4,9,10,8,14,20]

a=Mi_Lista_p[0:8]
b=Mi_Lista_p[11:18]
a.extend(b)
a.sort()
a=list(set(a))
print(a[0]*a[0],a[0]*a[1],a[0]*a[2],a[0]*a[3],a[0]*a[4],a[0]*a[5],a[0]*a[6],a[0]*a[7],a[0]*a[8],)
#print(a)





