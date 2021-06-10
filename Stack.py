# Creating Node class

class Node:
	# constructor
	def __init__(self, data,next=None):
		self.data = data;
		self.next = next;

	def getData(self):
		return self.data;
class Stack:
	# constructor
	def __init__(self):
		self.top = None;
	# push data to the top of Stack
	def push(self,data):
		if (self.top):
			curr = Node(data);
			curr.next = self.top;
			self.top = curr;
		else:
			self.top = Node(data);
	# pop data from top of Stack and return it or return -1
	def pop(self):
		if (self.top):
			count = self.top.getData();
			self.top = self.top.next;
			return count;
		else:
			return -1;
	# return true if is empty or false
	def isEmpty(self):
		return (self.top == None);

	def printList(self):
		curr = self.top;
		string = "";
		while (curr):
			if (curr.next != None):
				string = string+str(curr.getData())+",";
			else:
				string = string+str(curr.getData());
			curr = curr.next;
		print(string);

def main():

	stack = Stack();
	stack.push(1);
	stack.push(2);
	stack.push(3);
	stack.push(4);
	stack.push(5);
	stack.printList();

	string = "";
	while (stack.isEmpty() != True):
		data = stack.pop();
		if (stack.isEmpty() != True):
			string = string+str(data)+",";
		else:
			string = string+str(data);
	print(string);
	print(stack.pop());

main();