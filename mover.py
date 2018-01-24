from potential import potential
from robot import robot
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

if __name__ == "__main__":
	gX = int(input("Enter X coordinate of the goal: "))
	gY = int(input("Enter Y coordinate of the goal: "))

	X = int(input("Enter X coordinate of the initial position: "))
	Y = int(input("Enter Y coordinate of the initial position: "))
	
	n = int(input("Enter the number of obstacles: "))
	oX = []
	oY = []
	for i in range(n):
		oX.append(int(input("X coordinate of obstacle " + str(i + 1) + ": ")))
		oY.append(int(input("Y coordinate of obstacle " + str(i + 1) + ": ")))
	
	rO = int(input("Enter radius of the obstacle (Assuming they're all the same) : "))
	rG = 0.2

	sO = 10

	a = 0.001
	b = 0.03

	pot_env = potential(gX, gY, oX, oY)
	rob = robot(X, Y)

	curX, curY = rob.getCurrentLocation()
	distG, theG = pot_env.getParamsFromGoal(curX, curY)
	
	xPlot = []
	yPlot = []
	xPlot.append(X)
	yPlot.append(Y)

	max_iter = 10000
	iter_ = 0

	while(distG > rG and iter_ <= max_iter):
		iter_ += 1
		delX = a * (distG - rG) * (math.cos(theG))
		delY = a * (distG - rG) * (math.sin(theG))

		distO, theO = pot_env.getParamsFromObstacles(curX, curY)
		if (distO[0] != -1):
			for i, j in zip(distO, theO):
				# print "Distance from obstacle: " + str(i)
				if (i < rO):
					delX = delX - 2.5 * (math.cos(j))
					delY = delY - 2.5 * (math.sin(j))
				elif (i < sO + rO):
					delX = delX - b * (sO + rO - i) * (math.cos(j))
					delY = delY - b * (sO + rO - i) * (math.sin(j))

		# print delX, delY
		# print "Distance from Goal: " + str(distG)
		# print "Curr coordinates: " + str(rob.getCurrentLocation())
		rob.updateLocation(delX, delY)
		
		curX, curY = rob.getCurrentLocation()
		xPlot.append(curX)
		yPlot.append(curY)

		distG, theG = pot_env.getParamsFromGoal(curX, curY)

	ax = plt.axes()
	for i in range(n):
		ax.add_patch(patches.Circle((oX[i], oY[i]), rO, hatch = '/', fill = False))

	plt.plot(xPlot, yPlot)
	plt.show()

	# To print the Potential field
	X, Y = np.meshgrid(np.arange(0, 100), np.arange(0, 100))
	U, V = [], []
	for P in range(100):
		U.append([])
		V.append([])
		for j, k in zip(X[P], Y[P]):
			# print j, k
			rob = robot(j, k)
			curX, curY = rob.getCurrentLocation()
			distG, theG = pot_env.getParamsFromGoal(curX, curY)
			
			delX = a * (distG - rG) * (math.cos(theG))
			delY = a * (distG - rG) * (math.sin(theG))

			distO, theO = pot_env.getParamsFromObstacles(curX, curY)
			if (distO[0] != -1):
				for i, j in zip(distO, theO):
					# print "Distance from obstacle: " + str(i)
					if (i < rO):
						delX = delX - 2.5 * (math.cos(j))
						delY = delY - 2.5 * (math.sin(j))
					elif (i < sO + rO):
						delX = delX - b * (sO + rO - i) * (math.cos(j))
						delY = delY - b * (sO + rO - i) * (math.sin(j))

			U[P].append(delX)
			V[P].append(delY)

	U = np.array(U)
	V = np.array(V)
	
	plt.figure()
	Q = plt.quiver(X, Y, U, V)
	qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
	                   coordinates='figure')
	plt.plot(xPlot, yPlot)
	plt.show()