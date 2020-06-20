#Doubly linked lists are just normal, singly linked lists with one added feature,
#a link to the previous node as well in addition to a link to the next node.
#Although the worst case time complexities of all operations in a doubly linked list are same as that of a singly linked list,
#Some operations are technically faster. For example, lookup or searching, is O(n/2) as search can begin from both ends
#But O(n/2) = O(n), so it is still the same as that for a singly linked list.

#Implementation of doubly linked list is almost exactly the same as that for singly linked list,
#With just the added feature of the pointer to the previous node.
#So lets implement it.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.tail
        self.length = 0


    def append(self, data):
        new_node = Node(data)
        if self.head == None: #If linked list is empty, we make head and tail both equal to the new node
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else: #Else, we make the previous pointer of the new node point to the present tail.
            new_node.previous = self.tail
            self.tail.next = new_node #Then we make the next pointer of the present tail point to the new node thus establishing a two way link between the present tail and the new node
            self.tail = new_node #Finally we update the tail to be equal to the new node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head #We make the next of the new node point to the present head
            self.head.previous = new_node #We establish a two-way link by making the previous of the present head point to the new node
            self.head = new_node #Finally we update the head
            self.length += 1
            return


