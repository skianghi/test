#Bar graph maker
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style


fig, ax = plt.subplots()
z=plt.bar(1,0,align='center')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return z,

def update(frame):

    z.set_height = np.sin(frame)
    return z,

ani = animation.FuncAnimation(fig, update, frames=100,init_func=init, blit=True)
plt.show()
