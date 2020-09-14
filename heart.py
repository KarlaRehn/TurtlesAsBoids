from math import cos, sin
from numpy import linspace
import matplotlib.pyplot as plt

def heart(t):
	x = 15*(sin(t)**3)
	y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
	return x, y

def d_heart(t, h = 0.0000001):
	dx, dy = [(p[0]-p[1])/(2*h) for p in zip(heart(t+h),heart(t-h))]
	return dx, dy

if __name__ == "__main__":
	T = linspace(-10, 10, 1000)
	X = []
	Y = []

	for t in T:
		H = heart(t) # men se! funktionen anropas 1000 gånger utan problem
		X.append(H[0])
		Y.append(H[1])


	plt.plot(X, Y, 'ro')
	plt.show()
	
