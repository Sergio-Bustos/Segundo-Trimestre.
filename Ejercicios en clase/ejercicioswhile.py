# Ejercicios en clase: Bucle While

# Ejercicio bucle infinito

print("---- Ejercicio 1 ----")

numeroo = 1
while True: # Mientras sea verdadera
    print(numeroo) # Imprime el numero
    numeroo += 1 # Y le va sumando uno a uno lo que genera un bucle infinito

# Ejercicio de restarle al numero ingresado

print("---- Ejercicio 2 ----")

num = int(input("Ingresa un numero entero: ")) # Pedir numero entero
while num > 0: # Mientras el numero sea mayor a cero
    print(f"{num}") # Se imprime el numero 
    num-= 1 # Y se le resta de a 1 en un uno hasta que llegue a cero y el bucle se rompa

print("Termino el conteo") # Y si es menor a 0  o es 0 el ingresado o ya llego hasta a cero imprime esto

# Ejercicio tabla de multiplicar

print("---- Ejercicio 3 ----")

numero = int(input("Ingresa un numero de la tabla de multiplicar: "))
i = 1 # Inicializacion desde 1 (Para que multiplique desde 1 el numero que se le pide)
print(f"Inicia el contador del numero {numero}: ") # Mostrar que el codigo se esta iniciando

while i <= 10: # Mientras que i sea menor o igual 10 
    print(f"{numero} * {i} = {numero * i}") # Se multiplica numero por i
    i += 1 # Donde i va aumentando de uno en uno,haciendo numero * 1 luego numero * 2,y asi.


# Ejercicio Break

print("---- Ejercicio 4 ----")

nu = 1 # Numero
while True: # Mientras es verdadero
    print(nu) # Imprime el numero
    nu += 1 # Y le va sumando
    break # Pero se rompe justo cuando es 2,por lo tanto se finaliza el bucle y se queda en 1

# Ejercicio Break con condicional

print("---- Ejercicio 5 ----")

x = int(input("Ingresa un numero entero: ")) # Numero int
while True: # Mientras sea verdadera
    x -= 1 # Se le resta uno a x
    print(x) # Lo imprime
    if x == 0: # Hasta que llegue  
        break # Y termina
        
    print("Se termino el bucle") 

# Ejercicio while - else

print("---- Ejercicio 6 ----")

chance = 1 # Numero int
while chance <= 3: # Mientras el chance sea menor a 3
    txt = input("ESCRIBE SI: ") # Pedir SI O cualquier otro
    if txt == "SI": # Si es si
        print("Ok,lo conseguiste en el intento",chance) # Consiguio ganer y se imprime
        break # Y se rompe
    chance += 1 # Y si no se cumple,se va sumando el numero de chances que ha usado
else: # Y si ya es mayor a 3,agoto sus tres intentos
    print("Has agotado tus tres intentos")



    