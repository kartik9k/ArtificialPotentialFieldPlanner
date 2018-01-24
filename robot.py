class robot():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getCurrentLocation(self):
		return self.x, self.y

	def updateLocation(self, delx, dely):
		self.x = self.x + delx
		self.y = self.y + dely