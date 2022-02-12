class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    =================================================
    #Helper Function to Insert Data in the BST 
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_BST(self.root,data)
    def insert_BST(self,node,data):
        if data<=node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self.insert_BST(node.left,data)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self.insert_BST(node.right,data)
   ==================================================
  #Helper Function to Traverse Over the BST
    def Traverse(self):
        if not self.root:
            return "BST is empty"
        else:
            return self.in_order(self.root)

    def in_order(self,node):
        if node.left:
            self.in_order(node.left)
        print(node.data,end="-->")
        if node.right:
            self.in_order(node.right)
            
  ====================================================
  #Helper Function to find data in the BST
    def search(self,data):
        if self.root:
            return self.search_data(self.root,data)
        else:
            return 'BSt is empty'
          
          
          
    def search_data(self,node,data):
        if data<=node.data:
            if node.data==data:
                print(str(node.data) +" Data Found ")
                return 
            if node.left==None:
                print('Data Not Found')
                return 
            return self.search_data(node.left,data)
        else:
            if node.data==data:
                print(str(node.data) +"Data Found")
                return 
            if node.right==None:
                print('Data not Found')
                return
            return self.search_data(node.right,data)
   #========================================================
def remove_Node(self,node,data):
        if not node:
            return 'BST is empty'
        if data<node.data:
            node.left=self.remove_Node(node.left,data)
        elif data>node.data:
            node.right=self.remove_Node(node.right,data)
        else:
            if not node.right and not node.left:  #Case 1: Leaf node
                print('Removing the leaf node')
                del node
                return 
            elif not node.left:                     # Case 2  (a): Only right Child
                print("Removing node with right Child")
                temp=node.right
                del node
                return temp
            elif not node.right:                     # Case 2 (b): Only left Child
                print("Removing node with left Child")
                temp=node.left
                del node
                return temp
            print("Removing the nodw with 2 child")     #Case 3 : Node with both child
            temp=self.getPredecessor(node.left)
            node.data=temp.data
            node.left=self.remove_Node(node.left,temp.data)
        return node
    def getPredecessor(self,node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

