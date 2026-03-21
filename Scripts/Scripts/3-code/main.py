"""
DocStrings:
Este script realiza duas tarefas visuais baseadas na sua imagem:Decomposição de um Vetor V:
Mostra o vetor original e suas componentes V_x e V_y.Soma de Dois Vetores V_1 e V_2: Mostra os vetores originais e o vetor Resultante R.

A Lógica na Decomposição: No primeiro gráfico, você verá o vetor azul V. O script calcula V_x (vermelho) e V_y (verde).
Geometricamente, você percebe que V = V_x + V_y (a soma das componentes vermelha e verde forma a seta azul).
"""

import math

import matplotlib.pyplot as plt
import numpy as np  # noqa: F401


def configurar_grafico(ax, titulo, limite):
    """Configura a aparência do gráfico (eixos, grade, título)."""
    ax.set_title(titulo)
    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)
    ax.axhline(0, color="black", linewidth=1)  # Eixo X
    ax.axvline(0, color="black", linewidth=1)  # Eixo Y
    ax.grid(True, linestyle="--")
    ax.set_aspect("equal", adjustable="box")  # Mantém a proporção 1:1


def plotar_vetor(ax, x, y, color, label):
    """Plota um vetor como uma seta saindo da origem (0,0)."""
    ax.quiver(
        0, 0, x, y, angles="xy", scale_units="xy", scale=1, color=color, label=label
    )


# --- 1. Visualização da Decomposição de um Vetor V ---
def plotar_decomposicao(modulo, angulo_graus):
    """Gera o gráfico de decomposição de um vetor V."""
    fig, ax = plt.subplots(figsize=(6, 6))
    configurar_grafico(
        ax, f"Decomposição do Vetor V ({modulo} u a {angulo_graus}°)", 12
    )

    # Converter ângulo para radianos e calcular componentes
    angulo_rad = math.radians(angulo_graus)
    vx = modulo * math.cos(angulo_rad)
    vy = modulo * math.sin(angulo_rad)

    # Plotar o Vetor Original V
    plotar_vetor(ax, vx, vy, "blue", "Vetor Original V")

    # Plotar as Componentes Vx e Vy
    plotar_vetor(ax, vx, 0, "red", "Componente Vx")
    plotar_vetor(ax, 0, vy, "green", "Componente Vy")

    # Adicionar legenda e mostrar
    ax.legend()
    plt.show()


# --- 2. Visualização da Soma de Vetores V1 e V2 (Resultante) ---
def plotar_resultante(v1_x, v1_y, v2_x, v2_y):
    """Gera o gráfico da soma de dois vetores V1 e V2."""
    fig, ax = plt.subplots(figsize=(6, 6))
    limite = max(abs(v1_x + v2_x), abs(v1_y + v2_y)) + 5
    configurar_grafico(ax, "Soma de Vetores: V1 + V2 = R", limite)

    # Vetores Originais
    plotar_vetor(ax, v1_x, v1_y, "blue", "Vetor V1")
    plotar_vetor(ax, v2_x, v2_y, "green", "Vetor V2")

    # Vetor Resultante R
    r_x = v1_x + v2_x
    r_y = v1_y + v2_y
    plotar_vetor(ax, r_x, r_y, "purple", "Vetor Resultante R")

    # Adicionar legenda e mostrar
    ax.legend()
    plt.show()


# --- Execução dos Exemplos ---

# Exemplo 1: Decomposição (V=10 u, ângulo=30°)
plotar_decomposicao(10, 30)

# Exemplo 2: Resultante (V1 = (5, 5), V2 = (-3, 2))
plotar_resultante(5, 5, -3, 2)
