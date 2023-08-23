"""Python built-in data structure list can be used as a stack. Instead of push(), append() is used to add 
elements to the top of the stack while pop() removes the element in LIFO order. 
Unfortunately, the list has a few shortcomings. The biggest issue is that it can run into speed issues as 
it grows. The items in the list are stored next to each other in memory, if the stack grows bigger than
 the block of memory that currently holds it, then Python needs to do some memory allocations. This can 
 lead to some append() calls taking much longer than other ones."""

stack = []
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

########################################################################################################

"""Python stack can be implemented using the deque class from the collections module. Deque is preferred
 over the list in the cases where we need quicker append and pop operations from both the ends of the
   container, as deque provides an O(1) time complexity for append and pop operations as compared to
     list which provides O(n) time complexity. """
 
from collections import deque
stack = deque()
stack.append(3)
stack.append(4)
stack.append(4)

print(stack)

print(stack.pop())
print(stack.pop())

print(stack)


##########################################################################################################
"""Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the 
put() function and get() takes data out from the Queue. """

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

