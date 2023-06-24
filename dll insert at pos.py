#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
        
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp #44's prev=200
        n.next=temp.next#44's next=30
        temp.next.prev=n #30's prev=44
        temp.next=n #20's next=new node
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
l.insert_pos(2)
print()
l.display()


