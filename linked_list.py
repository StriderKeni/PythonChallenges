class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = Node()

	def insert(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next!=None:
			cur = cur.next
		cur.next = new_node

	def display(self):
		elements = []
		cur = self.head
		while cur.next!=None:
			cur = cur.next
			elements.append(cur.data)
		return elements

	def remove_duplicates(self):
		cur = self.head
		while cur.next!=None:
			next_node = cur.next
			if cur.data == next_node.data:
				temp = next_node.next
				next_node.next = None
				cur.next = temp
			else:
				cur = cur.next


if __name__ == '__main__':

	my_linked_list = LinkedList()
	for i in range(int(input())):
		my_linked_list.insert(int(input()))

	my_linked_list.remove_duplicates()
	print(my_linked_list.display())




