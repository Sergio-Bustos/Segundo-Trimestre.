# Ejercicios practicos de condicionales en clase


print("----- Ejercicio 1 ----")

vocal = input("Ingresa una vocal: ") # Para pedir una vocal

if vocal == "a": 
    print("A") # Convierte la letra a mayuscula
elif vocal == "A":
    print("a") # Convierte la letra a minuscula
elif vocal == "e":
    print("E") # Convierte la letra a mayuscula
elif vocal == "E":
    print("e") # Convierte la letra a minuscula
elif vocal == "i":
    print("I") # Convierte la letra a mayuscula
elif vocal == "I":
    print("i") # Convierte la letra a minuscula
elif vocal == "o":
    print("O") # Convierte la letra a mayuscula
elif vocal == "O":
    print("o") # Convierte la letra a minuscula
elif vocal == "u":
    print("U") # Convierte la letra a mayuscula
elif vocal == "U":
    print("u") # Convierte la letra a minuscula
else:
    print(f"La letra {vocal} no es una vocal.") # Por si la letra no es ni A,E,I,O,U ya que es de vocales



# Taller 1 de condicionales

# Ejercicio 1: Verifica si un numero es positivo,negativo o cero

print("---- Taller 1 de condicionales ----")

print("---- Ejercicio 1 ----")

numero = float(input("Ingresa un numero por favor: ")) # Para pedir el numero

if numero > 0: # Si es mayor a cero
    print("El numero es positivo")

elif numero == 0: # Si es igual a cero
    print("El numero es cero")

else: # Si no es ni cero ni positivo (osea negativo)
    print("El numero es negativo")


# Ejercicio 2: Calcula el mayor de dos numeros ingresados

print("---- Ejercicio 2 ----")

numeroo = float(input("Ingresa un numero por favor: ")) # Para pedir un primer numero
numeroo2 = float(input("Ingresa otro numero por favor: ")) # Para pedir un segundo numero

if numeroo > numeroo2: # Si el numero uno es mayor que el dos
    print(f"El numero {numeroo} (Numero uno) es mayor que {numeroo2} (Numero dos)")

elif numeroo2 > numeroo: # Si el numero dos es mayor que el uno
    print(f"El numero {numeroo2} (Numero dos) es mayor que {numeroo} (Numero uno)")

else: # Si son dos iguales
    print("Los numeros son iguales")

# Ejercicio 3: Determina si un numero es par o impar

print("---- Ejercicio 3 ----")

numero1 = int(input("Ingresa un numero entero por favor: ")) # Para pedir el numero

if numero1 % 2 == 0: # Si al dividir por 2 da 0
    print("El numero es par")

else: # Si al dividir por 2 de residuo queda algo (diferente a 0)

    print("El numero es impar")

# Ejercicio 4: Dado un numero verifica si esta entre 10  20

print("---- Ejercicio 4 ----")

nume = float(input("Ingresa un numero: "))

if nume >= 10 and nume <= 20: # Si esta entre 10 y 20
    print("El numero esta entre 10 y 20")

else: # Si no esta entre 10 y 20
    print("El numero no esta entre 10 y 20")


# Ejercicio 5: Dados tres numeros,encuentra el mayor usando condicionales

print("---- Ejercicio 5 ----")

num1 = float(input("Ingresa un numero: ")) # Para pedir un numero
num2 = float(input("Ingresa otro numero: ")) # Para pedir otro numero
num3 = float(input("Ingresa otro numero final: ")) # Para pedir un numero final

if num1 > num2 and num1 > num3: # Si el numero 1 es mayor que los demas
    print("El numero 1 es mayor que los otros dos")

elif num2 > num1 and num2 > num3: # Si el numero dos es mayor que los demas
    print("El numero dos es mayor que el numero uno y tres")

elif num3 > num1 and num3 > num2: # Si el numero tres es mayor que los demas
    print("El numero tres es mayor que los otros dos")

else: # Si ninguno es mayor que los otros dos y/o todos son iguales
    print("Todos son iguales")

# Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a 100$

print("---- Ejercicio 6 ----")

precio = float(input("Ingresa el precio actual de la papa: ")) # Para pedir el precio de la papa
if precio > 100: # Si el precio es mayor a 100$:
    des1 = precio * 0.10 # Hacerle un descuento del 10%
    descuentofinal = precio - des1 # Restar el descuento del 10% calculado al precio original
    print(f"El precio final con 10% de descuento por ser mayor a 100$ es de: {descuentofinal}$")

