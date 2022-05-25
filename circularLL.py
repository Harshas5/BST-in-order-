class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class circularLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while  node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            

    def createCLL(self,nodevalue):
        node = Node(nodevalue)
        self.next = node
        self.head = node
        self.tail = node

    def insert(self,nodevalue,location):
        
        if self.head is None:
            return " no linked list is exist"
        else:
            newnode = Node(nodevalue)
            if location == 0:
                newnode.next=self.head
                self.head = newnode
                self.tail.next = newnode
            elif location ==1:
                newnode.next = self.head
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location-1 :
                    tempnode = tempnode.next
                    index+=1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode

        return 'the inseertion is completed.....!'

    def travers(self):
        if self.head is None:
            print('no vaues exist in linked list')
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode ==self.tail.next:
                    break


    def searching(self,searchvalue):
        if self.head is None:
            print('no values in list')
        else:
            tempnode = self.head
            while tempnode:
                if  tempnode.value==tempnode:
                    return tempnode.value
                tempnode= tempnode.next
                if tempnode == self.tail.next:
                    return " no value is exist"
    def deleting(self,location):
        if self.head is None:
            return 'nothing to delete'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head=None
                    self.tail =None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location ==1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head=None
                    self.tail =None
                else:
                    node = self.head
                    while node is not None:
                        if node == self.tail:
                            break
                        else:
                            node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location-1 :
                        tempnode = tempnode.next
                        index +=1 
                nextnode = tempnode.next
                tempnode.next = nextnode.next

    def deletingholeCLL(self):
        self.head = None
        self.tail.next =None
        self.tail= None


CLL = circularLL()
CLL.createCLL(1000)
CLL.insert(0,0)
CLL.insert(3,1)
CLL.insert(56,0)
CLL.insert(4,3)
CLL.insert(3,2)
CLL.travers()
#print(CLL.searching(1))

print([node.value for node in CLL])

CLL.deleting(2)

print([node.value for node in CLL])



