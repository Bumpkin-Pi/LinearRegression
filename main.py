import math

import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np

data = pd.read_csv("data.csv")

Σx = 0
Σy = 0
Σxy = 0
Σx2 = 0
n = len(data)

for i in range(len(data)):
    Σx += data.iloc[i].x
    Σy += data.iloc[i].y
    #print(Σy)
    Σxy += data.iloc[i].x * data.iloc[i].y
    Σx2 += toPower(data.iloc[i].x, 2)
    plt.scatter([data.iloc[i].x], [data.iloc[i].y], color="black")


#print(f'Σx = {Σx}\nΣy = {Σy}\nΣxy = {Σxy}\nΣx2 = {Σx2}')

#Main functions
m = (
        (n * Σxy - Σx * Σy) /
        (n * Σx2 - toPower(Σx, 2))
)
b = (Σy - (m * Σx)) / n

plt.plot(list(range(0, 100)), [m * X + b for X in range(0, 100)], color="red")

print(f'y = {m}x + {b}')

plt.show()