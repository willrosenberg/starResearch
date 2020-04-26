import numpy as np

class Triangles:
	def __init__(self):
		self.triangles = #2D array triangle, indexes
		self.points = #2D array points, coords
		self.normals = self.createNormal()
		self.gradients = self.createGradient()

	def createNormal(self):
		normals = []
		for i in self.triangles:
			vector1 = np.subtract(self.points[i[0]], self.points[i[2]])
			vector2 = np.subtract(self.points[i[1]], self.points[i[2]])
			normal = np.cross(vector1, vector2)
			normals.append(normal)

		return normals


	def createGradient(self):
		gradients = []
		for i in normals:
			gradient = np.zeros(2)
			i = np.divide(i,(-i[2]))
			gradient[0] = i[0]
			gradient[1] = i[1]
			gradients.append(gradient)

		return gradient



	

