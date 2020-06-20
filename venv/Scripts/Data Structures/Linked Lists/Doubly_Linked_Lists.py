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


    def insert(self, position, data):
        if position == 0:
            self.prepend(data) #Inserting at position 0 is equivalent to prepending. So instead of repeating code, we simple call the prepend method
            return
        if position >= self.length:
            self.append(data) #Similarly, inserting ata position >= the length of the list is equivalent to appending, so we call the append method
            return
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1): #We traverse upto one position before the position where we want to insert the new node
                current_node = current_node.next
            new_node.previous = current_node #We make the previous of the new node point to the current node
            new_node.next = current_node.next #And the next point to the next of the current node.
            current_node.next = new_node #Then we break the link between the current node and the next node and make the next of the current node point to the new node
            new_node.next.previous = new_node #And finally we update the previous of the next node to point to the new node instead of the current node. This way, the new node gets inserted in betwwen the current and the next nodes.
            self.length += 1
            return


