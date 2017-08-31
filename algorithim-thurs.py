class Node:
    def __init__(self, value, previous = None):
        self.value = value
        self.previous = previous

class MyQueue:
    def__init__(self):
        self.first = None
        self.last = None

    def peek(self):
        # Return the next node.
        while self.peek.next == value:
            return value
        pass
    
    def dequeue(self):
        # Return the next node and remove it from the queue.
        while self.dequeue.next == value:
            # Need to remove it here.
            # What do I return?????
        pass

    def enqueue(self, value):
        # Add the new node to the end of the queue.
        while self.enqueue.next == value:
            return enqueue.last
        pass

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