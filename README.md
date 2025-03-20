# GUÍA DE PYTHON

# Índice de Contenidos

01. [Variables y sus Tipos](#variables-y-sus-tipos)
02. [Lectura y Escritura de datos](#lectura-y-escritura-de-datos)
03. [Lectura y Escritura de Archivos](#lectura-y-escritura-de-archivos)
    - [Lectura y escritura de un archivo txt](#lectura-y-escritura-de-un-archivo-txt)
    - [Lectura y escritura de un archivo csv](#lectura-y-escritura-de-un-archivo-csv)
04. [Operadores](#operadores)
05. [Conversiones](#conversiones)
06. [Operaciones Aritméticas](#operaciones-aritméticas)
07. [Funciones](#funciones)
08. [Programacion Orientada a Objetos](#programacion-orientada-a-objetos)

## VARIABLES Y SUS TIPOS

### Variables Enteras

```python
edad: int = 30  # Una variable de tipo entero
```

### Variables Reales

```python
temperatura: float = 36.6  # Un número con decimales
```
### Variables de tipo de cadena de texto

```python
nombre: str = "Zedmous"  # Un texto
```

### Variables lógicas

```python
isEngineer: bool = True  # Valor lógico
```

### Variables Complejos

```python
numero: complex = 3 + 4j
print(numero)  # Salida: (3+4j)
# Acceder a la parte real e imaginaria
print(numero.real)  # Parte real: 3.0
print(numero.imag)  # Parte imaginaria: 4.0
```

### Listas

```python
numeros: list[int] = [1, 2, 3, 4]  # Lista de enteros
```

### Tuplas

```python
coordenadas: tuple[float, float] = (10.0, 20.0)  # Una tupla de dos valores flotantes
```

### Conjuntos

```python
frutas: set[str] = {"manzana", "naranja", "pera"}  # Conjunto de cadenas de texto
```

### Diccionarios

```python
estudiante: dict[str, int] = {"edad": 25, "notas": 90}  # Diccionario con claves y valores específicos
```

## LECTURA Y ESCRITURA DE DATOS

### Leer e imprimir una Cadena

```python
# Leer texto desde el teclado
nombre: str = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")
```

### Leer e imprimir un número entero

```python
# Leer un número entero
edad: int = int(input("Introduce tu edad: "))
print(f"Tienes {edad} años.")
```

### Leer e imprimir un número decimal

```python
# Leer un número decimal
altura: float = float(input("Introduce tu altura en metros: "))
print(f"Mides {altura} metros.")
```
## LECTURA Y ESCRITURA DE ARCHIVOS

### Leer e imprimir de un archivo txt
"r": Leer (read), abre un archivo para lectura.
"w": Escribir (write), crea o sobrescribe un archivo.
"a": Agregar (append), añade contenido al final del archivo.
"r+": Leer y escribir.

```python
# Escribir texto en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!\n")
    archivo.write("Esta es una nueva línea de texto.")

# Leer todo el contenido de un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # .strip() elimina saltos de línea adicionales

# Agregar texto a un archivo existente
with open("archivo.txt", "a") as archivo:
    archivo.write("\nNueva línea añadida.")

# Leer y escribir
with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    archivo.write("\nAñadido al final.")

```

### Escribir dados de un archivo CSV

```python
import csv

# Crear y escribir en un archivo CSV
with open("datos.csv", "w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Nombre", "Edad", "Ciudad"])
    escritor.writerow(["Zedmous", 30, "Santa Rosa"])

```

### Leer dados de un archivo CSV

```python
import csv

# Leer un archivo CSV
with open("datos.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)


```
## ESTRUCTURAS DE CONTROL DE FLUJO

### Estructuras de decisión

#### If-Elif-Else

```python
edad: int = 20
if edad < 18:
    print("Menor de edad")
elif 18 <= edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
```

#### Operador Ternario

```python
edad: int = 25
mensaje: str = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
# Salida: Mayor de edad
```

#### Estructura match-case (Python 3.10+):

```python
opcion: int = 2
match opcion:
    case 1:
        print("Elegiste la opción 1")
    case 2:
        print("Elegiste la opción 2")
    case _:
        print("Opción no válida")
```

#### Manejo de Errores:

```python
try:
    numero: int = int(input("Introduce un número entero: "))
    print(f"Número ingresado: {numero}")
except ValueError:
    print("Entrada inválida. Debes ingresar un número.")
```
## Estructuras de Repetitivas

### Ciclo While

```python
contador: int = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar el contador
# Salida: 0, 1, 2, 3, 4
```

### Ciclo For

```python
numeros: list[int] = [1, 2, 3, 4]
for numero in numeros:
    print(f"Número: {numero}")
# Salida: 1, 2, 3, 4
```

### Iteración sobre un rango de números:

```python
for i in range(5):  # Rango de 0 a 4
    print(f"Iteración: {i}")
# Salida: 0, 1, 2, 3, 4
```

### Uso de Break y Continue:
break: Termina el bucle de inmediato.
continue: Salta a la siguiente iteración.
```python
# Ejemplo con break
for i in range(10):
    if i == 5:
        break  # Salir del bucle
    print(i)
# Salida: 0, 1, 2, 3, 4

# Ejemplo con continue
for i in range(5):
    if i == 2:
        continue  # Saltar la iteración
    print(i)
# Salida: 0, 1, 3, 4


```

## OPERADORES

### Operadores lógicos

#### Operador AND

```python
a: bool = True
b: bool = False
print(a and b)  # Salida: False
```

#### Operador OR

```python
a: bool = True
b: bool = False
print(a or b)  # Salida: False
```

#### Operador NOT

```python
a: bool = True
print(not a)  # Salida: False
```

### Operadores Comparativos

#### Igual a (==)

```python
a: int = 10
b: int = 20
print(a == b)  # Salida: False

```

#### Diferente de (!=)

```python
a: int = 10
b: int = 20
print(a != b)  # Salida: True
```

#### Mayor que (>)

```python
a: int = 30
b: int = 20
print(a > b)  # Salida: True
```

#### Menor que (<)

```python
a: int = 10
b: int = 20
print(a < b)  # Salida: True
```

#### Mayor o igual que (>=)

```python
a: int = 20
b: int = 20
print(a >= b)  # Salida: True
```

#### Menor o igual que (<=)

```python
a: int = 15
b: int = 20
print(a <= b)  # Salida: True
```

## CONVERSIONES

### Convertir de entero a real

```python
# Ejemplo de conversión de entero a real
numero_entero: int = 5
numero_real: float = float(numero_entero)
print(numero_real)  # Salida: 5.0
```

### Convertir de real a entero

```python
# Ejemplo de conversión de real a entero
numero_real: float = 9.8
numero_entero: int = int(numero_real)  # Se trunca la parte decimal
print(numero_entero)  # Salida: 9
```

### Convertir de string a enteros

```python
cadena: str = "123"  # Cadena que contiene un número
numero: int = int(cadena)  # Conversión a entero
print(numero)  # Salida: 123
```

### Convertir de entero a strings

```python
numero: int = 123
texto: str = str(numero)
print(texto)  # Salida: "123"
```

## OPERACIONES ARITMETICAS

### Operaciones Aritméticas

```python
a: int = 10
b: int = 5
#Suma
suma: int = a + b
print(suma)  # Salida: 15
#Resta
resta: int = a - b
print(resta)  # Salida: 5
#Multiplicación
multiplicacion: int = a * b
print(multiplicacion)  # Salida: 50
#División
division: float = a / b
print(division)  # Salida: 2.0
#División Entera
division_entera: int = a // b
print(division_entera)  # Salida: 2
#División Residuo
residuo: int = a % b
print(residuo)  # Salida: 0
#Potencia
potencia: int = a ** 2
print(potencia)  # Salida: 100
```

### Operaciones de Asignación
```python
a: int = 10
a += 5  # Equivale a: a = a + 5
print(a)  # Salida: 15

a *= 2  # Equivale a: a = a * 2
print(a)  # Salida: 30
```

### Prioridad de Operadores (Precedencia)

El orden de evaluación sigue estas reglas:

  1  Paréntesis: ( )

  2  Potencias: **

  3  Multiplicación/División/Módulo: *, /, //, %

  4  Suma/Resta: +, -

```python
resultado: float = (2 + 3) * 2 ** 2 / 4
print(resultado)  # Salida: 5.0
```
## FUNCIONES

### Funcion Básica
```python
# Función que suma dos números
def sumar(a: int, b: int) -> int:
    return a + b

# Llamada a la función
resultado: int = sumar(5, 3)
print(f"La suma es: {resultado}")
# Salida: La suma es: 8
```

### Parámetros y valores predeterminados
```python
# Función que suma dos números
def saludar(nombre: str = "Invitado") -> None:
    print(f"Hola, {nombre}!")

saludar("Zedmous")  # Salida: Hola, Zedmous!
saludar()           # Salida: Hola, Invitado!
```
### Función con múltiples retornos
```python
def dividir(a: int, b: int) -> tuple[int, int]:
    cociente: int = a // b
    residuo: int = a % b
    return cociente, residuo

cociente, residuo = dividir(10, 3)
print(f"Cociente: {cociente}, Residuo: {residuo}")
# Salida: Cociente: 3, Residuo: 1
```
## PROGRAMACIÓN ORIENTADA A OBJETOS

### Crear una Clase
```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    def saludar(self) -> None:
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto (instancia) de la clase
persona1: Persona = Persona("Zedmous", 74)
persona1.saludar()
# Salida: Hola, soy Zedmous y tengo 74 años.
```

### Herencia
```python
class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, asignatura: str):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def enseñar(self) -> None:
        print(f"Estoy aprendiendo {self.asignatura}.")

# Crear instancia de la clase hija
profesor: Profesor = Profesor("Zedmous", 74, "Matemáticas Avanzadas e Inteligencia Artificial")
profesor.saludar()  # Método de la clase padre
profesor.enseñar()  # Método de la clase hija
# Salida: Hola, soy Zedmous y tengo 74 años.
#         Estoy aprendiendo Matemáticas Avanzadas e Inteligencia Artificial.
```

### Encapsulamiento
```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo

    def consultar_saldo(self) -> None:
        print(f"Saldo actual: {self.__saldo}")

# Crear una cuenta bancaria
cuenta: CuentaBancaria = CuentaBancaria("Zedmous", 1000.0)
cuenta.consultar_saldo()
# Salida: Saldo actual: 1000.0

```

### Polimorfismo
```python
class Dragon:
    def hacer_sonido(self) -> None:
        print("Graaararrarrarrararrara!")

class Gato:
    def hacer_sonido(self) -> None:
        print("Miau!")

# Polimorfismo en acción
animales: list[object] = [Dragon(), Gato()]
for animal in animales:
    animal.hacer_sonido()
# Salida: Guau!
#         Miau!
```