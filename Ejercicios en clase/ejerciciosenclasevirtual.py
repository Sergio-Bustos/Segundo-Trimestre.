# Programa que pide un número hasta que sea múltiplo de 7

num = int(input("Ingresa un número: "))  


while num % 7 != 0:
    print("El número no es múltiplo de 7, intenta de nuevo.")
    num = int(input("Ingresa un número: "))
print(f"¡Correcto! {num} es múltiplo de 7.")


# Programa para registrar un contacto en un diccionario

contacto = {}  


nombre = input("Ingresa el nombre del contacto: ")
numero = input("Ingresa el número de teléfono: ")
email = input("Ingresa el correo electrónico: ")


contacto["nombre"] = nombre
contacto["numero"] = numero
contacto["email"] = email


print("\n--- Contacto Registrado ---")
print(contacto)


# Simulación de cajero automático

saldo = 1000  

print(f"Saldo inicial: ${saldo}\n")


while saldo > 0:
    retiro = int(input("Ingresa el monto a retirar: "))
    
    if retiro <= saldo:
        saldo -= retiro  
        print(f"Retiro exitoso. Saldo restante: ${saldo}\n")
    else:
        print(f"Error: No puedes retirar más de ${saldo}\n")

print("Saldo agotado. Cajero fuera de servicio.")


# Suma de numeros


sumatoria = 0


numero = int(input("Ingresa un número (0 para terminar): "))


while numero != 0:
    sumatoria += numero  
    numero = int(input("Ingresa un número (0 para terminar): "))
print("La suma total es:", sumatoria)



# Solicitar dos números y mostrar cuál es mayor o si son iguales.



num = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num > num2:
    print(f"El numero {num}  es > {num2}")
elif num < num2:
    print(f"El numero {num} es < {num2}")
else:
    print("Son iguales")

# Productos

total = 0

while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == "fin":
        break  
    
    precio = float(input(f"Ingrese el precio de {producto}: "))
    total += precio


print(f"El total de la compra es: ${total}")


# Ingreso de productos y precios con descuento


producto1 = input("Ingrese el nombre del primer producto: ")
precio1 = float(input(f"Ingrese el precio de {producto1}: "))

producto2 = input("Ingrese el nombre del segundo producto: ")
precio2 = float(input(f"Ingrese el precio de {producto2}: "))

producto3 = input("Ingrese el nombre del tercer producto: ")
precio3 = float(input(f"Ingrese el precio de {producto3}: "))


total = precio1 + precio2 + precio3


descuento = 0
if total > 100000:
    descuento = total * 0.10  

print("\n--- Detalle de la compra ---")
print(f"{producto1}: ${precio1}")
print(f"{producto2}: ${precio2}")
print(f"{producto3}: ${precio3}")


print(f"\nTotal sin descuento: ${total}")
print(f"Descuento aplicado: ${descuento}")
print(f"Total a pagar: ${total - descuento}")



# Pedir un número y sumar sus dígitos con while.



numero = int(input("Ingrese un número: "))


suma = 0


while numero > 0:
    digito = numero % 10   
    suma += digito          
    numero = numero // 10   

print(f"La suma de los dígitos es: {suma}")



# Solicitar palabras hasta que se repita una.



palabras = []

while True:
    palabra = input("Ingrese una palabra: ")
    
    if palabra in palabras:
        print(f"La palabra '{palabra}' ya se ingresó. ¡Fin del programa!")
        break  # Salimos del bucle si la palabra se repite
    
    palabras.append(palabra)  # Guardamos la palabra si no se repite


print("\nPalabras ingresadas:")
print(palabras)


# Pedir tres números y mostrar el mayor de ellos.


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 == num2 == num3:
    print("Son iguales todos")
else:
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:  
        mayor = num3

    print(f"El número mayor es: {mayor}")




# Crear un diccionario con información de un estudiante (nombre, edad, programa). Mostrarlo.

dicc = {}

nombre = input("Ingresa el nombre del estudiante: ")
edad = int(input("Ingresa la edad: "))
programa = input("Ingresa el programa vinculado: ")

dicc["nombre"] = nombre
dicc["edad"] = edad
dicc["programa"] = programa

print(dicc)


# Mostrar la tabla de multiplicar de un número ingresado


numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"\n--- Tabla de multiplicar del {numero} ---")
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1  



# Diccionario de 5 palabras en ingles y su traduccion a español,pedir e imprimirla



diccionario = {
    "house": "casa",
    "cat": "gato",
    "dog": "perro",
    "book": "libro",
    "water": "agua"
}

palabra = input("Ingrese una palabra en inglés: ").lower()


if palabra in diccionario:
    print(f"La traducción de '{palabra}' es '{diccionario[palabra]}'")
else:
    print(f"No se encontró la palabra '{palabra}' en el diccionario.")

# Suma de 10 numeros de una lista


lista = [1,2,3,4,5,6,7,8,9,10]
suma = sum(lista)
print("Lista: ",lista)
print("Suma de los numeros: ",suma)