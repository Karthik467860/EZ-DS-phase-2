#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):#1 iteratn 1 happen
            temp=temp.next

        np.next=temp.next
        temp.next=np
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp:
                if(temp.next!=None):
                    print(temp.data,"-->", end=" ")
                    temp=temp.next
                else:
                    print(temp.data,end=" ")
                    temp=temp.next  
obj=Singlelinkedlist()
#node creation-initializing
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
obj.head.next=n1 #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_position(3,100)
obj.display()
print("")
print("before inserting 555")
obj.display()
print("")
print("after inserting 555")
obj.insert_position(3,555)
obj.display()
