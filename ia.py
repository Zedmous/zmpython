"""
ZEDMOUS.DEV — Laboratorio de Inteligencia Artificial / Machine Learning desde Cero
Entrenamiento de una Red Neuronal Lineal (Regresión Lineal Multivariable) mediante
Descenso del Gradiente (Gradient Descent) con NumPy puro.

Objetivo: Descubrir automáticamente los pesos reales de la ecuación:
          target = 2 * xs - 3 * zs + 5 + ruido
"""

import numpy as np

print("=== ZEDMOUS.DEV | Entrenamiento de Modelo Lineal con Descenso del Gradiente ===")

# 1. Generación del dataset de entrenamiento (1000 observaciones)
np.random.seed(42)
observations = 1000
xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = np.random.uniform(low=-10, high=10, size=(observations, 1))
inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))
targets = 2 * xs - 3 * zs + 5 + noise

# 2. Inicialización aleatoria de pesos (weights) y sesgo (bias) en [-0.1, 0.1]
init_range = 0.1
weights = np.random.uniform(low=-init_range, high=init_range, size=(2, 1))
biases = np.random.uniform(low=-init_range, high=init_range, size=1)

# 3. Hiperparámetros de entrenamiento
learning_rate = 0.02
epochs = 150

# 4. Bucle de optimización por Descenso del Gradiente (Minimización de pérdida L2 / MSE)
for epoch in range(1, epochs + 1):
    # Forward pass: predicción lineal y = X @ W + b
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - targets

    # Función de costo L2 dividida entre 2*N
    loss = np.sum(deltas ** 2) / 2 / observations

    if epoch in (1, 10, 25, 50, 100, 150):
        print(f"  Época {epoch:3d}/{epochs} | Pérdida (Loss MSE): {loss:.6f}")

    # Backward pass: cálculo de gradientes y actualización de parámetros
    deltas_scaled = deltas / observations
    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate * np.sum(deltas_scaled)

print("\n=== Resultados del Modelo Aprendido vs. Ecuación Real (2*x - 3*z + 5) ===")
print(f"  Peso aprendido w1 (esperado  2.0): {weights[0, 0]:.4f}")
print(f"  Peso aprendido w2 (esperado -3.0): {weights[1, 0]:.4f}")
print(f"  Sesgo aprendido b (esperado  5.0): {biases[0]:.4f}")

