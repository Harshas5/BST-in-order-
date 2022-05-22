class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class singalil:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while  node:
            yield node
            node = node.next

    #insert the value
    def insertsl(self,value,location ):
        newnode = Node(value)
        if self.head is None:
            self.head =newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next=self.head
                self.head = newnode

            elif location == 1:
                newnode.next =None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index +=1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
    def deletion(self,location):
        if self.head is None:
            print(' no nodes in sll')
        else:
            if location==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None    
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None    
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    node.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index +=1
                nextnode = tempnode.next
                tempnode.next= nextnode.next





singalylinkedlist=singalil()



singalylinkedlist.insertsl(0,4)
singalylinkedlist.insertsl(0,1)
singalylinkedlist.insertsl(0,0)
singalylinkedlist.insertsl(1,3)



print([node.value for node in singalylinkedlist])


singalylinkedlist.deletion(2)

print([node.value for node in singalylinkedlist])

        


