datos = [1, 2, 3, 4, 5]

import heapq

heapq.heapify(datos)
print("Heap:", datos)

heapq.heappush(datos, 6)
print("Heap after pushing 6:", datos)

minimino = heapq.heappop(datos)
print("Minimum element:", minimino)
print("Heap after popping minimum:", datos)

datos2 = [(2, 'A'), (4, 'B'), (3, 'C'), (2, 'D'), (12, 'E')]
heapq.heapify(datos2)
print("Heap of tuples:", datos2)