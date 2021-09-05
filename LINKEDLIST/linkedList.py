#Creating the node class

from ast import NodeTransformer
from typing import Counter


class Node:
    def __init__(self,data) :
        self.data=data
        self.nextNode=None

#CREATING The Linked List class

class LinkedList:
    def __init__(self) :
        self.head=None
        self.sizeOfLinkedList=0

    #Inserting the element at the start of the LinkedList
    #O(1) ==> It's really fast
    def insertAtStart(self,data):
        self.sizeOfLinkedList=self.sizeOfLinkedList+1
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node
    #Inserting the element at the End of the LinkedList
    #Linner O(N)
    def endInsert(self,data):
        self.sizeOfLinkedList=self.sizeOfLinkedList+1
        new_node=Node(data)
        actual_node=self.head
        while actual_node.nextNode is not None:
            actual_node=actual_node.nextNode
        actual_node.nextNode=new_node
    #Printing Put the length of the Whole List
    def length_of_list(self):
        return self.sizeOfLinkedList
    # Delete the node fro mthe linked List
    def deleteNode(self,data):
        #1 =>If LinkList is Empty
        if self.head is None:
            return
        actual_node=self.head
        privous_node=None
        #2 => Iterating over linkedList until "actual_node=data node"
        while actual_node is not None and actual_node.data!=data:
            privous_node=actual_node
            actual_node=actual_node.nextNode
        #3 => When iterating is completed and there is no data found
        if actual_node is None:
            return
        #4 => Data is First node (self.head)
        self.sizeOfLinkedList=self.sizeOfLinkedList-1
        if privous_node is None :
            self.head=actual_node.nextNode
        else:
            #5 => Data is in Middle
            privous_node.nextNode=actual_node.nextNode

    #Printing all element from the linkedlist
    #O(1) 
    def traverse(self):
        actual_node=self.head
        while actual_node is not None:
            print(actual_node.data,end='-->')
            actual_node=actual_node.nextNode
        print('NULL')
    # Finding the element in the LinkedList
    def FindElement(self,data):
        #The list is empty
        counter=0
        if self.head is None:
            return 
        actual_node=self.head
        while actual_node:
            if actual_node.data==data:
                print(actual_node.data ,'is present at ',counter,' Index')
                break
            else:
                actual_node=actual_node.nextNode
                counter+=1
    # Inserting the element at give index in the list     
    def insertInMiddle(self,data,index):
        #If the index value is out of range then The "DATA" is added at end if the list
        if int(index)> self.sizeOfLinkedList:
            print('Index value :', index,'is out of size of list, therefore adding element at end of the list.')
            print('Data Inserted Successfully')
            return self.endInsert(data)
        #If the index value is 0 then adding the element in starting
        if index==0:
            self.insertAtStart(data)
            print('Data Inserted Successfully')
            return
        actual_node=self.head
        privous_node=None
        new_node=Node(data)
        counter=0
        while actual_node.nextNode is not None:
            if counter == index:
                 privous_node.nextNode=new_node # privouseNode ==>newNode
                 new_node.nextNode=actual_node#newNode ==> actualNode
                 print('Data Inserted Successfully')
                 break
            else:
                privous_node=actual_node
                actual_node=actual_node.nextNode
                counter+=1

    def reverse_linkedList(self):
        actual_node=self.head
        privous_node=None
        while actual_node:
            temp =actual_node # creating a temp variable and point it to actual node
            actual_node=actual_node.nextNode
            temp.nextNode=privous_node #temp next node is pointing towards the privouseNode which is none
            privous_node=temp # Now pointing the privouse node to the temp
        self.head=temp # Now temp is the Firt element "Head " of the reversed List 

        
if __name__=='__main__':
    nodeData=LinkedList()
    nodeData.insertAtStart(12)
    nodeData.insertAtStart(13)
    nodeData.insertAtStart(14)
    nodeData.insertAtStart(15)
    nodeData.endInsert(74)
    #nodeData.length_of_list()
    #nodeData.deleteNode(15)
    
    
    #nodeData.length_of_list()
    nodeData.FindElement(15)
    print('Before inserting :====>')
    nodeData.traverse()
    nodeData.insertInMiddle(2222,3)
    nodeData.traverse()
    nodeData.insertInMiddle(1111,0)
    nodeData.traverse()
    nodeData.insertInMiddle(3333,112)
    #print('After inserting :====>')
    nodeData.traverse()
    #print(nodeData.sizeOfLinkedList)
    
    nodeData.traverse()
    nodeData.reverse_linkedList()
    nodeData.traverse()
