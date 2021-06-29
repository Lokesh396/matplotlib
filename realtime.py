import pandas as pd
import random
from matplotlib import pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

xvals=[]
yvals=[]
index=count()

def animate(i):
    xvals.append(next(index))
    yvals.append(random.randint(0,5))
    plt.cla()
    plt.plot(xvals,yvals)
ani=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.tight_layout()
plt.show()
