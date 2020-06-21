#Stacks are linear data-structures which can be implemented using either stacks or linked lists
#Insertion and deletion of elements in a stack take place from one end only.
#Stacks follow the LIFO rule - Last In First Out, where the last element that is inserted, is the first element that comes out.
#The main operations that can be performed on a stack , with their time complexities are as follows:
#Push (Insert) - O(1)
#Pop (Remove) - O(1)
#Peek (Retrieve the top element) - O(1)

#Here we'll implement a stack using linked lists

#Linked Lists are made of nodes. So we create a node class.
#It will contain the data and the pointer to the next node.
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


#Now we create the Stack class
#It will consist of a constructor having the top pointer, i.e., the pointer which points to the top element of the stack at any given time
#The length variable which keeps track of the length of the stack, and a bottom pointer which points to bottom most element of the stack
#After this will come the methods associated with a stack
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

#The peek method will allow us to peek at the top element,i.e.,
#It will return the element at the top of the stack without removing it from the stack.
#Since for this we only need to see what the top pointer points at, the time complexity will be O(1)
    def peek(self):
        return self.top


#Next comes the push operation, where we insert an element at the top of the stack
#Again this only requires access to the top pointer and inl=volves no looping.
#So time complexity is O(1)
    def push(self, data):
        new_node = Node(data)
        if self.top == None: #If the stack is empty, we make the top and bottom pointer both point to the new node
            self.top = new_node
            self.bottom = new_node
            self.length += 1
            return self.top
        else: #Otherwise, we make the next of the top pointer, which was pointing to None, point to the new node and then update the top pointer
            self.top.next = new_node
            self.top = new_node
            self.length += 1
            return self.top

