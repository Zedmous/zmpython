"""
ZEDMOUS.DEV — Unidad 3: Los 5 Ejercicios Prácticos Resueltos de Condicionales
Curso: Fundamentos de Python (UPP IUJO • 20H)
"""


def ejercicio_1_mayoria_edad() -> None:
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")


def ejercicio_2_clasificar_nota() -> None:
    nota = float(input("Ingresa tu nota (0 a 20): "))
    if nota >= 10:
        print("Aprobado")
    else:
        print("Aplazado")


def ejercicio_3_temperatura() -> None:
    temperatura = float(input("Ingresa la temperatura en °C: "))
    if temperatura > 35:
        print("Calor extremo")
    elif temperatura >= 26:
        print("Hace calor")
    elif temperatura >= 15:
        print("Clima agradable")
    else:
        print("Hace frío")


def ejercicio_4_signo_numero() -> None:
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")


def ejercicio_5_calculadora() -> None:
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    if operacion == "+":
        print(f"Resultado: {a + b}")
    elif operacion == "-":
        print(f"Resultado: {a - b}")
    elif operacion == "*":
        print(f"Resultado: {a * b}")
    elif operacion == "/":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: división entre cero")
    else:
        print("Operación no válida")


if __name__ == "__main__":
    print("=== Laboratorio Unidad 3: 5 Ejercicios de Condicionales ===")
    ejercicio_5_calculadora()

