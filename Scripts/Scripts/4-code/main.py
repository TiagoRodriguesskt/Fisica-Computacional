'''
Script: Calculadora de Vetor Resultante (Regra do Paralelogramo)
'''

import math

import matplotlib.pyplot as plt
import numpy as np  # noqa: F401


def calcular_resultante_grafica(a, b, angulo_graus):
    # 1. Conversão para Radianos
    rad = math.radians(angulo_graus)

    # 2. Lei dos Cossenos (Versão Física/Soma Vetorial)
    # R = sqrt(A² + B² + 2AB * cos(theta))
    r_quadrado = a**2 + b**2 + 2 * a * b * math.cos(rad)
    r = math.sqrt(r_quadrado)

    # 3. Coordenadas para o Gráfico
    # Vetor A no eixo X
    ax, ay = a, 0
    # Vetor B com inclinação theta
    bx, by = b * math.cos(rad), b * math.sin(rad)
    # Vetor Resultante R
    rx, ry = ax + bx, ay + by

    # --- Visualização ---
    fig, plot = plt.subplots(figsize=(8, 6))

    # Plotando os vetores principais (A e B)
    plot.quiver(
        [0, 0],
        [0, 0],
        [ax, bx],
        [ay, by],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=["blue", "green"],
        label=["Vetor A", "Vetor B"],
        width=0.015,
    )

    # Plotando as linhas pontilhadas do paralelogramo
    plot.plot([ax, rx], [ay, ry], "k--", alpha=0.5)
    plot.plot([bx, rx], [by, ry], "k--", alpha=0.5)

    # Plotando a Resultante R
    plot.quiver(
        0,
        0,
        rx,
        ry,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="red",
        label=f"Resultante R ({r:.2f})",
        width=0.02,
    )

    # Configurações de layout
    limite = max(a, b, r) + 1
    plot.set_xlim(-1, limite)
    plot.set_ylim(-1, limite)
    plot.set_aspect("equal")
    plot.grid(True, linestyle=":")
    plot.legend()
    plot.set_title(f"Soma de Vetores: Ângulo de {angulo_graus}°")

    plt.show()
    return r


# Exemplo de uso baseado na aula
modulo_a = 5
modulo_b = 7
angulo = 60  # graus

resultante = calcular_resultante_grafica(modulo_a, modulo_b, angulo)
print(f"O módulo do vetor resultante é: {resultante:.2f}")
