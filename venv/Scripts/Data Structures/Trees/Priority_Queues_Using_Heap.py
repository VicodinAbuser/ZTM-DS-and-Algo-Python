# Priority Queues, as the name suggests, are queues where the elements have different priorities
# And it does not always follow the FIFO rule.
# They can be implemented in a number of ways, out of which heap is the most commonly used one.
#In Python, it is available using “heapq” module. The property of this data structure in Python is that each time the smallest of heap element is popped(min heap).
#Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element  returns the smallest element each time.
#Operations we can perform on heap using heapq module are:
#heapify(iterable) : This function converts the iterable into a heap. i.e. in heap order.
#heappush(heap, ele) : This function inserts an element into heap. The order is adjusted, so as heap structure is maintained.
#heappop(heap) : This function removes and returns the smallest element from heap. Again, he order is adjusted, so as heap structure is maintained.
#heappushpop(heap, ele) : This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.
#eapreplace(heap, ele) : This function also inserts and pops element in one statement, but in this, minimum element is first popped, then the new element is pushed.
#heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().


import heapq

# initializing list
li = [5, 7, 9, 1, 3]

#using heapify to convert list into heap
heapq.heapify(li)

#printing created heap
print("The created heap is : ", end="")
print(list(li))
#The created heap is : [1, 3, 9, 7, 5]


#using heappush() to push elements into heap
heapq.heappush(li, 4)

#printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))
#The modified heap after push is : [1, 3, 4, 7, 5, 9]


#using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
#The popped and smallest element is : 1


#Creating two identical heaps to demonstrate the difference between heappushpop and heapreplace
li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))
#The popped item using heappushpop() is : 2


# using heapreplace() to push and pop items simultaneously
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))
#The popped item using heapreplace() is : 3
