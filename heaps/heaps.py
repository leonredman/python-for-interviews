# to find the min and max
# Heaps 
import heapq
# Heaps under the hoodin python they are really implemented with arrays
# To create an empty heap we jut create a list and push values to that heap
# by default heaps are min heaps in python
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# The Min value is always at index [0], thats how heaps are implemented
print(minHeap[0])
# yeild 2

# while the length of the heap is non-zero we can loop thu the heap. 
# while looping we can we can pop values from the heap
while len(minHeap):
  print(heapq.heappop(minHeap))

# yeild 2 3 4

  # Pythone does not have max heaps by default, the work around is
  # to use min heap and multiply each value that we push  by -1 when 
  # push & pop. When we pop the value we also multiply by -1 to negate that value
  maxHeap = []
  heapq.heappush(maxHeap, -3)
  heapq.heappush(maxHeap, -2)
  heapq.heappush(maxHeap, -4)

  # Max is always at index 0  (must multiply by neg one to negate the original negative value)
  print(-1 * maxHeap[0])
  # yeild 4

  while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
  # yeild 4 3 2


# if you already have the list of values you want to build the heap
# you can call the built in heap function called heapify in python 
# can build it in linear time using heapify
# while array is not empty  we can loop and keep printing the values from smallest to largest

import heapq
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
  print(heapq.heappop(arr))
# yeild 1 2 4 5 8