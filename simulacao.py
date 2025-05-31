import numpy as np
import matplotlib.pyplot as plt

# Definição do modelo
def atualizar(P, Q):
    P_next = P - 0.1 * (Q - 500)
    Q_next = Q + 0.2 * (P - 100)
    return P_next, Q_next

# Condições iniciais
casos = {
    'A': (100, 500),
    'B': (200, 500),
    'C': (100, 600),
    'D': (100, 400)
}

n_iter = 30  # número de iterações

# Gerar gráfico de simulação (evolução no tempo)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, (caso, (P0, Q0)) in enumerate(casos.items()):
    P_vals = [P0]
    Q_vals = [Q0]
    
    P, Q = P0, Q0
    for _ in range(n_iter):
        P, Q = atualizar(P, Q)
        P_vals.append(P)
        Q_vals.append(Q)
    
    ax = axes[idx]
    ax.plot(P_vals, label='Preço (P)', marker='o')
    ax.plot(Q_vals, label='Quantidade (Q)', marker='s')
    ax.axhline(100, color='blue', linestyle='--', alpha=0.5)
    ax.axhline(500, color='orange', linestyle='--', alpha=0.5)
    ax.set_title(f'Caso {caso}: P₀={P0}, Q₀={Q0}')
    ax.set_xlabel('Ano (n)')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.savefig('simulacao.png')  # Salva como simulacao.png
plt.show()
