import heapq
import sys
import matplotlib.pyplot as plt

class TrainingPoint:
	def __init__(self, string, c = -1):
		self.string = string.lower()
		self.x = self.calc1()
		self.y = self.calc2()
		self.c = c

	# measure of readability
	def calc1(self):
		non_alphabetic = 0
		for char in self.string:
			non_alphabetic += char.isalpha()
		return non_alphabetic/len(self.string)

	# measure of tags
	def calc2(self):
		res = 0
		keywords = ["img", "script", "src", "href", "cookie"]
		for keyword in keywords:
			res += self.string.__contains__(keyword)
		return res

def distance(point1, point2):
	return (point1.x - point2.x)**2 + (point1.y - point2.y)**2

def train_points():
	training_points = []
	with open('training.txt', 'r') as file:
		num_points = int(file.readline())
		for i in range(num_points):
			string = file.readline()
			c = int(file.readline())
			training_point = TrainingPoint(string, c)
			# training_points.add_point(training_point)
			training_points.append(training_point)
	return training_points

def find_k_nearest_neighbour(k, point, points):
	best_neighbours = []
	heapq.heapify(best_neighbours)
	for neighbour in points:
		d = distance(point, neighbour)
		c = neighbour.c
		heapq.heappush(best_neighbours, (d,c))

	malicious = 0
	for i in range(k):
		(_, c) = heapq.heappop(best_neighbours)
		malicious += c
	return malicious > k//2

def main():
	k = 1
	training_points = train_points()
	x_malicious = []
	x_benign = []
	y_malicious = []
	y_benign = []
	for point in training_points:
		# point is malicious
		if point.c:
			x_malicious.append(point.x)
			y_malicious.append(point.y)
		# point is benign
		else:
			x_benign.append(point.x)
			y_benign.append(point.y)
	plt.show()
	while True:
		string = input("Enter your string: ")
		if string == 'x':
			break
		point = TrainingPoint(string)
		print(find_k_nearest_neighbour(k, point, training_points))
		plt.scatter(x_malicious,y_malicious, color = 'red', label = 'malicious')
		plt.scatter(x_benign,y_benign, color = 'blue', label ='benign')
		plt.scatter(point.x, point.y, color = 'black')
		plt.xlabel('Measure of readability')
		plt.ylabel('Number of HTML keywords') 
		plt.legend()
		plt.show()

main()
