import random as rd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

n = 20.0
step = 0.5
a = 10.0

xs = np.arange(0.0, n, step)
ys = []

for x in xs:
	b = rd.uniform(0.0, 20.0)
	y = a*x + b
	ys.append(y)


matplotlib.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots()
ax.plot(xs, ys, "o")
ax.set_title("problem 9")
plt.savefig("problem9_1.png")