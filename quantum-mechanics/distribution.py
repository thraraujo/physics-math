import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


# The parametrized function to be plotted
def f(energy, temperature):
    return 1 / (np.exp(temperature * energy - 10) + s*1)

energy = np.linspace(0, 1, 1000)

s = 1 # fermi-dirac
#s = -1 # bose-einstein


# Define initial parameters
init_temperature = 5

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(energy, f(energy, init_temperature), lw=2)
ax.set_xlabel('Energy')

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the temperature.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
temp_slider = Slider(
    ax=axfreq,
    label='Temperature',
    valmin=0.1,
    valmax=30,
    valinit=init_temperature,
)

# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(energy, temp_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
temp_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    temp_slider.reset()
button.on_clicked(reset)

plt.show()
