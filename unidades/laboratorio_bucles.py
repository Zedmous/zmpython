"""
ZEDMOUS.DEV — Unidad 4: Los 7 Ejercicios Prácticos Resueltos de Bucles (while y for)
Curso: Fundamentos de Python (UPP IUJO • 20H)
"""


def ejercicio_1_contador_while() -> None:
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1


def ejercicio_2_centinela_while() -> None:
    suma = 0
    numero = int(input("Ingresa un número (0 para salir): "))
    while numero != 0:
        suma += numero
        numero = int(input("Ingresa otro número (0 para salir): "))
    print("Suma total:", suma)


def ejercicio_3_contrasena_while() -> None:
    clave_correcta = "python123"
    clave = input("Ingresa la contraseña: ")
    while clave != clave_correcta:
        print("Contraseña incorrecta.")
        clave = input("Intenta de nuevo: ")
    print("Acceso concedido.")


def ejercicio_4_multiplos_for() -> None:
    for i in range(5, 51, 5):
        print(i)


def ejercicio_5_letras_palabra_for() -> None:
    palabra = input("Ingresa una palabra: ")
    for letra in palabra:
        print(letra)


def ejercicio_6_suma_lista_for() -> None:
    numeros = [4, 7, 1, 3, 9]
    suma = 0
    for n in numeros:
        suma += n
    print("Suma total:", suma)


def ejercicio_7_tabla_multiplicar_for() -> None:
    numero = int(input("¿Qué tabla deseas ver?: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    print("=== Laboratorio Unidad 4: 7 Ejercicios de Bucles ===")
    ejercicio_1_contador_while()
    ejercicio_6_suma_lista_for()

