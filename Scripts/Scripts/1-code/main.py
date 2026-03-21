'''
Docstrings:
Script de Simulação Física (Leis de Newton)
Este código calcula a trajetória de um objeto sob influência da gravidade e resistência do ar, um problema clássico de Física I.
'''

import matplotlib.pyplot as plt
import numpy as np  # noqa: F401

# 1. Parâmetros Físicos (Constantes)
g = 9.81  # Aceleração da gravidade (m/s^2)
m = 1.0  # Massa do objeto (kg)
k = 0.1  # Coeficiente de resistência do ar (kg/s)
dt = 0.01  # Passo de tempo (s) - Precisão da simulação
t_total = 10.0  # Tempo total de observação

# 2. Condições Iniciais (Variáveis)
t = 0
v = 50.0  # Velocidade inicial (m/s)
y = 0.0  # Posição inicial (m)

# Listas para armazenar dados para o gráfico
tempos = [t]
posicoes = [y]

# 3. Loop de Integração Numérica (O "Motor" da Física)
while y >= 0 and t < t_total:
    # Cálculo da Força Resultante: F = F_gravidade + F_resistencia
    F_res = -k * v
    F_grav = -m * g
    F_total = F_grav + F_res

    # Segunda Lei de Newton: a = F / m
    a = F_total / m

    # Atualização de Euler (Cálculo Diferencial Numérico)
    v = v + a * dt  # v(t + dt) = v(t) + a*dt
    y = y + v * dt  # y(t + dt) = y(t) + v*dt
    t = t + dt

    tempos.append(t) # type: ignore
    posicoes.append(y)

# 4. Visualização dos Resultados
plt.plot(tempos, posicoes)
plt.title("Simulação de Lançamento Vertical com Resistência do Ar")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")
plt.grid(True)
plt.show()
