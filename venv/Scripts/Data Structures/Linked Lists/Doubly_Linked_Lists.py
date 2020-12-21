#Doubly linked lists are just normal, singly linked lists with one added feature,
#a link to the previous node as well in addition to a link to the next node.
#Although the worst case time complexities of all operations in a doubly linked list are same as that of a singly linked list,
#Some operations are technically faster. For example, lookup or searching, is O(n/2) as search can begin from both ends
#But O(n/2) = O(n), so it is still the same as that for a singly linked list.

#Implementation of doubly linked list is almost exactly the same as that for singly linked list,
#With just the added feature of the pointer to the previous node.
#We'll have the same methods which do the exact same thing. The pars which will be different from the singly linked list are explained
#So lets implement it.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()


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


    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None: #If after deleting the first node the list becomes empty or there remains only one node, we set the tail equal to the head
                self.tail = self.head
            if self.head != None:
                self.head.previous = None #We set the previous pointer of the new head to be None
            self.length -= 1
            return
        try:  # Try block required as if the value is not found then current_node.next will be None and there is no data parameter to compare.
            while current_node!= None and current_node.next.data != data:
                current_node = current_node.next
            if current_node!=None:
                current_node.next = current_node.next.next
                if current_node.next != None: #If the node deleted is not the last node(i.e., the node next to the next to the current node is !- None),
                    current_node.next.previous = current_node #Then we set the previous of the node next to the deleted node equal to the current node, so a two-way link is established
                else:
                    self.tail = current_node #If the deleted node is the last node then we update the tail to be the current node
                self.length -= 1
                return
        except AttributeError:
            print("Given value not found.")
            return


    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            #print(self.head)
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                self.head.previous = None #We update the previous of the new head to be equal to None
            self.length -= 1
            return

        if position>=self.length:
            position = self.length-1

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next != None: #Similar logic to the delete_by_value method
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return


#I'll create a Doubly linked list and call all its methods in the same sequence as I did in the Singly Linked List implementation
#The answers should come out to be the same
my_linked_list = DoublyLinkedList()
my_linked_list.print_list()
#Empty

my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.print_list()
#5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list()
#4 5 2 9

my_linked_list.insert(2,7)
my_linked_list.print_list()
#4 5 7 2 9

my_linked_list.insert(0,0)
my_linked_list.insert(6,0)
my_linked_list.insert(9,3)
my_linked_list.print_list()
#This position is not available. Inserting at the end of the list
#0 4 5 7 2 9 0 3

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
#0 4 5 7 2 9 0

my_linked_list.delete_by_value(0)
my_linked_list.print_list()
#4 5 7 2 9 0

my_linked_list.delete_by_position(3)
my_linked_list.print_list()
#4 5 7 9 0

my_linked_list.delete_by_position(0)
my_linked_list.print_list()
#5 7 9 0

my_linked_list.delete_by_position(8)
my_linked_list.print_list()
#5 7 9

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
#Given value not found.

print(my_linked_list.length)
#3


#The answers are all same. Meaning our doubly linked list works properly