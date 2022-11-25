# to find the min and max
# Heaps 
import heapq
# under the hood they are really arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0, thats how heaps are implemented
print(minHeap[0])

# to loop thru a heap
while len(minHeap):
  print(heapq.heappop(minHeap))

  # No max heaps by default, the work around is
  # to use min heap and multiply by -1 when 
  # push & pop