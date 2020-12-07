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
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
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
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

#Next comes the insert operation, where we insert a data at a specified position
#If the position is greater than the length of the list, we simply follow the procedure of the append method where we add the node to the end of the list
#If the position is equal to 0, we follow the prepend procedure, where we append the node at the head
#If the postition is somewhere in between, then we create a temporary node which traverses the list upto the previous position of the position we want to enter the new node
#Now the 'next' of the temporary node is pointing to the next node in the list, wehre we want to insert our new node
#So first we link the new node and the node at the desired position by making the 'next' of the new node equal to the 'next' of the temporary node
#The temporary node and the new node point to the same position now, the position we want to insert the new node
#So we update the 'next' of the temporary node to point to the new node.
#This way, our new node occupies the position it intended to and the node which was originally there, gets pushed to the next position
#Since this requires traversal of the list, it is an O(n) operation.
    def insert(self, position, data):
        if position >= self.length:
            if position>self.length:
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1


#Next comes the delete_by_value method where the user can enter a value and if the value is found in the list, it will be deleted.
#(If the value is found multiple times, only the first occurence of thevalue will be deleted.)
#First we check if the list is empty. If yes, we print appropriate message. If not, then we create a temporary node.
#Then we check if the value of the head is equal to the value we want deleted.
#If yes, we make the head equal to the node pointed by the 'next' of the head. Then we check if there are only one or zero nodes in the list
#If yes, then we update the tail to be equal to the head.
#By Doing this, the original 'head' gets disconnected from the list and the head becomes updated to what was originally the second node
#If these two cases are not encountered, then we have to traverse the list and check every node.
#So we loop until either the current node becomes None, signifying the end of the list, or until the data of the node next to the current node equals the data we want deleted.
#After coming out of the loop we check if the current node is not equal to None, it means the next node of the current node is the one we want deleted
#So we make the 'next' of the current node point to the next to the next of the current node.
#Effectively, we bypass the node we want deleted and establish a connection between the current and the next to next of the current nodes.
#After deleting the required node, we check if the current node's 'next' points to None, i.e., if it is the last node. If yes, then we update the tail
#And if the current node is None, it means we traversed the entire list but couldn't find the value.
#Time complexity is pretty clearly O(n)
    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next!= None and current_node.next.data != data:
            #if current_node.data == data:
            #    previous_node.next = current_node.next
            #    return
            current_node = current_node.next
        if current_node.next!=None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")


#Another functionality of linked lists can be deleting a node based on its position.
#It follows more or less the same procedure as delete_by_value method.
#Only real difference is instead of traversing the list till the current node becomes None or the next node equals the required data,
#Here we traverse the list till the position one place behind the position we want deleted, similar to the insert operation
#And then we bypass the next node to the current node and link it to the next to the next node of the current node.
#We do a similar check for tail and update it just like in the delete_by_value method.
#This operation too has a time complexity of O(n) in the worst case.
    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return


#We will import this file while reversing a linked list. So we must make sure that it runs only
#when it is the main file being run and not also when it is being imported in some other file.
if __name__ == '__main__':

    my_linked_list = LinkedList()
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
    print(my_linked_list.length)
#3
