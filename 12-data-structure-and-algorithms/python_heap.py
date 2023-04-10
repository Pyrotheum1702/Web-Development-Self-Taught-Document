import heapq

list_1 = [1, 1, 4, 6, 7, 2, 3, 66, 32, 9, 24, 13, 28, 15]

# Convert list_1 to a heap
heapq.heapify(list_1)
print(list_1)

# Pop the lowest value in heap
print(heapq.heappop(list_1))
# Result: 1
print(list_1)
# Result: [1, 6, 2, 15, 7, 4, 3, 66, 32, 9, 24, 13, 28]
print(heapq.heappop(list_1))
# Result: 1
print(list_1)
# Result: [2, 6, 3, 15, 7, 4, 28, 66, 32, 9, 24, 13]
print(heapq.heappop(list_1))
# Result: 2
print(list_1)
# Result: [3, 6, 4, 15, 7, 13, 28, 66, 32, 9, 24]
print(heapq.heappop(list_1))
# Result: 3
print(list_1)
# Result: [4, 6, 13, 15, 7, 24, 28, 66, 32, 9]

# Insert a value to a heap
heapq.heappush(list_1, 3)
print(list_1)
# Result: [3, 4, 13, 15, 6, 24, 28, 66, 32, 9, 7]
heapq.heappush(list_1, 7)
print(list_1)
# Result: [3, 4, 7, 15, 6, 13, 28, 66, 32, 9, 7, 24
heapq.heappush(list_1, 5)
print(list_1)
# Result: [3, 4, 5, 15, 6, 7, 28, 66, 32, 9, 7, 24, 13]
heapq.heappush(list_1, 2)
print(list_1)
# Result: [2, 4, 3, 15, 6, 7, 5, 66, 32, 9, 7, 24, 13, 28]
