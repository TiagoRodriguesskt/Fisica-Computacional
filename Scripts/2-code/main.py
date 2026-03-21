'''
Docstrings:
O Algoritmo: Transformando Cálculo em Código
O que era uma equação complexa se torna uma sequência lógica de atribuição de variáveis:
'''


# Estrutura de dados para o estado
estado = {
    "x": 1.0,  # Posição inicial (m)
    "v": 0.0,  # Velocidade inicial (m/s)
    "a": 0.0,  # Aceleração
    "t": 0.0,  # Tempo
}

# Constantes do sistema
k = 10.0  # Constante da mola
m = 1.0  # Massa
dt = 0.01  # Resolução temporal
t = 0.0

# O Loop de Simulação (Física Computacional)
for _ in range(1000):
    # 1. Cálculo da 'Lógica de Negócio' (Física)
    estado["a"] = -(k / m) * estado["x"]

    # 2. Atualização do Estado (Integração Numérica)
    estado["v"] += estado["a"] * dt
    estado["x"] += estado["v"] * dt

    # Atualização da variável tempo
    t += dt  # t = t + dt

    # 3. Log/Persistência (Opcional)
    print(f"Tempo: {t:.2f} | Posição: {estado['x']:.4f}")