else: # Si no es mayor a 100$ no habra descuento
    print(f"El total es {precio}$,no habra descuento por no ser mayor a 100$")


# Ejercicio 7: Verifica si una persona puede votar (mayor o igual a 18 años)

print("---- Ejercicio 7 ----")

edadd = int(input("Hola!,ingresa tu edad por favor: ")) # Ingresa la edad
if edadd >= 18: # Si es mayor o igual a 18 (siendo mayor de edad)
    print("Puedes votar,vota bien!") 
else:
    print("No puedes votar,ten paciencia")

# Ejercicio 8: Dado el precio y tipo de cliente (VIP o Normal),aplica un descuento del 20% solo a VIP

print("---- Ejercicio 8 ----")


cliente = int(input("Bienvenido al sistema! Ingresa 1 si eres VIP,y 2 si eres cliente normal. El precio es 500$ normal: ")) # Si es VIP o normal
precioactual = 500
if cliente == 1: # Si es VIP por poner la opcion 1
    desc = precioactual * 0.20 # Para calcular el precio con 20% de descuento
    descuentofinal2 = precioactual - desc # Para restar el precio original con el precio de  20% de descuento calculado
    print(f"El precio por ser VIP,paso de ser {precioactual}$ a {descuentofinal2}$ por un 20% de descuento")

else: # Si no es VIP,osea normal pagando el precio normal
    print(f"No eres vip,pagaras {precioactual}$")

# Ejercicio 9: Determina si un numero es multiplo de 5 y de 3 al mismo tiempo

print("---- Ejercicio 9 ----")

num11 = int(input("Ingresa un numero entero por favor: ")) # Ingresar un int
if num11 % 5 == 0 and num11 % 3 == 0: # Si el numero al dividirlo por 5 y 3 no le queda residuo siendo su multiplo
    print("El numero si es multiplo de 5 y 3")

elif num11 % 5 == 0: # Si el numero al dividirlo por 5 no le queda residuo siendo su multiplo
    print("El numero solo es multiplo por 5")

elif num11 % 3 == 0: # Si el numero al dividirlo por 3 no le queda residuo siendo su multiplo
    print("El numero solo es multiplo por 3")

else: # Si el numero no es multiplo de ni de 5 ni de 3
    print("El numero no es multiplo ni de 5 y 3")


# Ejercicio 10: Dado un numero,verifica si es divisible entre dos numeros dados

print("---- Ejercicio 10 ----")


principal = int(input("Ingresa un numero entero: ")) # Pedir un numero int
primerdivisor = int(input("Ingresa un primer numero por el cual creas que es divisible: ")) # Para pedir un numero por el cual crea que es divisible por el numero principal dado
segundodivisor = int(input("Ingresa un segundo numero por el cual creas que es divisible: "))# Para pedir otro numero por el cual crea que es divisible por el numero principal dado

if principal % primerdivisor == 0 and principal % segundodivisor ==0: # Si al dividir el numero principal por el primer divisor y segundo divisor no hay residuo,siendo divisor de ambos
    print(f"El numero si es divisible por el {primerdivisor} y el {segundodivisor}")

elif principal % primerdivisor == 0: # Si al dividir el numero principal solo es divisible por el primer divisor
    print(f"El numero solo es divisible por el {primerdivisor}")

elif principal% segundodivisor ==0:  # Si al dividir el numero principal solo es divisible por el segundo divisor
    print(f"El numero solo es divisible por el {segundodivisor}")

else: # Si no es divisible ni por el primer divisor ni el segundo divisor
    print(f"El numero no es divisible por ningun numero")


# Ejercicio 11: Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”

print("---- Ejercicio 11 ----")

nu1 = int(input("Ingresa un primer numero entero: ")) # Ingresar un primer int
nu2 = int(input("Ingresa un segundo numero entero: ")) # Ingresar un segundo int
nu3 = int(input("Ingresa un tercer numero entero: ")) # Ingresar un tercer int
nu4 = int(input("Ingresa un cuarto numero entero: ")) # Ingresar un cuarto int
nu5 = int(input("Ingresa un quinto numero entero: ")) # Ingresar un quinto int

listaa = [nu1,nu2,nu3,nu4,nu5] # Agregar los numeros dados por el usuario en la lista
print(listaa)

if nu3 > 10: #  Si el numero 3 es mayor a 10
    print(f"El tercer numero ({nu3}) es mayor a 10")

elif nu3 == 10: # Si el numero 3 es igual 10
    print(f"El tercer numero ({nu3}) es igual a 10")

