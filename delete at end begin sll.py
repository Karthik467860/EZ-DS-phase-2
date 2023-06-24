#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singlelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp.data means first node's data
                temp=temp.next#establishing linked list
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while(temp.next!=None):
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iterations
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next#20 1 point 40
        temp.next=None #30s next will be null
obj=Singlelinkedlist()
#node creation-initializing
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1 #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
obj.delete_first()
print()
obj.display()
print()
obj.delete_at_end()
obj.display()
print()
obj.delete_position(2)
obj.display()




