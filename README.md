# 🐍 Guía Maestra & Laboratorios de Fundamentos de Python (`zmpython`)

<p align="center">
  <img src="./assets/portada_python_zedmous.png" alt="Portada Oficial Fundamentos de Python — ZEDMOUS.DEV" width="520" />
</p>

<p align="center">
  <a href="https://zedmous.netlify.app/assets/docs/guia_fundamentos_python_zedmous.pdf"><img src="https://img.shields.io/badge/📄_Descargar_Guía_Maestra_PDF-ZEDMOUS.DEV-ef4444?style=for-the-badge" alt="Guía PDF" /></a>
  <a href="https://zedmous.netlify.app"><img src="https://img.shields.io/badge/Portafolio-zedmous.netlify.app-38bdf8?style=for-the-badge" alt="Portafolio" /></a>
  <img src="https://img.shields.io/badge/UPP_IUJO-20_Horas_Académicas-10b981?style=for-the-badge" alt="UPP IUJO" />
</p>

> **Autoría & Cátedra:** **Ing. Eduardo Nieves (`Zedmous`)** — Arquitecto de Software & Matemático  
> **Guía Oficial en PDF (9 Páginas):** [`docs/Guia_Maestra_Fundamentos_de_Python_Zedmous.pdf`](./docs/Guia_Maestra_Fundamentos_de_Python_Zedmous.pdf) | [Ver en línea en `zedmous.netlify.app`](https://zedmous.netlify.app/assets/docs/guia_fundamentos_python_zedmous.pdf)

---

## 🗂️ Estructura del Repositorio

| Archivo / Carpeta | Descripción |
| :--- | :--- |
| [`docs/Guia_Maestra_Fundamentos_de_Python_Zedmous.pdf`](./docs/Guia_Maestra_Fundamentos_de_Python_Zedmous.pdf) | **Guía Maestra Oficial en PDF (9 Páginas):** las 8 unidades completas, tablas técnicas, 12 ejercicios resueltos y POO. |
| [`app.py`](./app.py) | Script ejecutable que demuestra en consola las **8 Unidades del curso** (`python app.py`). |
| [`unidades/laboratorio_condicionales.py`](./unidades/laboratorio_condicionales.py) | Los **5 Ejercicios Prácticos Resueltos** de estructuras condicionales (`if`, `elif`, `else`). |
| [`unidades/laboratorio_bucles.py`](./unidades/laboratorio_bucles.py) | Los **7 Ejercicios Prácticos Resueltos** de estructuras repetitivas (`while` y `for`). |
| [`ds.py`](./ds.py) | **Bonus Ciencia de Datos:** Generación y graficación 3D multivariable con `NumPy` y `Matplotlib`. |
| [`ia.py`](./ia.py) | **Bonus Inteligencia Artificial:** Entrenamiento de una Regresión Lineal con Descenso del Gradiente desde cero en `NumPy`. |

---

## 📌 Índice de Contenidos por Unidades

1. [Unidad 1: Variables, los 11 Tipos de Datos, Casting y Ciclo `E → P → S`](#unidad-1-variables-los-11-tipos-de-datos-casting-y-ciclo-e--p--s)
2. [Unidad 2: Operadores Aritméticos, Precedencia PEMDAS y Tablas de la Verdad](#unidad-2-operadores-aritméticos-precedencia-pemdas-y-tablas-de-la-verdad)
3. [Unidad 3: Estructuras Condicionales (`if`, `elif`, `else`, `match-case`) + 5 Ejercicios](#unidad-3-estructuras-condicionales-if-elif-else-match-case--5-ejercicios)
4. [Unidad 4: Estructuras Repetitivas (`while` y `for`) + 7 Ejercicios](#unidad-4-estructuras-repetitivas-while-y-for--7-ejercicios)
5. [Unidad 5: Funciones Modulares, `lambda`, `*args`, `**kwargs`, Recursión y 43 Built-ins](#unidad-5-funciones-modulares-lambda-args-kwargs-recursión-y-43-built-ins)
6. [Unidad 6: Estructuras de Datos (`list`, `tuple`, `set`, `dict`), Pilas, Colas y Comprensión](#unidad-6-estructuras-de-datos-list-tuple-set-dict-pilas-colas-y-comprensión)
7. [Unidad 7: Programación Orientada a Objetos (POO), Encapsulamiento y Duck Typing](#unidad-7-programación-orientada-a-objetos-poo-encapsulamiento-y-duck-typing)
8. [Unidad 8: Entornos Virtuales (`venv`), Excepciones y Archivos (`TXT` y `CSV`)](#unidad-8-entornos-virtuales-venv-excepciones-y-archivos-txt-y-csv)

---

## Unidad 1: Variables, los 11 Tipos de Datos, Casting y Ciclo `E → P → S`

### 1.1 Declaración con Tipado Explícito (*Type Hints*)

```python
edad: int = 30                                          # Entero (int)
temperatura: float = 36.6                               # Real con decimales (float)
nombre: str = "Zedmous"                                 # Cadena de texto (str)
is_engineer: bool = True                                # Valor lógico booleano (bool)
vacio: None = None                                      # Ausencia de valor (NoneType)
numero_complejo: complex = 3 + 4j                       # Complejo (real: 3.0, imag: 4.0)
numeros: list[int] = [1, 2, 3, 4]                       # Lista ordenada y mutable
coordenadas: tuple[float, float] = (10.0, 20.0)         # Tupla ordenada e inmutable
frutas: set[str] = {"manzana", "naranja", "pera"}       # Conjunto sin duplicados
estudiante: dict[str, int] = {"edad": 25, "notas": 90}  # Diccionario clave: valor
datos_binarios: bytes = b"hola"                         # Secuencia inmutable de bytes
```

### 1.2 Funciones de Conversión (*Casting*)

| Función | Convierte a... | Ejemplo y Resultado |
| :--- | :--- | :--- |
| `int(x)` | Entero (trunca decimales) | `int("42"), int(9.8), int(True)` &rarr; `42, 9, 1` |
| `float(x)` | Número decimal | `float("3.14"), float(5)` &rarr; `3.14, 5.0` |
| `str(x)` | Cadena de texto | `str(123), str(True)` &rarr; `"123", "True"` |
| `bool(x)` | `False` para `0, 0.0, "", [], (), {}, None`; resto `True` | `bool(""), bool(1), bool([])` &rarr; `False, True, False` |
| `list(x)` / `tuple(x)` / `set(x)` | Lista, tupla o conjunto sin duplicados | `set([1, 2, 2, 3])` &rarr; `{1, 2, 3}` |

### 1.3 Ciclo Entrada (`input`) &rarr; Proceso &rarr; Salida (`print` con `f-strings`)

```python
# 1. ENTRADA (input siempre retorna str; convertimos con int/float)
nombre: str = input("Introduce tu nombre: ")
edad: int = int(input("Introduce tu edad: "))
altura: float = float(input("Introduce tu altura en metros: "))

# 2. PROCESO
edad_futura: int = edad + 5

# 3. SALIDA
print(f"Hola, {nombre}! Mides {altura}m y en 5 años tendrás {edad_futura} años.")
```

---

## Unidad 2: Operadores Aritméticos, Precedencia PEMDAS y Tablas de la Verdad

### 2.1 Operadores Aritméticos y de Asignación

```python
a: int = 10
b: int = 3

suma: int = a + b               # 13
resta: int = a - b              # 7
multiplicacion: int = a * b     # 30
division: float = a / b         # 3.3333... (siempre float)
division_entera: int = a // b   # 3 (descarta decimales)
residuo: int = a % b            # 1 (módulo / resto)
potencia: int = 2 ** 3          # 8

# Prioridad de Operadores (PEMDAS): 1) ()  2) **  3) *, /, //, %  4) +, -
resultado: float = (2 + 3) * 2 ** 2 / 4   # Salida: 5.0
```

### 2.2 Operadores Relacionales, Lógicos y Tablas de la Verdad

| `A` | `B` | `not A` ($\neg A$) | `A and B` ($A \land B$) | `A or B` ($A \lor B$) |
| :---: | :---: | :---: | :---: | :---: |
| `True` | `True` | `False` | `True` | `True` |
| `True` | `False` | `False` | `False` | `True` |
| `False` | `True` | `True` | `False` | `True` |
| `False` | `False` | `True` | `False` | `False` |

```python
a: bool = True
b: bool = False

print(a and b)  # Salida: False (exige que ambas sean True)
print(a or b)   # Salida: True  (basta que al menos una sea True)
print(not a)    # Salida: False (invierte el valor booleano)
```

---

## Unidad 3: Estructuras Condicionales (`if`, `elif`, `else`, `match-case`) + 5 Ejercicios

```python
# 1. Escalera condicional if - elif - else
temperatura: float = 28.0
if temperatura > 35:
    print("Calor extremo")
elif temperatura >= 26:
    print("Hace calor")
elif temperatura >= 15:
    print("Clima agradable")
else:
    print("Hace frío")

# 2. Operador Ternario en una línea
edad: int = 25
mensaje: str = "Mayor de edad" if edad >= 18 else "Menor de edad"

# 3. Pattern Matching Estructural (match - case, Python 3.10+)
operacion: str = "+"
match operacion:
    case "+":
        print("Suma")
    case "-":
        print("Resta")
    case _:
        print("Operación no válida")
```

> 💻 **Laboratorio Resuelto:** Revisa los 5 ejercicios completos en [`unidades/laboratorio_condicionales.py`](./unidades/laboratorio_condicionales.py).

---

## Unidad 4: Estructuras Repetitivas (`while` y `for`) + 7 Ejercicios

| Tipo de Repetición | ¿Se conoce el límite previo? | Estructura Asociada | Caso Real de Ingeniería |
| :--- | :--- | :--- | :--- |
| **Determinada** | Sí (tope fijo conocido) | `for` + `range()` | Médico con 10 citas diarias / Tope de 50 citas SAIME |
| **Indeterminada** | No (depende de condición/centinela) | `while` | Facturación en tienda / Validación de contraseña |

```python
# Bucle while con centinela (Repetición Indeterminada)
contador: int = 1
while contador <= 5:
    print(f"Iteración: {contador}")
    contador += 1

# Bucle for con range(inicio, fin, paso) y control con break / continue
for i in range(5, 51, 5):
    if i == 25:
        continue  # Salta el 25
    print(i)
```

> 💻 **Laboratorio Resuelto:** Revisa los 7 ejercicios completos en [`unidades/laboratorio_bucles.py`](./unidades/laboratorio_bucles.py).

---

## Unidad 5: Funciones Modulares, `lambda`, `*args`, `**kwargs`, Recursión y 43 Built-ins

```python
# 1. Función con Type Hints, Docstring y múltiples retornos (tupla)
def dividir_con_resto(a: int, b: int) -> tuple[int, int]:
    """Retorna el cociente entero y el residuo de dividir a entre b."""
    return a // b, a % b

cociente, residuo = dividir_con_resto(10, 3)

# 2. Función Lambda, *args (tupla variable) y **kwargs (diccionario variable)
cuadrado = lambda x: x ** 2
def sumar_todo(*numeros: int) -> int:
    return sum(numeros)

def mostrar_perfil(**datos: object) -> None:
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# 3. Función Recursiva (Factorial con caso base)
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)
```

---

## Unidad 6: Estructuras de Datos (`list`, `tuple`, `set`, `dict`), Pilas, Colas y Comprensión

```python
from collections import deque

# 1. Pila (LIFO: Last In, First Out) usando list
pila: list[str] = []
pila.append("plato 1")
pila.append("plato 2")
ultimo = pila.pop()           # Extrae "plato 2"

# 2. Cola (FIFO: First In, First Out) usando collections.deque en O(1)
cola = deque(["cliente 1", "cliente 2"])
primero = cola.popleft()      # Atiende a "cliente 1"

# 3. Comprensión de Listas (List Comprehension)
cuadrados: list[int] = [x ** 2 for x in range(5)]                  # [0, 1, 4, 9, 16]
pares: list[int] = [x for x in range(10) if x % 2 == 0]            # [0, 2, 4, 6, 8]
```

---

## Unidad 7: Programación Orientada a Objetos (POO), Encapsulamiento y Duck Typing

| Nivel de Visibilidad | Sintaxis en Python | Equivalente en Java | Comportamiento |
| :--- | :--- | :--- | :--- |
| **Público** | `self.nombre` | `public` | Accesible libremente desde dentro y fuera de la clase. |
| **Protegido** | `self._edad` | `protected` | Convención para uso interno de la clase y sus subclases. |
| **Privado** | `self.__saldo` | `private` | Activa *Name Mangling* (`_Clase__saldo`) encapsulando el atributo. |

```python
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> None:
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, asignatura: str) -> None:
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def ensenar(self) -> None:
        print(f"Impartiendo la cátedra de {self.asignatura}.")

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto: float) -> None:
        if monto > 0:
            self.__saldo += monto

    def consultar_saldo(self) -> None:
        print(f"Saldo actual de {self.__titular}: ${self.__saldo:.2f}")

# Polimorfismo y Duck Typing
class Dragon:
    def hacer_sonido(self) -> None:
        print("¡Graaararrarrara!")

class Gato:
    def hacer_sonido(self) -> None:
        print("¡Miau!")

for criatura in [Dragon(), Gato()]:
    criatura.hacer_sonido()
```

---

## Unidad 8: Entornos Virtuales (`venv`), Excepciones y Archivos (`TXT` y `CSV`)

### 8.1 Crear y Activar un Entorno Virtual (`venv`)

```bash
# 1. Crear el entorno virtual aislado
python -m venv .venv

# 2. Activar en Windows vs Linux/macOS
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

# 3. Instalar dependencias del proyecto
pip install -r requirements.txt
```

### 8.2 Manejo de Excepciones (`try / except / else / finally`)

```python
try:
    divisor: int = int(input("Introduce un divisor entero: "))
    resultado: float = 100 / divisor
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Entrada inválida. Debes ingresar un número entero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operación finalizada.")
```

### 8.3 Lectura y Escritura de Archivos `TXT` y `CSV` con `with open()`

```python
import csv

# Escribir y leer archivo TXT
with open("files/notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("¡Hola, mundo!\nSegunda línea de texto.\n")

with open("files/notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# Escribir y leer archivo CSV
with open("files/datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Nombre", "Edad", "Ciudad"])
    escritor.writerow(["Zedmous", 30, "Barquisimeto"])

with open("files/datos.csv", "r", encoding="utf-8") as archivo_csv:
    for fila in csv.reader(archivo_csv):
        print(fila)
```

---

<p align="center">
  <b>ZEDMOUS.DEV</b> • Ing. Eduardo Nieves — Arquitectura de Software, Matemáticas Aplicadas & Docencia Universitaria<br/>
  <a href="https://zedmous.netlify.app">zedmous.netlify.app</a> • <a href="https://github.com/Zedmous">github.com/Zedmous</a>
</p>
