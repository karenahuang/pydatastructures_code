#Binary Tree

class Node:
    #constructor... method called when object created from
    #class and allows class to initialize attributes of a class
    def _init_(self,key):
        self.left = None
        self.right = None
        self.val = key


#create root
root = Node(1)

#Now tree will exist with 1 as the root
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
