# ------ Taller y ejercicios en clase de practica aparte ------

print("----- Taller y ejercicios con While,condicionales y estucturas")

# Pide a usuario numeros enteros y sumalos hasta que ingrese un 0. Luego muestra el total

print("---- Ejercicio 1 ----")


total_suma = 0 # Inicializar la variable de suma


while True: # Mientras es verdadera
     numerooo = int(input("Ingresa un numero entero: ")) # Ingresar un numero
     if numerooo == 0: # Si es cero se rompe el bucle
          break
     else: # Y si no es cero empieza el total de la suma sumandole el numero
          total_suma += numerooo # Y se va sumando
          print("La suma total es",total_suma) # Y se imprime el total
print("Bucle finalizado")

# Crea un programa que pida una contraseña valida usando while hasta que escriba 'python123' correctamente 

print("---- Ejercicio 2 ----")

contraseña = "" # Contraseña
while contraseña!= "python123": # Mietnras la contraseña no es igual a python123
     contraseña = input("Ingresa una contraseña: ") # Se le pide la contraseña
print("Contraseña correcta,has ingresado") #Se imprime si es correcta,y si no,se intenta de nuevo

# Pide productos uno por uno y guardalos en una lista. Termina cuando el usuario escriba "fin". Luego muestra toda la lista

print("---- Ejercicio 3 ----")

productos = [] # Lista inicial

while True: # Mientras es verdadera
    pedidio=input("ingresa el producto: ") # Le pide un producto
    if pedidio=="fin": # Si pone fin se rompe el bucle 
        break
    productos.append(pedidio) # Se rompe el bucle y le añade los productos que ingreso antes de que se rompiera el bucle
print(f"en total pediste {productos}") # Imprime la lista


# Pide 10 números al usuario. Usa while para contarlos y guarda cuántos son pares y cuántos impares.

print("---- Ejercicio 4 ----")

# Inicializamos contadores
listapares = [] # Lista de pares
listaimpares = [] # Lista de impares
lista_numeros = [] # Lista de numeros totales

# Solicitamos los números al usuario usando un bucle while

while len(lista_numeros) < 10: # Mientras la lista de numeros completos no tenga mas de 10
        
        # Solicitamos un número al usuario
        entrada = int(input(f"Ingresa el número: "))

        # Añadimos el número a la lista
        lista_numeros.append(entrada)

        # Verificamos si el número es par o impar
        if entrada % 2 == 0: # Si el residuo de la división entre 2 es 0, es par 
            listapares.append(entrada)
        else: # Y si no se agrega a la de impares claramente
            listaimpares.append(entrada)



# Mostramos los resultados
print("\n--- Resultados ---")
print(f"Lista de números ingresados: {lista_numeros}")
print(f"Cantidad de números pares: {listapares}")
print(f"Cantidad de números impares: {listaimpares}")



# Pide al usuario ingresar notas entre 0 y 5 hasta que escriba "salir". Guarda las notas en una lista y muestra el promedio.

print("---- Ejercicio 5 -----")

notaslista = []  # Lista inicial

while True:  # Mientras es verdadera
    notas = int(input("Ingresa una nota:  ")) # Se pide una nota
    notaslista.append(notas)  # Se agrega a la lista
    
    pregunta = input("Escribe 'salir' si deseas salir, y si no, pon 'seguir': ") # Si escribe salir sale,si no no
    if pregunta.lower() == "salir":  # Si escribe salir,se rompe el bucle
        break

# Ahora sí, calculamos el promedio al final

promedio = sum(notaslista) / len(notaslista)
print(f"En total pusiste las siguientes notas: {notaslista}")
print(f"Promedio de las notas: {promedio}")



# Pide un número y genera su tabla del 1 al 10 con while.

print("---- Ejercicio 6 ----")

i = 1 # Contador
num = int(input("Ingresa un numero: ")) # Se pide un numero
while i <= 10: # Mientras es menor o igual a 10 
   print(f" {num} * {i} = {num*i}") # Se hace la operacion
   i += 1


# El programa tiene un número secreto (ej. 17). El usuario tiene que adivinarlo. Con cada intento, el programa dice si es mayor o menor.


print("---- Ejercicio 7 ----")



numerosec = 17 # Numero int

while True: # Mientras sea verdadera
   nume = int(input("Ingresa un numero el cual adivinaras el que tenemos en mente: ")) # Se pide un int
   if nume > 17: # Si es mayor a 17
      print("Mayor al que tenemos en mente,sigue intentando")
   elif nume < 17: # Si es menor a 17
      print("Menor al que tenemos en mente,sigue intentandolo")
   else: # Si lo adivina
      print("Lo lograste felicidades!")
      break
   

# Crea una tupla con frutas. Usa while para pedirle al usuario que adivine frutas hasta que acierte una que esté en la tupla

print("---- Ejercicio 8 ----")

# Tupla con frutas

frutas = ("manzana", "pera", "banano", "uva", "fresa") # Tupla de frutas


# Bucle while para pedir al usuario que adivine

while True: # Mientras es verdadero
    intento = input("Escribe el nombre de una fruta: ")  # Le pide el nombre de una fruta
    
    if intento.lower() in frutas:  
        # Si la fruta está en la tupla

        print(f"¡Correcto! '{intento}' está en la lista de frutas.")
        break  # Se detiene el bucle
    else:
        # Si la fruta no está en la tupla

        print("Esa fruta no está en la lista, intenta de nuevo.")


