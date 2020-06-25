#DFS or Depth First Search is another traversal algorithm.
#In this, we traverse to the depths of the tree/graph until we can't go further, in which case, we go back up and repeat the process for the unvisited nodes
#DFS Traversals can be of 3 types - PreOrder, InOrder, and PostOrder.
#Again , to implement this, we'll need a BST which we have already coded. So we'll use that.

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
                            parent_node.right = current_node.left
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

#Now we'll implementthe three kinds of DFS Traversals.
    def DFS_Inorder(self):
        return inorder_traversal(self.root, [])

    def DFS_Preorder(self):
        return preorder_traversal(self.root, [])

    def DFS_Postorder(self):
        return postorder_traversal(self.root, [])



def inorder_traversal(node, DFS_list):
    if node.left:
        inorder_traversal(node.left, DFS_list)
    DFS_list.append(node.data)
    if node.right:
        inorder_traversal(node.right, DFS_list)
    return DFS_list


def preorder_traversal(node,DFS_list):
    DFS_list.append(node.data)
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    return DFS_list


def postorder_traversal(node, DFS_list):
    if node.left:
        postorder_traversal(node.left, DFS_list)
    if node.right:
        postorder_traversal(node.right, DFS_list)
    DFS_list.append(node.data)
    return DFS_list


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

#Inorder traversal for this tree : [0, 1, 3, 5, 7, 10, 13, 65]
#Preorder Traversal for this tree : [5, 3, 1, 0, 7, 13, 10, 65]
#Postorder Traversal for this tree : [0, 1, 3, 10, 65, 13, 7, 5]


print(my_bst.DFS_Inorder())
#[0, 1, 3, 5, 7, 10, 13, 65]

print(my_bst.DFS_Preorder())
#[5, 3, 1, 0, 7, 13, 10, 65]

print(my_bst.DFS_Postorder())
#[0, 1, 3, 10, 65, 13, 7, 5]