else: # Si el numero 3 es menor a 10
    print(f"El tercer numero ({nu3}) es menor a 10")

# Ejercicio 12: Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.

print("---- Ejercicio 12 ----")

listas = [3,5,7,9] # Lista de numeros

if 7 in listas: # Si el numero 7 esta en la lista
    print(f"El numero 7 si esta en la lista ({listas})")

else: # Si el numero 7 no esta en la lista
    print(f"El numero 7 no esta en la lista ({listas})")

# Ejercicio 13: Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.

print("---- Ejercicio 13 ----")

lista1 = [4,6,2,8] # Lista de numeros

suma = lista1[0] + lista1[1] # Sumar los dos primeros elementos de la lista

if suma > 10: # Si la suma de los primeros dos numeros de la lista es mayor una suma alta
    print(f"La suma de los dos primeros elementos de la lista ({lista1}) es considerada una suma alta")

else: # Si la suma de los primeros dos numeros es igual o menor a 10 siendo una suma baja
    print(f"La suma de los dos primeros elementos de la lista ({lista1}) se consideran una suma baja")


# Ejercicio 14: Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.

print("---- Ejercicio 14 ----")

lista22 = ["Ana","Luis","Pedro","Marta"] # Lista de nombres
print(lista22)
preg = input("Adivina! Cual es el elemento de la posicion -1 en la lista anterior, escribelo tal cual por favor: ") # Preguntar cual es el elemento -1 en la lista segun el usuario

if preg == "Marta": # Si el nombre dado "Marta" por el usuario si esta en el final de la lista
    print("Nombre correcto")
else: # Si puso el nombre que no esta en el final de la lista
    print("Nombre diferente")

# Ejercicio 15: Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.

print("---- Ejercicio 15 ----")

color1 = input("Ingresa un color por favor empezando en mayuscula: ") # Pedir un color
color2 = input("Ingresa otro color por favor empezando en mayuscula: ") # Pedir otro color
color3 = input("Ingresa un ultimo color por favor empezando en mayuscula: ") # Pedir otro color final

lista = [color1,color2,color3]

if lista[1] == "Azul": # Si el segundo color es Azul cambiarlo a Beige;
    lista[1] = "Beige" 
    print(f"Color azul cambiado en la lista quedando asi: {lista}")

else: # Si el segundo color en la lista no es el azul no se cambia
    print(f"La lista quedara intacta")

# Ejercicio 16: Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.

print("---- Ejercicio 16 ----") # Lista de numeros 

tupla = (5,8,12,20)
if tupla[0] < tupla[-1]: # Si el primer valor de la lista es menor que el ultimo valor de la lista se considera "Orden ascendente"
    print("La tupla cuenta con un orden ascendente")

else: # Si el primer valor de la lista es mayor que el ultimo valor de la lista se considera "Orden descendente"
    print("La tupla cuenta con un orden descendente")

# Ejercicio 17: Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”

print("---- Ejercicio 17 ----")

edades = (25,32,28) # Lista de numeros

if edades[1] > 30: # Si el segundo valor de la lista es mayor a 30
    print(f"La segunda edad en la tupla ({edades}) es una edad mayor a 30 años")

elif edades[1] == 30: # Si el segundo valor de la lista es igual a 30
    print(f"La segunda edad en la tupla ({edades}) es una edad igual a 30 años")

else: # Si el segundo valor valor de la lista es menor por no cumplir ser mayor,o igual
    print(f"La segunda edad en la tupla ({edades}) es una edad menor a 30 años")


# Ejercicio 18: Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.

print("---- Ejercicio 18 ----")

nu111 = int(input("Ingresa el numero 1: ")) # Ingresar un int
nu222 = int(input("Ingresa el numero 2: ")) # Ingresar un int
nu333 = int(input("Ingresa el numero 3: ")) # Ingresar un int

tuplae = (nu111,nu222,nu333) # Tupla de numeros
listafi = list(tuplae) # Pasar a lista la tupla

if listafi[1] == 2: # Si el segundo elemento de la lista es 2 cambiarlo a 10
    listafi[1] = 10
    print(f"La lista cambiada el numero 2 de la segunda posicion por 10 es: {listafi}")

    tuplafi = tuple(listafi) # Convertir a tupla final
    print(f"La tupla cambiada el numero 2 de la segunda posicion por el numero 10 es: {tuplafi}")

else: # No se hace nada ya que el segundo valor no es igual 2 
    print("No se cambiara nada y se dejara intacto")


# Ejercicio 19: Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.

print("---- Ejercicio 19 ----")

