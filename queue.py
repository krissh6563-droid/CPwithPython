# Initializig the queue
queue = []
#adding element to the queue
def add(data):
    queue.append(data)
    print(queue)

def delete():
    queue.pop(0)
    print(queue)
add(2)
add(3)
add(4)
delete()

#methos second  using dqueue
from collections import deque
q = deque()
#add element to the queue
def add(data):
    q.append(data)
    print(q)
    
#delete element to the queue
def delete():
    q.popleft()
    print(q)

add(1)
add('a')
add(3)
delete()

