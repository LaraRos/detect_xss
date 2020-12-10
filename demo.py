import heapq
import sys


class TrainingPoint:
	def __init__(self, string, c = -1):
		self.string = string
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

class TrainingPoints:
	def __init__(self):
		self.points = []

	def add_point(self, point):
		self.points.append(point)

def distance(point1, point2):
	return (point1.x - point2.x)**2 + (point1.y - point2.y)**2

def train_points():
	training_points = TrainingPoints()
	with open('training.txt', 'r') as file:
		num_points = int(file.readline())
		for i in range(num_points):
			string = file.readline()
			c = int(file.readline())
			training_point = TrainingPoint(string, c)
			training_points.add_point(training_point)
	return training_points

def find_k_nearest_neighbour(k, point, points):
	best_neighbours = []
	heapq.heapify(best_neighbours)
	for neighbour in points.points:
		d = distance(point, neighbour)
		c = neighbour.c
		heapq.heappush(best_neighbours, (d,c))

	malicious = 0
	for i in range(k):
		(_, c) = heapq.heappop(best_neighbours)
		malicious += c
	return malicious > k//2

def main():
	k = 3
	training_points = train_points()
	while True:
		string = input("Enter your string: ")
		point = TrainingPoint(string)
		print(find_k_nearest_neighbour(k, point, training_points))

main()






		







		


