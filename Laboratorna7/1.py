import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-2,5)
y1 = np.sin(5*x)
y = x*y1

ax.plot(y)

plt.show()
