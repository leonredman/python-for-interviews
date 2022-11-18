# Queues in python ( are double ended queues by default)
# we can import them
from collections import deque
# adding values to the right side we can append to the queue
queue = deque(1)
queue.append(1)
queue.append(2)
print(queue)
# yeild deque([1, 2])  - not much different from a stack

# the benefit is we can pop from the left of the queue and do this operation in constant time unlike with a stack
queue.popleft()
print(queue)
# yeild deque([2])

# since its double ended we can add to the left
queue.appendleft(1)
print(queue)
# yeild deque([1, 2])
# we can also pop from the right side if we want to
queue.pop()
print(queue)
# deque([1])
