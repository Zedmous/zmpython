"""
ZEDMOUS.DEV — Laboratorio de Ciencia de Datos con Python (NumPy + Matplotlib 3D)
Generación de un dataset sintético multivariable (y = 2*x - 3*z + 5 + ruido)
y visualización del hiperplano 3D.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# 1. Generar datos de entrada sintéticos reproducibles
np.random.seed(42)
observations = 1000
xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = np.random.uniform(low=-10, high=10, size=(observations, 1))

inputs = np.column_stack((xs, zs))
print(f"[Data Science] Matriz de entrada (inputs): {inputs.shape}")

# 2. Construir el objetivo real (Target: plano 2*x - 3*z + 5 con ruido uniforme)
noise = np.random.uniform(-1, 1, (observations, 1))
targets = 2 * xs - 3 * zs + 5 + noise
print(f"[Data Science] Vector objetivo (targets):  {targets.shape}")

# 3. Graficar la nube de puntos 3D
fig = plt.figure("ZEDMOUS.DEV — Visualización 3D de Datos de Entrenamiento", figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
scatter = ax.scatter(xs.flatten(), zs.flatten(), targets.flatten(), c=targets.flatten(), cmap="viridis", s=10, alpha=0.75)
ax.set_title("Plano Sintético: y = 2x - 3z + 5 + ruido")
ax.set_xlabel("Variable X (xs)")
ax.set_ylabel("Variable Z (zs)")
ax.set_zlabel("Objetivo (Targets)")
ax.view_init(elev=22, azim=110)
fig.colorbar(scatter, ax=ax, shrink=0.6, label="Valor de Target")

os.makedirs("files", exist_ok=True)
out_img = "files/grafico_3d_regresion.png"
plt.savefig(out_img, dpi=150, bbox_inches="tight")
print(f"[Data Science] Gráfico 3D guardado en: {out_img}")

if os.environ.get("MPLBACKEND", "").lower() != "agg":
    plt.show()
