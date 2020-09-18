# TODO a class that reresents the individual elements in our LL
class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next_node(self):
		return self.next_node

	def set_next_node(self, new_next):
		self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
        	self.head = new_node
        	self.tail = new_node
        else:
        	new_node.set_next(self.head)
        	self.head = new_node


    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
        	self.head = new_node
        	self.tail = new_node
        else:
        	self.tail.set_next(new_node)
        	self.tail = new_node

    def remove_head(self):
        if not self.head:
        	return None
        if not self.head.get_next():
        	head = self.head
        	self.head = None
        	self.tail = None
        	return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value


    def remove_tail(self):
        if not self.head:
        	return None
        elif not self.head.get_next():
        	tail = self.tail
        	self.head = None
        	self.tail = None
        	return tail.get_value()
        else:
        	prev = self.head
        	curr = prev
        	while curr.get_next():
        		prev = curr
        		curr = curr.get_next()
        		if curr == self.tail:
        			prev.set_next(None)
        			self.tail = prev
        			return curr.get_value()

    def contains(self, value):
        # TODO time permitting

    def get_max(self):
        # TODO time permitting