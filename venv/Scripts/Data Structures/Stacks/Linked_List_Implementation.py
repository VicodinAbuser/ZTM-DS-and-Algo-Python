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
        if self.top is None:
            return None
        return self.top.data


#Next comes the push operation, where we insert an element at the top of the stack
#Again this only requires access to the top pointer and inl=volves no looping.
#So time complexity is O(1)
    def push(self, data):
        new_node = Node(data)
        if self.top == None: #If the stack is empty, we make the top and bottom pointer both point to the new node
            self.top = new_node
            self.bottom = new_node
        else: #Otherwise, we make the next of the new node, which was pointing to None, point to the present top and then update the top pointer
            new_node.next = self.top
            self.top = new_node
        self.length += 1

#Next comes the pop operation wehere we remove the top element from the stack
#Its time complexity is O(1) as well
    def pop(self):
        if self.top == None: #If the stack is empty, we print an appropriate message
            print("Stack empty")
        else: #Else we make the top pointer point to the next of the top pointer and decrease the length by 1, effectively deleting the top element.
            self.top = self.top.next
            self.length -= 1
            if(self.length == 0): #We make the bottom pointer None if there was only 1 element in the stack and that gets popped
                self.bottom = None

#Finally we'll implement a print method which prints the elements of the stack from top to bottom
#This will be an O(n) operation as we'll obviously have to traverse the entire linked list to print all elelments
    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while(current_pointer!=None):
                print(current_pointer.data)
                current_pointer = current_pointer.next


my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.top.data)
#discord

print(my_stack.bottom.data)
#gogle

my_stack.pop()
my_stack.print_stack()
#udemy
#google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Stack Empty

