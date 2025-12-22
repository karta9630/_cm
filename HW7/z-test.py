#Z=(Xˉ−μ) / (σ / n^(1/2))
import math
data=[58, 89, 100,77, 39]
mu = 70
sigma = 1.96
x_bar = sum(data) / 5
z = (x_bar-mu)/(sigma/math.sqrt(5))
print(z)