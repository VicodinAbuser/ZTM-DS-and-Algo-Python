#BFS or Breadth First Search is a traversal algorithm for a tree or graph, where we start from the root node(for a tree)
#And visit all the nodes level by level from left to right. It requires us to keep track of the chiildren of each node we visit
#In a queue, so that after traversal through a level is complete, our algorithm knows which node to visit next.
#Time complexity is O(n) but the space complexity can become a problem in some cases.

#To implement BFS, we'll need a Binary Search Tree, which we have already coded. So we'll use that.

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


#Now we implement the BFS method.
    def BFS(self):
        current_node = self.root #We start with the root node
        BFS_result = [] #This will store the result of the BFS
        queue = [] #Queue to keep track of the children of each node
        queue.append(current_node)  #We add the root to the queue first
        while len(queue) > 0:
            current_node = queue.pop(0)  #We extract the first element of the queue and make it the current node
            BFS_result.append(current_node.data)  #We push the data of the current node to the result list as we are currently visiting the current node
            if current_node.left: #If left child of the current node exists, we append it to the queue
                queue.append(current_node.left)
            if current_node.right: #Similarly, if right child exists, we append it to the queue
                queue.append(current_node.right)
        return BFS_result

#Finally, we will implement the Recursive version of the BFS.
    def Recursive_BFS(self, queue, BFS_list):
        if len(queue) == 0:
            return BFS_list
        current_node = queue.pop(0)
        BFS_list.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.Recursive_BFS(queue, BFS_list)


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

#The BFS Traversal for this tree should be : [5,3,7,1,13,0,10,65]

print(my_bst.BFS())
#[5, 3, 7, 1, 13, 0, 10, 65]

print(my_bst.Recursive_BFS([my_bst.root],[])) #We need to pass the root node as an array and an empty array for the result
#[5, 3, 7, 1, 13, 0, 10, 65]

