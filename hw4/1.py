import numpy as np

# 多項式 P(z)，係數由低到高
def P(z, c):
    val = 0
    for k in reversed(range(len(c))):
        val = val * z + c[k]
    return val

# 導數 P'(z)
def dP(z, c):
    val = 0
    for k in reversed(range(1, len(c))):
        val = val * z + k * c[k]
    return val

def complex_gradient_descent(c, z0, eta=0.01, tol=1e-8, max_iter=10000):
    z = z0
    for _ in range(max_iter):
        grad = np.conj(dP(z, c)) * P(z, c)
        z = z - eta * grad
        if abs(P(z, c)) < tol:
            break
    return z
c = [-1, 0, 0, 0, 0, 1]  # z^5 - 1

for z0 in [1+0.5j, -1+0.5j, 0.5+1j, -0.5-1j]:
    root = complex_gradient_descent(c, z0)
    print(root)
