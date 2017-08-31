# class Node:
#     def __init__(self, value, previous = None):
#         self.value = value
#         self.previous = previous

# class MyQueue:
#     def__init__(self):
#         self.first = None
#         self.last = None

#     def peek(self):
#         # Return the next node.
#             return self.first
#         pass
    
#     def dequeue(self):
#         # Return the next node and remove it from the queue.
#         node_to_return = self.first

#         if node_to_return == self.last:
#             self.last = None
#             self.first = None
#         else:
#             self.first = self.first.previous
#         pass

#     def enqueue(self, value):
#         # Add the new node to the end of the queue.
#         new_node = Node(value)

#         if self.first == None and self.last == None:
#             self.first == new_node
#             self.last == new_node
#         else:
#             self.last.previous = new_node
#             self.last = new_node
#         pass

# Queues:
#     First object in is the first object out.
#     Real life example would be a Notification Service (Notify something else 
#     that something happened.)
#     One example would be nginx.

# Interface:
#     Object oriented term. It hides the complexity behind anything and provides a
#     simple way to input and output through that interface.
#     Interface Methods:
#         enqueue
#         dequeue
#         peek

# Stacks:
#     Is a linked list.
#     Interface methods:
#         pop() Removes the top node from the stack and returns it
#         push()
#         peek()

class Node:
    def __init__(self, value, below = None)
        self.value = value
        self.below = below

class MyStack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top
        pass
    
    def pop(self):
        if self.top == None:
            return None

        node_to_return == self.top
        self.top = self.top.previous
        return node_to_return
        pass

    def push (self, value):
        new_node = Node(value)
        new_node.below = self.top
        self.top = new_node
        pass