import random as rd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def regression(xs, ys):

	xmean = np.mean(xs)
	ymean = np.mean(ys)

	numerator = 0
	denumerator = 0

	for x, y in zip(xs, ys):
		numerator += ((x - xmean) * (y - ymean))
		denumerator += ((x - xmean) * (x - xmean))

	w1 = numerator/denumerator
	w0 = ymean - w1 * xmean

	return w0, w1


	

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

w0, w1 = regression(xs, ys)

ax.plot(xs, w0 + (w1*xs))

plt.savefig("problem9_2.png")