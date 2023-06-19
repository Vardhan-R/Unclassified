import matplotlib.pyplot as plt, numpy as np

f_1, f_2 = 1.5, 1.5

wv = lambda f: np.sin(2 * np.pi * f * np.linspace(0, 1, 100, True))

p = wv(f_1)

nN = len(p)

base = np.e ** (-2j * np.pi * np.linspace(0, 1, nN))

plt.plot(np.abs(np.dot(p, np.array([base ** (f) for f in range(nN)]))))
plt.xlim(0, 10)
plt.show()