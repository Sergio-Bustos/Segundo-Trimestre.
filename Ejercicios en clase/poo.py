# Ejercicios de POO individuales de manera autonoma en clases acronicas


# Ejemplo de ABSTRACCIÓN en Programación Orientada a Objetos (POO)
# Clase Auto con estados "apagado" y "encendido".
# Se muestran solo métodos simples (encender, conducir).


class Auto:
    def __init__(self):
        # Al crear un auto, inicia apagado
        self._estado = "apagado"
        print("El auto esta apagado por ahora")

    def encender(self):
        # Cambiamos el estado y mostramos mensaje
        self._estado = "encendido"
        print("El auto está encendido ahora")

    def conducir(self):
        # Verificamos si el auto está apagado o encendido
        if self._estado == "apagado":
            print("No puedes conducir, el auto está apagado")
        else:
            print("Conduciendo el auto")


# ------------------- PROGRAMA PRINCIPAL -------------------

mi_auto = Auto()          # Crear auto
mi_auto.conducir()        # Intentar conducir apagado
mi_auto.encender()        # Encender auto
mi_auto.conducir()        # Conducir encendido


