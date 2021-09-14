from typing import Counter


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.privous=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodeLength=0

    #This function add item at the end of the linked List 
    #so we have manipulate the takk node in 0(1) running time
    def  insert_end(self,data):
        self.nodeLength=self.nodeLength+1
        new_node=Node(data)

        #When the list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.privous=self.tail
            self.tail.next=new_node
            self.tail=new_node

    #Insert Element at the start of the linked list 
    def insertStart(self,data):
        self.nodeLength=self.nodeLength+1
        new_node=Node(data)
        #When the list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.privous=new_node
            self.head=new_node

    #Traverse the linked list in forward direct 
    def traverse_forward(self):
        actual_node=self.head
        while actual_node is not None:
            print(actual_node.data,end=" ==> ")
            actual_node=actual_node.next
        print('NULL')
    #Traverse the linked list in backward direct 
    def traverse_backward(self):
        actual_node=self.tail
        while actual_node is not None:
            print(actual_node.data,end=" ==> ")
            actual_node=actual_node.privous
        print('NULL')
    
    def insert_in_middle(self,data,index):
        #when index value is 0 ==>Then insert at start Function is  called
        if index==0:
            return self.insertStart(data)
        actual_node=self.head
        new_node=Node(data)
        #When the index is bigger than the length of the list then Data is added at the end
        if int(index) >self.nodeLength:
            return self.insert_end(data)
        #
        for i in range(0,index-1):
            actual_node=actual_node.next
        new_node.privous=actual_node
        new_node.next=actual_node.next
        actual_node.next.privous=new_node
        actual_node.next=new_node
        self.nodeLength=self.nodeLength+1

    def find_element(self,data):
        actual_node=self.head
        counter=0
        while actual_node:
            if actual_node.data==data:
                print(actual_node.data ,'is present at ',counter,' Index')
                break
            else:
                actual_node=actual_node.next
                counter+=1
            

if __name__=='__main__':
    doubleDirList=DoubleLinkedList()
    doubleDirList.insert_end(1)
    
    doubleDirList.insert_end(2)

    doubleDirList.insertStart(11)
    
    doubleDirList.insertStart(22)
    
    doubleDirList.insert_in_middle('end',13)
    
    doubleDirList.insert_in_middle('start',0)
    doubleDirList.insert_in_middle('middle',3)
    doubleDirList.find_element('end')
    doubleDirList.traverse_forward()
    
