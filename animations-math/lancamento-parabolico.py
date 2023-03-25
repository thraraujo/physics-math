import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

theta = np.pi / 4
v0 = 50
g = 9.8
m = 2


fig, ax = plt.subplots()

def y(x):
    return v0 * np.sin(theta)* x - (g * x ** 2) / 2


def K(x):
    kin = m * ((v0 * np.cos(theta))**2 + (v0 * np.sin(theta) - g * x )**2 ) / 2
    return kin 

def P(x):
    pot = m * g * (v0 * np.sin(theta)* x - (g * x ** 2) / 2)
    return pot

def E(x):
    return K(x) + P(x)


t = np.arange(0, 4, 0.01)
line, = ax.plot(t, K(t))

def animate(i):
    line.set_ydata(K(t + i / 50))  # update the data.
    return line,



ani = animation.FuncAnimation(
    fig, animate, interval=50, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
