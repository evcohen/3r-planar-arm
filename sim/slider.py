import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # make room for the slider at the bottom

dot, = ax.plot([0], [0], 'ro', markersize=10)
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 1)

slider_ax = fig.add_axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(slider_ax, 'X position', -3, 3, valinit=0)

def update(val):
    x = slider.val
    dot.set_xdata([x])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()