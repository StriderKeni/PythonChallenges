class Differente:


	def __init__(self, a):
		self.__elements = a

	def computeDifference(self):
		self.max_arr = max(self.__elements)
		self.min_arr = min(self.__elements)
		self.maximumDifference = self.max_arr - self.min_arr


if __name__ == '__main__':
	
	_ = input()
	a = [int(e) for e in input().split(' ')]
	d = Differente(a)
	d.computeDifference()
	print(d.maximumDifference)

	
