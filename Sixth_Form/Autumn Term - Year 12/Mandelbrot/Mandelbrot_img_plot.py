import numpy as np
import matplotlib.pyplot as plt

d, h = 800, 600  # pixel density (= image width) and image height
n, r = 100, 500  # number of iterations and escape radius (r > 2)

x = np.linspace(0, 2, num=d + 1)
y = np.linspace(0, 2 * h / d, num=h + 1)

A, B = np.meshgrid(x - 1, y - h / d)
C = 2.0 * (A + B * 1j) - 0.5

Z, dZ = np.zeros_like(C), np.zeros_like(C)
S, T, D = np.zeros(C.shape), np.zeros(C.shape), np.zeros(C.shape)

for k in range(n):
    M = abs(Z) < r
    S[M], T[M] = S[M] + np.exp(-abs(Z[M])), T[M] + 1
    Z[M], dZ[M] = Z[M] ** 2 + C[M], 2 * Z[M] * dZ[M] + 1

plt.imshow(S ** 0.1, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot_set_1.png", dpi=250)

N = abs(Z) > r  # normalized iteration count
T[N] = T[N] - np.log2(np.log(abs(Z[N])) / np.log(r))

plt.imshow(T ** 0.1, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot_set_2.png", dpi=250)

N = abs(Z) > 2  # exterior distance estimation
D[N] = 0.5 * np.log(abs(Z[N])) * abs(Z[N]) / abs(dZ[N])

plt.imshow(D ** 0.1, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot_set_3.png", dpi=250)

X, Y = C.real, C.imag
R = 150 * 2 / d  # scaling depends on figsize

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X, Y, s=R ** 2, c=D ** 0.1, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot_plot.png", dpi=250)