# Crea un diccionario con 5 palabras en español y su traducción al inglés. Usa while para que el usuario ingrese una palabra en español y muestre su traducción (si está).

print("---- Ejercicio 9 ----")

dicc = {
    "negro": "Black",
    "playa": "Beach",
    "sol": "Sun",
    "profesor": "Teacher",
    "alegria": "Happiness"
}

while True: # Mientras sea verdadero
    palabras = input("Ingresa una palabra en español que quieras saber en inglés: ").lower() # Pide la palabra en español
    if palabras in dicc: # Si esta en el diccionario se imprime su traduccion a ingles
        print(f"La palabra en español '{palabras}' en inglés es: {dicc[palabras]}")
        break
    else: # Si no,no esta y se vuelve a pedir hasta que ponga una palabra que este en el diccionario
        print("No está en nuestro diccionario, por favor pon otra, gracias!") 


# 10. Calculadora básica

# Haz un menú dentro de un while para que el usuario elija:

# 1. Sumar

# 2. Restar

# 3. Multiplicar

# 4. Dividir

# 5. Salir

# Luego realiza la operación con dos números ingresados.



print("---- Ejercicio 10 ----")

dicci = {
    "1": "Sumar",
    "2": "Restar",
    "3": "Multiplicar",
    "4": "Dividir",
    "5": "Salir de la calculadora"
}

while True:
    print(dicci)  # mostrar menú primero
    calculadora = input("Ingresa la opción de cálculo que deseas (ej: 1): ")
    
    if calculadora == "5":
        print("Saliste de la calculadora! :)")
        break

    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))

    if calculadora == "1": #Suma
        print(f"El resultado de la suma es: {num1 + num2}")
    elif calculadora == "2": #Resta
        print(f"El resultado de la resta es: {num1 - num2}")
    elif calculadora == "3": #Multiplicacion
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif calculadora == "4": #Division
        if num2 != 0: # Si no es cero se divide normal
            print(f"El resultado de la división es: {num1 / num2}")
        else: # Pero si es cero se imprime esto:
            print("Error: no se puede dividir entre 0")
    else: # Si puso 6,7 o general mayor a 5
        print("Opción inválida, intenta de nuevo.")




# Pide nombres y edades de personas y guárdalos en un diccionario. Detente cuando el usuario escriba "salir" como nombre. Luego muestra el diccionario completo.


print("---- Ejercicio 11 ----")

# Crear un diccionario vacío para guardar los datos

personas = {}

print("Escribe 'salir' como nombre para terminar.\n")

while True:
    nombre = input("Ingresa un nombre: ")
    
    if nombre.lower() == "salir":  # Condición para salir del bucle
        break
    
    edad = input("Ingresa la edad de la persona: ")
    
    # Guardamos el nombre como clave y la edad como valor en el diccionario
    personas[nombre] = edad

print("\nDiccionario de personas registrado:")
print(personas)

# Crea una lista de 5 colores. Usa un bucle while para que el usuario escriba colores hasta encontrar uno que esté en la lista

print("---- Ejercicio 12 ----")


lista = ["Rojo","Verde","Azul","Blanco","Aquamarina"] # Lista

while True: # Mientras sea verdadera
    coloresss = input("Ingresa un color el cual creas essta en la tupla secreta: ") # Se le pide un color
    if coloresss in lista: # Si esta se imprime:
        print("Si esta en la lista! Felicidades")
        break # Y se rompe el bucle
    else: # Y si no se imprime esto:
        print("No esta en la lista,vuelve a intentarlo!")



# Pide un número y muestra sus potencias desde la 1 hasta la 5 con while.

print("---- Ejercicio 13 ----")


nueeeee = int(input("Ingresa un numero: "))
i = 1 # Contador

while i<= 5: # Mientras el contador sea menor o igual a 5
    print(f"{nueeeee} ** {i} = {nueeeee ** i}") # Se hace la operacion
    i += 1 # Y se le va sumando y si no se rompe

# Pide 5 números con while y guarda en una lista sus cuadrados. Al final, muestra la lista.

print("---- Ejercicio 14 -----")
listacuad = [] # Lista de resultados
i = 0 # Contador
while True:
    nume1 = int(input("Ingresa un numero: "))  # Se pide un int
    cuadrado = nume1 **2 # Se hace la operacion
    print(f"{nume1} ** 2 = {cuadrado}")  # Se imprime
    listacuad.append(cuadrado) # Se añade a la lista
    i += 1 # Se va sumando el contador
    if i == 5: # Si llega hasta 5
        break # Se rompe el bucle


print(f"Lista de los cuadrados  = {listacuad}") # imprimir


# Crea un programa que te deje registrar estudiantes con su nota final (nombre y nota). Usa un diccionario. El usuario debe poder agregar varios hasta que escriba "fin".

print("---- Ejercicio 15 ----")


diccccc = {} # Diccionario

while True: # Mientras sea verdadera
    nom = input("Ingresa un nombre: ") # Se pide nombre
    nota = float(input("Ingresa una nota: ")) # Se pide nota
    diccccc[nom] = nota # Y se usa el nombre como clave y su edad como valor
    
    siono = input("Escribe 'Fin' si no deseas ingresar más estudiantes: ") # Se pregunta si desea ingresar mas estudiantes
    if siono == "Fin": # Si es 'Fin' se rompe y si no sigue el bucle
        break # Se rompe

print("\nDiccionario final:") 
print(diccccc) # Se imprime el diccionario final