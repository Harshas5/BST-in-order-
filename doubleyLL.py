class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
        
class circularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while  node:
            yield node
            node = node.next

    def createDLL(self,nodevalue):
        node = Node(nodevalue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node

        return 'node is created succussfully'
    
    def insert(self,newvalue,location):
        if self.head is None:
            return ' no linked list to insert'
        else:
            newnode = Node(newvalue)

            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode

            elif location == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode

            else:
                tempnode= self.head
                index =0
                while index < location-1:
                    tempnode = tempnode.next
                    index +=1
                nextnode = tempnode.next
                newnode.next = nextnode
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode

    def travers(self):
        if self.head is None:
            print('no list is kali ')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def reversTraversel(self):
        if self.head is None:
            print('no list is kali ')
        else:
            node = self.tail
            while node :
                print(node.value)
                node = node.prev



                

        
DLL = circularLL()
DLL.createDLL(1)

print([node.value for node in DLL])

DLL.insert(2,0)
DLL.insert(3,1)
DLL.insert(4,2)
DLL.insert(5,3)
DLL.travers()

print("   ")
DLL.reversTraversel()


print([node.value for node in DLL])

