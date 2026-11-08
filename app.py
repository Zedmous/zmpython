"""
ZEDMOUS.DEV — Guía Maestra de Fundamentos de Python (PY-01 • UPP IUJO)
Archivo Principal: Demostración Interactiva de las 8 Unidades del Curso
Autor: Ing. Eduardo Nieves (Zedmous) — https://zedmous.netlify.app
"""

from collections import deque
import sys


def demo_unidad_1_tipos_y_casting() -> None:
    print("\n--- [UNIDAD 1] Ciclo E -> P -> S, Tipos de Datos y Casting ---")
    nombre: str = "Zedmous"
    edad: int = int("30")
    altura: float = float("1.75")
    complejo: complex = 3 + 4j
    edad_futura: int = edad + 5
    print(f"Usuario: {nombre} | Edad actual: {edad} | En 5 años: {edad_futura} | Altura: {altura}m")
    print(f"Complejo: {complejo} (Real: {complejo.real}, Imag: {complejo.imag})")
    print(f"Evaluación Truthy/Falsy: bool('')={bool('')}, bool(1)={bool(1)}, bool([])={bool([])}")


def demo_unidad_2_operadores_y_tablas_verdad() -> None:
    print("\n--- [UNIDAD 2] Operadores Aritméticos, Precedencia y Tablas de la Verdad ---")
    a, b = 10, 3
    print(f"Aritmética (a=10, b=3): a/b={a/b:.2f} | a//b={a//b} | a%b={a%b} | 2**3={2**3}")
    resultado_pemdas: float = (2 + 3) * 2 ** 2 / 4
    print(f"Precedencia PEMDAS ((2 + 3) * 2 ** 2 / 4): {resultado_pemdas}")
    print("Tabla de la Verdad (A, B -> not A | A and B | A or B):")
    for p in (True, False):
        for q in (True, False):
            print(f"  A={str(p):5} B={str(q):5} -> not A={str(not p):5} | and={str(p and q):5} | or={str(p or q):5}")


def demo_unidad_3_condicionales() -> None:
    print("\n--- [UNIDAD 3] Estructuras Condicionales (if/elif/else, Ternario) ---")
    temperatura: float = 28.5
    if temperatura > 35:
        clima = "Calor extremo"
    elif temperatura >= 26:
        clima = "Hace calor"
    elif temperatura >= 15:
        clima = "Clima agradable"
    else:
        clima = "Hace frío"
    nota: float = 16.0
    estado: str = "Aprobado" if nota >= 10 else "Aplazado"
    print(f"Temperatura {temperatura}°C -> {clima} | Nota {nota}/20 -> {estado}")


def demo_unidad_4_bucles() -> None:
    print("\n--- [UNIDAD 4] Estructuras Repetitivas (while y for) ---")
    multiplos_5 = [i for i in range(5, 51, 5)]
    numeros = [4, 7, 1, 3, 9]
    suma = 0
    for n in numeros:
        suma += n
    print(f"Múltiplos de 5 (5..50): {multiplos_5}")
    print(f"Suma acumulativa de {numeros}: {suma}")


def demo_unidad_5_funciones() -> None:
    print("\n--- [UNIDAD 5] Funciones Modulares, Lambda, *args, **kwargs y Recursión ---")
    cuadrado = lambda x: x ** 2

    def sumar_todo(*numeros: int) -> int:
        return sum(numeros)

    def factorial(n: int) -> int:
        return 1 if n <= 1 else n * factorial(n - 1)

    print(f"Lambda cuadrado(6): {cuadrado(6)} | sumar_todo(1,2,3,4,5): {sumar_todo(1, 2, 3, 4, 5)}")
    print(f"Recursión factorial(5): {factorial(5)} | divmod(10, 3): {divmod(10, 3)}")


def demo_unidad_6_estructuras_datos() -> None:
    print("\n--- [UNIDAD 6] Colecciones, Pilas (LIFO), Colas (FIFO) y List Comprehension ---")
    a, b = {1, 2, 3}, {3, 4, 5}
    print(f"Conjuntos A={a}, B={b} -> Unión: {a | b} | Intersección: {a & b} | Diferencia A-B: {a - b}")

    pila = ["plato 1", "plato 2"]
    pila.append("plato 3")
    ultimo_pila = pila.pop()

    cola = deque(["cliente 1", "cliente 2"])
    cola.append("cliente 3")
    primero_cola = cola.popleft()

    pares = [x for x in range(10) if x % 2 == 0]
    print(f"Pila LIFO extrajo: '{ultimo_pila}' | Cola FIFO atendió: '{primero_cola}'")
    print(f"List Comprehension (pares 0..9): {pares}")


def demo_unidad_7_poo() -> None:
    print("\n--- [UNIDAD 7] Programación Orientada a Objetos (POO) y Duck Typing ---")

    class CuentaBancaria:
        def __init__(self, titular: str, saldo: float) -> None:
            self.titular = titular
            self.__saldo = saldo

        def depositar(self, monto: float) -> None:
            if monto > 0:
                self.__saldo += monto

        def consultar_saldo(self) -> float:
            return self.__saldo

    class Perro:
        def hablar(self) -> str:
            return "¡Guau!"

    class Robot:
        def hablar(self) -> str:
            return "Bip bop"

    cuenta = CuentaBancaria("Zedmous", 1000.0)
    cuenta.depositar(250.0)
    sonidos = [entidad.hablar() for entidad in (Perro(), Robot())]
    print(f"Cuenta de {cuenta.titular} -> Saldo encapsulado: ${cuenta.consultar_saldo():.2f}")
    print(f"Polimorfismo / Duck Typing (Perro y Robot): {sonidos}")


def demo_unidad_8_excepciones_y_archivos() -> None:
    print("\n--- [UNIDAD 8] Manejo de Excepciones y Persistencia en Archivos ---")
    ruta = "files/demo_curso.txt"
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("ZEDMOUS.DEV — Fundamentos de Python\n")
        archivo.write("Persistencia segura con administrador de contexto with open().\n")

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = [linea.strip() for linea in archivo]
    print(f"Archivo '{ruta}' leído correctamente ({len(lineas)} líneas): {lineas[0]}")


def ejecutar_todas_las_demos() -> None:
    print("==========================================================================")
    print("  ZEDMOUS.DEV | Guía Maestra de Fundamentos de Python (8 Unidades)")
    print("==========================================================================")
    demo_unidad_1_tipos_y_casting()
    demo_unidad_2_operadores_y_tablas_verdad()
    demo_unidad_3_condicionales()
    demo_unidad_4_bucles()
    demo_unidad_5_funciones()
    demo_unidad_6_estructuras_datos()
    demo_unidad_7_poo()
    demo_unidad_8_excepciones_y_archivos()
    print("\n✅ Demostración integral de las 8 Unidades completada con éxito.")


if __name__ == "__main__":
    ejecutar_todas_las_demos()
