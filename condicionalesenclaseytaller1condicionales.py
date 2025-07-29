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

    print("El nuero es impar")

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

elif num2 > num1 and num2 > num3:
    print("El numero dos es mayor que el numero uno y tres")
elif num3 > num1 and num3 > num2:
    print("El numero tres es mayor que los otros dos")
else:
    print("Todos son iguales")

# Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a 100$

print("---- Ejercicio 6 ----")

precio = float(input("Ingresa el precio actual de la papa: "))
if precio > 100:
    des1 = precio * 0.10
    descuentofinal = precio - des1
    print(f"El precio final con 10% de descuento por ser mayor a 100$ es de: {descuentofinal}$")
else:
    print(f"El total es {precio}$,no habra descuento por no ser mayor a 100$")


# Ejercicio 7: Verifica si una persona puede votar (mayor o igual a 18 años)

print("---- Ejercicio 7 ----")

edadd = int(input("Hola!,ingresa tu edad por favor: "))
if edadd >= 18:
    print("Puedes votar,vota bien!")
else:
    print("No puedes votar,ten paciencia")

# Ejercicio 8: Dado el precio y tipo de cliente (VIP o Normal),aplica un descuento del 20% solo a VIP

print("---- Ejercicio 8 ----")


cliente = int(input("Bienvenido al sistema! Ingresa 1 si eres VIP,y 2 si eres cliente normal. El precio es 500$ normal: "))
precioactual = 500
if cliente == 1:
    desc = precioactual * 0.20
    descuentofinal2 = precioactual - desc
    print(f"El precio por ser VIP,paso de ser {precioactual}$ a {descuentofinal2}$ por un 20% de descuento")
else:
    print(f"No eres vip,pagaras {precioactual}$")

# Ejercicio 9: Determina si un numero es multiplo de 5 y de 3 al mismo tiempo

print("---- Ejercicio 9 ----")

num11 = int(input("Ingresa un numero entero por favor: "))
if num11 % 5 == 0 and num11 % 3 == 0:
    print("El numero si es multiplo de 5 y 3")
elif num11 % 5 == 0:
    print("El numero solo es multiplo por 5")
elif num11 % 3 == 0:
    print("El numero solo es multiplo por 3")
else:
    print("El numero no es multiplo ni de 5 y 3")

# Ejercicio 10: Dado un numero,verifica si es divisible entre dos numeros dados

print("---- Ejercicio 10 ----")


principal = int(input("Ingresa un numero entero: "))
primerdivisor = int(input("Ingresa un primer numero por el cual creas que es divisible: "))
segundodivisor = int(input("Ingresa un segundo numero por el cual creas que es divisible: "))

if principal % primerdivisor == 0 and principal % segundodivisor ==0:
    print(f"El numero si es divisible por el {primerdivisor} y el {segundodivisor}")
elif principal % primerdivisor == 0:
    print(f"El numero solo es divisible por el {primerdivisor}")
elif principal% segundodivisor ==0: 
    print(f"El numero solo es divisible por el {segundodivisor}")
else:
    print(f"El numero no es divisible por ningun numero")


# Ejercicio 11: Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”

print("---- Ejercicio 11 ----")

nu1 = int(input("Ingresa un primer numero entero: "))
nu2 = int(input("Ingresa un segundo numero entero: "))
nu3 = int(input("Ingresa un tercer numero entero: "))
nu4 = int(input("Ingresa un cuarto numero entero: "))
nu5 = int(input("Ingresa un quinto numero entero: "))

listaa = [nu1,nu2,nu3,nu4,nu5]
print(listaa)

if nu3 > 10:
    print(f"El tercer numero ({nu3}) es mayor a 10")
elif nu3 == 10:
    print(f"El tercer numero ({nu3}) es igual a 10")
else:
    print(f"El tercer numero ({nu3}) es menor a 10")

# Ejercicio 12: Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.

print("---- Ejercicio 12 ----")

listas = [3,5,7,9]

if 7 in listas:
    print(f"El numero 7 si esta en la lista ({listas})")
else:
    print(f"El numero 7 no esta en la lista ({listas})")

# Ejercicio 13: Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.

print("---- Ejercicio 13 ----")

lista1 = [4,6,2,8]

suma = lista1[0] + lista1[1]

if suma > 10:
    print(f"La suma de los dos primeros elementos de la lista ({lista1}) es considerada una suma alta")
else:
    print(f"La suma de los dos primeros elmentos de la lista ({lista1}) se consideran una suma baja")


# Ejercicio 14: Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.

print("---- Ejercicio 14 ----")

lista22 = ["Ana","Luis","Pedro","Marta"]
print(lista22)
preg = input("Adivina! Cual es el elemento de la posicion -1 en la lista anterior, escribelo tal cual por favor: ")

if preg == "Marta":
    print("Nombre correcto")
else:
    print("Nombre diferente")

# Ejercicio 15: Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.

print("---- Ejercicio 15 ----")

color1 = input("Ingresa un color por favor: ")
color2 = input("Ingresa otro color por favor: ")
color3 = input("Ingresa un ultimo color por favor: ")

lista = [color1,color2,color3]

if lista[1] == "Azul":
    lista[1] = "Beige" 
    print(f"Color azul cambiado en la lista quedando asi: {lista}")
else:
    print(f"La lista quedara intacta")

# Ejercicio 16: Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.

print("---- Ejercicio 16 ----")

tupla = (5,8,12,20)
if tupla[0] < tupla[-1]:
    print("La tupla cuenta con un orden ascendente")
else:
    print("La tupla cuenta con un orden descendente")

# Ejercicio 17: Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”

print("---- Ejercicio 17 ----")

edades = (25,32,28)

if edades[1] > 30:
    print(f"La segunda edad en la tupla ({edades}) es una edad mayor a 30 años")
elif edades[1] == 30:
    print(f"La segunda edad en la tupla ({edades}) es una edad igual a 30 años")
else:
    print(f"La segunda edad en la tupla ({edades}) es una edad menor a 30 años")


# Ejercicio 18: Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.

nu111 = int(input("Ingresa el numero 1: "))
nu222 = int(input("Ingresa el numero 2: "))
nu333 = int(input("Ingresa el numero 3: "))

tuplae = (nu111,nu222,nu333)
listafi = list(tuplae)

if listafi[1] == 2:
    listafi[1] = 10
    print(f"La lista cambiada el numero 2 de la segunda posicion por 10 es: {listafi}")
    tuplafi = tuple(listafi)
    print(f"La tupla cambiada el numero 2 de la segunda posicion por el numero 10 es: {tuplafi}")
else:
    print("No se cambiara anda y se dejara intacto")