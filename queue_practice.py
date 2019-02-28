import queue as Queue

class Solution:

	def __init__(self):
		pass

	def put_in(self, string):
		self.q = Queue.Queue()
		for char in string:
			self.q.put(char)


	def print_out(self):
		while not self.q.empty():
			print(self.q.get())

if __name__ == '__main__':

	s = input()
	new_queue = Solution()
	new_queue.put_in(s)
	new_queue.print_out()


	
