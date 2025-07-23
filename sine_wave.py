import numpy as np
import matplotlib.pyplot as plt

T = 100
f = 1/T
n = 5
t = np.linspace(0, 1/f, 1000)
a = np.sin(2*np.pi*f*t*n)

plt.figure(figsize=(10,3))
plt.plot(t, a)
plt.xlabel("x")
plt.ylabel("sin(t)")
plt.show()