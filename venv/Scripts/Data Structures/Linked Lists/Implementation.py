#Linked lists are, as the name suggests, a list which is linked.
#It consists of nodes which contain data and a pointer to the next node in the list.
#The list is connected with the help of these pointers.
#These nodes are scattered in memory, quite like the buckets in a hash table.
#The node where the list starts is called the head of theblist and the node where it ends, or last node, is called the tail of the list.
#The average time complexity of some operations invloving linked lists are as follows:
#Look-up : O(n)
#Insert : O(n)
#Delete : O(n)
#Append : O(1)
#Prepend : O(1)
#Python doesn't have a built-in implementation of linked lists, we have to build it on our own
#So, here we go.


#First we define a class Node which will act as a blueprint for each of our nodes
class Node():
    def __init__(self, data): #When instantiating a Node, we will pass the data we want the node to hold
        self.data = data #The data passed during instantiation will be stored in self.data
        self.next = None #This self.next will act as a pointer to the next node in the list. When creating a new node, it always points to null(or None).


#Next we define the class LinkedList which will have a head pointer to point to the beginning of the list and a tail pointer to
#point to the end of the list. An optional value of length can also be stored to keep track of the length of the linked list.
#When the list is created , it is empty and there is no node to point to. So head will point to None at the time of creation of linked list
#And since the list is empty at the time of creation, we will point the tail to whatever the head is pointing to, i.e., None
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

#Next comes the append method with which we will add nodes to the end of the linked list.
#To do this, we will just pass the data we want to append. The append method will create a new instance of the Node class,
#Effectively creating a new node, with the data passed to the instance, so that the new node will contain the data the user wants to enter
#Then we will check if the list is empty. If it is, we will point the head to the new node just created and the tail to the head,
#as there is only one node in the list, so the head and tail point to the same node. Also, we will set the length equal to 1.
#If the list isn't empty, then we will make the 'next' pointer of the last node(pointed at by 'tail') point to the new node
#And update the tail to point to the new node as this has become the last node in the list now. And we'll increase the length.
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1


#Next operation we'll implement is prepend, wehre we add a node at the head of the list.
#For this, we will call the prepend method and pass the value we want to enter, which will create a new object of the node class
#Then we will make the 'next' of the new node point to the head ,as the head is currently pionting to the first node of the list
#And then we will update the head to point to new node as we want the new node to be new first node, i.e, the new head.
#And ofcourse, we'll increase the length by 1
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


#Now we will implement the print function to print the values in the nodes of the linked list
#We will check if the list is empty or not. If it is, we will printout "Empty"
#Else, we will create a new node which will point to the head. Then we will loop until the node we created becomes None
#Inside the loop we will print the data of the current node and then make the current node equal to the node pointed by the current node
#Since this requires us to traverse the entire lenth og the linked list, this is an O(n) operation.
    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data)
                current_node = current_node.next


#Next comes the insert operation, where we insert a data at a specified position

'''    def insert(self, position, data):
        if position == self.length:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position < self.length:
            new_node = Node(data)
            i = 0
            while i < position:
'''