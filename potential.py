import math

class potential():
	def __init__(self, gX, gY, oX, oY):
		self.gX = gX
		self.gY = gY

		self.oX = oX
		self.oY = oY

	def getParamsFromGoal(self, x, y):
		dist = math.sqrt((x - self.gX) * (x - self.gX) + (y - self.gY) * (y - self.gY))
		theta = math.atan2((self.gY - y),(self.gX - x))

		return dist, theta

	def getParamsFromObstacles(self, x, y):
		if (len(self.oX) != 0 and len(self.oY) != 0):
			dist = []
			theta = []

			for i, j in zip(self.oX, self.oY):
				d = math.sqrt((x - i) * (x - i) + (y - j) * (y - j))
				t = math.atan2((j - y),(i - x))

				dist.append(d)
				theta.append(t)


			return dist, theta

		else:
			return [-1],[-1]