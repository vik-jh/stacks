

from sys import stdin

class Node :

	def __init__(self, data) :
		self.data = data
		self.next = None

class Stack :

	def __init__(self) :
		self.__head = None
		self.__size = 0


	def getSize(self) :
		return self.__size


	def isEmpty(self) :
		return self.__size == 0


	def push(self, data) :
		newNode = Node(data)

		if self.__head is None :
			self.__head = newNode

		else :
			newNode.next = self.__head
			self.__head= newNode

		self.__size += 1


	def pop(self) :
		if self.__head is None :
			return -1

		ans = self.__head.data

		self.__head = self.__head.next
		self.__size -= 1

		return ans


	def top(self) :
		if self.__head is None :
			return -1

		return self.__head.data
		


#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1