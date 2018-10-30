# Find 3 largest and 4 smallest.
# elements of a list.
import heapq

grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print('the largest = ', heapq.nlargest(3, grades))
print('the smallest = ', heapq.nsmallest(4, grades))

# Ternary Operator.
x, y = 50, 25
res = True if (x < y) else False

H = [21,1,45,78,3,5]

'''
heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0.
          But rest of the data elements are not necessarily sorted.
heappush - This function adds an element to the heap without altering the current heap.
heappop - This function returns the smallest data element from the heap.
heapreplace - This function replaces the smallest data element with a new value supplied in the function.
'''

# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)



# Python code to demonstrate use of zip.
stocks = {
    'Goog' : 520.54,
    'FB' : 76.45,
    'yhoo' : 39.28,
    'AMZN' : 306.21,
    'APPL' : 99.76
    }

# sorting according to values.
zipped_1 = zip(stocks.values(), stocks.keys())
print(sorted(zipped_1))

# sorting according to keys.
zipped_2 = zip(stocks.keys(), stocks.values())
print(sorted(zipped_2))
