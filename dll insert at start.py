#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
        
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head#temp=first node
            while temp:
                print(temp.data,"<-->",end=" ")
                #temp.data means first node's data
                temp=temp.next#establishing linked list
l=doublelinkedlist()
#node creation-initializing
n1=Node(100)#so n.data in Node class will be 10
l.head=n1   #assigning first node as head
n2=Node(200)
n2.previous=n1
n1.next=n2
n3=Node(300)
n3.previous=n2
n2.next=n3
l.display()
l.insert_start()
print()
l.display()


