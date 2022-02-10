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
