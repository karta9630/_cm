# t=(Xˉ−μ) / (s / n^(1/2))
#s^2=∑(Xi​−Xˉ)^2/(n-1)
import math
data=[58, 89, 100,77, 39]
mu = 70
x_bar = sum(data) / 5
s = math.sqrt(sum((x-x_bar)**2 for x in data) / (5 - 1))
t=(x_bar-mu)/(s/math.sqrt(5))
print(f"{t:.2f}")