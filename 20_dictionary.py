import math
import matplotlib.pyplot as plt

p_values = [[0.2, 0.2, 0.2, 0.2, 0.2]]
q_values = [[0.3, 0.1, 0.1, 0.2, 0.3]]

# calculation for p_values
print(p_values)
alpha = 0
p_sum = 0
h_x_p = []

for a in range(0, 5):
    for i in range(0, 4):
        p_sum += pow(p_values[0][i], alpha)
    h_x_p.append((1 / 1 - alpha) * math.log(p_sum, 2))
    alpha += 0.5

print(alpha)
print(h_x_p)

# calculation for q_values
print(q_values)
alpha = 0
q_sum = 0
h_x_q = []

for a in range(0, 5):
    for i in range(0, 4):
        q_sum += pow(q_values[0][i], alpha)
    h_x_q.append((1 / 1 - alpha) * math.log(q_sum, 2))
    alpha += 0.5

print(alpha)
print(h_x_q)

# Information divergence between distributions of p and q of order alpha
alpha = 0
pq_sum = 0
h_x_pq = []

for a in range(0, 5):
    for i in range(0, 4):
        pq_sum += (pow(p_values[0][i], alpha) * pow(q_values[0][i], 1 - alpha))
    h_x_pq.append((-1 / 1 - alpha) * math.log(pq_sum, 2))
    alpha += 0.5

print(alpha)
print(h_x_pq)

# Graphs
plt.plot(h_x_p)
