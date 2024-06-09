### Metodos de listas ###

Lista = [1,2,3,4,5,6,7,8]

#print(Lista.index(2))     # El metodo index cuando se le pasa un parametro me dice el valor de esa posicion
#Lista.append(9)           #Metodo de agregar un valor en la lista ya creada la posicion en la que se agrega es en el ultimo index de la misma
#print(Lista)      
#Lista.clear()             #Elimina todo los valores de la lista
#print(Lista)
#copia = Lista.copy()      #Copia la lista completa y la podemos almacenar en otra variable para realizar otras operaciones
#print(Lista, copia)    
#print(Lista.count(1))   
#Lista_2 = [0,9,2,4,5,6,7,12,45]
#Lista.extend(Lista_2)     #Metodo que combina dos lista       
#print(Lista)
#Lista.insert(0,2)          #Este metodo recibe dos parametros el primer parametro es la posicion del index y la segunda es el valor a insertar
#print(Lista)
#Lista.pop(3)                #Metodo para eliminar un solo valor de la lista, el valor a eliminar es el que le pasemos por paremetro si no le pasamos ninguno por defecto eliminara el ultimo
#print(Lista)
#Lista.remove(3)           #Metodo que elimina el valor que le pasemos como parametro, si hay mas de un mismo valor elimina el primero que necuentre por orden de indixe
#print(Lista)
#Lista.reverse()           # Metodo para reversar el orden de la lista 
#print(Lista)  
#Lista.sort()               # Metodo para ordenar la lista por valores del menos al mayor
#print(Lista)


### Operaciones entre listas ###

Mi_Lista = [4,3,2,1,6,5,7,5,"Hola","Soy Janer","Imprimir", 4,9,10,8,14,20]
#print(Mi_Lista)

"""
Se tiene una lista que combina diferentes tipos  de datos como se puede ver a continuacion se quiere realizar diferentes operaciones con la misma lista.
tales operaciones son:

1)Se debe devolver la miltiplicacion de los numero del 1 al 9
2)Se debe imprimir la lista en pantalla y solo debe aparecer la palabra "imprimir"
3)Se debe imprimir en pantalla la combina de palabras "Hola", "Soy Janer" y tengo 24 anos, jugando con los valores de la lista 
4)Se debe ordenar la lista de mayor a menor eliminando los valores string
--5)Se debe elminar listar el total de valores que contiene la lista
6)Se debe realizar al menos una operacion basica de cada operacion con los valores de la lista
7)Se debe separar los elementos strign de los elementos enteros y mostrarlos en pantalla en dos listas diferentes

"""

#1)

#Multiplicacion = Mi_Lista[:7]
#Multiplicacion.sort()
#Multiplicacion_1 = Mi_Lista[12:15]
#Multiplicacion_1.sort()
#multo_2 = Multiplicacion_1[:2]
#Multiplicacion.extend(multo_2)
#a = Multiplicacion[0]*Multiplicacion[1]*Multiplicacion[2]*Multiplicacion[3]*Multiplicacion[4]*Multiplicacion[5]*Multiplicacion[6]*Multiplicacion[7]*Multiplicacion[8]
#print(a)

#2)
#print(Mi_Lista[-7])

#3)
#print(Mi_Lista[-9], Mi_Lista[-8])

#4)
#Mi_Lista.pop(-7)
#Mi_Lista.pop(-7)
#Mi_Lista.pop(-7)
#Mi_Lista.sort()
#unicas = list(set(Mi_Lista))
#print(Mi_Lista)
#print(unicas)

#5)
#Cantidad_Valores = len(Mi_Lista)
#print(Cantidad_Valores)

#6)
#multi = Mi_Lista[1]*Mi_Lista[3]
#print(multi)
#sum = Mi_Lista[2]+Mi_Lista[4]
#print(sum)
#resta = Mi_Lista[2]-Mi_Lista[4]
#print(resta)
#divi = Mi_Lista[2]/Mi_Lista[4]
#print(divi)

#7)

#a = Mi_Lista[:8]
#a.sort()
#b = Mi_Lista[12:19]
#b.sort()
#a.extend(b)
#c = Mi_Lista[8:11]
#
#print(a)
#print(c)