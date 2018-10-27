# Find 3 largest and 4 smallest.
# elements of a list.
import heapq

grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print('the largest = ', heapq.nlargest(3, grades))
print('the smallest = ', heapq.nsmallest(4, grades))