primernum = int(input("Ingresa el numero 4: ")) # Ingresar el int 4
segundonum = int(input("Ingresa el numero 9: ")) # Ingresar el int 9

tupla = (primernum,segundonum) # Agregar en una tupla los dos numeros int

if tupla[1] > 5: # Si el segundo valor de la tupla es mayor a 5
    print("Coordenada alta")

else: # Si el segundo valor de la tupla no es mayor a 5
    print("Coordenada baja")

# Ejercicio 20: Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.

print("---- Ejercicio 20 ----")

prinum = int(input("Ingresa el numero 3: ")) # Ingresar el int 3
segunnum = int(input("Ingresa el numero 4: ")) # Ingresar el int 4

tupla1 = (prinum,segunnum) # Agregar en una tupla el int 3 y 4
print(f"Hemos creado una tupla con el numero 3 y 4  ({tupla1}) ahora danos otros dos numeros a continuacion porfavor para crear otra: ")

tercernum = int(input("Ingresa el numero 3 nuevamente: ")) # Ingresar el int 3
cuartonum = int(input("Ingresa el numero 5 por favor: ")) # Ingresar el int 5

tupla2 = (tercernum,cuartonum) # Agregar en una tupla el int 3 y 5
print(f"Tu segunda tupla es: {tupla2},muchas gracias por tu tiempo,ahora vamos a lanzar un resultado si son iguales o diferentes: ")

if tupla1 == tupla2:  # Si la tupla 1 y tupla 2 son iguales
    print("Tuplas iguales")

else: # Si la tupla 1 y tupla 2 no son iguales
    print("Tuplas diferentes")

# Ejercicio 21: Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.

print("---- Ejercicio 21 ----")

dicc = {
    "nombre": input("Ingresa tu nombre: "), # Pedir nombre
    "edadd": int(input("Ingresa tu edad: ")) # Pedir int
}

if dicc["edadd"] >= 18: # Si la clave 'edad' es mayor o igual 18 siendo 'Adulto'
    print(f"Eres un adulto {dicc['nombre']}!")

else: # Si la clave 'edad' no es mayor o igual a 18 siendo 'Menor de edad'
    print(f"Eres un menor de edad {dicc['nombre']}!") 


# Ejercicio 22: Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.

print("---- Ejercicio 22 ----")

dii = {
    "nombreuser": input("Ingresa tu nombre por favor: "), # Pedir nombre
    "edad": int(input("Ingresa tu edad: ")) # Pedir edad
}

if dii["edad"] > 18: # Si la clave 'edad' es mayor a 18 cambiarla por 21:
    dii["edad"] = 21
    print(f"El diccionario con la edad cambiada por ser mayor 18 años es: {dii}")

else: # Si la clave 'edad' no es mayor a 18 no cambiarla y dejarla intacta
    print(f"El diccionario sin el valor cambiado e intacta es: {dii}")

# Ejercicio 23: Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario.

print("---- Ejercicio 23 ----")

diicc = {
    "Nombre": input("Ingresa tu nombre: ") # Pedir nombre
}

if "ciudad" not in diicc: # Si la clave 'ciudad' no esta en el diccionario agregarla con valor "Bogota"
    diicc["ciudad"] = "Bogota"
    print(f"El diccionario con la nueva clave 'ciudad' es: {diicc}")

else: # Si la clave 'ciudad' si esta en el diccionario y no agregar nada
    print(f"El diccionario tiene la clave 'ciudad' por lo tanto se dejara intacto asi: {diicc}")

# Ejercicio 24: Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.

print("---- Ejercicio 24 ----")

dicd = {
    "producto": input("Ingresa un producto: "), # Pedir un producto
    "precio": float(input("Ingresa el precio por favor: ")) # Pedir el precio
}

if "precio" in dicd: # Si la clave 'precio' esta en el diccionario y mostrarlo
    print(f"La clave 'precio' si esta en el diccionario,y se ve asi: {dicd['precio']}")

else: # Si la clave 'precio' no esta en el diccionario y mostrar 'No hay precio'
    print("No hay precio en el diccionario.")

# Ejercicio 25: Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”

print("---- Ejercicio 25 ----")


did = {
    "pan": 1200,  # Clave precio del pan
    "leche": 2000 # Clave precio de la leche
}

if "pan" in did: # Si 'pan' esta en el diccionario mostrar el precio
    print(f"El precio del pan es de: {did['pan']}")
else: # Si no esta en el diccionario mostrar 'Producto no disponible"
    print("Producto no disponible por que no contamos con el precio")