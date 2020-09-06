#Binary Search Trees are a non-linear data structure.
#They consist of a root node and zero, one or two children where the children can again have 0,1, or 2 nodes as their children and so on
#In most cases, the time complexity of operations on a BST, which include, lookups, insertions and deletions, take O(log N) time
#Except for the worst case, where the tree is heavily unbalanced with all the nodes being on one side of the tree.
#In that case, it basically becomes a linked list and the time complexities go up to O(n)

#Lets implement an unbalanced Binary Search Tree first
#We will need a node class to store information about each node
#It will store the data and the pointers to its left and right children
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#Now we will implement the Binary Search Tree having a constructor with the root node initialised to None
#And the three methods, lookup, insert and delete
class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0


#For the insert method, we check if the root node is None, then we make the root node point to the new node
#Otherwise, we create a temporary pointer which points to the root node at first.
#Then we compare the data of the new node to the data of the node pointed by the temporary node.
#If it is greater then first we check if the right child of the temporary node exists, if it does, then we update the temporary node to its right child
#Otherwise we make the new node the right child of the temporary node
#And if the new node data is less than the temporary node data, we follow the same procedure as above this time with the left child.
#The complexity is O(log N) in avg case and O(n) in worst case.
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while(current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return


#Now we will implement the lookup method.
#It will follow similar logic as to the insert method to reach the correct position.
#Only instead of inserting a new node we will return "Found" if the node pointed by the temporary node contains the same value we are looking for
    def search(self,data):
        if self.root == None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right


#Finally comes the very complicated remove method.
#This one is too complicated for me to explain while writing. So I'll just write the code down with some comments
#explaining which conditions are being checked
    def remove(self, data):
        if self.root == None: #Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: #Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else: #Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                #Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                #Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None: #Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                #Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"




my_bst = BST()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)
'''
            5
        3       7
    1               13
0                10     65
'''

(my_bst.remove(13))
'''
            5
        3       7
    1               65
0                10     
'''
my_bst.remove(5)
'''
            7
        3       65
    1        10     
0                
'''
my_bst.remove(3)
'''
            7
        1       65
    0        10                     
'''
my_bst.remove(7)
'''
            10
        1       65
    0                
'''
my_bst.remove(1)
'''
            10
        0       65
                     
'''
my_bst.remove(0)
'''
            10
                65
                     
'''
my_bst.remove(10)
'''
           65
                
                     
'''
my_bst.remove(65)
'''
           
                
'''

my_bst.insert(10)
'''
        10


'''
print(my_bst.root.data)
#10
