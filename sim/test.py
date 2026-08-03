import numpy as np
import matplotlib.pyplot as plt
range = np.linspace(0, np.pi, 100)
plt.plot(np.cos(range), np.sin(range))
plt.axis("equal")
plt.title("yay!")
plt.show()